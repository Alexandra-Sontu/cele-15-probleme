"""Elevii clasei a V-a se repartizează în clase câte 25 în ordinea mediilor clasei a IV-a. Radu este pe locul x în ordinea mediilor. În
ce clasa va fi repartizat (A, B, C, D sau E)?. Exemplu : date de intrare : x=73 date de ieşire : C."""
a=int(input("Radu e pe locul"))
if a//25==0:
    print("A")
elif a//25==1:
    print("B")
elif a//25==2:
    print("C")
elif a//25==3:
    print("D")
else:
    print("E")