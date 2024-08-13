FROM python:3-slim

WORKDIR /Ajedrez

RUN apk update
RUN apk add git
RUN git clone https://github.com/um-computacion-tm/ajedrez-2024-facundomala1.git
WORKDIR /ajedrez-2024-facundomala1
RUN git checkout develop
RUN pip install -r requirements.txt 


RUN pip install -r requirements.txt

CMD [ "sh", "-c", "coverage run -m unittest && coverage report -m && python -m game" ]