words_list = ['Kamil', 'Mandarynka', 'Pies', 'Python2025']
short_words = []
long_words = []

# for i in range(len(words_list)):
#     print(i)
#     print(words_list[i])
#     if len(words_list[i]) > 5:
#         long_words.append(words_list[i])
#     else:
#         short_words.append(words_list[i])

for word in words_list:
    print(word)
    if len(word) > 5:
        long_words.append(word)
    else:
        short_words.append(word)
print(long_words)
