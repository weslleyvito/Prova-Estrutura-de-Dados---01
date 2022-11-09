class FilaPrioridade:
    def __init__(self):
        self.__fila = []
                
    
    def push(self, professor):
        if self.empty() == True:
            self.__fila.append(professor)
        else:
            for index in range(0, len(self.__fila)):
                if self.__fila[index].tempo_de_ifce <= professor.tempo_de_ifce:
                    self.__fila.insert(index, professor)
                else:
                    self.__fila.append(professor)

    def pop(self):
        self.__fila.pop(0)

    def empty(self):
        if len(self.__fila) == 0: #verifica se a fila comtem elementos atraves da finção len()
            return True
        return False
    
    def change_priority(self):
        pass

    def lengh(self):
        pass

    def __str__(self):
        if self.empty == True: #verifica se a lista esta vazia atraves do metodo interno empty
            return '[]' 
        ret = ', '.join(str(professor) for professor in self.__fila) #define a formatação da string caso existam elementos na lista
        return ret