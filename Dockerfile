FROM python:3.10-slim
WORKDIR /app
COPY . /app

RUN apt update -y && apt install awscli -y
RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 8000

CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
