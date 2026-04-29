# import functools
#
# from more_itertools.more import repeat_last
# from numpy.ma.core import repeat
#
# lis=[1,3,5,6,2]
# print("The sum of the list elements is : ", end="")
# print(functools.reduce(lambda a,b:a+b,lis))
# print("The maximum element of the list is : ", end="")
# print(functools.reduce(lambda a,b:a if a>b else b,lis))

# Ex 1

# def determina_castigator(j1, j2):
#     if j1 == j2:
#         return "Egalitate!"
#
#     if (j1 == "piatra" and j2 == "foarfeca") or \
#             (j1 == "foarfeca" and j2 == "hartie") or \
#             (j1 == "hartie" and j2 == "piatra"):
#         return "Jucatorul 1 castiga!"
#     else:
#         return "Jucatorul 2 castiga!"
#
#
# def joc():
#     while True:
#         print("\n Piatra-Hartie-Foarfeca")
#
#         jucator1 = input("Jucatorul 1 : (piatra, hartie, foarfeca): ").lower()
#         jucator2 = input("Jucatorul 2 : (piatra, hartie, foarfeca): ").lower()
#
#         optiuni_valide = ["piatra", "hartie", "foarfeca"]
#
#
#         rezultat = determina_castigator(jucator1, jucator2)
#         print(rezultat)
#
#         break
#
#
# joc()


# Ex 2

# def genereaza_factura(nume_client, **produse):
#     print(f"\nFactura lui: {nume_client}")
#     print("-" * 30)
#
#     total = 0
#
#     for produs, pret in produse.items():
#         print(f"{produs}: {pret} lei")
#         total += pret
#
#     print("-" * 30)
#     print(f"Total de plata: {total} lei")
#
#
#
# genereaza_factura(
#     "Andi",
#     paine=5,
#     lapte=7,
#     oua=12,
#     mere=10
# )
#
#

# Ex 4

# square_list = lambda lst: list(map(lambda x: x**2, lst))
#
# my_list = [5, 6, 8]
# result = square_list(my_list)
# print(result)

# Ex 5

# a = [(0, 2), (4, 3), (9, 9), (10, -1)]
#
# sorted_a = sorted(a, key=lambda x: x[1])
#
# print(sorted_a)

# Ex 6

# intreg_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#
# even_list = list(filter(lambda x: x % 2 == 0, intreg_list))
# odd_list = list(filter(lambda x: x % 2 != 0, intreg_list))
#
# print("Numere pare:", even_list)
# print("Numere impare:", odd_list)

# Ex 7

# pretprod_list=[50,70,20,10,None,None,100]
#
# filtru_list=list(filter(lambda x: x !=None, pretprod_list))
# print(filtru_list)
#
# reducere_list=[x*0.9 for x in filtru_list]
# print(reducere_list)

# Ex 8

# data = "2023-04-24 09:03:32.744178"
#
# extrage = lambda x: (x.split(" ")[0].split("-")[0],  # an
#                      x.split(" ")[0].split("-")[1],  # luna
#                      x.split(" ")[0].split("-")[2],  # zi
#                      x.split(" ")[1])               # ora
#
# an, luna, zi, ora = extrage(data)
#
# print("an:",an)
# print("luna=",luna)
# print("zi=",zi)
# print("ora=",ora)

# Ex 9

# def sum_lists(list1, list2):
#     return [a + b for a, b in zip(list1, list2)]
#
# list1 = [1, 2, 3, 4, 5]
# list2 = [10, 20, 30, 40, 50]
#
# result = sum_lists(list1, list2)
# print(result)

#Ex 10

# pare = [x for x in range(0, 101) if x % 2 == 0]
# print(pare)
# cuburi = [x**3 for x in range(1, 11)]
# print(cuburi)
# list1 = [1, 2, 3, 4, 5]
# list2 = [4, 5, 6, 7, 8]
#
# comune = [x for x in list1 if x in list2]
# print(comune)

# Ex 11

# pare = {x for x in range(0, 20) if x % 2 == 0}
# print(pare)
# text = "programare python"
#
# litere = {c for c in text if c != " "}
# print(litere)
# text = "Invatam programare in Python lejer"
#
# cuvinte = {cuv for cuv in text.split() if len(cuv) >= 5}
# print(cuvinte)

#
# Ex 12

sq = {x: x**2 for x in range(1, 11)}
print(sq)
text = "programare python"

freq = {c: text.count(c) for c in text if c != " "}
print(freq)
divi = {x: [d for d in range(1, x+1) if x % d == 0] for x in range(1, 11)}
print(divi)






