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
            price=str(price)
            indexOfComma=len(price)-2
            priceConverted=str(price)[:indexOfComma]+","+str(price)[indexOfComma:]
            print("Price found for the game "+name+"("+id+"), price is "+priceConverted)
            return str(priceConverted)
        else:
            print("Could not find price for the game "+name+" with the id "+id)
            return False
    else:
        print("Could not find id for the game "+name)
        return False

def getNameFromTable(wbActive,row):
    wb = openpyxl.load_workbook(str(name)).active
    linha=2 #nao pega o primeiro pois é o header
    names=list()
    while wb['A'+str(linha)].value != None:
        names.append(str(wb['A'+str()].value))
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

def getValueFromName(name):
    price = getSteamPrice(name)
    if price is not False:
        return price
    else:
        return "N"

def start(tableName):
    wb = openpyxl.load_workbook(str(tableName))
    wbActive=wb.active
    currentRow=2 #pra pular o header
    while wbActive.cell(row=currentRow,column=1).value != None:
        gameName=wbActive.cell(row=currentRow,column=1).value
        value=getValueFromName(gameName)
        wbActive.cell(row=currentRow,column=5).value=value
        currentRow=currentRow+1
    wb.save(tableName)

start("jogos.xlsx")

