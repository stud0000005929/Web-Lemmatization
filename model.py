import spacy


def init_model(model_name):
    try:
        nlp = spacy.load(model_name)
        return nlp
    except OSError:
        spacy.cli.download(model_name)
        nlp = spacy.load(model_name)
        return nlp
