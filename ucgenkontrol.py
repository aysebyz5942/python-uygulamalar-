def ucgenmi(a,b,hipotenus):
    if a**2+b**2==hipotenus**2:
        return "bu bir üçgendir!!!"
    else:
        return "bu bir ucgen değildir."

print(ucgenmi(3,4,5))
print(ucgenmi(3,4,6))