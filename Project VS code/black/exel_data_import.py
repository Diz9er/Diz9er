import xlrd, xlwt

rb = xlrd.open_workbook('C:/Users/Univer/Desktop/FIO_for_BD/spis_FIO.xlsx')
sheet = rb.sheet_by_index(0)
x=0
y=0
while True:
    val = sheet.row_values(x)[y]
    print(val)
    y+=1
    if y>2:
        x+=1
        y=0
    if x > 100:
        break
