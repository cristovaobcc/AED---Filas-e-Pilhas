import collections

class Fila:

    # inicializador/construtor da fila
    def __init__(self, seq = None, max_tamanho = 0):
        # atributos privados
        self.__inicio = None
        self.__fim = self.__inicio
        self.__tamanho = 0
        self.__max = max_tamanho # tamanho máximo da fila
        self.__errofilacheia = 'a fila está cheia'
        self.__errofilavazia = 'a fila está vazia'
        self.__iterando = None  # auxiliar para iterar com lazy evaluation

        # se o objeto passado no construtor for iterável
        # pegar os elementos e jogar na fila.
        if seq is not None and isinstance(seq, collections.Iterable):
            for e in seq:
                self.inserir(e)
        elif seq is not None: # não é iterável
            raise TypeError('o objeto fornecido não é iterável')

    def __iter__(self):
        return self

    def __next__(self):
        if self.__iterando is None:
            self.__iterando = self.__inicio
        else:
            self.__iterando = self.__iterando.proximo
        if self.__iterando is not None:
            return self.__iterando.conteudo
        raise StopIteration

    # classe interna para representar um nó
    class No:
        # inicializador/construtor do nó
        def __init__(self, conteudo):
            self.conteudo = conteudo
            self.proximo = None

    def __len__(self):
        return self.__tamanho

    def __str__(self):
        retorno = '-> '
        for i, e in enumerate(self):
            retorno += e.__repr__()  # o repr aqui permite uma representação bruta no elemento da lista
            if i < len(self) - 1:
                retorno += ', '

        retorno += ' <-'
        return retorno

    def __repr__(self):
        return self.__str__()

    def tamanho(self):
        return self.__tamanho

    def vazia(self):
        if self.__inicio == None:
            return True
        else:
            return False
    def cheia(self):
        if self.__tamanho == self.__max and self.__max != 0:
            return True
        else:
            return False

    def inserir(self, conteudo):
        novo = self.No(conteudo)

        if self.__inicio == self.__fim and self.__tamanho == 0:
            self.__inicio = self.__fim = novo
        # caso o tamanho máximo seja limitado, verifique se é possível inserir o elemento
        elif self.__max != 0:
            if self.__tamanho < self.__max:
                self.__fim.proximo = novo
                self.__fim = novo
            else:
                raise Exception(self.__errofilacheia)

        else:
            self.__fim.proximo = novo
            self.__fim = novo

        self.iterando = None
        self.__tamanho += 1

    # remove o elemento do início da fila e o devolve à função que o chamou.
    def remover(self):
        if self.__inicio is not None:
            elemento = self.__inicio
            self.__inicio = self.__inicio.proximo
            elemento.proximo = None
            return elemento.conteudo
        else:
            raise Exception(self.__errofilavazia)