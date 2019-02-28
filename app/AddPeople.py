import json
path = "Database/People"

def addPeople():
        _name       = input("Name: ")
        _sname      = input("Surname: ")
        _id         = input("ID: ")
        _stat       = input("Status: ")
        _height     = input("Height: ")
        _age        = input("Age: ")
        _hair       = input("Hair Color: ")
        _country    = input("Current Country:")
        _nation     = input("Nationality:")
        _appearance = input("Apperance:")
        _sex        = input("Sex:")
        _weight     = input("Weight:")
        _eyes       = input("Color of eyes:")
        _adress     = input("Address:")

        _dict ={"name"  : _name,
                "sname" :_sname,"id" :_id,"status" :_stat,
                "height" :_height,"age" :_age,"hair" :_hair,
                "country" :_country, "nation" : _nation,
                "apperance":_appearance, "sex":_sex,
                "weight":_weight, "eyes":_eyes,
                "address":_adress
        }
        with open('data.json', 'r') as readfile:
                readdata = json.load(readfile)

        data = readdata
        #data['people'] = []
        data['people'].append(_dict)
        with open('data.json', 'w') as of:
                json.dump(data, of, indent=4)
                of.write("\n")

addPeople()