#Andrus Correa Web A

def cesar(letra, clave):
    m_descifrado = ""
    for alfabeto in letra:
        if alfabeto.isalpha():
            n = ord(alfabeto)
            n -= clave
            if alfabeto.isupper():
                if n < ord('A'):
                    n += 26
            else:
                if n < ord('a'):
                    n += 26
            alfabeto_descifrado = chr(n)
            m_descifrado += alfabeto_descifrado
        else:
            m_descifrado += alfabeto
    return m_descifrado

m_codificado = input("Escribir el mensaje codificado: ")
clave = int(input("Digite la clave: "))
m_descifrado = cesar(m_codificado, clave)
print("El mensaje decifrado es: " ,m_descifrado) 

