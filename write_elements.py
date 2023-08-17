with open('elements.html', 'w') as file:
    for i in range (500):
        file.write(f'<img src="image{i}.jpg" alt="image">\n')