FROM tensorflow/tensorflow:2.3.0-gpu as develop
# this stage is the one we do development in

# Install system libraries for python packages
RUN apt-get update &&  DEBIAN_FRONTEND=noninteractive apt-get install -y \
        graphviz \
        python3-tk \
    # now in the same command clean up the pacakges to shrink layer size
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Install other python library requirements
COPY requirements.txt ./
RUN python3 -m pip install --upgrade pip \
    && python3 -m pip install --no-cache-dir -r requirements.txt

FROM develop as deploy
# this stage is for deploying the application
# copy in source
COPY src /opt/project/src
# change permissions
RUN chmod a+rwx -R /opt/project