
def verificar(s):
    s = s.lower()

    ocorrencias = s.count('a')

    if ocorrencias > 0:
        return f"A letra 'a' aparece {ocorrencias} vzs na string."
    else:
        return "A letra 'a' não foi encontrada na string."

string = input("Informe a palavra para verificar quantas vzs aparece a letra 'a': ")

resultado = verificar(string)

print(resultado)
