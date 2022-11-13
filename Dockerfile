FROM python:3.8-slim

RUN mkdir -p /app
COPY app.py /app
COPY requirements.txt /app
WORKDIR /app
RUN pip3 install -r requirements.txt
EXPOSE 8081
CMD ["app.py"]
ENTRYPOINT ["python"]