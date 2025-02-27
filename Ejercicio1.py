
def longest_unique_substring(s):
    longitud = 0
    inicio = 0
    caracteres_utilizados = {}
    subcadena = ""

    for i, char in enumerate(s):
        if char in caracteres_utilizados and inicio <= caracteres_utilizados[char]:
            inicio = caracteres_utilizados[char] + 1
        else:
            if i - inicio + 1 > longitud:
                longitud = i - inicio + 1
                subcadena = s[inicio:i + 1]
        caracteres_utilizados[char] = i

    return subcadena

print( longest_unique_substring("abcabcbb") )
print( longest_unique_substring("abcdefgfhijklmnopqer"))
