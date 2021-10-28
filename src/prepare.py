import unicodedata
import pandas as pd
import re
import nltk

def process_readme(text):
    """Process README text.
    """
    return text

def process_readmes(df):
    """Processed READMEs to dataframe.
    """
    return df

if __name__ == "__main__":
    df = process_readmes('repos.csv')
    df.to_csv('processed_text.csv', index=0)