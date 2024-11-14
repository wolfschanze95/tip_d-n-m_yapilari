a=5
b="a"
c="55"
d=0.5
str(c) # 55
bool(b) # True
int(a) # 5
float(d) # 0.5



"HESAP MAKİNESİ"
sayi1=input("lütfen değer girin=")
sayi2=input("lütfen değer girin=")
a=float(sayi1)
b=float(sayi2)
print("toplam",a+b)
print("fark",a-b)
print("çarpım",a*b)
print("üssü",a**b)
print("bölüm",a/b)

"İKİ NOKTA ARASI UZAKLIK"
x1=int(input("lütfen x1 gir"))
x2=int(input("lütfen x2 gir"))
y1=int(input("lütfen y1 gir"))
y2=int(input("lütfen y2 gir"))
formul=((x1-x2)**2+(y1+y2)**2)**0.5
print("karekök içinde {}-{}`nin karesi+ {}+{}`nin karesi:{}".format(x1,x2,y1,y2,formul))
