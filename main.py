def replace_word():
    str = "hi guys, i am canis. coffee coffee coffee"
    words_to_replace = input ("enter the word to replace: ")
    word_placement = input ("word replacement: ")
    print(str.replace(words_to_replace, word_placement))


replace_word()