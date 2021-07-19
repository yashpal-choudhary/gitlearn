'''
Problem statement : 
Write a function which takes a positive integer number n and prints the Fibonacci sequence [1 1 2 3 5 8 13 … ] upto n.
'''


class Task:

    def __init__(self, n: int) -> None:
        self.n = n

    def main(self):
        '''
        Attributes
        ----------
        Input : n (positive integer number ) 
        output : prints the Fibonacci sequence [1 1 2 3 5 8 13 … ] upto n
        '''
        res = [0]*self.n
        a = 0
        b = 1
        res[0] = a+b
        for i in range(1, self.n):
            res[i] = a+b
            a, b = res[i-1], res[i]
        return res


if __name__ == '__main__':
    n = int(input('Enter the positive integer n : '))
    result = Task(n).main() if isinstance(
        n, int) and n > 0 else "Enter the positive interger"
    print(result)
