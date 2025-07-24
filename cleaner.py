class Cleaner:
    def __init__(self, df):
        df.columns = df.columns.str.strip()
        df = df.loc[:, ~df.columns.str.contains('^Unnamed')]
        df.dropna(how='all', inplace=True)
        self.df = df
