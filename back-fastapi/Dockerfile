FROM python:3.11.3-alpine

WORKDIR /src

COPY ./requirements.txt /requirements.txt

RUN pip install --no-cache-dir --upgrade -r /requirements.txt

COPY ./ /

CMD ["uvicorn", "main:app", "--host", "back_fastapi", "--port", "8000"]
