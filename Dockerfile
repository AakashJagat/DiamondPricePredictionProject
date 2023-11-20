FROM python:3.8-slim-buster
WORKDIR /service
COPY requiremnts.txt . 
COPY . ./
RUN pip install requiremnts.txt
ENTRYPOINT [ "python3","app.py" ]

