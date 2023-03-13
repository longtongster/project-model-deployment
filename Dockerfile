FROM python:3

RUN pip install Flask
RUN pip install matplotlib
RUN mkdir app
WORKDIR app

COPY ./project-model-deployment .

EXPOSE 5000
CMD [ "python", "appie.py" ]
