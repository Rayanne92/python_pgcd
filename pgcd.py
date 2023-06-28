def PGCD(a,b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

a = int(input("Entrer la valeur de a : "))
b = int(input("Entrer la valeur de b : "))

print("Le PGCD de : ", a, "et le PGCD de : ", b, "est : ", PGCD(a,b))