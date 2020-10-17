"""Într-o tabără, băieţii sunt cazaţi câte 4 într-o căsuţă, în ordinea sosirii. Ionel a sosit al n-lea. În a câta căsuţă se va afla?
Exemplu : date de intrare : n=69 date de ieşire : casuta 17."""
a=int(input("Ionel a sosit al:"))
if a<=4:
    print("Ionel va fi cazat in casuta 1")
else:
    print("Ionel va fi cazat in casuta",(a//4)+1)