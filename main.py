aliens = []

for alien in range(30):
    new_Alien = {'color': 'green', 'points': 5, 'speed': 'medium'}
    aliens.append(new_Alien)

# Change the values of the first 3 aliens in the dictionary
for number in aliens[:3]:
    if number['color'] == 'green':
        number['color'] = 'yellow'
        number['points'] = '10'
        number['speed'] = 'fast'

# Show the first 5 aliens
for value in aliens[:5]:
    print(value)

print(f"The total number of aliens is {len(aliens)}")
