
texto = input("Informe um texto: ")

VOGAIS = "AEIOU"

# Exemplo utilizando um iteravel
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")

else:
    print()
    print("Executa no final do laço")


#exemplo com build-in range
for numero in range(0, 51, 5):
    print(numero, end=" ")    