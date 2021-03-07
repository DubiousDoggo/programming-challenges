import random
import time

mod = 1000000007

def main():
    print(suminvmod(input()))

def test(n):
    return ''.join(random.choice(['0', '1', '?']) for _ in range(n))

def suminvmod(string: str):
    ones = 0
    questions = 0
    inversions = 0

    for digit in string:

        if digit == '1':
            ones += 1
        else:
            if digit == '?':
                inversions *= 2

            inversions += ones * pow(2, questions, mod)
            if questions > 0:
                inversions += questions * pow(2, questions - 1, mod)

            if digit == '?':
                questions += 1
        
            inversions %= mod

    return inversions

if __name__ == '__main__':
    main()
