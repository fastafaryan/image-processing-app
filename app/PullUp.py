import json
from pprint import pprint
''' reads json file and picks the wanted datas'''

'''can search separeta datas by order
		_name
		_sname      
		_id        
		_stat       
		_height     
		_age       
		_hair       
		_country    
		_nation     
		_appearance 
		_sex        
		_weight     
		_eyes       
		_adress
'''
#search given dictionary for finding wanted data(_data) in dictionary(data) type-> key value in dictionary
def searchDict(_data, data, _type):
	indicator = []
	for key in data['people'][::]:
		if _data in key["{}".format(_type)]:
			indicator.append(key["id"])
	return indicator
#use searchDict funtion for every key
def sbyName(_pname, data):
	nlist = searchDict(_pname, data, "name")
	return nlist

def sbySName(_psname,data):
	nlist = searchDict(_psname, data, "sname")
	return nlist

def sbyID(_pid,data):
	nlist = searchDict(_pid, data, "id")
	return nlist

def sbyStat(_pstat,data):
	nlist = searchDict(_pstat, data, "status")
	return nlist

def sbyHeight(_ph,data):
	nlist = searchDict(_ph, data, "height")
	return nlist

def sbyAge(_page,data):
	nlist = searchDict(_page, data, "age")
	return nlist

def sbyHair(_phair,data):
	nlist = searchDict(_phair, data, "hair")
	return nlist

def sbyCountry(_pcountry,data):
	nlist = searchDict(_pcountry, data, "country")
	return nlist

def sbyNation(_pnat,data):
	nlist = searchDict(_pnat, data, "nation")
	return nlist

def sbyApperance(_papp,data):
	nlist = searchDict(_papp, data, "apperance")
	return nlist

def sbySex(_ps,data):
	nlist = searchDict(_ps, data, "sex")
	return nlist

def sbyWeight(_pw,data):
	nlist = searchDict(_pw, data, "weight")
	return nlist

def sbyEyes(_pey,data):
	nlist = searchDict(_pey, data, "eyes")
	return nlist

def sbyAdress(_pad,data):
	nlist = searchDict(_pad, data, "address")
	return nlist

#for multiple given inputs get max coupling to decide searched person
def croSSSearch(_pname=None, _psname=None, _pid=None,
				_pstat=None, _ph=None, _age=None, _phair=None,
				_pc=None, _pnat=None, _papp=None, _ps=None,
				_pw=None, _pe=None, _pad=None):
				pass

def strikeOut(idlist):
	pass

def main():
	#this will change due to linkage btw GUI and .json asked data
	inputData=["Fatih","Koc","13219581","Normal","171","22","Green","Turkey","Suri", "White","Male","11", "Blue","ZB"]
	#open the json file and scan it into "data"
	with open("data.json") as datafile:
		data = json.load(datafile)

	#data types that json includes in dict
	dataType = ["name", "sname", "id", "status", "height", "age", "hair", "country", "nation", "nation", "apperance", "sex", "weight", "eyes", "address"]
	
	#decide search type
	#input data >1   ->> multiple search(data, type=input)
	#input data == 1 ->> just call needed search function(data, type, inputdata)
	#inputData[N] N->14
	datalist = [""]*14
	for i in range(14):
		ask = inputData[i]
		datalist[i] =searchDict(ask, data, dataType[i])
		#print("ask:",ask)
		#print("datalist i:",datalist[i])

	idlist = datalist[2]
	
	d1list =[]
	#if persons ID is given and .json has it -> exact match
	if idlist != None:
		personID = searchDict(inputData[2], data, "id")
		personID = personID[0]
	for key in data["people"]:
		if personID in key["id"]:
			print(key)##SEARCHED PERSON DATA

	for k in datalist:
		for i in k:
			#print(i)
			d1list.append(i)
	counter=[0]*len(d1list)
	person=[0]*len(d1list)
	for i in range(len(d1list)):
		stone = d1list[i]
		for j in d1list:
			if stone == j:
				counter[i] +=1    #hit number for each data
				person[i]=stone	  #couple hit numbers and data pos.
	print(counter)
	print(person)
	#determine the positions of max hits 
	m = max(counter)
	f = [i for i, j in enumerate(counter) if j == m]
	print(f)
	print(counter.index(max(counter)))





if __name__=="__main__":
	main()
	