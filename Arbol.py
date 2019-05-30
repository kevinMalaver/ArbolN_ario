def numero_de_filas():
    fh = open("Laberinto.txt")
    x = len(fh.readlines())
    fh.close()
    return x
def leer_archivo():
    fh = open("Laberinto.txt")
    x = []
    for line in fh.read():
        y = [v for v in line.split()]
        if y != []:
            x.append(int(y[0]))
    fh.close()
    return x

x= leer_archivo()
filas = numero_de_filas()
print(x)
columnas = int(len(x) / filas)
print(columnas)
print(filas)