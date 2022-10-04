#con while
from audioop import avg
from builtins import print
from statistics import mean

cont = 1
list = []
while cont<=3:
    variab = (int)(input("Introduce un número"))
    list.append(variab)
    cont = cont + 1
print(list)
#con for
list2 = []
for cont2 in range(3):
    variab = (int)(input("Introduce un número"))
    list2.append(variab)
print(list2)
print(sum(list))
print(mean(list))
