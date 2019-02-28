import cv2
from PIL import Image, ImageTk
import tkinter
from tkinter import filedialog
import finder
import os
import detector
import pickle 
import imutils
import face_recognition
import database

class app:
    def __init__(self):
        
        ######## MAIN WINDOW ########
        self.window = tkinter.Tk()
        self.window.title("Controler App")
        self.window.configure(background='black')
        ## dynamic resizing for frames
        self.window.grid_columnconfigure(0, weight=3)
        self.window.grid_columnconfigure(1, weight=2)
        self.window.grid_columnconfigure(2, weight=1)
        self.window.grid_rowconfigure(0, weight=3)
        self.window.grid_rowconfigure(1, weight=1)
        ######## MAIN WINDOW ########

        ######## VIDEO FRAME ########
        self.video_frame = tkinter.Canvas(self.window, width = 780, height = 540, borderwidth=0, highlightthickness=0, bg='white')
        self.video_frame.grid(row=0, column=0, sticky="nsew")
        ######## VIDEO FRAME ########

        ######## MAP FRAME ########
        self.map_frame = tkinter.Frame(self.window, width = 270, height = 540, borderwidth=0, highlightthickness=0, bg='white')
        self.map_frame.grid(row=0, column=1, sticky="nsew")
        canv = tkinter.Canvas(self.map_frame, relief=tkinter.SUNKEN)
        canv.config(width=270, height=540)
        #canv.config(scrollregion=(0,0,1000, 1000))
        #canv.configure(scrollregion=canv.bbox('all'))
        canv.config(highlightthickness=0)
        sbarV = tkinter.Scrollbar(self.map_frame, orient=tkinter.VERTICAL)
        sbarH = tkinter.Scrollbar(self.map_frame, orient=tkinter.HORIZONTAL)
        sbarV.config(command=canv.yview)
        sbarH.config(command=canv.xview)
        canv.config(yscrollcommand=sbarV.set)
        canv.config(xscrollcommand=sbarH.set)
        sbarV.pack(side=tkinter.RIGHT, fill=tkinter.Y)
        sbarH.pack(side=tkinter.BOTTOM, fill=tkinter.X)
        canv.pack(side=tkinter.LEFT, expand=tkinter.YES, fill=tkinter.BOTH)
        im=Image.open("./assets/map2.png")
        width,height=im.size
        canv.config(scrollregion=(0,0,width,height))
        im2=ImageTk.PhotoImage(im)
        imgtag=canv.create_image(0,0,anchor="nw",image=im2)
        ######## MAP FRAME ########

        ######## LOG FRAME ########
        self.log_frame = tkinter.Frame(self.window, width = 1050, height = 180, borderwidth=0, highlightthickness=0,  bg='black')
        self.log_frame.grid(row=1, columnspan=2, sticky="nsew")
        self.log_frame.grid_propagate(0)
        ######## LOG FRAME ########

        ######## BUTTON FRAME ########
        self.button_frame = tkinter.Frame(self.window, width = 210, height = 540, borderwidth=0, highlightthickness=0,  bg='black')
        self.button_frame.grid(row=0, rowspan=2, column=2, sticky="nsew")
        ######## BUTTON FRAME ########

        ######## BUTTONS ########
        # Plate Recognition Buttton
        self.b_plate_recognition = tkinter.Button(self.button_frame, text="Plate Recognition", command= lambda: self.findPlates(self.log_frame))
        self.b_plate_recognition.pack(fill=tkinter.BOTH, expand=1)

        # Plate Information Buttton
        self.b_plate_information = tkinter.Button(self.button_frame, text="Plate Information", command= lambda: self.plateInfo(self.log_frame))
        self.b_plate_information.pack(fill=tkinter.BOTH, expand=1)

        # Stream Face ID Buttton
        self.b_stream_face = tkinter.Button(self.button_frame, text="Detect Video", command=self.detectVideo)
        self.b_stream_face.pack(fill=tkinter.BOTH, expand=1)

        # Stream Face ID Buttton
        self.b_detect_camera = tkinter.Button(self.button_frame, text="Detect Camera", command=self.detectCamera)
        self.b_detect_camera.pack(fill=tkinter.BOTH, expand=1)

        # Stream Image ID Buttton
        self.b_stream_image = tkinter.Button(self.button_frame, text="Detect Image", command= lambda: self.detectImage(self.log_frame))
        self.b_stream_image.pack(fill=tkinter.BOTH, expand=1)

        # Log Check Buttton
        self.b_log_check = tkinter.Button(self.button_frame, text="Log Check")
        self.b_log_check.pack(fill=tkinter.BOTH, expand=1)

        # Attach To Database Buttton
        self.b_attach_database = tkinter.Button(self.button_frame, text="Attach To Database")
        self.b_attach_database.pack(fill=tkinter.BOTH, expand=1)

        # Find People Buttton
        self.b_find_people = tkinter.Button(self.button_frame, text="Find People", command=self.searchPeople)
        self.b_find_people.pack(fill=tkinter.BOTH, expand=1)

        # Add People Buttton
        self.b_add_people = tkinter.Button(self.button_frame, text="Add People", command=self.addPeople)
        self.b_add_people.pack(fill=tkinter.BOTH, expand=1)

        # Access Plate Data Buttton
        self.b_access_plate_data = tkinter.Button(self.button_frame, text="Access Plate Data")
        self.b_access_plate_data.pack(fill=tkinter.BOTH, expand=1)

        # Cross Search Buttton
        self.b_cross_search = tkinter.Button(self.button_frame, text="Cross Search")
        self.b_cross_search.pack(fill=tkinter.BOTH, expand=1)
        ######## BUTTONS ########

        self.window.mainloop()
    
    def findPlates(self, log_frame):
        dump, textboxValue = finder.searchDB("J+ YSB 55")
        ########## LOGGING INFORMATION ##########
        # create a wrapper for log frame 
        wrapper = tkinter.Frame(log_frame, width = 1050, height = 180, borderwidth=0, highlightthickness=0, padx=10, pady=10, bg='black')
        wrapper.grid()
        wrapper.grid_propagate(0) #prevent frame from shrinking 
        info = tkinter.Label(wrapper, text=textboxValue, bg='black', fg='white') #display title
        info.grid()
        ########## LOGGING INFORMATION ##########

    # prints plate information to log
    def plateInfo(self, log_frame):
        index, dump = finder.searchDB("J+ YSB 55")
        plateInfo = finder.getData(index)
        ########## LOGGING INFORMATION ##########
        # create a wrapper for log frame 
        wrapper = tkinter.Frame(log_frame, width = 1050, height = 180, borderwidth=0, highlightthickness=0, padx=10, pady=10, bg='black')
        wrapper.grid()
        wrapper.grid_propagate(0) #prevent frame from shrinking 
        info = tkinter.Label(wrapper, text=plateInfo, bg='black', fg='white') #display title
        info.grid()
        ########## LOGGING INFORMATION ##########

    # detects people from videos and displays on the screen 
    def detectVideo(self):
        dc = detector.detector()
        dc.detectVideo(self.window, self.video_frame, self.log_frame)
    
    def detectCamera(self):
        dc = detector.detector()
        dc.detectCamera(self.window, self.video_frame, self.log_frame)

    # detects people from images and displays on the screen 
    def detectImage(self, log_frame):
        # open file dialog to select image
        filename =  tkinter.filedialog.askopenfilename(initialdir = os.getcwd(), title = "Select file", filetypes = (("jpeg files","*.jpg"),("png files","*.png*")))
        # run detector, returns names
        names = detector.detector().detectImage(filename, 'encodings.pickle')
        # open detected image and display it on the screen
        img = ImageTk.PhotoImage(Image.open('assets/output.png').resize((self.video_frame.winfo_width(),self.video_frame.winfo_height())))
        panel = tkinter.Label(self.video_frame, image = img, borderwidth=0, highlightthickness=0)
        panel.image = img # keep a reference!
        panel.grid()
        ########## LOGGING INFORMATION ##########
        # create a wrapper for log frame 
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

    def addPeople(self):
        db = database.database()
        db.addPeople()

    def searchPeople(self):
        db = database.database()
        db.searchPeople()