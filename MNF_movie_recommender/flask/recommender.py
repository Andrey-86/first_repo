import numpy as np
import pandas as pd
from sklearn.decomposition import NMF
from sqlalchemy import create_engine
import pickle

engine = create_engine('postgresql+psycopg2://postgres:postgres@localhost:5432/movies', echo=False)
df = pd.read_sql('movies', engine, index_col=0)

nmf_model = pickle.load(open('nmf_model.pkl', 'rb'))

def nmf(user_movies, user_ratings):
    reviews = pd.pivot_table(df, values='rating', index='userId', columns='title')
    mean_values = round(reviews.mean().mean(), 1)
    reviews = reviews.fillna(mean_values)

    query = np.zeros(len(reviews.columns))
    for i in range(len(user_movies)):
        query[list(reviews.columns).index(user_movies[i])] = user_ratings[i]

    new_query=query.reshape(-1,1).T
    new_p = nmf_model.transform(new_query)
    nmf_Q = nmf_model.components_
    new_prediction = np.dot(new_p,nmf_Q)
    MOVIES = reviews.columns[np.argsort(new_prediction)][0][-6:-1]

    return MOVIES
