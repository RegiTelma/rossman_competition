import pandas as pd
import numpy as np
import datetime



store = pd.read_csv('data/store.csv')


def merge_clean(df, store):
    df = df.drop_duplicates()
    df = df.dropna()

    # convert string Date to datetime
    df['Date'] = pd.to_datetime(df.Date, format='%Y-%m-%d')

    df = pd.merge(df, store, how='outer', on='Store')
    
    # ohe shopping days are 1 and closed is 0
    df['StateHoliday'] = df.StateHoliday.apply(lambda x: 1 if x in ['0', 0.0] else 0)


    interval_dict = {np.nan: 0, 'Jan,Apr,Jul,Oct':1, 'Feb,May,Aug,Nov':2, 'Mar,Jun,Sept,Dec': 3}
    df['PromoInterval'] = df['PromoInterval'].map(interval_dict)
    

    return df



def downcast(df):
    for col in df.columns:
            if pd.api.types.is_numeric_dtype(df[col]):
                df[col] = pd.to_numeric(df[col], downcast='integer')

    df.DayOfWeek = df.DayOfWeek.astype('int8')
    
    # median imputing and converting to int (nobody cares for half a meter to the Competition)
    median_distance = df.CompetitionDistance.median()
    competiton_distance = df.CompetitionDistance.fillna(median_distance).round()
    df.CompetitionDistance = pd.to_numeric(competiton_distance, downcast='integer')

    df.CompetitionOpenSinceMonth = df.CompetitionOpenSinceMonth.fillna(0).round().astype('int')
    df.CompetitionOpenSinceYear = df.CompetitionOpenSinceYear.fillna(0).round().astype('int')
    df.Promo2SinceWeek = df.Promo2SinceWeek.fillna(0).round().astype('int')
    df.Promo2SinceYear = df.Promo2SinceYear.fillna(0).round().astype('int')

    return df



# feature engineer a promo running time
def feature_engineer(df):
    year = datetime.today().year
    df['Promo2_time'] = year - df.Promo2SinceYear

    return df


def encoder(df):
    import category_encoders as ce

    # create an object of the OneHotEncoder
    ce_one = ce.OneHotEncoder(cols=['Promo', 'Promo2','SchoolHoliday','Open']) 
    df = ce_one.fit_transform(df)


    
    return df


def preprocessor(df):
    df = merge_clean(df)
    df = downcast(df)
        
    return df




