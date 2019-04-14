FROM python:3.7
EXPOSE 5000

WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY app.py ./
COPY ./bd_init ./bd_init
COPY ./Image ./Image
COPY ./infrastructure ./infrastructure
COPY ./static ./static
COPY ./templates ./templates

CMD python app.py