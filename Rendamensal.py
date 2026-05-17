from copy import copy
from email import charset
from re import search
from time import sleep
from serpapi import GoogleSearch


class Rendamensal:
    def __init__(self, valor_inicial, taxa_juros_mensal, meses):
        self.valor_inicial = valor_inicial
        self.taxa_juros_mensal = taxa_juros_mensal
        self.meses = meses

    def calcular_rendimento(self):
        rendimento = copy.deepcopy(self.valor_inicial)
        for _ in range(self.meses):
            rendimento += rendimento * self.taxa_juros_mensal
        return rendimento

    def calcular_rendimento_com_numpy(self):
        return self.valor_inicial * (1 + self.taxa_juros_mensal) ** self.meses 
def opcoes_de_trabalho():
    habilidades = input("Digite suas habilidades separadas por vírgula: ")

    busca = f"ideias de trabalho para quem sabe {habilidades}"

    params = {
        "engine": "google",
        "q": busca,
        "hl": "pt-br",
        "gl": "br",
        "api_key": "SUA_CHAVE_API_AQUI"
    }

    search = GoogleSearch(params)
    resultados = search.get_dict()
    
    print("\nIdeias encontradas:\n")
    
    for item in resultados.get("organic_results", [])[:5]:
        titulo = item.get("title")
        link = item.get("link")
        resumo = item.get("snippet")

        print(f"Título: {titulo}")
        print(f"Resumo: {resumo}")
        print(f"Link: {link}")
        print("-" * 40)

Rendamensal = input ("Digite o valor recebido mensalmente: ")
sleep (1)
aluguel = input ("Você paga aluguel? (sim/não) ")
if aluguel.lower() == "sim":
        valor_aluguel = input ("Digite o valor do aluguel: ")
else : valor_aluguel = 0
sleep (1)
mercado = input ("Quanto você gasta mensalmente com mercado? ")
sleep (1)
transporte = input ("Quanto você gasta mensalmente com transporte? ")
sleep (1)
energia = input ("Quanto você gasta mensalmente com energia? ")
sleep (1) 
agua = input ("Quanto você gasta mensalmente com água? ")
sleep (1)
internet = input ("Quanto você gasta mensalmente com internet? ")
sleep (1)
telefone = input ("Quanto você gasta mensalmente com telefone? ")
sleep (1)
outros = input ("Quanto você gasta mensalmente com outros gastos? ")
sleep (1)
for outros in range (1, 100):
    outros = input ("Digite o valor de outros gastos ou digite '0' para finalizar: ")
    if outros == '0':
        break
despesas_mensais = int(valor_aluguel) + int(mercado) + int(transporte) + int(energia) + int(agua) + int(internet) + int(outros) + int(telefone)
renda_mensal = int(Rendamensal) - despesas_mensais
print ("Analisando suas informações...")
sleep (3)
print (f"Sua renda mensal é de R${renda_mensal:.2f} .")
if renda_mensal > 0:
    print ("Ótimo, sua renda mensal é maior que suas despesas mensais, isso é um bom sinal! Com isso você pode criar um plano de investimento ou economizar para alcançar seus objetivos financeiros.")
else:    print ("Cuidado, suas despesas mensais são maiores que sua renda mensal, isso pode dificultar alcançar seus objetivos financeiros. Considere reduzir suas despesas ou aumentar sua renda.")

desejo_de_investimento = input ("Você tem interesse em investir seu dinheiro? (sim/não) ")
if desejo_de_investimento.lower() == "sim":
    valor_investimento = input ("Digite o valor que deseja investir: ")
else: valor_investimento = 0
valor_investimento = int(valor_investimento)
if valor_investimento < 1000:
    taxa_de_juros = 0.01
elif valor_investimento < 10000:
    taxa_de_juros = 0.02
else:    taxa_de_juros = 0.03
jurops_anuais = taxa_de_juros * 12
print ("Analisando suas informações...")
sleep (3)
if valor_investimento > 0:
    print (f"Com um investimento de R${valor_investimento} a uma taxa de juros mensal de {taxa_de_juros*100}%, você pode esperar um rendimento anual de R${valor_investimento * jurops_anuais:.2f}.")
