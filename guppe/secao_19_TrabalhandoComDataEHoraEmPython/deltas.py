# -*- coding: UTF-8 -*- #  Configuração para não da problema nos comentário
"""
Trabalhando com deltas de data e hora

data_inicial = dd/mm/yyyy 12:55:34.9999999
data_final = dd/mm/yyyy 12:55:34.9999999

import datetime
#  Temos a data de hoje
data_hoje = datetime.datetime.now()

#  Data para ocorrer um determinado evento no futuro
aniversario = datetime.datetime(2021, 4, 20, 0)

#  calculando o delta
tempo_para_evento = aniversario - data_hoje

print(type(tempo_para_evento))
print(repr(tempo_para_evento))
print(tempo_para_evento)

print(f'faltam {tempo_para_evento.days} dias, {tempo_para_evento.seconds // 60 // 60} horas...')
"""
import datetime
data_da_compra = datetime.datetime.now()

print(data_da_compra)
regra_boleto = datetime.timedelta(days=3)
print(regra_boleto)
vencimento_boleto =data_da_compra + regra_boleto
print(vencimento_boleto)
