name = []
year_born = []
Gender = []
year = 2017
s = str(')')
i = len(name)
i = int(input())
while True:
    _name = input()
    yb = int(input())
    yb=2017-yb
    yb=str(yb)
    year_born.append(yb)
    GenD = input()
    GenD.capitalize()
    Gender.append(GenD)
    name.append(_name)
    if len(name)==i:
        break
print("--Customers Information--")
for x in range(0,len(name)):
    print(name[x],"(age :",year_born[x]+")")
    x+=1
    if x==len(name):
        break