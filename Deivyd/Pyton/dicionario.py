planet = {
    'Name': 'Earth',
    'moons': 1
}
print(planet.get('Name'))
print(planet['Name'])
#modificador de valore
planet.update({'Name' : 'makemake'})
planet['name'] = 'makemake'
planet.update({
    'name': 'Jupiter',
    'moons': 79
})
planet['name'] = 'Jupiter'
planet['moons'] = 79
planet['orbital period'] = 4333
planet.pop('orbital period')
planet['diameter (km)'] = {
    'polar': 133709,
    'equatorial': 142984
}
print(f'{planet["name"]} polar diameter: {planet["diameter (km)"]["polar"]}')
planet['circumference (km)'] = {
    'polar': 6752,
    'equatorial': 6792
}

print(f'{planet["name"]} has a polar circumference of {planet["circumference (km)"]["polar"]}')

rainfall = {
    'october': 3.5,
    'november': 4.2,
    'december': 2.1
}
for key in rainfall:
    print(f"{key}: {rainfall[key]}cm")
if 'december' in rainfall:
    rainfall['december'] = rainfall['december'] +1
    
else:
    rainfall['december'] = 1
total_rainfall = 0
for value in rainfall.values():
    total_rainfall = total_rainfall + value
print(f'There was {total_rainfall}cm in the last quarter.')
