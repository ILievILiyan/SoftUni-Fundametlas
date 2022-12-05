class WORDS_MODIFICATION:
    def __init__(self, words):
        self.words = words

    def repeat_func(self):
        return ''.join(map(lambda x: x * len(x), self.words))

    def reverse_func(self):
        return "".join(element[::-1] for element in self.words)



words: list = input().split()
obj = WORDS_MODIFICATION(words)
print(obj.repeat_func())
print(obj.reverse_func())
