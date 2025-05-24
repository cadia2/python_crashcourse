alien_0 = {'x_position': 0, 
           'y_position': 25,
           'speed': 'medium'}

if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3

alien_0['x_position'] = alien_0['x_position'] + x_increment

print(f"New position: {alien_0['x_position']}")

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
}

alien_0 = {'color': 'green', 'speed': 'slow' }

point_value = alien_0.get('points', 'No point value assigned.')
print(point_value)
