
# TASK 1
# You're running a poll to find out your friends' favourite dessert 
# and decide to write a program to help you keep track of all the suggestions and who voted for each.
# Your program should keep reading in lines (until an empty line) which contain: 
# the person's name, 
# then a colon (:) 
# then their favourite dessert.
# -- like this: Georgina:apple pie

# Your program should keep reading in lines (until an empty line) which contain the person's name, then a colon (:) then their favourite dessert.


# TASK 2 - find a maximum value in a dictionary of numbers

# example

temperatures = {
  'Stockholm': -5, 'Helsinki': -2,
  'Lund': -1, 'Edinburgh': -1,
  'St Petersburg': -4,
}

# TASK 3

# The aim in this question is to find the main characters in a novel by doing textual analysis. We will hypothesise that the most frequent capitalised words in a novel are likely to be the character names.
# You should write a program to open a file called novel.txt and read in all the words. For this purpose let's assume that words are groups of letters and punctuation separated by spaces.
# Your program should then count the number of times each word appears and print out the top 3 words which start with a capital letter.
# You can experiment on other novels freely available from Project Gutenberg (http://www.gutenberg.org/wiki/Main_Page)
# In this question we treat a word as a group of letters and punctuation separated by spaces. This means that Dr and Dr. would count as different words, as would Grok and Grok,. Correctly normalising these examples to the same word is part of the process of tokenisation, but we're not going to worry about that here
# https://en.wikipedia.org/wiki/Tokenization