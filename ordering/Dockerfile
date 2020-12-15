FROM python:3.8-alpine3.10

WORKDIR /code

COPY . /code

RUN pip install -r requirements.txt


EXPOSE 8000

ENTRYPOINT [ "python", "manage.py" ]

CMD [ "runserver" , "0.0.0.0:8000"]