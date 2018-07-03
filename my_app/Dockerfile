# this is an official Python runtime, used as the parent image
FROM python:3.6.5-slim

# set the working directory in the container to /app
WORKDIR /flask_app

# add the current directory to the container as /app
ADD . /flask_app

# execute everyone's favorite pip command, pip install -r
RUN pip install --trusted-host pypi.python.org -r requirements.txt

# unblock port 500 for the Flask app to run on
EXPOSE 5000

# execute the Flask app
CMD ["python", "run.py"]
