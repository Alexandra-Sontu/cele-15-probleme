"""La un concurs se dau ca premii primilor 100 de concurenţi, tricouri de culoare albă, roşie, albastră şi neagră, în această
secvenţă. Ionel este pe locul x. Ce culoare va avea tricoul pe care-l va primi? Exemplu : date de intrare : x=38 date de ieşire :
rosie"""
a=int(input("Locul ocupat de Ionel"))
if a>100:
    print("Nu primeste tricou")
elif a%4==1:
    print("alba")
elif a%4==2:
    print("rosie")
elif a%4==3:
    print("albastra")
else:
    print("neagra")