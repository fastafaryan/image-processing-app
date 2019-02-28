# import the necessary packages
import cv2
from PIL import Image, ImageTk
import tkinter
from tkinter import filedialog
#import map
import finder
import os
import detector
import pickle 
import imutils
import face_recognition

###################### GUI METHODS ######################
# prints found plate number to log
def findPlates():
    dump, textboxValue = finder.searchDB("J+ YSB 55")
    # update log
    log_text.delete('1.0', tkinter.END)
    log_text.insert(tkinter.END, "Approximative Plate Number: "+textboxValue)
    log_text.pack()

# prints plate information to log
def plateInfo():
    index, dump = finder.searchDB("J+ YSB 55")
    plateInfo = finder.getData(index)
    # update log
    log_text.delete('1.0', tkinter.END)
    log_text.insert(tkinter.END, plateInfo)
    log_text.pack()

# opens select file diaglog
def openFile():
    filename =  tkinter.filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select file", filetypes = (("jpeg files","*.jpg"),("png files","*.png*")))
    img = ImageTk.PhotoImage(Image.open(filename).resize((video_frame.winfo_width(),video_frame.winfo_height())))
    panel = tkinter.Label(video_frame, image = img, borderwidth=0, highlightthickness=0)
    panel.image = img # keep a reference!
    panel.grid()

# detects people from videos and displays on the screen 
def detectVideo():
    videoFile =  tkinter.filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select file", filetypes = (("mp4 files","*.mp4"),("png files","*.png*")))
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
        print(stream.get(1))
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
                matches = face_recognition.compare_faces(data["encodings"],	encoding)
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
            # print detected names to log
            log_text.delete('1.0', tkinter.END)
            log_text.insert(tkinter.END, "DETECTED PEOPLE\n")
            for name in names:
                if name is not 'Unknown':
                    log_text.insert(tkinter.END, str(name+'\n'))
                    log_text.pack()
    # close the video file pointers
    stream.release()

# detects people from images and displays on the screen 
def detectImage():
    # open file dialog to select image
    filename =  tkinter.filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select file", filetypes = (("jpeg files","*.jpg"),("png files","*.png*")))
    # run detector, returns names
    names = detector.detector().detectImage(filename, 'encodings.pickle')
    # open detected image and display it on the screen
    img = ImageTk.PhotoImage(Image.open('assets/output.png').resize((video_frame.winfo_width(),video_frame.winfo_height())))
    panel = tkinter.Label(video_frame, image = img, borderwidth=0, highlightthickness=0)
    panel.image = img # keep a reference!
    panel.grid()
    # print detected names to log
    log_text.delete('1.0', tkinter.END)
    log_text.insert(tkinter.END, "DETECTED PEOPLE\n")
    for name in names:
        if name is not 'Unknown':
            log_text.insert(tkinter.END, str(name+'\n'))
            log_text.pack()

###################### GUI METHODS ######################

###################### GUI ELEMENTS ######################
# Main Window
window = tkinter.Tk()
window.title("Controler App")
window.configure(background='black')
## dynamic resizing for frames
window.grid_columnconfigure(0, weight=3)
window.grid_columnconfigure(1, weight=2)
window.grid_columnconfigure(2, weight=1)
window.grid_rowconfigure(0, weight=1)
window.grid_rowconfigure(1, weight=1)

# Video frame
video_frame = tkinter.Canvas(window, width = 630, height = 360, borderwidth=0, highlightthickness=0, bg='white')
video_frame.grid(row=0, column=0, sticky="nsew")

# Map frame
map_frame = tkinter.Frame(window, width = 420, height = 360, borderwidth=0, highlightthickness=0, bg='pink')
map_frame.grid(row=0, column=1, sticky="nsew")

# Console frame
console_frame = tkinter.Frame(window, width = 630, height = 180, borderwidth=0, highlightthickness=0, bg='black')
console_frame.grid(row=1, column=0, sticky="nsew")

# Log frame
log_frame = tkinter.Frame(window, width = 420, height = 180, borderwidth=0, highlightthickness=0,  bg='white')
log_frame.grid(row=1, column=1, sticky="nsew")
# Log Text Area
scrollbar = tkinter.Scrollbar(log_frame)
scrollbar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
log_text = tkinter.Text(log_frame, wrap=tkinter.WORD, yscrollcommand=scrollbar.set, borderwidth=0, highlightthickness=0)
log_text.pack()
scrollbar.config(command=log_text.yview)

# Button frame
button_frame = tkinter.Frame(window, width = 210, height = 540, borderwidth=0, highlightthickness=0,  bg='black')
button_frame.grid(row=0, rowspan=2, column=2, sticky="nsew")

# Plate Recognition Buttton
b_plate_recognition = tkinter.Button(button_frame, text="Plate Recognition", command=findPlates)
b_plate_recognition.pack(fill=tkinter.BOTH, expand=1)

# Plate Information Buttton
b_plate_information = tkinter.Button(button_frame, text="Plate Information", command=plateInfo)
b_plate_information.pack(fill=tkinter.BOTH, expand=1)

# Stream Face ID Buttton
b_stream_face = tkinter.Button(button_frame, text="Detect Video", command=detectVideo)
b_stream_face.pack(fill=tkinter.BOTH, expand=1)

# Stream Image ID Buttton
b_stream_image = tkinter.Button(button_frame, text="Detect Image", command=detectImage)
b_stream_image.pack(fill=tkinter.BOTH, expand=1)

# Log Check Buttton
b_log_check = tkinter.Button(button_frame, text="Log Check")
b_log_check.pack(fill=tkinter.BOTH, expand=1)

# Attach To Database Buttton
b_attach_database = tkinter.Button(button_frame, text="Attach To Database")
b_attach_database.pack(fill=tkinter.BOTH, expand=1)

# Open Image Folder Buttton
b_open_image_folder = tkinter.Button(button_frame, text="Open Image Folder", command=openFile)
b_open_image_folder.pack(fill=tkinter.BOTH, expand=1)

# Find People Buttton
b_find_people = tkinter.Button(button_frame, text="Find People")
b_find_people.pack(fill=tkinter.BOTH, expand=1)

# Add People Buttton
b_add_people = tkinter.Button(button_frame, text="Add People")
b_add_people.pack(fill=tkinter.BOTH, expand=1)

# Access Plate Data Buttton
b_access_plate_data = tkinter.Button(button_frame, text="Access Plate Data")
b_access_plate_data.pack(fill=tkinter.BOTH, expand=1)

# Cross Search Buttton
b_cross_search = tkinter.Button(button_frame, text="Clear Screen")
b_cross_search.pack(fill=tkinter.BOTH, expand=1)
###################### GUI ELEMENTS ######################

window.mainloop()