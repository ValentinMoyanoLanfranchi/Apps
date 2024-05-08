import requests
import streamlit as st
import openai
import os

client = openai.OpenAI()
openai.api_key = api_key
def openai_request(prompt):
    headers = {"Authorizacion": f"Bearer {api_key}"}
    response = client.images.generate(
    model="dall-e-3",
    prompt="a white siamese cat",
    size="1024x1024",
    quality="standard",
    n=1,
)
    if response.status_code != 200:
        raise Exception(response.json())
    else:
        image_url = response.data[0].url

    return image_url

def download_image(url, filename):
    response = requests.get(url)
    with open(filename, "wb") as file:
        file.write(response.content)

st.set_page_config(page_title="AI Image Generator", page_icon="", layout="centered")
st.title("AI image Generator")
description = st.text_area("Describe de image")

if st.button("Generate"):
    with st.spinner("Generating"):
        url = openai_request(description)
        filename = "./AI_images/image_generator.png"
        download_image(url, filename)
        st.image(filename, use_column_width=True)
        with open(filename, "rb") as f:
            image_data = f.read()
        download = st.download_button(label="Download Image", data=image_data, file_name="image_generated.jpg")
