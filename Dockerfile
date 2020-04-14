FROM python:latest

COPY model_binary.dat.gz /app/
COPY requirements.txt /app/
COPY app.py /app/

WORKDIR /app/

RUN pip install -r requirements.txt

ENTRYPOINT ["python"]

CMD ["app.py"]