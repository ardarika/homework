file = open('text.txt', 'r')
for line in file:
    words = line.split(' ')

new_list = []
words_num = []

for i in words:
    new_list.append(i)
    words_num.append(words.count(i))

print(dict(sorted(dict(zip(new_list, words_num)).items(), key=lambda x: x[1], reverse=True)))

file.close()