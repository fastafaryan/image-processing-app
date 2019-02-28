import tkinter
import json
from AutoScrollbar import *

class database:

    def __init__(self):
        #define variables to get them through GUI
        self.firstname = tkinter.StringVar()
        self.lastname = tkinter.StringVar()
        self.ID = tkinter.StringVar()
        self.status = tkinter.StringVar()
        self.height = tkinter.StringVar()
        self.age  = tkinter.StringVar()
        self.hair = tkinter.StringVar()
        self.country = tkinter.StringVar()
        self.nation = tkinter.StringVar()
        self.apperance= tkinter.StringVar()
        self.sex = tkinter.StringVar()
        self.weight = tkinter.StringVar()
        self.eyes = tkinter.StringVar()
        self.address = tkinter.StringVar()
    
    ############ CREATES A POPUP TO ADD INFORMATION ############
    def addPeople(self):
        #create new window for input data
        new = tkinter.Toplevel(bg="white")
        new.title('Add new person')
        new.geometry("450x330+500+180")
        new.resizable(0, 0)
        #create frame for window
        mainframe = tkinter.Frame(new,bg="white")
        mainframe.grid(column = 0, row = 0, sticky = (tkinter.N, tkinter.W, tkinter.E, tkinter.S))
        mainframe.columnconfigure(0, weight = 1)
        mainframe.rowconfigure(0, weight = 1)

        #create labels and entry labels for data
        tkinter.Label(master=mainframe, text="Name", bg="white").grid(row = 0, column = 0)
        tkinter.Entry(master=mainframe, width=50, textvariable=self.firstname).grid(row = 0, column = 1)
        tkinter.Label(master=mainframe, text="Surname",bg="white").grid(row = 1,column = 0)
        tkinter.Entry(master=mainframe, width=50,textvariable=self.lastname).grid(row = 1,column = 1)
        tkinter.Label(master=mainframe, text="ID",bg="white").grid(row = 2, column = 0)
        tkinter.Entry(master=mainframe, width=50, textvariable=self.ID).grid(row = 2, column = 1) 
        tkinter.Label(master=mainframe, text="Status",bg="white").grid(row = 3, column = 0)
        tkinter.Entry(master=mainframe, width=50, textvariable=self.status).grid(row= 3, column = 1) 
        tkinter.Label(master=mainframe, text="Height",bg="white").grid(row = 4, column = 0)
        tkinter.Entry(master=mainframe, width=50, textvariable=self.height).grid(row =4, column = 1)
        tkinter.Label(master=mainframe, text="Age",bg="white").grid(row = 5, column = 0)
        tkinter.Entry(master=mainframe, width=50, textvariable=self.age).grid(row =5, column = 1)
        tkinter.Label(master=mainframe, text="Hair",bg="white").grid(row = 6, column = 0)
        tkinter.Entry(master=mainframe, width=50, textvariable=self.hair).grid(row =6, column = 1)
        tkinter.Label(master=mainframe, text="Country",bg="white").grid(row = 7, column = 0)
        tkinter.Entry(master=mainframe, width=50, textvariable=self.country).grid(row =7, column = 1)
        tkinter.Label(master=mainframe, text="Nation",bg="white").grid(row = 8, column = 0)
        tkinter.Entry(master=mainframe, width=50, textvariable=self.nation).grid(row =8, column = 1)
        tkinter.Label(master=mainframe, text="Apperance",bg="white").grid(row = 9, column = 0)
        tkinter.Entry(master=mainframe, width=50, textvariable=self.apperance).grid(row =9, column = 1)
        tkinter.Label(master=mainframe, text="Sex",bg="white").grid(row = 10, column = 0)
        tkinter.Entry(master=mainframe, width=50, textvariable=self.sex).grid(row =10, column = 1)
        tkinter.Label(master=mainframe, text="Weight",bg="white").grid(row = 11, column = 0)
        tkinter.Entry(master=mainframe, width=50, textvariable=self.weight).grid(row =11, column = 1)
        tkinter.Label(master=mainframe, text="Eyes",bg="white").grid(row = 12, column = 0)
        tkinter.Entry(master=mainframe, width=50, textvariable=self.eyes).grid(row =12, column = 1)
        tkinter.Label(master=mainframe, text="Address",bg="white").grid(row = 12, column = 0)
        tkinter.Entry(master=mainframe, width=50, textvariable=self.address).grid(row =12, column = 1)
        #buttons for exit and add new person to database
        tkinter.Button(mainframe, text = 'Add new person', command = lambda: self.addToDataBase(new) ,bg="white").grid(row = 13, column = 1, sticky = tkinter.W)
        tkinter.Button(mainframe,text='Cancel',command=new.destroy,bg="white").grid(row = 13,column = 1,sticky = tkinter.N)

    ############ APPENDS ENTERED VALUES TO JSON FILE ############
    def addToDataBase(self, oldFrame):
        print(self.firstname.get())
        _dict ={"firstname"  : self.firstname.get(),
                "lastname" : self.lastname.get(), "id" : self.ID.get()," status" : self.status.get(),
                "height" : self.height.get(),"age" : self.age.get(), "hair" : self.hair.get(),
                "country" : self.country.get(), "nation" : self.nation.get(),
                "apperance": self.apperance.get(), "sex": self.sex.get(),
                "weight": self.weight.get(), "eyes": self.eyes.get(),
                "address": self.address.get()
        }
        with open('data.json', 'r') as readfile:
                readdata = json.load(readfile)

        data = readdata
        #data['people'] = []
        data['people'].append(_dict)
        with open('data.json', 'w') as of:
                json.dump(data, of, indent=4)
                of.write("\n")

        ###### DISPLAY INSERTION IS EXECUTED PERFECTLY ######
        # destroy mainframe
        oldFrame.destroy()
        # create new window for input data
        popup = tkinter.Toplevel(bg="white")
        popup.title('New Person Is Added!')
        popup.geometry("450x330+500+180")
        popup.resizable(0, 0)
        container = tkinter.Frame(popup,bg="white")
        container.grid(column = 0, row = 0, sticky = (tkinter.N, tkinter.W, tkinter.E, tkinter.S))
        popup.columnconfigure(0, weight = 1)
        popup.rowconfigure(0, weight = 1)
        text = tkinter.Label(container, text="New person is added!", bg="white", font=("Helvetica", 16)).grid(row = 0, sticky = tkinter.N, padx=(125,125), pady=(100,100))
        button = tkinter.Button(container,text='Exit',command=popup.destroy,bg="blue", fg="white").grid(row = 1, sticky = tkinter.N, padx=(125,125))
        ###### DISPLAY INSERTION IS EXECUTED PERFECTLY ######


    #### CREATES A POPUP TO ADD INFORMATION
    def searchPeople(self):
        #create new window for input data
        new = tkinter.Toplevel(bg="white")
        new.title('Search Person')
        new.geometry("450x330+500+180")
        new.resizable(0, 0)
        #create frame for window
        mainframe = tkinter.Frame(new,bg="white")
        mainframe.grid(column = 0, row = 0, sticky = (tkinter.N, tkinter.W, tkinter.E, tkinter.S))
        mainframe.columnconfigure(0, weight = 1)
        mainframe.rowconfigure(0, weight = 1)

        #create labels and entry labels for data
        tkinter.Label(master=mainframe, text="Name", bg="white").grid(row = 0, column = 0)
        tkinter.Entry(master=mainframe, width=50, textvariable=self.firstname).grid(row = 0, column = 1)
        tkinter.Label(master=mainframe, text="Surname",bg="white").grid(row = 1,column = 0)
        tkinter.Entry(master=mainframe, width=50,textvariable=self.lastname).grid(row = 1,column = 1)
        tkinter.Label(master=mainframe, text="ID",bg="white").grid(row = 2, column = 0)
        tkinter.Entry(master=mainframe, width=50, textvariable=self.ID).grid(row = 2, column = 1) 
        tkinter.Label(master=mainframe, text="Status",bg="white").grid(row = 3, column = 0)
        tkinter.Entry(master=mainframe, width=50, textvariable=self.status).grid(row= 3, column = 1) 
        tkinter.Label(master=mainframe, text="Height",bg="white").grid(row = 4, column = 0)
        tkinter.Entry(master=mainframe, width=50, textvariable=self.height).grid(row =4, column = 1)
        tkinter.Label(master=mainframe, text="Age",bg="white").grid(row = 5, column = 0)
        tkinter.Entry(master=mainframe, width=50, textvariable=self.age).grid(row =5, column = 1)
        tkinter.Label(master=mainframe, text="Hair",bg="white").grid(row = 6, column = 0)
        tkinter.Entry(master=mainframe, width=50, textvariable=self.hair).grid(row =6, column = 1)
        tkinter.Label(master=mainframe, text="Country",bg="white").grid(row = 7, column = 0)
        tkinter.Entry(master=mainframe, width=50, textvariable=self.country).grid(row =7, column = 1)
        tkinter.Label(master=mainframe, text="Nation",bg="white").grid(row = 8, column = 0)
        tkinter.Entry(master=mainframe, width=50, textvariable=self.nation).grid(row =8, column = 1)
        tkinter.Label(master=mainframe, text="Apperance",bg="white").grid(row = 9, column = 0)
        tkinter.Entry(master=mainframe, width=50, textvariable=self.apperance).grid(row =9, column = 1)
        tkinter.Label(master=mainframe, text="Sex",bg="white").grid(row = 10, column = 0)
        tkinter.Entry(master=mainframe, width=50, textvariable=self.sex).grid(row =10, column = 1)
        tkinter.Label(master=mainframe, text="Weight",bg="white").grid(row = 11, column = 0)
        tkinter.Entry(master=mainframe, width=50, textvariable=self.weight).grid(row =11, column = 1)
        tkinter.Label(master=mainframe, text="Eyes",bg="white").grid(row = 12, column = 0)
        tkinter.Entry(master=mainframe, width=50, textvariable=self.eyes).grid(row =12, column = 1)
        tkinter.Label(master=mainframe, text="Address",bg="white").grid(row = 12, column = 0)
        tkinter.Entry(master=mainframe, width=50, textvariable=self.address).grid(row =12, column = 1)
        #buttons for exit and add new person to database
        tkinter.Button(mainframe, text = 'Search', command = lambda: self.searchDatabase(new) ,bg="white").grid(row = 13, column = 1, sticky = tkinter.W)
        tkinter.Button(mainframe,text='Cancel',command=new.destroy,bg="white").grid(row = 13,column = 1,sticky = tkinter.N)

    # Searches people from JSON file with respect to given entries
    def searchDatabase(self, oldFrame):
        # Load JSON file
        with open("data.json") as datafile:
            data = json.load(datafile)
        
        # Create a dictionary for entries
        dc = {
            "firstname" : self.firstname.get(),
            "lastname" : self.lastname.get(),
            "ID" : self.ID.get(),
            "status" : self.status.get(),
            "height" : self.height.get(),
            "age" : self.age.get(), 
            "hair" : self.hair.get(),
            "country" : self.country.get(), 
            "nation" : self.nation.get(),
            "apperance" : self.apperance.get(), 
            "sex" : self.sex.get(),
            "weight" : self.weight.get(), 
            "eyes" : self.eyes.get(),
            "address" : self.address.get()
        } 

        # Create a new dictionary which contains only defined entries
        definedValues = {}
        for key, value in dc.items():
            if(value):
                definedValues[key] = value
        
        # List to hold matched people
        matchedPeople = []
        # Loop over every person in the JSON data
        for person in data["people"]:
            # Controller variable to check if current person matches
            isMatched = True
            # Loop over defined values change isMatched variable to False if there is no match
            for key, value in definedValues.items():
                if (isMatched == False):
                    break
                if(person[key] != value):
                    isMatched = False
            # if there is a match append current person to matchedPeople list
            if(isMatched==True):
                matchedPeople.append(person)
        
        ###### DISPLAY INSERTION IS EXECUTED PERFECTLY ######
        # destroy mainframe
        oldFrame.destroy()
        # create new window for input data
        popup = tkinter.Toplevel(bg="white")
        popup.title('Search Results')
        popup.geometry("480x640+500+180")
        vscrollbar = AutoScrollbar(popup)
        vscrollbar.grid(row=0, column=1, sticky=tkinter.N+tkinter.S)
        canvas = Canvas(popup, yscrollcommand=vscrollbar.set, borderwidth=0, highlightthickness=0, bg="white")
        canvas.grid(row=0, column=0, sticky=tkinter.W+tkinter.N, padx=10)
        vscrollbar.config(command=canvas.yview)
        popup.grid_rowconfigure(0, weight=1)
        popup.grid_columnconfigure(0, weight=1)
        ###### DISPLAY INSERTION IS EXECUTED PERFECTLY ######

        # Print matched people to command line 
        for i, person in enumerate(matchedPeople):
            print(person)
            name = person["firstname"]+" "+person["lastname"]
            nameLabel = tkinter.Label(canvas, text=name, font=("Helvetica",16), bg="white").grid()
            for key,value in person.items():
                if key != "firstname" and key != "lastname": 
                    label = tkinter.Label(canvas,text=key+" : "+value, bg="white").grid()
                