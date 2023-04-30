import random
import csv

random_xy_values = []

def write_to_csv(filename, array):
    with open(filename, mode='w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csvwriter.writerow(['x', 'y'])
        
        for row in array:
            csvwriter.writerow(row)
        

def generate_random_values(ux,ox,uy,oy,n):

    for _ in range(n):
       x = round(random.uniform(ux, ox), 2)
       y = round(random.uniform(uy, oy), 2)
       random_xy_values.append([x, y])

    return random_xy_values

random_xy_values = generate_random_values(254,675,230,557,20)
random_xy_values = generate_random_values(431,768,20,405,20)
random_xy_values = generate_random_values(48,492,57,267,20)
random.shuffle(random_xy_values)
# Ausgabe des zweidimensionalen Arrays
for value in random_xy_values:
    print(value)
write_to_csv('Ladestationen.csv', random_xy_values)