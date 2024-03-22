#Para criar uma função, use a palavra-chave def seguida por um nome, parênteses e o corpo da função com seu respectivo código:
def rocket_parts():
   print("payload, propellant, structure")
rocket_parts()
#output = rocket_parts()
#output is None
def Rocket_parts():
    return "payload, propellant, structure"
Output = Rocket_parts()
Output
any([True,False,False])
str()
str(15)
def distance_from_earth(destination):
    if destination == "Moon":
        return "238,855"
    else:
        return "Unable to compute to that destination"
distance_from_earth('Moon')
def days_to_complete(distance,speed):
    hour = distance/speed
    return hour / 24
days_to_complete(238855, 75)
def generate_report(main_tank, external_tank, hydrogen_tank):
    output = f"""Fuel Report:
    Main tank: {main_tank}
    External tank: {external_tank}
    Hydrogen tank: {hydrogen_tank} 
    """
    print(output)
generate_report(80,70,75)
from datetime import timedelta,datetime

def arrival_time(destination, hours=51):
    now = datetime.now()
    arrival = now + timedelta(hours=hours)
    return arrival.strftime(f"{destination} Arrival: %A %H:%M")
arrival_time('Moon')
def variable_length(*args):
    print(args)
variable_length()
()
variable_length("one", "two")
('one', 'two')
variable_length(None)
(None,)
def sequence_time(*args):
    total_minutes = sum(args)
    if total_minutes < 60:
        return f"Total time to launch is {total_minutes} minutes"
    else:
        return f"Total time to launch is {total_minutes/60} hours"
sequence_time(4,14,18)
def variable_lenght(**kwargs):
    print(kwargs)
def crew_members(**kwargs):
    print(f"{len(kwargs)} astronauts assigned for this mission: ")
    for title, name in kwargs.items():
        print(f"{title}: {name}")
crew_members(captain="Neil Armstrong", pilot="Buzz Aldrin", command_pilot="Michael Collins")
def fuel_report(**fuel_tanks):
    for name, value in fuel_tanks.items():
        print(f'{name}: {value}')
fuel_report(main=50, external=100, emergency=60)