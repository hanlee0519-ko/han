FROM python:3.9.0

WORKDIR /home/

RUN git clone https://github.com/hanlee0519-ko/han.git

WORKDIR /home/han/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN echo "SECRET_KEY=_&l_n9s)j3&bp!cwbyvb4z9n=l@g^*_4rx+-voe^ye6alb*ij$" > .env

RUN python manage.py migrate

EXPOSE 8000

CMD ["gunicorn", "han.wsgi", "--bind", "0.0.0.0:8000"]