# project-model-deployment

This goal of this project is to deploy a pytorch model using flask on an EC2 instance. 
A second objective is to containerize the application using docker.

The application allows one to upload a cat or dog image and let the pytorch image classify the image.

## Prepare the EC2 instance

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
- Include the notebook that was used to train the pytorch model
  - train a cats vs dogs model
  - save the weights
  - experiment with tips from the course
  - same transforms during testing as during inference
- create a requirements.txt
- connect to DNS



