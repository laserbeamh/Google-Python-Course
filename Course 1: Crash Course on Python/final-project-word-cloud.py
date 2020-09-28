"""
This script will take an input file, clean the text of punctuation,
remove any common words and, finally, produce a word cloud image.
"""
#Install dependencies
!pip install wordcloud
!pip install fileupload
!pip install ipywidgets

using_jupyter = input("Are you using a Jupyter Notebook? (yes/no)")
if using_jupyter == yes:
	!jupyter nbextension install --py --user fileupload
	!jupyter nbextension enable --py fileupload
elif using_jupyter == no:
	break
else:
	print("Not a valid choice. Not installing Jupyter depends")

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
file = file.open(filepath)

#Open/read file contents

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

    # LEARNER CODE START HERE
    frequency = {}

    #wordcloud
    cloud = wordcloud.WordCloud()
    cloud.generate_from_frequencies()
    return cloud.to_array()
