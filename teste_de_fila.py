from fila import Fila

fila_sem_max = Fila()

# testando inserir em fila sem maximo de elementos definidos.
print("fila sem maximo de elementos definidos")
fila_sem_max.inserir("Joker")
fila_sem_max.inserir("Bruce Wayne")
fila_sem_max.inserir("James Gordon")
fila_sem_max.inserir("Selina")
print(fila_sem_max)


# testando inserir em fila com maximo de elementos definidos.
fila_com_max = Fila(max_tamanho=5)
fila_com_max.inserir("Comedian")
fila_com_max.inserir("Spectral")
fila_com_max.inserir("Sally Jupiter")
fila_com_max.inserir("Roschach")
fila_com_max.inserir("Night Owl")
print("fila com maximo de elementos definidos")
print(fila_com_max)

try:
    fila_com_max.inserir("Manhattan")
except Exception:
    print("A fila está cheia")


for i in range(fila_sem_max.tamanho()):
    print(fila_sem_max.remover())
