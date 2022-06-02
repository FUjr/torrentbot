from pyparsing import col
from DB import DB
import openpyxl
workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.titel = 'PTBOT-pttime'

db = DB.DB()
data  = db.dump_table('pttime')
row = 2
for i in data:
    colunm = 1
    for j in i:
        worksheet.cell(row=row,column=colunm).value = j
        colunm += 1
    row += 1
workbook.save('pttime.xlsx')