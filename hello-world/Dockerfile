FROM python:3.9-slim

ADD . /app

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 8080

# CMD ["gunicorn", "-b", "0.0.0.0:8080]", "app"]
# for cloud run
CMD exec gunicorn --bind :$PORT --workers 1 --threads 8 --timeout 0 main:app
# CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 0 main:app