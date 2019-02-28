#Created by Ali AKDEMİR
#Verilen plaka için tam eşleşme arar
#Tam eşleşme databasede bulunamadıysa benzer plakayı arar
#Plaka üzerine kayıtlı logu bulur
def searchDB(plate):
    matchCon=False
    with open('Database/archieve-plate.txt') as file:
        file_contents = file.read()
        saved = file_contents.split('\n')
    #print(saved)

    # make a loop that counts the hit numbers and decide possible match
    starter = list(plate)
    listsaved = list(file_contents)
    
    if matchCon == False:
        #for perfect matching
        i, indexhash=0,0
        for item in saved:
            i+=1
            if (item.find(plate)) != -1:
                print ('{0}. sirada bulunan plaka eslesmesi {1} '.format(i,item))#matched plate and its place
                indexhash=i #indexhash helps getting index of report from txt that includes report indexes which we need to get wanted report

    if matchCon == False:
        #for suitable match
        count= [0] * len(saved)
        for i in range(len(saved)):
            x = len(saved[i])
            if len(starter) > len(saved[i]):
                x = len(starter)
            for j in range(x):
                if starter[j] == saved[i][j]:
                    count[i]+=1
        #print(max(count))
        it=0
        for i in range(len(count)):
            if count[i] == max(count):
                it = i
        
        print("Tahmini plaka eslesmesi: {}".format(saved[it]))
    #return saved[it]
    return indexhash, saved[it]

def getData(indexhash):
    #print(indexhash)
    #find index of report using indexhash
    with open('Database/hash-plate.txt') as file1:
        fileCo = file1.read()
        fileCo = fileCo.split("\n")
        #print(fileCo)
        indexreport = fileCo[indexhash-1]
        #print(indexreport)

    #find reports from reports folder and print if neccesary return it for wanted places
    with open('Database/reports/{}.txt'.format(indexreport)) as file2:
        report3x = file2.read()
        #print(report3x)
        return report3x


'''if __name__ == "__main__":
    indexofplate = searchDB("34 Byh 55")
    getData(indexofplate)'''