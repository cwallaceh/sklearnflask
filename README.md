# Flask API for scikit learn in Docker
A simple Flask application in a docker image that can serve predictions from a scikit-learn model inside a Docker container. Reads a pickled sklearn model into memory when the Flask app is started and returns predictions through the /predict endpoint. Any sklearn model can be used for prediction.

### Dependencies
- scikit-learn
- Flask
- pandas
- numpy

## Build the docker image
To build the docker image run:
```
docker build . -t model
```
Or run the file: 'create_image.sh'

### Running the container
Run the docker container as:
```
docker run -p 8080:8080 model:latest
```
Or run the file: 'docker_run.sh'

# Endpoints
### /predict (POST)
Returns a dict with the prediction given a JSON object representing independent variables.

### /info (GET)
Return the model info, version and help.
