"""
Создать текстовый файл (не программно), сохранить в нём несколько строк,
выполнить подсчёт строк и слов в каждой строке.
poem_file.txt:
I was angry with my friend;
I told my wrath, my wrath did end.
I was angry with my foe:
I told it not, my wrath did grow.

And I waterd it in fears,
Night & morning with my tears:
And I sunned it with smiles,
And with soft deceitful wiles.

And it grew both day and night,
Till it bore an apple bright.
And my foe beheld it shine,
And he knew that it was mine.

And into my garden stole.
When the night had veiled the pole;
In the morning glad I see,
My foe outstretchd beneath the tree.
"""
num_lines = 1
with open("poem_file.txt") as poem:
    print(f'Число строк {len(poem.readlines())}')
with open("poem_file.txt") as poem:
    for line in poem:
        print(f'Строка {num_lines}, в строке {len(line.split())} слов')
        num_lines += 1
