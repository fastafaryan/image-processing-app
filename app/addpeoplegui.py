
def addPeople():
	#window.withdraw()
    #create new window for input data
	new = Toplevel(bg="white")
	new.title('Add new person')
	new.geometry("450x320+500+180")
	new.resizable(0, 0)
    #create frame for window
	mainframe = Frame(new,bg="white")
	mainframe.grid(column = 0, row = 0, sticky = (N, W, E, S))
	mainframe.columnconfigure(0, weight = 1)
	mainframe.rowconfigure(0, weight = 1)
    #define variables to get them through GUI
	var_name = ""
	var_sname = ""
	var_ID = ""
	var_stat = ""
	var_height = ""
	var_age  = ""
	var_hair = ""
	var_country = ""
	var_nation= ""
	var_apperance=""
	var_sex=""
	var_weight=""
	var_eyes=""
	var_adress=""
    #create labels and entry labels for data
	Label(master=mainframe, text="Name", bg="white").grid(row = 0, column = 0)
	Entry(master=mainframe, width=50, textvariable=var_name).grid(row = 0, column = 1)
	Label(master=mainframe, text="Surname",bg="white").grid(row = 1,column = 0)
	Entry(master=mainframe, width=50,textvariable=var_sname).grid(row = 1,column = 1)
	Label(master=mainframe, text="ID",bg="white").grid(row = 2, column = 0)
	Entry(master=mainframe, width=50, textvariable=var_ID).grid(row = 2, column = 1) 
	Label(master=mainframe, text="Status",bg="white").grid(row = 3, column = 0)
	Entry(master=mainframe, width=50, textvariable=var_stat).grid(row= 3, column = 1) 
	Label(master=mainframe, text="Height",bg="white").grid(row = 4, column = 0)
	Entry(master=mainframe, width=50, textvariable=var_height).grid(row =4, column = 1)
	Label(master=mainframe, text="Age",bg="white").grid(row = 5, column = 0)
	Entry(master=mainframe, width=50, textvariable=var_age).grid(row =5, column = 1)
	Label(master=mainframe, text="Hair",bg="white").grid(row = 6, column = 0)
	Entry(master=mainframe, width=50, textvariable=var_hair).grid(row =6, column = 1)
	Label(master=mainframe, text="Country",bg="white").grid(row = 7, column = 0)
	Entry(master=mainframe, width=50, textvariable=var_country).grid(row =7, column = 1)
	Label(master=mainframe, text="Nation",bg="white").grid(row = 8, column = 0)
	Entry(master=mainframe, width=50, textvariable=var_nation).grid(row =8, column = 1)
	Label(master=mainframe, text="Apperance",bg="white").grid(row = 9, column = 0)
	Entry(master=mainframe, width=50, textvariable=var_apperance).grid(row =9, column = 1)
	Label(master=mainframe, text="Sex",bg="white").grid(row = 10, column = 0)
	Entry(master=mainframe, width=50, textvariable=var_sex).grid(row =10, column = 1)
	Label(master=mainframe, text="Weight",bg="white").grid(row = 11, column = 0)
	Entry(master=mainframe, width=50, textvariable=var_weight).grid(row =11, column = 1)
	Label(master=mainframe, text="Eyes",bg="white").grid(row = 12, column = 0)
	Entry(master=mainframe, width=50, textvariable=var_eyes).grid(row =12, column = 1)
	Label(master=mainframe, text="Adress",bg="white").grid(row = 12, column = 0)
	Entry(master=mainframe, width=50, textvariable=var_adress).grid(row =12, column = 1)
	#buttons for exit and add new person to database
	Button(mainframe, text = 'Add new person', command = add_to_db,bg="white").grid(row = 13, column = 1, sticky = W)
	Button(mainframe,text='Cancel',command=new.destroy,bg="white").grid(row = 13,column = 1,sticky = N)
def add_to_db():
	pass
