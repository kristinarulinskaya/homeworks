# Напишите программу, которая принимает текст и выводит два слова: наиболее часто встречающееся и самое длинное.


def build_word_dict(word_lst):
    words_dct = {}
    for i in word_lst:
        if i in words_dct:
            words_dct[i] += 1
        else:
            words_dct[i] = 1
    return words_dct


def get_number_frequent_word(words_dct):
    values = list(words_dct.values())
    values.sort()
    return values[-1]


def func(text):
    word_lst = text.split(' ')
    words_dct = build_word_dict(word_lst)
    number = get_number_frequent_word(words_dct)
    word_with_maxlen, frequent_word = '', ''

    for k in words_dct:
        if len(k) > len(word_with_maxlen):
            word_with_maxlen = k

        if words_dct[k] == number:
            frequent_word = k

    return word_with_maxlen, frequent_word


my_text = 'It is a long established fact that a reader will be distracted by the readable ' \
          'content of a page when looking at its layout'
print(func(my_text))