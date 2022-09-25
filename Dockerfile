FROM python:latest

WORKDIR /app

COPY . . 

RUN mkdir ~/.kaggle

RUN mv .kaggle/ ~/

RUN pip install --upgrade pip &&\
	pip install -r requirements.txt

CMD ["bash"]