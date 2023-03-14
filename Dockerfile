FROM python
COPY . /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD [ "flask run" ]