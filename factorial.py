def factorial(n):
    num = 1
    while n >= 1:
        num = num * n
        n = n - 1
    return num

n = int(input("ป้อนตัวเลข: "))
f =factorial(n)
print(f)