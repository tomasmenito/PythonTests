import json,requests,openpyxl

def findIdByName(name):
    url="http://api.steampowered.com/ISteamApps/GetAppList/v0001/"
    response=requests.get(url)
    data=response.json()
    for index in range(len(data['applist']['apps']['app'])):
        if data['applist']['apps']['app'][index]['name'] == name:
            return str(data['applist']['apps']['app'][index]['appid'])
    return False

def findPriceById(id):
    url="http://store.steampowered.com/api/appdetails?appids="+str(id)
    response=requests.get(url)
    data=response.json()
    if data is not None:
        if data[id]['success']==True:
            return str(data[id]['data']['price_overview']['final'])
    return False

def getSteamPrice(name):
    id=findIdByName(name)
    if id is not False:
        price = findPriceById(id)
        if price is not False:
            print("Price found for the game "+name+"("+id+"), price is "+str(price))
            return str(price)
        else:
            print("Could not find price for the game "+name+" with the id "+id)
            return False
    else:
        print("Could not find id for the game "+name)
        return False

def getNamesFromTable(name):
    wb = openpyxl.load_workbook(str(name)).active
    linha=2 #nao pega o primeiro pois é o header
    names=list()
    while wb['A'+str(linha)].value != None:
        names.append(str(wb['A'+str(linha)].value))
        linha=linha+1
    return names

def setValuesOnTable(values,name):
    wb = openpyxl.load_workbook(str(name))
    wbActive = wb.active
    currentRow=2
    for value in values:
        wbActive.cell(row=currentRow,column=5).value=value
        currentRow=currentRow+1
    wb.save(name)

def getValuesFromNames(names):
    values=list()
    for name in names:
        price = getSteamPrice(name)
        if price is not False:
            values.append(price)
        else:
            values.append("N")
    return values

names = getNamesFromTable("jogos.xlsx") #lista de nomes
values = getValuesFromNames(names)  #lista de valores
setValuesOnTable(values,"jogos.xlsx")

'''    
setValuesOnTable(values,"jogos.xlsx")
#print(getNamesFromTable("jogos.xlsx"))
   
if getSteamPrice("Toren") is not False:
    print(getSteamPrice("Toren"))

wb = openpyxl.load_workbook('jogos.xlsx').active
linha=1
while wb['A'+str(linha)].value != None:
    name= str(wb['A'+str(linha)].value)
    linha=linha+1
    url="http://api.steampowered.com/ISteamApps/GetAppList/v0001/"
    response=requests.get(url)
    data=response.json()
    id=""
    for index in range(len(data['applist']['apps']['app'])):
        if data['applist']['apps']['app'][index]['name'] == name:
            print("achou o jogo " + name)
            id=str(data['applist']['apps']['app'][index]['appid'])
    url="http://store.steampowered.com/api/appdetails?appids="+id
    response=requests.get(url)
    data=response.json()
    if data is not None:
        if data[id]['success']==True:
            print ("O preco do jogo "+name+" é "+str(data[id]['data']['price_overview']['final']))
'''
