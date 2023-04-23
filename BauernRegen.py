import random
import csv

random_xy_values = []

def write_to_csv(filename, array):
    with open(filename, mode='w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        csvwriter.writerow(['Feuchte', 'Regenwahrscheinlichkeit', 'Ergebnis'])
        
        for row in array:
            csvwriter.writerow(row)
        

def generate_random_values(ux,ox,uy,oy,n,result):

    for _ in range(n):
       x = round(random.uniform(ux, ox), 2)
       y = round(random.uniform(uy, oy), 2)
       random_xy_values.append([x, y,result])

    return random_xy_values

#random_xy_values = generate_random_values(16,22,5,95,30,"Warten")
#random_xy_values = generate_random_values(11,16,80,95,20,"Ernten")
#random_xy_values = generate_random_values(14.5,16,5,79,15,"Warten")
#random_xy_values = generate_random_values(11,14.4,5,79,25,"Ernten")
#random_xy_values.append([13,45,"Warten"])
#random.shuffle(random_xy_values)
random_xy_values = generate_random_values(14.5,22,5,95,10,"Warten")
random_xy_values = generate_random_values(11,16,77,95,5,"Ernten")
random_xy_values = generate_random_values(14,16,5,79,5,"Warten")
random_xy_values = generate_random_values(11,14.4,5,79,10,"Ernten")
random.shuffle(random_xy_values)
# Ausgabe des zweidimensionalen Arrays
for value in random_xy_values:
    print(value)
write_to_csv('ErnteBauern2.csv', random_xy_values)