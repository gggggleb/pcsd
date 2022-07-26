FROM python:alpine

COPY ./docker-conf.py ./config.py

RUN pip install --index-url https://git.glebmail.xyz/api/packages/PythonPrograms/pypi/simple pcsd

CMD pcsd

EXPOSE 4010