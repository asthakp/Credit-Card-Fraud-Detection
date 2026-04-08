def load_data():
    import pandas as pd
    from src.db_connection import get_engine
    engine=get_engine()
    df=pd.read_sql('select * from transactions',engine)
    return df