class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':']
        for i in self.file_names:
            with open(i, encoding='utf-8') as file:
                words = []
                for line in file:
                    line = line.lower().strip()
                    for j in punctuation:
                        line = line.replace(j, '')
                    line = line.replace(' - ', ' ')
                    words.extend(line.split())
                all_words[i] = words
            return all_words

    def find(self, word):
        word = word.lower()
        result = {}
        for name, words in self.get_all_words().items():
            if word.lower() in words:
                result[name] = words.index(word) + 1
        return result

    def count(self, word):
        word = word.lower()
        result = {}
        for name, words in self.get_all_words().items():
            result[name] = words.count(word)
        return result


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())
print(finder2.find('TEXT'))
print(finder2.count('teXT'))
