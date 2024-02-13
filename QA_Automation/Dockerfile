# For more information, please refer to https://aka.ms/vscode-docker-python

FROM python:3.10-slim

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

# Dependencies
RUN apt-get install -y python3
# RUN apt-get install -y python-pytest

RUN mkdir -p /srv/test_module

COPY requirements.txt /srv/requirements.txt
RUN python -m pip install -r requirements.txt

COPY /test_module /srv/test_module

# change to the appropriate folder
WORKDIR /srv/test_module

# Creates a non-root user with an explicit UID and adds permission to access the /app folder
# For more info, please refer to https://aka.ms/vscode-docker-python-configure-containers
# RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
# USER appuser

# During debugging, this entry point will be overridden. For more information, please refer to https://aka.ms/vscode-docker-python-debug
CMD python3 -m pytest test_Divar_Web_search_Vehicle.py

#***********************************************************************

