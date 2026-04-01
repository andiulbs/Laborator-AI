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

def genereaza_factura(nume_client, **produse):
    print(f"\nFactura lui: {nume_client}")
    print("-" * 30)

    total = 0

    for produs, pret in produse.items():
        print(f"{produs}: {pret} lei")
        total += pret

    print("-" * 30)
    print(f"Total de plata: {total} lei")



genereaza_factura(
    "Andi",
    paine=5,
    lapte=7,
    oua=12,
    mere=10
)




