FROM python:3.9

WORKDIR /home/crawler

COPY ./requirements.txt /home/crawler/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /home/crawler/requirements.txt

COPY ./app /home/crawler/app

CMD ["uvicorn", "app.crawler:app", "--reload", "--host", "0.0.0.0", "--port", "8888"]
