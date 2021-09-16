FROM python:3.9

WORKDIR /blog

COPY requirements.txt requrirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD ['python3', 'manage.py', 'runserver', '0.0.0.0:8000']
