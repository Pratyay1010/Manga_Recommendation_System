import pickle
import pandas as pd

manga_titles = pd.read_pickle("Pickle Files/manga_titles.pkl")
similarity = pickle.load(open("Pickle Files/similarity.pkl", "rb"))
manga_img_url = pd.read_pickle("Pickle Files/manga_img_and_url.pkl")

df = pd.DataFrame({"title": manga_titles})


def recommend_manga(name):
    index = df[df['title'] == name].index[0]

    similar_mangas = sorted(list(enumerate(similarity[index])), key=lambda x: x[1], reverse=True)[1:11]

    recommendation = []
    for name in similar_mangas:
        recommendation.append(df.iloc[name[0]]['title'])

    return recommendation