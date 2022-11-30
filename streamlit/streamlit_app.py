
import requests
import streamlit as st
import time



#google/pegasus-xsum
#farleyknight/arxiv-summarization-t5-base-2022-09-21
#Stancld/longt5-tglobal-large-16384-pubmed-3k_steps"
#allenai/led-large-16384-arxiv
st.set_page_config(layout="wide")

art_text = ''
pdf_text = ''

st.set_option("deprecation.showfileUploaderEncoding", False)

st.markdown("<h1 style='text-align: center; color: white;'>Text Summarization</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: grey;'>Try summarizing your research paper by uploading a pdf or summarizing a news article in the text box below!", unsafe_allow_html=True)


col1, col2 = st.columns((1,1))



st.header("arXiv summarization")
st.image('img/arxiv.png',width = 100)
uploaded_file = st.file_uploader("Choose a pdf")

if st.button("Summarize research paper"):
    if uploaded_file is not None:
        files = {"uploaded_file": uploaded_file.getvalue()}

        start = time.time()
        res = requests.post(f"http://backend:8080/summarize",files=files)
        text = res.json()
        st.write(" Time taken", time.time()- start)
    
        try:
            pdf_text = text.get("summ")
        except Exception as e:
            pdf_text = e

    st.write("Length of original text = ",text.get("length"))
    st.write("Length of summarized text = ",len(pdf_text))
    st.write(pdf_text)
        
st.header("News summarization")
st.image('img/CNN.png',width = 100)
short_text = st.text_area('Text to summarize')

if st.button("Summarize article"):

    start = time.time()
    text = {"text":short_text}
    
    res = requests.post(f"http://backend:8080/short",params=text)
    summarize = res.json()
    st.write("Time taken = ",time.time()-start)

    art_text = summarize.get("summ")


    st.write("Length of original text = ",len(short_text))
    st.write("Length of summarized text = ",len(art_text))

    st.write(art_text)
        
  




#style = st.selectbox("Choose the style", [i for i in STYLES.keys()])






