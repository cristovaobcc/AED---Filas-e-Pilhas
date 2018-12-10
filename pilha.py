import collections


class Pilha:

    # inicializador/construtor da pilha
    def __init__(self, seq=None, max_tamanho = 0):
        # atributos privados
        self.__topo = None
        self.__tamanho = 0
        self.__max = max_tamanho  # tamanho máximo da pilha
        self.__erroindice = 'índice fora dos limites da pilha'
        self.__erropilhacheia = 'a pilha está cheia'
        self.__erropilhavazia = 'a pilha está vazia'
        self.__iterando = None  # auxiliar para iterar com lazy evaluation


        # se o objeto passado no construtor for iterável
        # pegar os elementos e jogar dentro da lista.
        if seq is not None and isinstance(seq, collections.Iterable):
            for e in seq:
                self.inserir(e)
        elif seq is not None:  # não é iterável
            raise TypeError('o objeto fornecido não é iterável')


    def __iter__(self):
        return self

    def __next__(self):  # percorre a pilha aplicando o conceito de lazy evaluation.
        if self.__iterando is None:
            self.__iterando = self.__topo
        else:
            self.__iterando = self.__iterando.proximo
        if self.__iterando is not None:
            return self.__iterando.conteudo
        raise StopIteration

    # classe interna para representar cada elemento (nó)
    class No:
        # inicializador/construtor de cada nó
        def __init__(self, conteudo):
            self.conteudo = conteudo
            self.proximo = None


    # devolve a quantidade de elementos da pilha
    def __len__(self):
        return self.__tamanho

    # devolve a pilha em formato de string em sua forma bruta!
    def __str__(self):
        retorno = '-> '
        for i, e in enumerate(self):
            retorno += e.__repr__() # O repr aqui permite uma representação bruta no elemento da lista
            if i < len(self) - 1:
                retorno += ', '

        retorno += ' <-'
        return retorno

    def __repr__(self):
        return self.__str__()

    # Inserir no topo da pilha
    def inserir(self, conteudo):
        novo = self.No(conteudo)

        # se o topo é nulo, a pilha está vazia. Então o elemento é inserido.
        if self.__topo is None:
            self.__topo = novo
        # caso o tamanho máximo seja limitado, verifique se é possível inserir o elemento.
        elif self.__max != 0:
            if self.__tamanho < self.__max:
                novo.proximo = self.__topo
                self.__topo = novo
            else:
                raise Exception(self.__erropilhacheia)

        else:  # caso não haja tamanho máximo de pilha, insira o elemento novo.
            novo.proximo = self.__topo
            self.__topo = novo

        self.__iterando = None
        self.__tamanho += 1


    #  Remove o elemento que se encontra no topo da pilha e o devolve à função que o chamou.
    def remover(self):
        if self.__topo is not None:
            elemento = self.__topo
            self.__topo = self.__topo.proximo
            elemento.proximo = None
            return elemento.conteudo
        else:
            raise Exception(self.__erropilhavazia)


    # Verifica quem é o topo da pilha e devolve o conteúdo do topo. Se vazio, devolve None.
    def vertopo(self):
        if self.__topo != None:
            return self.__topo.conteudo
        else:
            return self.__topo

    # se a pilha está vazia, devolve True. Caso contrário, False.
    def vazia(self):
        if self.__topo == None:
            return True
        else:
            return False

    # se a pilha estiver cheia, devolve True. Caso contrário, False.
    # caso a pilha não tenha tamanho limitado, então nunca estará cheia.
    def cheia(self):
        if self.__tamanho == self.__max and self.__max != 0:
            return True
        else:
            return False

    def tamanho(self):
        return self.__tamanho