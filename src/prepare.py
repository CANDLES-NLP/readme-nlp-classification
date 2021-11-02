import unicodedata
import pandas as pd
import re
from nltk import tokenize, stem, corpus

def process_readme(text):
    """Process README text.
    """
    tokenizer = tokenize.toktok.ToktokTokenizer()
    text = tokenizer.tokenize(text, return_str=True)
    text = (unicodedata.normalize('NFKD', text)
            .encode('ascii', 'ignore').decode('utf-8', 'ignore').lower())
    words = re.sub(r"[^a-z\s]", ' ', text).split()
    snowball = stem.SnowballStemmer(language='english')
    stopwords = corpus.stopwords.words('english')
    words = [snowball.stem(word) for word in words if word not in stopwords]
    return ' '.join(words)

def process_readmes(df):
    """Processed READMEs to dataframe.
    """
    df['readme'] = df['readme'].apply(process_readme)
    df['words'] = df.readme.apply(str.split).apply(len)
    df = df[df.words>12]
    freqs = df.language.value_counts().rename('lang_freq')
    df = df.merge(freqs.to_frame(), left_on='language', right_index=True)
    df = df[df.lang_freq >= 90]
    return df

if __name__ == "__main__":
    df = process_readmes(pd.read_csv('trending.csv'))
    print(f'saving {len(df)} records...\n{df.head()}')
    df.to_csv('processed.csv', index=0)