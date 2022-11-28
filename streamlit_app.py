import streamlit as st
import textract
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import tempfile
from scripts import create_chunks


@st.experimental_singleton
def get_model():
    a_model = AutoModelForSeq2SeqLM.from_pretrained("Stancld/longt5-tglobal-large-16384-pubmed-3k_steps")
    return a_model

@st.experimental_singleton
def get_tokenizer():
    a_tokenizer = AutoTokenizer.from_pretrained("Stancld/longt5-tglobal-large-16384-pubmed-3k_steps")
    return a_tokenizer

st.write("Hello world")
model = get_model()
tokenizer = get_tokenizer()


uploaded_file = st.file_uploader("Upload pdf")
text = ''
if st.button("Summarize"):
    st.write('Summarizing')

    context = None
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp:
        temp.write(uploaded_file.getvalue())
        temp.flush()
        context = textract.process(temp.name)
        text = context.decode("UTF-8")


    chunks = create_chunks(text,tokenizer)
    inputs = [tokenizer(chunk, return_tensors="pt") for chunk in chunks]

    summarized_text =[]
    for input in inputs:
        output = model.generate(**input)
        summarized_text.append(tokenizer.decode(*output, skip_special_tokens=True))

    st.write(summarized_text)