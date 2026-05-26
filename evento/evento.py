from datetime import datetime

class Evento:
    def __init__(self, nome_evento: str, data_e_horario: datetime, qtd_participantes: int):
        self.nome_evento = nome_evento
        self.data_e_horario = data_e_horario
        self.qtd_participantes = qtd_participantes
        self.lista_de_restricoes = []

    # ======================
    # PROPRIEDADES DA CLASSE
    # ======================

    @property
    def nome_evento(self):
        return self.__nome_evento
    
    @nome_evento.setter
    def nome_evento(self, novo_nome: str):
        if not isinstance(novo_nome, str):
            raise TypeError("Tipo de nome Inálido!")

        if not novo_nome.strip():
            raise ValueError("Nome inválido")

        self.__nome_evento = novo_nome        
    
    @property
    def data_e_horario(self):
       return self.__data_e_horario

    @data_e_horario.setter
    def data_e_horario(self, novo_horario: datetime):
        if not isinstance(novo_horario, datetime):
            raise TypeError('horario deve estar no formato de tempo')
            
        self.__data_e_horario = novo_horario

    @property
    def qtd_participantes(self):
        return self.__qtd_participantes
    
    @qtd_participantes.setter
    def qtd_participantes(self, qtd_atualizada: int):
        if qtd_atualizada <= 0:
            raise ValueError('quantidade de participantes nao pode ser negativa ou nula')
        
        self.__qtd_participantes = qtd_atualizada

    # =======
    # MÉTODOS
    # =======

    def adicionar_restricao(self, restricao: str):
        if not isinstance(restricao, str):
            raise TypeError("A restrição deve ser uma string")

        self.lista_de_restricoes.append(restricao)

    def to_dict(self):
        return {
            "nome_evento": self.nome_evento,
            "data_e_horario": {
                "year": self.data_e_horario.year,
                "month": self.data_e_horario.month,
                "day": self.data_e_horario.day,
                "hour": self.data_e_horario.hour,
                "minute": self.data_e_horario.minute,
                "second": self.data_e_horario.second
            },
            "qtd_participantes": self.qtd_participantes,
            "lista_de_restricoes": self.lista_de_restricoes
        }

    # ==========
    # OPERADORES
    # ==========

    def __eq__(self, other):
        if not isinstance(other, Evento):
            raise ValueError('Comparação só funciona entre eventos')
        
        # =====================================================
        # Checa se TODOS os atributos são iguais, pode ser que talvez seja melhor checar somente alguns.
        # ======================================================
        for caracteristica_do_evento, _  in self.__dict__.items():
            if getattr(self, caracteristica_do_evento) != getattr(other, caracteristica_do_evento):
                return False
            
        return True