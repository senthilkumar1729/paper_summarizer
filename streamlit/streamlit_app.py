
import requests
import streamlit as st
#google/pegasus-xsum
#farleyknight/arxiv-summarization-t5-base-2022-09-21
#Stancld/longt5-tglobal-large-16384-pubmed-3k_steps"
#allenai/led-large-16384-arxiv

st.set_option("deprecation.showfileUploaderEncoding", False)
st.title("Summarize research papers")


uploaded_file = st.file_uploader("Choose an image")


#style = st.selectbox("Choose the style", [i for i in STYLES.keys()])


if st.button("Summarize"):
    if uploaded_file is not None:
        files = {"uploaded_file": uploaded_file.getvalue()}
        st.write("ooga Booga")
        res = requests.post(f"http://backend:8080/summarize",files=files)
        #st.image(image, width=500)
        text = res.json()
        #st.write(text.get('name'))

        try:
            st.write(text.get("name"))
        except Exception as e:
            st.write(e)
        #st.write(files)
        st.write("END")

