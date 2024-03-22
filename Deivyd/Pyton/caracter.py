fact = "the mom has no atmosphere."
two_facts = fact + " non sound can be heared in Moon"
print (two_facts)
moon_radius = "The Moon has a radius of 1,080 miles."
mult_line = "The Moon has no atmosphere. \n Non sound can be heard on Moon. \n The moon radius is 1,080 miles."
# preste atençao a \ usada, se usar a barra errada vai dar outra coisa.
print(mult_line)
multiline = """The Moon has no atmospheree
Non sound can be heared on Moon
The Moon radius is 1,080 miles"""
# aspas triplas consideram o enter como quebra de linha
print(multiline)
#seta o texto como title e  coloca todas as iniciais em maiusculo
heading = "temperatures and facts about the moon"
heading_upper = heading.title()
print(heading_upper)
#separa por linha todos os espaços (removendo o /n só separa tudo)
temperatures = "Daylight: 260 F\n Nighttime: -280 F"
temperatures_list = temperatures.split('\n')
print(temperatures_list)
#Verifica e da a saida como falsa pala a palavra Moon
print("Moon" in "This text will describe facts and challenges with space travel")
#verifica e da a saida como verdadeira para a palavra Moon
print("Moon" in "This text will describe facts about the Moon")
#localiz a palavra dentro do codigo e da como saida o numero de vezes que a palavra foi encontrada no codigo
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.find("Moon"))
#retorna o número total de ocorrências de uma determinada palavra em uma cadeia de caracteres
temperatures = """Saturn has a daytime temperature of -170 degrees Celsius, while Mars has -28 Celsius."""
print(temperatures.count("Mars"))
print(temperatures.count("Moon"))
# divide o texto após um caracter expecifico
temperatures = "Mars Average Temperature: -60 C"
parts = temperatures.split(':')
print(parts)
print(parts[-1])
#extrai valor numerico dentro do str
mars_temperature = "The highest temperature on Mars is about 30 C"
for item in mars_temperature.split():
    if item.isnumeric():
        print(item)
#O método .join() requer um objeto iterável (como uma lista do Python) como um argumento, portanto, seu uso é diferente de outros métodos de cadeia de caracteres:
moon_facts = ["The Moon is drifting away from the Earth.", "On average, the Moon is moving about 4cm every year."]
print(' '.join(moon_facts))
# % formata o texto conforme a variavel especificada
mass_percentage = "1/6"
print("On the Moon, you would weigh about %s of your weight on Earth." % mass_percentage)
#também pode ser usada para outras variaveis e variaveis diversas
print("""Both sides of the %s get the same amount of sunlight, but only one side is seen from %s because the %s rotates around its own axis when it orbits %s.""" % ("Moon", "Earth", "Moon", "Earth"))
# o metodo .format usa dentro do codigo chaves para determinar a variavel
print("On the Moon, you would weigh about {} of your weight on Earth.".format(mass_percentage))
# formato em multiplas variaveis
print("""You are lighter on the {0}, because on the {0} you would weigh about {1} of your weight on Earth.""".format("Moon", mass_percentage))
