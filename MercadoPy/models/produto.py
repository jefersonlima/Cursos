# -*- coding: UTF-8 -*- #  Configuração para não da problema nos comentário
"""
Mercado Produto
"""
from utils.helper import formata_float_str_moeda

class Produto:
    contador: int = 1

    def __init__(self: object, nome: str, preco: float) -> None:
        self.__codigo: int = Produto.contador
        self.__nome: str = nome
        self. __preco: float = preco
        Produto.contador += 1

    @property
    def codigo(self: object) -> int:
        return self.__codigo

    @property
    def nome(self: object) -> int:
        return self.__nome

    @property
    def preco(self: object) -> int:
        return self.__preco

    def __str__(self) -> str:
        return f'Códido: {self.codigo} \nNome: {self.nome} \nPreço: {formata_float_str_moeda(self.preco)}'
