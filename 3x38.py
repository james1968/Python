states = {
        'Oregon': 'OR',
        'Florida': 'FL',
        'California': 'CA',
        'New York':, 'NY',
        'Michigan':, 'MI'
    }

cities = {
        'CA': 'San Francisco',
        'MI': 'Detroit',
        'FL': 'Florida'
    }


cities['NY'] = 'New York'
cities['OR'] = 'Portland'

print('-' * 10)
print("NY State has: ", cities['NY'])
print("OR State has: ", cities['OR'])

print('-' * 10)
print("Michigan's abbreviation is: ", states['Michigan'])
print("Michigan has: ", cities[states['Michigan']])

print('-' * 10)
for state, abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

print('-' * 10)
for abbrev, city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

    
