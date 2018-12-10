from pilha import Pilha

pilha_sem_max = Pilha()

# testando função inserir sem máximo de elementos
pilha_sem_max.inserir('Iron man')
pilha_sem_max.inserir('Thor')
pilha_sem_max.inserir('Spiderman')
print(pilha_sem_max)

# testando função inserir sem máximo de elementos
pilha_com_max = Pilha(max_tamanho=4)
pilha_com_max.inserir("It")
pilha_com_max.inserir('Red Rose')
pilha_com_max.inserir('The shinning')
pilha_com_max.inserir('Storm of century')
print(pilha_com_max)
# pilha_com_max.inserir("Stephen King")

# testando a remoção de elementos
for i in range(pilha_sem_max.tamanho()):
    print(pilha_sem_max.remover())
    # testando se a pilha está vazia
    if pilha_sem_max.vazia():
        print("--> Agora a pilha está vazia")

# testando se uma pilha com limite de elementos está cheia
if pilha_com_max.cheia():
    print('--> a pilha com limite de elementos está cheia.')

# testando a função topo de uma pilha
print(pilha_com_max.vertopo())

print("Removendo elementos")
for i in range(pilha_com_max.tamanho()):
    print(pilha_com_max.remover())
    if pilha_com_max.vazia():
        print('--> Agora pilha com limite de elementos está vazia.')
