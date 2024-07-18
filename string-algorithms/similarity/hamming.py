texto1 = "cat"
texto2 = "dog"
c = 0

for i, j in zip(texto1, texto2):
    if i != j:
        c += 1

print(c)

