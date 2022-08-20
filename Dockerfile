FROM python:3.10

COPY requirements.txt .
ENV FLASK_ENV="docker"
ENV FLASK_APP=main.py
RUN pip install -r requirements.txt

COPY . .

CMD ["flask", "run", "--host=0.0.0.0"]