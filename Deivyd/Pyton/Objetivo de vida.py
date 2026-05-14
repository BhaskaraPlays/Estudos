from asyncio import sleep


nome = input("Como te chamas? ")
print ("Olá " + nome)
idade = input("Quantos anos tens? ")    
print ("escolha um objetivo de vida: viajar ou comprar uma casa")
print ("1 - viajar")
print  ("2 - comprar uma casa")
objetivo = input ("Digite o número correspondente ao seu objetivo de vida: ")
if objetivo == "1":
    objetivo = "viajar"
elif objetivo == "2":    objetivo = "Comprar uma casa"
else: print ("Opção inválida, por favor escolha 1 ou 2.")
print  ("Vamos montar um objetivo de vida com as tuas respostas ")  
idade_objetivo = input ("qual idade deseja chegar a esse objetivo? ")
trabalho = input ("qual seu trabalho atual? ")
renda = input ("qual sua renda atual? ")
despesas = input ("qual valor das suas despesas mensais? ")
renda_mensal = int(renda) - int(despesas)
tempo_restante = int(idade_objetivo) - int(idade)
if objetivo == "viajar":
    objetivo = int(15000)
elif objetivo == "Comprar uma casa":
    objetivo = int(500000)
despesas_anuais = int(despesas) * 12
renda_anuais = int(renda) * 12
if renda_anuais > despesas_anuais:
    print ("Ótimo, sua renda anual é maior que suas despesas anuais, isso é um bom sinal para alcançar seu objetivo de vida!")
else:    print ("Cuidado, suas despesas anuais são maiores que sua renda anual, isso pode dificultar alcançar seu objetivo de vida. Considere reduzir suas despesas ou aumentar sua renda.")
objetivo_real = int (objetivo) - (renda_anuais - despesas_anuais) * tempo_restante
if objetivo_real <= 0:
    print ("Parabéns, você tem um plano financeiro sólido para alcançar seu objetivo de vida!")
Necessario = tempo_restante * 12 * (int(objetivo) / tempo_restante)
if Necessario <= renda_anuais - despesas_anuais:
    print ("Ótimo, com o seu plano financeiro atual, você tem uma boa chance de alcançar seu objetivo de vida!")   
tempo_necessario = int(objetivo) / (renda_anuais - despesas_anuais)

if tempo_necessario <= tempo_restante: 
    print ("Ótimo, com o seu plano financeiro atual, você tem uma boa chance de alcançar seu objetivo de vida dentro do prazo desejado!")
else:   
    print ("Cuidado, com o seu plano financeiro atual, pode ser difícil alcançar seu objetivo de vida dentro do prazo desejado. Considere ajustar suas despesas ou aumentar sua renda para garantir que você possa alcançar seus objetivos dentro do prazo desejado.") 
meses_restantes = tempo_restante * 12
meses_precisos =int(int(objetivo) / (renda_anuais - despesas_anuais) * 12)
sleep (2)
print ("Você levaria aproximadamente " + str(meses_precisos) + " meses para alcançar seu objetivo de vida, com o plano financeiro atual.")