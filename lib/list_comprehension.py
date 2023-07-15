#!/usr/bin/env python3

def return_evens(num_list):
    even_nums = [num for num in num_list if num % 2 == 0]
    return even_nums

def make_exclamation(sentence_list):
    exclamations = [sentence + "!" for sentence in sentence_list]
    return exclamations