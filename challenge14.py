import random
#random.seed(100)

def MonteCarloPi(trials: int) -> float:
    assert trials > 0
    inside = 0
    for i in range(trials):
        x2 = random.random()**2
        y2 = random.random()**2
        if (x2 + y2)**2 <= 1:
            inside += 1
        pi = (float(inside)/trials) * 4
       
    return round(pi, 3)

if __name__ == '__main__':
    print(MonteCarloPi(100000))