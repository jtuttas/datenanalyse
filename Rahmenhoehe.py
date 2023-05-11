import random
import csv

random_xy_values = []

def write_to_csv(filename, array):
    with open(filename, mode='w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csvwriter.writerow(['Koerpergroesse', 'Schrittlaenge','Rahmengroesse'])
        
        for row in array:
            csvwriter.writerow(row)
        
def generate_random_values(mx,my,sx,sy,n,t):
    for _ in range(n):
        x = round(random.gauss(mx, sx), 2)
        y = round(random.gauss(my, sy), 2)
        random_xy_values.append([x, y,t])
    return random_xy_values

random_xy_values = generate_random_values(160.5,74.75,7,3,20,"S")
random_xy_values = generate_random_values(173.5,84,7,3,20,"M")
random_xy_values = generate_random_values(184,90.25,7,3,20,"L")
random_xy_values = generate_random_values(197,97.25,7,3,20,"XL")
random.shuffle(random_xy_values)
# Ausgabe des zweidimensionalen Arrays
for value in random_xy_values:
    print(value)
write_to_csv('Rahmenhoehe.csv', random_xy_values)