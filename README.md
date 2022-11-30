# Paper Summarizer


## Requirement

- Docker
- Docker compose

## Usage

```
$ git clone https://github.com/senthilkumar1729/paper_summarizer
```

Go into the project directory and run the command:

```
$ docker-compose up -d --build
```

The webapp should be available on `http://localhost:8080` with a streamlit frontend

![alt text](https://github.com/senthilkumar1729/paper_summarizer/blob/main/img/titlepage.png)

Try upoloading a research paper as a pdf for paper summarization or try pasting a news article in the text area for news summarization!

![alt text](https://github.com/senthilkumar1729/paper_summarizer/blob/main/img/news.png)

t5 model needs a bit more finetuning...

![alt text](https://github.com/senthilkumar1729/paper_summarizer/blob/main/img/arxiv.png)
