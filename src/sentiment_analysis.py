from transformers import DistilBertTokenizer, TFDistilBertForSequenceClassification
from transformers import pipeline

model_checkpoint = "distilbert-base-uncased-finetuned-sst-2-english"
distil_bert_model = pipeline(task="sentiment-analysis", model=model_checkpoint)


def get_sentiment(df, text_col, distil_bert_model = distil_bert_model):
    '''
    Gets sentiment on a dataframe col
    
    :params df (pd.DataFrame) : The data in a pandas dataframe.
    :params text_col (str) : The column containing the text you want to get sentiment on.
    
    :returns df (pd.DataFrame) : The dataframe with a new column containing sentiment.
    '''
    df[f'sentiment_{text_col}'] = df[text_col].apply(lambda x: distil_bert_model(x))

    df[f'sentiment_{text_col}_label'] = df[f'sentiment_{text_col}'].apply(lambda x: x[0]['label'])
    df[f'sentiment_{text_col}_score'] = df[f'sentiment_{text_col}'].apply(lambda x: x[0]['score'])
    df.drop(columns = f'sentiment_{text_col}', inplace = True)
    
    return df