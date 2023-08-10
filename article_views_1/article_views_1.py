import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    df = views[views.author_id == views.viewer_id]
    df = df[["author_id"]].rename(columns = { 'author_id':'id'} ).drop_duplicates()
    df = df.sort_values(by='id').reset_index(drop=True)
    return df
