import time

print("Informe o arquivo: (0 para sair): " )
nameFile = input()

tempo_inicial = (time.time())

if nameFile == "0":
    print("\nEncerrando...")
else:
    print("\nProcessando...")
    file = open(nameFile, "r")

    print("Caminho: ")

tempo_final = (time.time()) 
print("Tempo: " , tempo_final - tempo_inicial)
