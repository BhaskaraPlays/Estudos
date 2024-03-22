planets = ["Mercury", "Venus", "Earth", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune"]
print("The first planet is:", planets[0])
print("The second planet is:", planets[1])
print("The third planet is:", planets[2])
planets[3] = "red planet"
print("Mars is also known as:", planets[3])
number_planets = len(planets)
print(f"There are {number_planets} planets in solar sistem")
#Adicionar valores a variavel usando .append
planets.append("Pluto")
#remover itens da lista usando .pop
planets.pop() #Goodbye Pluto
print("The last planet is:", planets[-1])
print("The penutimate planet is:", planets[-2])
jupter_index = planets.index("Jupiter")
print(f"Jupiter is {jupter_index +1} planet from the sun")
gravity_on_Earth = 1.0
Gravity_on_Moon = 0.166
gravity_on_planets = [0.378, 0.907, 1, 0.377, 2.36, 0.916, 0.889, 1.12]
bus_weight = 124054 # in Newtons, on Earth
print(f"On Earth, a double-decker bus weighs {bus_weight} N")
print(f"On Mercury, a double-decker bus weighs {bus_weight * gravity_on_planets[0]} N")
print("The lightest a bus would be in the solar system is", bus_weight * min(gravity_on_planets), "N")
print("The heaviest a bus would be in the solar system is", bus_weight * max(gravity_on_planets), "N")
#Fatia listas
planets_before_earth = planets [0:2]
print(planets_before_earth)
planets_after_earth = planets [3:]
print(planets_after_earth)
#Juntando listas
amalthea_group = ["Metis", "Adrastea", "Amalthea", "Thebe"]
galilean_moons = ["Io", "Europa", "Ganymede", "Callisto"]

regular_satellite_moons = amalthea_group + galilean_moons
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
#classificar em ordem alfabetica. .sort(reverse=true) para classificar de forma reversa
regular_satellite_moons.sort()
print("The regular satellite moons of Jupiter are", regular_satellite_moons)
user_planet = input("Please enter the name of the planet (With a capital letter to start)")
planet_index = planets.index(user_planet)
print("Here the planets closer than " + user_planet)
print(planets[0:planet_index])
print("Here are the planets further than " + user_planet)
print(planets[planet_index + 1:])