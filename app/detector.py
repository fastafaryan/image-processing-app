import face_recognition
import pickle
import cv2
import tkinter
import imutils
import os
from PIL import Image, ImageTk

class detector:
    def __init__(self):
        pass
    
    # accepts image and encoder files, returns names of the detected people
    def detectImage(self, imageFile, pickleFile):
        # load the known faces and embeddings
        print("[INFO] loading encodings...")
        data = pickle.loads(open(pickleFile, "rb").read())

        # load the input image and convert it from BGR to RGB
        image = cv2.imread(imageFile)
        rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

        # detect the (x, y)-coordinates of the bounding boxes corresponding
        # to each face in the input image, then compute the facial embeddings
        # for each face
        print("[INFO] recognizing faces...")
        boxes = face_recognition.face_locations(rgb)
        encodings = face_recognition.face_encodings(rgb, boxes)

        # initialize the list of names for each face detected
        names = []

        # loop over the facial embeddings
        for encoding in encodings:
            # attempt to match each face in the input image to our known
            # encodings
            matches = face_recognition.compare_faces(data["encodings"], encoding, tolerance=0.4)
            name = "Unknown"

            # check to see if we have found a match
            if True in matches:
                # find the indexes of all matched faces then initialize a
                # dictionary to count the total number of times each face
                # was matched
                matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                counts = {}

                # loop over the matched indexes and maintain a count for
                # each recognized face
                for i in matchedIdxs:
                    name = data["names"][i]
                    counts[name] = counts.get(name, 0) + 1

                # determine the recognized face with the largest number of
                # votes (note: in the event of an unlikely tie Python will
                # select first entry in the dictionary)
                name = max(counts, key=counts.get)
            
            # update the list of names
            names.append(name)

        # loop over the recognized faces
        for ((top, right, bottom, left), name) in zip(boxes, names):
            # draw the predicted face name on the image
            cv2.rectangle(image, (left, top), (right, bottom), (0, 255, 0), 3)
            y = top - 15 if top - 15 > 15 else top + 15
            cv2.putText(image, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)
        
        cv2.imwrite("assets/output.png", image)
        return names

    def detectVideo(self, window, video_frame, log_frame):
        videoFile =  tkinter.filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select file", filetypes = (("mp4 files","*.mp4"),("MP4 files","*.MP4*")))
        pickleFile = 'encodings.pickle'
        # load the known faces and embeddings
        data = pickle.loads(open(pickleFile, "rb").read())

        # initialize the pointer to the video file and the video writer
        stream = cv2.VideoCapture(videoFile)
        # loop over frames from the video file stream
        while True:
            # grab the next frame
            (grabbed, frame) = stream.read()
            
            # if the frame was not grabbed, then we have reached the
            # end of the stream
            if not grabbed:
                break
            if(stream.get(1)%10 == 0):
                # convert the input frame from BGR to RGB then resize it to have
                # a width of 750px (to speedup processing)
                rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                rgb = imutils.resize(frame, width=750)
                r = frame.shape[1] / float(rgb.shape[1])
                # detect the (x, y)-coordinates of the bounding boxes
                # corresponding to each face in the input frame, then compute
                # the facial embeddings for each face
                boxes = face_recognition.face_locations(rgb)
                encodings = face_recognition.face_encodings(rgb, boxes)
                names = []
                # loop over the facial embeddings
                for encoding in encodings:
                    # attempt to match each face in the input image to our known encodings
                    matches = face_recognition.compare_faces(data["encodings"],	encoding, tolerance=0.4)
                    name = "Unknown"
                    # check to see if we have found a match
                    if True in matches:
                        # find the indexes of all matched faces then initialize a
                        # dictionary to count the total number of times each face
                        # was matched
                        matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                        counts = {}
                        # loop over the matched indexes and maintain a count for
                        # each recognized face face
                        for i in matchedIdxs:
                            name = data["names"][i]
                            counts[name] = counts.get(name, 0) + 1
                        # determine the recognized face with the largest number
                        # of votes (note: in the event of an unlikely tie Python
                        # will select first entry in the dictionary)
                        name = max(counts, key=counts.get)
                    # update the list of names
                    names.append(name)

                # loop over the recognized faces
                for ((top, right, bottom, left), name) in zip(boxes, names):
                    # rescale the face coordinates
                    top = int(top * r)
                    right = int(right * r)
                    bottom = int(bottom * r)
                    left = int(left * r)
                    # draw the predicted face name on the image
                    cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                    y = top - 15 if top - 15 > 15 else top + 15
                    cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

                ########## IMAGE DISPLAY ##########
                frame = cv2.resize(frame,(video_frame.winfo_width(),video_frame.winfo_height()))
                frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
                img = Image.fromarray(frame)
                photo = ImageTk.PhotoImage(img)
                video_frame.create_image(0, 0, image = photo, anchor = tkinter.NW)
                window.update()
                window.update_idletasks()
                ########## IMAGE DISPLAY ##########

                ########## LOGGING INFORMATION ##########
                # CLEAR IF THERE IS ANY WRITING                
                try:
                    wrapper
                except NameError:
                    pass
                else:
                    wrapper.grid_forget()
                # CREATE A WRAPPER FOR LOG FRAME
                wrapper = tkinter.Frame(log_frame, width = 1050, height = 180, borderwidth=0, highlightthickness=0, padx=10, pady=10, bg='black')
                wrapper.grid()
                wrapper.grid_propagate(0) #prevent frame from shrinking
                title = tkinter.Label(wrapper, text="DETECTED PEOPLE", bg='black', fg='white') #display title 
                title.grid()
                for name in names:
                    if name is not 'Unknown':
                        label = tkinter.Label(wrapper, text=name, bg='black', fg='white') #display names 
                        label.grid()
                ########## LOGGING INFORMATION ##########
                
        # close the video file pointers
        wrapper.grid_forget()
        stream.release()

    def detectCamera(self, window, video_frame, log_frame):
        pickleFile = 'encodings.pickle'
        # load the known faces and embeddings
        data = pickle.loads(open(pickleFile, "rb").read())

        # initialize the pointer to the video file and the video writer
        stream = cv2.VideoCapture(0)
        # loop over frames from the video file stream
        while True:
            # grab the next frame
            (grabbed, frame) = stream.read()
            
            # if the frame was not grabbed, then we have reached the
            # end of the stream
            if not grabbed:
                break
            # convert the input frame from BGR to RGB then resize it to have
            # a width of 750px (to speedup processing)
            rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            rgb = imutils.resize(frame, width=750)
            r = frame.shape[1] / float(rgb.shape[1])
            # detect the (x, y)-coordinates of the bounding boxes
            # corresponding to each face in the input frame, then compute
            # the facial embeddings for each face
            boxes = face_recognition.face_locations(rgb)
            encodings = face_recognition.face_encodings(rgb, boxes)
            names = []
            # loop over the facial embeddings
            for encoding in encodings:
                # attempt to match each face in the input image to our known encodings
                matches = face_recognition.compare_faces(data["encodings"],	encoding, tolerance=0.4)
                name = "Unknown"
                # check to see if we have found a match
                if True in matches:
                    # find the indexes of all matched faces then initialize a
                    # dictionary to count the total number of times each face
                    # was matched
                    matchedIdxs = [i for (i, b) in enumerate(matches) if b]
                    counts = {}
                    # loop over the matched indexes and maintain a count for
                    # each recognized face face
                    for i in matchedIdxs:
                        name = data["names"][i]
                        counts[name] = counts.get(name, 0) + 1
                    # determine the recognized face with the largest number
                    # of votes (note: in the event of an unlikely tie Python
                    # will select first entry in the dictionary)
                    name = max(counts, key=counts.get)
                # update the list of names
                names.append(name)

            # loop over the recognized faces
            for ((top, right, bottom, left), name) in zip(boxes, names):
                # rescale the face coordinates
                top = int(top * r)
                right = int(right * r)
                bottom = int(bottom * r)
                left = int(left * r)
                # draw the predicted face name on the image
                cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)
                y = top - 15 if top - 15 > 15 else top + 15
                cv2.putText(frame, name, (left, y), cv2.FONT_HERSHEY_SIMPLEX, 0.75, (0, 255, 0), 2)

            # IMAGE DISPLAY
            frame = cv2.resize(frame,(video_frame.winfo_width(),video_frame.winfo_height()))
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame)
            photo = ImageTk.PhotoImage(img)
            video_frame.create_image(0, 0, image = photo, anchor = tkinter.NW)
            window.update()
            window.update_idletasks()
             ########## LOGGING INFORMATION ##########
            # CLEAR IF THERE IS ANY WRITING                
            try:
                wrapper
            except NameError:
                pass
            else:
                wrapper.grid_forget()
            # CREATE A WRAPPER FOR LOG FRAME
            wrapper = tkinter.Frame(log_frame, width = 1050, height = 180, borderwidth=0, highlightthickness=0, padx=10, pady=10, bg='black')
            wrapper.grid()
            wrapper.grid_propagate(0) #prevent frame from shrinking
            title = tkinter.Label(wrapper, text="DETECTED PEOPLE", bg='black', fg='white') #display title 
            title.grid()
            for name in names:
                if name is not 'Unknown':
                    label = tkinter.Label(wrapper, text=name, bg='black', fg='white') #display names 
                    label.grid()
            ########## LOGGING INFORMATION ##########
        # close the video file pointers
        wrapper.grid_forget()
        stream.release()