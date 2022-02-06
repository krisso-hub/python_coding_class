'''A program that prompt users to enter names of two 
primary colors to mix and produce secondary color. 
And the primary colors are Red, Blue and Yellow
Author: Ndubuisi  Date: 02/05/2022
'''

color_primary = ['red', 'blue', 'yellow'] # declaring list of primary colors

# The user write colors in any order
first_color = input('Enter the first primary color: ')
second_color = input('Enter the second primary color: ')
first_colors = first_color.lower() # The user can write in upper or lower letters
second_colors = second_color.lower()

if (first_colors and second_colors) not in color_primary:
    print('Wrong colors, the primary colors are red, blue and yellow')
elif (first_colors == 'red' and second_colors == 'blue') or (first_colors == 'blue' and second_colors == 'red'):
    print('The color mix  of red and blue gives purple color')
elif (first_colors == 'red' and second_colors == 'yellow') or (first_colors == 'yellow' and second_colors == 'red'):
    print('The color mix of red and yellow gives orange color')
elif (first_colors == 'blue' and second_colors == 'yellow') or (first_colors == 'yellow' and second_colors == 'blue'):
    print('The color mix of blue and yellow gives green color')

