FROM python:3.8
RUN mkdir /app/website
WORKDIR /app/website/
ADD . /app/website/
RUN pip install -r requirements.txt
CMD ["python", "/app/website/app.py"]