FROM python:latest@sha256:6b85854518f812d94cf2dfee2386df85b9cb78835a872d4769b4335f584c43ba
COPY . /app
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD [ "python", "app.py" ]