"""Cunoscând data curentă exprimată prin trei numere întregi reprezentând anul, luna, ziua precum şi data naşterii unei persoane,
exprimată la fel, să se facă un program care să calculeze vârsta persoanei respective în număr de ani împliniţi. Exemplu : Date
de intrare data curenta 2005 10 25 data nasterii 1960 11 2 Date de ieşre 44 ani."""
ac=int(input("Anul Curent"))
lc=int(input("Luna Curenta"))
zc=int(input("Ziua Curenta"))
an=int(input("Anul Nasterii"))
ln=int(input("Luna Nasterii"))
zn=int(input("Ziua Nasterii"))
if ln>lc:
    print((ac-an)+1,"Ani")
else:
    print(ac-an,"Ani")