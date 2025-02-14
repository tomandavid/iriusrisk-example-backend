FROM tiangolo/uvicorn-gunicorn-fastapi:python3.11

WORKDIR /app

COPY ./app /app/app
COPY ./requirements.txt /app/requirements.txt

RUN pip install --no-cache-dir -r /app/requirements.txt

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]
