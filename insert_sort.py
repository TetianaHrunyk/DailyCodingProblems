import random

def insert_sort(pole):
    print(pole)
    for i in range(1, len(pole)):       
        prvok = pole[i]
        print("Prvok: ", prvok)
        j = i-1
        while j >= 0 and pole[j] > prvok:           
            pole[j+1] = pole[j]
            j -= 1
            print(pole)
        pole[j+1] = prvok
        print(pole)

pole = [random.randrange(10, 100) for i in range(10)]
insert_sort(pole)