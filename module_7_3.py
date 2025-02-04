class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = list(file_names)

    def get_all_words(self):
        all_words = {}
        punctuation = [',', '.', '=', '!', '?', ';', ':', ' - ']

        for file_name in self.file_names:
            with open(file_name, 'r', encoding= 'utf-8') as file:
                text = file.read().lower()

                for symbol in punctuation:
                    text = text.replace(symbol, ' ')

                    words = text.split()
                    all_words[file_name] = words

        return all_words


    def find(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        positions = {}

        for file_name in all_words:
            words = all_words[file_name]
            if word in words:
                position = 0
                for w in words:
                    position += 1
                    if w == word:
                        positions[file_name] = position
                        break

        return positions

    def count(self, word):
        word = word.lower()
        all_words = self.get_all_words()
        counts = {}

        for file_name in all_words:
            words = all_words[file_name]
            count = 0
            for w in words:
                if w == word:
                    count += 1
            if count > 0:
                counts[file_name] = count

        return counts


# Пример выполняемого кода:
finder1 = WordsFinder('test_file.txt')
print(finder1.get_all_words())  # Все слова
print(finder1.find('TEXT'))  # 3 слово по счёту
print(finder1.count('teXT'))  # 4 слова teXT в тексте всего

finder2 = WordsFinder('Mother Goose - Monday’s Child.txt')
print(finder2.get_all_words())
print(finder2.find('Child'))
print(finder2.count('Child'))

finder3 = WordsFinder('Walt Whitman - O Captain! My Captain!.txt')
print(finder3.get_all_words())
print(finder3.find('captain'))
print(finder3.count('captain'))

finder4 = WordsFinder('Rudyard Kipling - If.txt')
print(finder4.get_all_words())
print(finder4.find('if'))
print(finder4.count('if'))