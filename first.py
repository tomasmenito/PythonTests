import requests
import openpyxl
res= requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
#for chunk in res.iter_content(100000):
    #print(chunk)


wb = openpyxl.load_workbook('s.xlsx')
print(wb.get_sheet_names())
sheet = wb.active
print(sheet)
print(sheet['C3'].value)

