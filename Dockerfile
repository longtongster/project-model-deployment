FROM python:3

RUN pip install Flask
RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
RUN mkdir app

WORKDIR app

COPY ./flaskapp .

EXPOSE 80
CMD [ "python", "appie.py" ]
