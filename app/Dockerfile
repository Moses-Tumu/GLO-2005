FROM python:3.7
EXPOSE 5000

WORKDIR /app

COPY requirements.txt /app
COPY users.csv /app
RUN pip install -r requirements.txt

COPY app.py /app
COPY ./Image ./Image
COPY ./infrastructure ./infrastructure
COPY ./static ./static
COPY ./templates ./templates
COPY ./generate_table ./

CMD python app.py