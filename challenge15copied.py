import random

def sample_gen_func(num):
    for x in range(num):
        yield x

def solution(sample_generator):
    sample_count = 0
    selected_sample = None

    for sample in sample_generator:
        sample_count += 1
        if random.random() <= 1.0 / sample_count:
            selected_sample = sample

    return selected_sample

def checkProb():
    x = []
    for i in range(100):
        x.append(pickRandom(sample_gen_func(1000)))
    plt.hist(x)
    plt.xlabel('Otcomes')
    plt.ylabel('Occurances')
    plt.plot()

if __name__ == '__main__':
    checkProb()