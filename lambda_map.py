#map() functions

numbers = [1,2,3,4] #raqamlar nomli ro'yxat
squared = map(lambda x: x**2,numbers)#sonning kvadratini hisoblaymiz
result = list(squared)# Map obyektini oddiy ro'yxatga aylantirib, natijani 'result'ga saqlaymiz
print(result) #natijani konsolga chiqarish
#[1,4,9,16
