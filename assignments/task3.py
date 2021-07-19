'''
Problem statement :
Write a function which takes a string s as input and prints the frequencies of all the words in the string. eg: quick fox lazy dog quick donkey fire fox input returns {quick: 2, fox: 2, lazy: 1, dog: 1, donkey: 1, fire: 1}. Use <space>  as the delimiter to identify what a word is.
'''


class Task():

    def __init__(self, s: str) -> None:
        self.s = s.lower()

    def main(self):
        d = {}
        for i in self.s.split():
            d[i] = d.get(i, 0) + 1
        return d


if __name__ == '__main__':
    s = input('Enter the string : ')
    result = Task(s).main()
    print(result)
