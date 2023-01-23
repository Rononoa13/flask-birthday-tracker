FROM python
COPY . /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -requirements.txt
CMD [ "python", "app.py" ]