
# coding: utf-8

# # Text Analytics in python using the numpy package
## The dataset can be found in: https://www.dropbox.com/sh/ltgo0fkxt136muo/AACDhSMCjd2oFR-NuiPAaCrTa?dl=0

# ## Part A: Word Games
# 
# Let's play around with words.  The code you will write for Part A will enable you to answer questions like:
# 
# 1. How many total words are there in H. G. Wells' <em>War of the Worlds</em>?
# 1. How many unique words are there in Shelley's <em>Frankenstein</em>?
# 1. How many times does the word <em>Jabberwocky</em> appear in Lewis Carroll's <em>Through the Looking-Glass</em>?
# 1. I'm trying to solve a crossword puzzle.  What word(s) in the official scrabble word list, sowpods, are 5 letters long and whose 2nd letter is <em>h</em> and 4th is <em>z</em>?
# 1. How many <em>four letter</em> words are there in Mark Twain's <em>Adventures of Huckleberry Finn</em>?
# 
# For Part A you will complete the Word Analysis and Data Questions functions below.  The Word Analysis functions will provide the primary data analysis to help you answer the questions defined in this notebook. The code you write for each Data Question's function will need to call the appropriate Word Analysis function(s) and then complete any additional processing  necessary to answer the specific question.  
# 
# - Answers to the specific questions above have been provided for you so that you can check that your code is working correctly.  
# - Text files for the relevant Gutenberg books have been provided in the A1 folder.

# In[ ]:

from __future__ import print_function, division

import string


# ## Word Analysis functions

# In[ ]:

def create_wordlist(filename, is_Gutenberg):
    """ Read a file, and create a list of all of the words in the file: 
        1. Strip off whitespace, and punctuation
        2. Replace hyphens with spaces
        3. If is_Gutenberg is True, skip the file header and footer.
        
        NOTE: Gutenberg Book Header and Footer
              Header ends with a line that starts with 
              "*** START OF THIS PROJECT GUTENBERG EBOOK"
              Footer begins with a line that starts with 
              "End of the Project Gutenberg EBook"
              
        HINT: The string module provides a string named `whitespace`, which 
              contains space, tab, newline, etc., and `punctuation` which 
              contains the punctuation characters.  You might also consider 
              using the string methods `strip`, `replace` and `startswith`

    filename: string
    is_Gutenberg: boolean, if True, skip Gutenberg header & footer
    returns: list of words
    """
 h = dict()
    fin = open(filename, 'r')
    if (is_Gutenberg==True):
        for line in fin:
            if "START OF THIS PROJECT GUTENBERG BOOK" in line:
                break               
        for line in fin:
            if "End of the Project Gutenberg EBook" in line:
                break              
    for line in fin:
        process_line(line, h)
    return h

def process_line(line, h):
    line = line.replace('-', ' ')

    for word in line.split():
        word = word.strip(string.punctuation + string.whitespace)
        word = word.lower()

        h[word] = h.get(word,0)+1

# In[ ]:

def word_frequency(word_list):
    counts = dict()
    for i in word_list:
        counts[i] = counts.get(i, 0) + 1
        hist, bin_edges = np.histogram(counts, bins = range(5))
        print(hist)
    """ Given a list of words, create a histogram (dictionary) which maps 
        each word to the number of times it appears in the list.

    word_list: list of words
    returns: histogram (dict - key:word, value: times word appears)
    """
    return


# In[ ]:

def crossword_cheat(words_list, word_length, match_letters = None):
    unique_words = set(word_list)
    for word in unique_words:
        if len(word) == word_length:
            print(word)
    """ From the provided list of unique words, identify and return a 
        list of word(s) that meet the criteria for word length and 
        matching letter/positions.

    words_list: list of unique words, i.e. each word only occurs once
    word_length: number of letters in word
    match_letters: dictionary key: letter position, value: letter, may be None
    returns: list of matching words
    """
    return  


# ## Data Questions

# ### A1: Total words
# 
# Return the total number of words contained in a Gutenberg book's text file.
# >What's the total number of words in  H. G. Wells' <em>War of the Worlds</em>?  
# >Answer: 60570

# In[ ]:

def A1(book):
    """ Return the total number of words contained in a Gutenberg text file.
        The question code should call the completed Word Analysis functions
    """ 
    words = create_wordlist(book, False)
    return total_words(words)

def total_words(h):
    return sum(h.values())

# In[ ]:

a1 = A1('data/war_of_the_worlds.txt')
# Answer: 60570
a1


# ### A2: Unique words
# Return the number of unique words contained in a Gutenberg book's text file.
# 
# >How many unique words does Shelley's <em>Frankenstein</em> have?  
# >Answer: 7062

# In[ ]:

def A2(book):
    wordlist = create_wordlist(book, False)
    num = different_words(wordlist)
    """ Return the number of unique words contained in a Gutenberg
        book's text file. The question code should call the 
        completed Word Analysis functions
    """  
    return num

def different_words(h):
    return len(h)

# In[ ]:

a2 = A2('data/frankenstein.txt')
# Answer: 7062
a2


# ### A3: Word frequency
# Return the number of times a word occurs in a Gutenberg book's text file, ignore case.  
# 
# >How many times does the word <em>Jabberwock</em> appear in Lewis Carroll's 
#  <em>Through the Looking-Glass</em>?  
# >Answer: 3

# In[ ]:

def A3(book, word):
    wordlist = create_wordlist(book, False)
    num = word_frequency(wordlist) 
    """ Return the number of times 'word' occurs in the Gutenberg 
        book's text file. The question code should call the completed 
        Word Analysis functions
    """
    
    return num


# In[ ]:

a3 =  A3('data/through_the_looking_glass.txt', 'Jabberwock')
# Answer: 3
a3


# ### A4: Scrabble word match
# Find and return the words in the official scrabble words list file which match the parameters for word length and letter/positions.
# 
# >What word(s) in the official scrabble words list, sowpods, are 5 letters long and whose 2nd letter is <em>h</em> and 4th is <em>z</em>?  
# >Answer: ['chizz', 'ghazi', 'khazi', 'whizz']

# In[ ]:

def A4(words_file, is_Gutenberg, word_length, match_letters):
    words = create_wordlist(words_file, is_Gutenberg)
    unique_words = set(words)
    for word in unique_words:
        if(len(word)==word_length) and (word.index('h') == match_letters):
            print(word)   
    """ Return the list of unique words from the words_file 
        which match the criteria.  The question code should call the 
        completed Word Analysis functions    
    """    
    return 

a4 = A4('data/sowpods.txt', False, 5, {1:'h', 3:'z'})
# Answer: ['chizz', 'ghazi', 'khazi', 'whizz']
a4


# ### A5: Book word match
# Find and return the words in the a Gutenberg book's text file which match the parameter for word length.  
# >How many four letter words appear in Mark Twain's <em>Adventures of Huckleberry Finn</em>?  
# >Answer: 895

# In[ ]:

def A5(words_file, word_length):
    cross = crossword_cheat(words_file, word_length, None)
    num = len(cross)
    """ Return the total number of unique words in words_file 
        which match the criteria.  The question code should call the 
        completed Word Analysis functions
    """
    return num

a5 = A5('data/adventures_of_huckleberry_finn.txt', 4)
# Answer: 895
a5

