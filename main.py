import streamlit as st

st.title("ai-scrapper")

url_text_input = st.text_input("Enter the URL to scrap: ")

if st.button("Start"):
    print("Start...")
    st.write(f"Scrapping {url_text_input}")

