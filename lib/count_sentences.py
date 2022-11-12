#!/usr/bin/env python3

class MyString:
    '''MyString in count_sentences.py'''

    def __init__(self, value=""):
        '''initializes the value'''
        if type(value) != str:
            print("The value must be a string.")
            self.value = ""
        else:
            self.value = value

    def is_sentence(self):
        '''returns True if value ends with a period and False otherwise.'''
        return self.value.endswith(".")

    def is_question(self):
        '''returns True if value ends with a question mark and False otherwise.'''
        return self.value.endswith("?")

    def is_exclamation(self):
        '''returns True if value ends with an exclamation mark and False otherwise.'''
        return self.value.endswith("!")

    def count_sentences(self):
        '''returns the number of sentences in the value.'''
        count = 0
        for char in self.value:
            if char in ".!?":
                count += 1
        return count

