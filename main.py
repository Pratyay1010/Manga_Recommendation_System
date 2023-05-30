import streamlit as st
import pandas as pd
from PIL import Image
import requests
from io import BytesIO
import api


st.set_page_config(layout="wide")

manga_titles = pd.read_pickle("Pickle Files/manga_titles.pkl")
manga_img_url = pd.read_pickle("Pickle Files/manga_img_and_url.pkl")

df = pd.DataFrame({"title": manga_titles})

st.markdown("<h1 style='text-align: center; color: orange;'>Manga Recommendation System</h1>", unsafe_allow_html=True)

option = st.selectbox(
    'Choice your Manga',
    df)

if st.button('Recommend'):
    img_list = {}

    st.header('Recommended Mangas')
    for name in api.recommend_manga(option):
        index = df[df['title'] == name].index[0]
        img_list[name] = manga_img_url['main_picture'][index]

    image_width = 200
    image_height = 300

    cols = st.columns(5)

    num_images = 10

    for i, (name, url) in enumerate(img_list.items()):
        # Check if the image URL exists
        response = requests.get(url)
        if response.status_code == 200:
            # Display the image
            image = Image.open(BytesIO(response.content))
            with cols[i % 5]:
                st.image(image, width=image_width)
                st.write(name)
        else:
            # Display a white image
            white_image = Image.new('RGB', (image_width, image_height), (255, 255, 255))
            with cols[i % 5]:
                st.image(white_image, width=image_width)
                st.write(name)

        # Break the loop if the desired number of images is reached
        if i + 1 == num_images:
            break

    img_list = {}
