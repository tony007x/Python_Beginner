box = []
num1 = int(input("ค่ากำหนดlen: "))
while True:
    len_box = num1
    break
while len_box == num1:
    n = int(input("ข้อมูล: "))
    box.append(n)
    if len(box)==num1:
        break
box.sort(reverse=True)
for i in range(0,len(box)):
    print(box[i])

