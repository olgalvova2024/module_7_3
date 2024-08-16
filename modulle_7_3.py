import string
class WordsFinder:
    def __init__(self, *file_name):
        self.file_name = file_name

    def get_all_words(self):
        all_word = {}
        table = str.maketrans("", "", string.punctuation)
        for i in self.file_name:
            name = i
            with open(name, encoding='utf-8') as file:
                file_content = str(file.read()).split()
                for j in range(len(file_content)-1):
                    file_content[j] = file_content[j].lower()
                    file_content[j] = file_content[j].translate(table)
                    all_word[i] = file_content
        return all_word

    def count(self, word):
        count_word = {}
        for name, words in self.get_all_words().items():
            number_word = 0
            for j in range(len(words)):
                if word.lower() == words[j]:
                    number_word += 1
            count_word[name] = number_word
        return count_word

    def find(self, word):
        find_word = {}
        for name, words in self.get_all_words().items():
            number_word = 0
            for j in range(len(words)):
                if word.lower() == words[j]:
                    number_word = j
                    break
            find_word[name] = number_word + 1
        return find_word



finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder1 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt',
                      'Rudyard Kipling - If.txt',
                      'Mother Goose - Monday’s Child.txt')
print(finder1.get_all_words())
print(finder1.find('the'))
print(finder1.count('the'))

