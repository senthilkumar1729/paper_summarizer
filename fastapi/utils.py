import nltk
from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
import tempfile

def get_model():
    a_model = AutoModelForSeq2SeqLM.from_pretrained("farleyknight/arxiv-summarization-t5-base-2022-09-21")
    return a_model




def get_tokenizer():
    a_tokenizer = AutoTokenizer.from_pretrained("farleyknight/arxiv-summarization-t5-base-2022-09-21")
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
        combined_length = len(tokenizer.tokenize(sentence)) + length # add the no. of sentence tokens to the length counter

        if combined_length  < tokenizer.max_len_single_sentence: # if it doesn't exceed
            chunk += sentence + " " # add the sentence to the chunk
            length = combined_length # update the length counter

            # if it is the last sentence
            if count == len(sentences) - 1:
                chunks.append(chunk) # save the chunk
            
        else: 
            chunks.append(chunk) # save the chunk
        # reset 
            length = 0 
            chunk = ""

            # take care of the overflow sentence
            chunk += sentence + " "
            length = len(tokenizer.tokenize(sentence))
        
    return chunks