# project-model-deployment

Simple flask app that can be used to upload and display an image

## Run using docker

It also has a Dockerfile. In order to run via a container first build the image and then run a container
To build the image type
`sudo docker image build -t flaskapp .`
in the directory of the Dockerfile.

After building the image you can create a container using
`sudo docker container run -d -p 80:80 --name image-app flaskapp`

After uploading an image you can check it is saved inside the container. For this get access the container using
` sudo docker container exec -it image-app bash`

## TODO
- create a requirements.txt
