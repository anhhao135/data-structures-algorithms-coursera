# python3
from random import seed
from random import randint

def max_pairwise_product_slow(numbers):
    n = len(numbers)
    max_product = 0
    for first in range(n):
        for second in range(first + 1, n):
            max_product = max(max_product,
                numbers[first] * numbers[second])

    return max_product

def max_pairwise_product_fast(numbers):
    n = len(numbers)
    firstHighest = 0
    secondHighest = 0
    for index in range(n):
        if numbers[index] >= firstHighest and numbers[index] >= secondHighest:
            secondHighest = firstHighest
            firstHighest = numbers[index]
            continue

        if numbers[index] >= secondHighest:
            secondHighest = numbers[index]
            continue

    max_product = firstHighest * secondHighest
    return max_product


if __name__ == '__main__':

    '''

    seed(1)

    while True:
        value1 = randint(2, 2 * 10000)
        input_numbers = []
        for i in range(value1):
            input_numbers.append(randint(0, 2 * 10000))


        #print(input_numbers)

        3print(max_pairwise_product_slow(input_numbers))
        #print(max_pairwise_product_fast(input_numbers))

        if max_pairwise_product_slow(input_numbers) != max_pairwise_product_fast(input_numbers):
            break








    
    '''

    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product_fast(input_numbers))


