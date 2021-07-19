'''
Problem statement :
Write a function which takes a positive integer number n and prints [1 2 FIZZ 4 BUZZ FIZZ 7 8 FIZZ BUZZ 11 FIZZ 13 14 FIZZBUZZ … n] where multiples of 3 are replaced by FIZZ, multiples of 5 are replaced by BUZZ and multiples of both are replaced by FIZZBUZZ.
'''


class Task:

    def __init__(self, n: int) -> None:
        self.n = n

    def main(self) -> list:
        '''
        Attributes
        ----------
        Input : n (positive integer number ) 
        output : multiples of 3 are replaced by FIZZ, multiples of 5 are replaced by BUZZ and multiples of both are replaced by FIZZBUZZ
        '''
        res = []
        for i in range(1, self.n+1):
            if i % 3 == 0 and i % 5 == 0:
                res.append('FIZZBUZZ')
            elif i % 3 == 0:
                res.append('FIZZ')
            elif i % 5 == 0:
                res.append('BUZZ')
            else:
                res.append(i)
        return res


if __name__ == '__main__':
    n = int(input('Enter the positive integer n : '))
    result = Task(n).main() if isinstance(
        n, int) and n > 0 else "Enter the positive interger"
    print(result)
