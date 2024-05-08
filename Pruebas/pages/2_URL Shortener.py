import streamlit as st
import pyshorteners

def shorter_URL (url):
    s = pyshorteners.Shortener()
    shortened_url = s.tinyurl.short(url)
    return shortened_url

st.set_page_config(page_title="URL Shortener", page_icon="/", layout="centered")
st.title("URL Shortener")
url = st.text_input("Enter the URL")
if st.button("Generate shorter URL"):
    st.write("URL Shortened: ", shorter_URL(url))