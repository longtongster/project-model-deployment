# project-model-deployment

Simple flask app that can be used to upload and display an image

## Prepera EC2 instance

Use an `ubuntu` AMI and use the user data that is available in the `user_data` file. This should install all the 
necessary packages to run the code in the repository. 

## Run the application using python

cd into the directory `flaskapp`. In order to run the app type:

`python3 appie.py`

this should start the app and run the application in debug model, open for all IP adresses and running on port 80

## Run the application using docker

It also has a Dockerfile. In order to run via a container first build the image and then run a container
To build the image type:

`sudo docker image build -t flaskapp .`

in the directory of the Dockerfile.

After building the image you can create a container using

`sudo docker container run -d -p 80:80 --name image-app flaskapp`

After uploading an image you can check it is saved inside the container. For this get access the container using

` sudo docker container exec -it image-app bash`

## TODO
- train a pytorch classifier - using pytorch workflow
  - train a cats vs dogs model
  - save the weights
  - experiment with tips from the course
  - same transforms during testing as during inference
- implement inference
  - inference via script - DONE
  - create a function `predict` - DONE
  - implement inference to work via flask - DONE
  - show prediction on the site
- create a requirements.txt
- connect to DNS



