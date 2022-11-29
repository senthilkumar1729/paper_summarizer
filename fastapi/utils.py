import nltk
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import tempfile

PATH = 'models/'
def get_model(model_name):
    model_path = PATH + model_name
    a_model = AutoModelForSeq2SeqLM.from_pretrained(model_path,local_files_only = True)
    return a_model




def get_tokenizer(model_name):
    model_path = PATH + model_name
    a_tokenizer = AutoTokenizer.from_pretrained(model_path,local_files_only = True)
    return a_tokenizer






def create_chunks(text:str, tokenizer:object)->list:
    """_summary_

    Parameters
    ----------
    text : str
        _description_
    tokenizer : object
        _description_

    Returns
    -------
    list
        _description_
    """  
    nltk.download('punkt')

    sentences = nltk.tokenize.sent_tokenize(text)
    print(len(sentences))
    length = 0
    chunk = ""
    chunks = []
    count = -1
    for sentence in sentences:
        count += 1
        combined_length = len(tokenizer.tokenize(sentence)) + length

        if combined_length  < tokenizer.max_len_single_sentence: 
            chunk += sentence + " " 
            length = combined_length 

          
            if count == len(sentences) - 1:
                chunks.append(chunk) 
            
        else: 
            chunks.append(chunk)
        # reset 
            length = 0 
            chunk = ""

            
            chunk += sentence + " "
            length = len(tokenizer.tokenize(sentence))
        
    return chunks