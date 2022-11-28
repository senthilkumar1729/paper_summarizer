
import uuid
import uvicorn
from fastapi import File
from fastapi import FastAPI
from fastapi import UploadFile
import textract
import tempfile
from utils import get_model, get_tokenizer, create_chunks

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome from the API"}


@app.post("/summarize")
def get_image(model_name:str = 'farleyknight/arxiv-summarization-t5-base-2022-09-21', uploaded_file: UploadFile = File(...)):
    text = ''
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as temp:
        temp.write(file)
        temp.flush()
        context = textract.process(temp.name)
        text = context.decode("UTF-8")

    model = get_model(model_name)
    tokenizer = get_tokenizer(model_name)


    chunks = create_chunks(text,tokenizer)
    inputs = [tokenizer(chunk, return_tensors="pt") for chunk in chunks]

    summarized_text = ''
    for input in inputs:
        output = model.generate(**input)
        summarized_text += str(tokenizer.decode(*output, skip_special_tokens=True))+'. '

    return {"name": summarized_text}


if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)