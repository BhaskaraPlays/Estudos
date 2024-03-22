second = int(input("insert seconds: "))
display_minutes = second // 60
display_hours = display_minutes // 60
display_days = display_hours // 24
print("this time in minutes are: ", display_minutes)
print("this time in hour are: ", display_hours )
print("This time in days will do: ", display_days)
demo_int = int('256')
print(demo_int)
demo_float= float("256.5")
print(demo_float)
#função round arredonda para cima se for maior a .5 ou para baixo se menos que .5 (para arredondar o .5 use o próximo modo)
print(round(1.4))
print(round(1.5))
print(round(2.5))
print(round(2.6))
#arrendondar numero para cima ou para baixo
from math import ceil, floor

round_up = ceil(12.5)
print(round_up)

round_down = floor(12.5)
print(round_down)
first_planet_input = input('Enter the distance from the sun for the first planet in km: ')
second_planet_input = input('Enter the distance from the sun for the second planet in km: ')
first_planet = int(first_planet_input)
second_planet = int(second_planet_input)
distance_km = first_planet - second_planet
print (abs(distance_km))
