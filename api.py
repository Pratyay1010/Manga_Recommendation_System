from fastapi import FastAPI
import recommender

app = FastAPI()

manga_name = ''


@app.get("/")
def home():
    return "Hello"


@app.post("/get-manga")
def recommend_manga(name: str):
    manga_name = name
    return recommender.recommend_manga(manga_name)
