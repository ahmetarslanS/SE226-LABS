from abc import ABC, abstractmethod


class FileReader(ABC):
    def __init__(self, address):
        self.address = address

    @abstractmethod
    def calculateFreqs(self):
        pass


class ListCount(FileReader):
    def calculateFreqs(self):
        with open(self.address, 'r') as file:
            content = file.read()
            letter_freqs = []
            for letter in content:
                if letter.isalpha():
                    letter_freqs.append(f"{letter} = {content.count(letter)}")
            return letter_freqs


class DictCount(FileReader):
    def calculateFreqs(self):
        with open(self.address, 'r') as file:
            content = file.read()
            letter_freqs = {}
            for letter in content:
                if letter.isalpha():
                    letter_freqs.setdefault(letter, 0)
                    letter_freqs[letter] += 1
            return letter_freqs


address = "C:/Users/qp/Desktop/weirdWords.txt"

list_count = ListCount(address)
list_result = list_count.calculateFreqs()
print("ListCount result: ", " ".join(list_result))

dict_count = DictCount(address)
dict_result = dict_count.calculateFreqs()
print("DictCount result: ", dict_result)
