import random
import matplotlib.pyplot as plt

def streamGenerator(num):
    for i in range(num):
        yield i    

def pickRandom(stream):
    selected = []
    
    for i in stream:
        if random.random() < 0.1:
            #print(selected)
            selected.append(i)
        if len(selected) > 500:
#            if random.random() < 0.5:
#                choice = random.randint(50, 100)
#            else:
#                choice = random.randint(0, 50)
            choice = random.randint(0, 10)
            selected.pop(choice)
            
            
    result = random.choice(selected)
    return result
    
def checkProb():
    x = []
    for i in range(100):
        x.append(pickRandom(streamGenerator(100000)))
    plt.hist(x)
    plt.xlabel('Otcomes')
    plt.ylabel('Occurances')
    plt.plot()

if __name__ == '__main__':

    checkProb()
    