
import uuid
import uvicorn
from fastapi import File
from fastapi import FastAPI, UploadFile
from fastapi import UploadFile
import textract
import tempfile
import io
import PyPDF2
from utils import get_model, get_tokenizer, create_chunks

#google/pegasus-xsum
#farleyknight/arxiv-summarization-t5-base-2022-09-21
#Stancld/longt5-tglobal-large-16384-pubmed-3k_steps"
#allenai/led-large-16384-arxiv



app = FastAPI()



@app.get("/")
def read_root():
    return {"message": "fastapi test"}

@app.post("/short")
def short_text(model_name:str = 'arxiv-summarization-t5-base-2022-09-21', text:str = ''):

  
    model_name = 'models/distilbart-xsum-12-3'
    model = get_model(model_name)
    tokenizer = get_tokenizer(model_name)
    print("Tecxt = ", text)
    input_ids = tokenizer(text, return_tensors="pt").input_ids
    outputs = model.generate(input_ids)
    summarized_text = tokenizer.decode(outputs[0], skip_special_tokens=True)
    print(summarized_text)
    return {"name": summarized_text}


@app.post("/summarize")
def get_image(model_name:str = 'arxiv-summarization-t5-base-2022-09-21', uploaded_file: UploadFile = File(default=None)):
    text = ''
  
    print(uploaded_file.file)
    xd = uploaded_file.file
  


    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp:
        temp.write(xd.read())
        temp.flush()
        context = textract.process(temp.name)
        text = context.decode("UTF-8")

    print("Model calls...")

    model_name = 'models/arxiv-summarization-t5-base-2022-09-21'
    model = get_model(model_name)
    tokenizer = get_tokenizer(model_name)


    chunks = create_chunks(text,tokenizer)
    inputs = [tokenizer(chunk, return_tensors="pt") for chunk in chunks]

    summarized_text = ''
    for input in inputs:
        output = model.generate(**input)
        summarized_text += str(tokenizer.decode(*output, skip_special_tokens=True))+'. '
    print(type(summarized_text))
    return {"name": summarized_text}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)