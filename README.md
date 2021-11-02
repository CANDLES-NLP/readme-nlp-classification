# README Classification
### A NLP multi-label classification project

# C.A.N.D.L.E.S

### James Allen
### Carolyn Davis
### Elihezer Lopez
### Steven Newton

- For this project, you will be scraping data from GitHub repository README files. The goal will be to build a model that can predict what programming language a repository is, given the text of the README file.

# Executive Summary

## Goal:
- Build a model that can predict the programming language of a repository on Github, given the text of the README file.

## Takeaways:
- Takeaways

## Recomendations:
- Recommendations

## Deliverables:
- A well documented Jupyter Notebook containing our group analysis

- Google slides suitable for a general audience that summarize your findings. Include a well-labelled visualization in your slides.

# Data Science Pipeline

## Planning
- The group took a look at the trending repositories on Github and then used that list built a dataset from. 

## Acquire
- The necessay python code was written to extract the text of the README file for each page, and the primary language of the repository and stored in an acquire.py file.

## Prepare
- A prepare.py file was created with functions to process the README text data and store as a .csv

## Explore
- Explore the data scraped from Github trending repositories:

    - What are the most common words in READMEs?
    
    - What does the distribution of IDFs look like for the most common words?
    
    - Does the length of the README vary by programming language?
    
    - Do different programming languages use a different number of unique words?


## Modeling

- Transform your documents into a form that can be used in a machine learning model. You should use the programming language of the repository as the label to predict.

- Try fitting several different models and using several different representations of the text (e.g. a simple bag of words, then also the TF-IDF values for each).

- Build a function that will take in the text of a README file, and tries to predict the programming language.

# Data Dictionary



# Conclusion

# Next Steps

## To Recreate This Project

- Make a copy of the final notebook, run each cell, and adjust any parameters as desired

## Sources
- 