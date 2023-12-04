import spacy
import pandas as pd


def init_model(model_name='ru_core_news_md'):
    try:
        nlp = spacy.load(model_name)
        return nlp
    except OSError:
        spacy.cli.download(model_name)
        nlp = spacy.load(model_name)
        return nlp

def get_json(text, model_name='ru_core_news_md'):

    nlp = init_model(model_name)

    doc = nlp(text)

    dfLemma = pd.DataFrame({'text': [token.text for token in doc],
                            'pos': [token.pos_ for token in doc],
                            'dep': [token.dep_ for token in doc]})

    return dfLemma.to_json(force_ascii=False)

def get_str(text, model_name='ru_core_news_md'):
    return str(get_json(text, model_name))
