print('Welcomme the Shape Area Calculator!')

print('Select the shape to calculate the area:')
print('1. Circle')
print('2. Square')
print('3. Rectangle')
print('4. Triangle')
shape = input('Enter the number corresponding to the shape (1-3): ')

if shape == '1':
    cirlce_radius = int(input('Enter the radius of the circle: '))
    pie = 3.14
    circle_area = pie * cirlce_radius * cirlce_radius
    print(f'The area of the circle is: {circle_area}')
elif shape == '2':
    square_side = int(input('Enter the length of the square: '))
    square_area = square_side * square_side
    print(f'The area of the square is: {square_area}')
elif shape == '3':
    rectangle_length = int(input('Enter the length of the rectangle: '))
    rectangle_breadth = int(input('Enter the breadth of the rectangle: '))
    rectangle_area = rectangle_length * rectangle_breadth
    print(f'The area of the rectangle is: {rectangle_area}')
elif shape == '4':
    triangle_base = int(input('Enter the base of the triangle: '))
    triangle_height = int(input('Enter the height of the triangle: '))
    triangle_area = 0.5 * triangle_base * triangle_height
    print(f'The area of the triangle is: {triangle_area}')
else:
    print('Invalid input. Please select a valid shape number (1-4).')
print('Welcomme the Shape Area Calculator!')    

    