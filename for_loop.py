list  = ["Tahsin","Sumiya","Rajib","Eva","Tamim","Rakib","Nirob","Al_Amin","Shakhor","Onik","Shamim","Ujjal","Sahariyar","Maruf","Milom","Emon","Jet","Riyad","Yeashin"]

for x in list:
    print(x)

test = ["Thsin","Sumiya","Razib","Eva"]

for x in test:
    print(x)
    if x == "Razib":
        break

name = ["tAhSin","SuMiYa","EvA","rAzIb"]

for x in name:
    if x == "SuMiYa":
        continue
    print(x)

for x in range(2,5):
    print(x)

for x in range(0 ,100 ,5):
    print(x)

x = ["razib","shakil","shagor","hamim","jubayer"]
y = ["sompa","masuam","mukta","suma"]

for A in x:
    for B in y:
        print(A,B)
