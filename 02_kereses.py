"""
Az KERESÉS esetében azt vizsgáljuk, 
hogy szerepel-e egy bizonyos tulajdonságú elem az adatsorban (itt a listában),
és ha igen, hányadik helyen.

A program azt vizsgálja, hogy szerepel-e a piros szín a listában, és ha igen, hányadik helyen.
"""
lista = ['kék', 'zöld', 'piros', 'fehér', 'piros']

# talalat = False
# index = 0
# while index < len(lista) and not talalat:
#       if lista[index] == 'piros':
# 	        talalat = True
#       index = index + 1

# if talalat:
#       print('Van a listában piros szín, az indexe: ', index-1)
# else:
#       print('Nincs a listában piros szín.')

#megnézi van-e piros
if 'piros' in lista:
    print("A listában van piros szín.")
else:
    print("A listában nics piros.")

#megszámolja hány 'piros' van a listában
print(lista.count('piros'))

#'for' függvénnyel megszámolja hány 'piros' van a listában
mennyi = 0
for szin in lista:
    if szin == 'piros':
        mennyi += 1
print(f"A listában {mennyi} alkalommal szerepel a 'piros' szín.")

#for ciklus indexszel
how_many_times = 0
for index in range(len(lista)):
    if lista[index] == 'piros':
        how_many_times += 1
print(f"Ennyiszer fordul elő a 'piros' szín a listában: {how_many_times}")