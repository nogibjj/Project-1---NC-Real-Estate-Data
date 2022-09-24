FROM python:latest

WORKDIR /app

COPY . . 

RUN pip install --upgrade pip &&\
	pip install -r requirements.txt

RUN chmod +x home_prices
RUN chmod +x download_data.sh

CMD ["./download_data.sh"]
#ENTRYPOINT ["python", "home_prices"]
#CMD ["python", "print('Hello')"]
#CMD ['echo', 'Hello']
#CMD ["home_prices", "download_data"]
#CMD ["home_prices", "analysis"]
#CMD ["home_prices", "filter", "'(bath ==2) & (bed == 3)'", "datasets/predicted-data.csv"]