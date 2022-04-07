# Index

#name = "LordTony" 
'''
name = "LordTony = 2547" 
# index ชื่อของตัวอักษร จะเริ่มต้นจาก 0
print(name[0:3]) 

print(name[-8:-2]) 
# ':' จะเอาตัวก่อนถึง ตำแหน่งสุดท้าย
# index จะนับช่องว่างด้วย
if name[0]== 'L':
    print('LLLLLLLLLLLL')
'''

#lenge funcrtion
'''
print(len(name))
#เช็คตำแหน่งข้อมูล ; ความยาว
'''
#strip
'''
print(len(name))
name=name.strip() 
print(len(name))
'''
#แปลง case
'''
print(name.upper())
print(name.lower())
print(name.capitalize())
'''
#replace
'''
ex_name = "Gun 1 is lordtony 1 1 1 1 1 1 1 1  "

print(ex_name.replace("1","2", 5)) # => ตามด้วยตำแหน่ง
'''
#check str
'''
ex_name = "Why Tony so handsome"

x = "Tony" in ex_name
y = "Why" in ex_name
print(x)
print(y)

if x:
    ex_name=ex_name.replace("Tony","Gun")
print(ex_name)
'''

#การต่อ string
'''
fname = "Lord"
lname = "Tony"
age = "17"

fullname = fname+lname+age
print("ชื่อต้น :"+ fname+"\nนามสกุล :"+lname+"\nอายุ : "+age)
'''

#การจัดรูปแบบการแสดงผล {}
'''
fname = "Lord"  # ตำแหน่งที่ 0
lname = "Tony"  # ตำแหน่งที่ 1
age = "17"      # ตำแหน่งที่ 2
salary = 500.321640

text = "ชื่อต้น: {2}\tนามสกุล: {1}\tอายุ: {0}\tอาชีพ: {3}\tเงินเดือน: {4:.2f}"
print(text.format(fname,lname,age ,"เกมเมอร์",salary))

'''

#นับจำนวนคำใน"ประโยค"
'''
fruit = "Hello my name is Gun. My nickname is Gun too."

print(fruit.count("Gun"))
'''

#เช็คคำขึ้นต้น
name = "นายเอกอนันต์ หล่อเท่"

print(name.startswith("นาย"))

if name.startswith("นาย"):
    print("เป็นผู้ชาย")
if name.endswith("หล่อ"):
    print("เป็นผู้หญิง")








