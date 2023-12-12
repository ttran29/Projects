import random
"""
This is going to be used in my function in order to get a random word from my text files
"""


def create_list(file_1):
    """
    This is the function to grab the  word 
    paramater: file_1 which is one of the text files i made (easywords.txt, mediumwords.txt, hardwords.txt)
    output: a random word will be generated from the list
    """
    word_list = []
    word_file = open(file_1)
    for word in word_file:
        word_list.append(word.strip()) 
    word_index = random.randint(0, len(word_list) - 1)
    return word_list[word_index]


















