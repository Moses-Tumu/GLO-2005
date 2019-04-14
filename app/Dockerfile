FROM python:3.7
EXPOSE 5000

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY app.py ./
COPY ./infrastructure ./infrastructure
COPY ./bd_init ./bd_init

CMD python app.py