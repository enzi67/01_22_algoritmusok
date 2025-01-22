"""Az ELDÖNTÉS esetében azt vizsgáljuk,
hogy szerepel-e egy bizonyos tulajdonságú elem az adatsorban (itt a listában).
A program azt vizsgálja, hogy van-e hárommal osztható szám a listában.
"""
lista = [2, 5, 4, 8, 9, 11, 10, 12, 15]
oszthato = []
# szam = []

index = 0
# if szam in szamok % 3 == 0:
#     print(f"Ez a szám:{szam} osztható hárommal")
while index < len(lista):
    if lista[index] % 3 == 0:
        oszthato.append(lista[index])
    index = index + 1

if oszthato == []:
     print('Van a listában hárommal osztható szám.', oszthato)
else:
       print('Nincs a listában hárommal osztható szám.')