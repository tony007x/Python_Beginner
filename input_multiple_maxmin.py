box =[]

while True:
    num = int(input("ป้อนต้วเลข (พิมพ์ 0 เพื่อหยุด): "))
    if num == 0:
        break
    box.append(num)

check = input("Min or Max: ")
check = check.upper()

if check == "MIN":
    box.sort()
    print(*box)
elif check == "MAX":
    box.sort(reverse=True)
    print(*box)