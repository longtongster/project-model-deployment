FROM python:3

RUN pip install Flask
RUN mkdir app
WORKDIR app

COPY ./flaskapp .

EXPOSE 80
CMD [ "python", "appie.py" ]
