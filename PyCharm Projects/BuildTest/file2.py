import json,requests,openpyxl,os,datetime,logging

def updateIDs(wbActive):
    print("Updating ID's")
    updated=0
    timer=datetime.datetime.now()
    url="http://api.steampowered.com/ISteamApps/GetAppList/v0001/"
    response=requests.get(url)
    data=response.json()
    currentRow=2 #pra pular o header
    changed=False;
    while wbActive.cell(row=currentRow,column=1).value != None: #percorre todos os jogos ate encontrar uma linha vazia
        if wbActive.cell(row=currentRow,column=2).value == None: #se a coluna onde fica o id esta vazia
            changed=False
            for index in range(len(data['applist']['apps']['app'])):
                if wbActive.cell(row=currentRow,column=1).value == (data['applist']['apps']['app'][index]['name']):
                    updated=updated+1
                    changed=True
                    wbActive.cell(row=currentRow,column=2).value = str(data['applist']['apps']['app'][index]['appid'])
                    break
            if not changed:
                wbActive.cell(row=currentRow,column=2).value='Wrong Name'
        currentRow=currentRow+1
    print(str(updated)+" ID's updated in "+str(datetime.datetime.now()-timer)+" seconds.")
    return wbActive

def updatePrices(wbActive):
    print("Updating prices")
    timer=datetime.datetime.now()
    updated=0
    currentRow=2;
    while wbActive.cell(row=currentRow,column=1).value != None: #percorre todos os jogos ate encontrar uma linha vazia
        try:
            id=int(wbActive.cell(row=currentRow,column=2).value)
            id=str(id)
        except ValueError:
            currentRow=currentRow+1
            continue
        url="http://store.steampowered.com/api/appdetails?appids="+id
        response=requests.get(url)
        data=response.json()
        if data is not None:
            if data[id]['success']==True:

                price=str(data[id]['data']['price_overview']['final'])
                indexOfComma=len(price)-2
                if wbActive.cell(row=currentRow,column=5).value != str(price)[:indexOfComma]+","+str(price)[indexOfComma:]:
                    updated=updated+1
                    wbActive.cell(row=currentRow,column=5).value=str(price)[:indexOfComma]+","+str(price)[indexOfComma:]
                    wbActive.cell(row=currentRow,column=6).value=datetime.datetime.now()
        currentRow=currentRow+1
    print(str(updated)+" prices updated in "+str(datetime.datetime.now()-timer)+" seconds")
    return wbActive

def start():
    logging.basicConfig(level=logging.DEBUG,format='%(asctime)s %(levelname)-8s %(message)s',datefmt='%a, %d %b %Y %H:%M:%S',filename='/log.log',filemode='w')
    for file in os.listdir():
        if(file.endswith(".xlsx")):
            wb = openpyxl.load_workbook(file)
            activesheet=wb.active
            activesheet=updateIDs(activesheet)
            activesheet=updatePrices(activesheet)
            wb.save(file)

start()