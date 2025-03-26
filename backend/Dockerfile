FROM python:3.10-slim


RUN apt-get update && apt-get install -y netcat-openbsd && apt-get clean



WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["bash", "wait-for-it.sh", "db", "5432", "--", "python", "manage.py", "runserver", "0.0.0.0:8000"]
