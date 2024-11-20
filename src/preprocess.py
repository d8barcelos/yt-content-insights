import json
import pandas as pd

def load_watch_history(uploaded_file):
    """
    Carrega e processa o arquivo de histórico do YouTube a partir do objeto UploadedFile.
    """
    data = json.load(uploaded_file)
    
    videos = [
        {
            "title": item.get('title'),
            "url": item.get('titleUrl'),
            "time": item.get('time'),
        }
        for item in data if 'title' in item
    ]
    return pd.DataFrame(videos)

def clean_data(df):
    """
    Realiza limpeza básica nos dados.
    """
    df.dropna(subset=['title'], inplace=True)
    df['time'] = pd.to_datetime(df['time'], errors='coerce')
    return df
