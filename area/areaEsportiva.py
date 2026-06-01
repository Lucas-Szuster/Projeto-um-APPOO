from area.area import Area
from evento.evento import Evento
from datetime import timedelta

# ======================
# IMPORTANTE: Como lista_eventos é um atributo interno que NÃO queremos chamar o getter (pois ele retorna uma cópia),
# deve-se utilizar o nome real do atributo, _lista_eventos.
# ======================

class AreaEsportiva(Area):
    # podemos expandir os itens permitidos
    ITENS_PERMITIDOS: list[str] = [
        "bola de futebol",
        "bola de basquete",
        "bola de vôlei",
        "bola de tênis",
        "raquete de tênis",
        "cesta de basquete móvel"
    ]

    def __init__(self, nome: str, qtd_pessoas: int, esporte_praticado: str, sistema_de_iluminacao: bool):
        super().__init__(nome, qtd_pessoas, timedelta(minutes=50))

        self.esporte_praticado = esporte_praticado
        self.sistema_de_iluminacao = sistema_de_iluminacao

    # ============
    # PROPRIEDADES
    # ============

    @property
    def esporte_praticado(self):
        return self.__esporte_praticado
    
    @esporte_praticado.setter
    def esporte_praticado(self, novo_esporte: str):
        if not isinstance(novo_esporte, str):
            raise TypeError("O esporte deve ser uma string")
        if not novo_esporte.strip():
            raise ValueError("O esporte não pode ser vazio")
        
        self.__esporte_praticado = novo_esporte

    @property
    def sistema_de_iluminacao(self):
        return self.__sistema_de_iluminacao
    
    @sistema_de_iluminacao.setter
    def sistema_de_iluminacao(self, nova_situacao_do_sistema_de_iluminacao):
        if not isinstance(nova_situacao_do_sistema_de_iluminacao, bool):
            raise TypeError("A área esportiva deve ter ou não um sistema de iluminação")

        self.__sistema_de_iluminacao = nova_situacao_do_sistema_de_iluminacao

    # =======
    # MÉTODOS
    # =======

    def adicionar_item_na_lista(self, item: str):
        if not isinstance(item, str):
            raise TypeError("O novo item deve ser uma string")
        
        if item.lower() not in AreaEsportiva.ITENS_PERMITIDOS:
            raise ValueError(f"O item a ser adicionado deve ser um item permitido. Itens permitidos: {AreaEsportiva.ITENS_PERMITIDOS}")
        
        self._lista_de_itens.append(item)

    def remover_item_da_lista(self, item):
        self._lista_de_itens.remove(item)

    def to_dict(self):
        return {
            "tipo": "AreaEsportiva",
            "nome": self.nome,
            "qtd_pessoas": self.qtd_pessoas,
            "esporte_praticado": self.esporte_praticado,
            "sistema_de_iluminacao": self.sistema_de_iluminacao,
            "lista_eventos": [evento.to_dict() for evento in self.lista_eventos],
            "lista_de_itens": self.lista_de_itens,
            "lista_restricoes": self.lista_restricoes
        }