"""
This script will take an input file, clean the text of punctuation,
remove any common words and, finally, produce a word cloud image.
"""
#Import various other modules
import wordcloud
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display
import fileupload
import io
import sys

#Prompt for a file
filepath = input("Enter the path to the file: ")
file = open(filepath)
file_contents = file.read()

#Open/read file contents
#print(file_contents)

#######################################################
#####Code to actually open/read file contents here#####
#######################################################

def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words you can use to process your text
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

    #Init empty dictionary
    frequency = {}

    #Add new dictionary entry if none exists, otherwise, word counter +1
    file_cleaned = file_contents.lower().replace(punctuations,"")
    frequency = {}
    for word in file_cleaned.split():
        if word not in uninteresting_words:
            if word not in frequency:
                frequency[word] = 1
            else:
                frequency[word] += 1

    #Generate wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies(frequencies)
    return cloud.to_array()

    #Display wordcloud
    myimage = calculate_frequencies(file_contents)
    plt.imshow(myimage, interpolation = 'nearest')
    plt.axis('off')
    plt.show()
