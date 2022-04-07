list = []

while True:
    num = int(input("ป้อนตัวเลข(พิมพ์ 0 เพื่อหยุด): "))
    if num == 0:
        break
    list.append(num)
print("ข้อมูล: ",list)
print("จำนวนที่มากที่สุด: ",max(list))