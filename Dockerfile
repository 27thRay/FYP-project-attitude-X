#Sets Base Image for container
FROM python:3.9-slim 
#lightweight image comes from python3.9

#set working dir for run, cmd, entrypoint, copy
WORKDIR /

#Install git to clone app code from remote repo
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

# Git clone the repo with a specific branch
RUN git clone -b docker_experiment https://github.com/27thRay/FYP-project-attitude-X.git

# Navigate into the cloned directory
WORKDIR /FYP-project-attitude-X

#Install app's python dependencies in container
RUN pip3 install --verbose -r requirements.txt

#Lets container listen to streamlit port 8501
EXPOSE 8501

#Tells docker how to test a container to see if it's still working
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

#Configure container that will run as executable
ENTRYPOINT ["streamlit", "run", "app.py", "--server.port=8501", "--server.address=0.0.0.0"]