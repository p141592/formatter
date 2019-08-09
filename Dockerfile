FROM python:3.7
COPY . /opt/application
WORKDIR /opt/application

RUN pip install -r requirements.pip

CMD python main.py
