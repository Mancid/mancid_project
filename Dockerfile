FROM python:3.6-buster
COPY . .
RUN apt-get install libpq-dev
RUN pip3 install -r requirements.txt
RUN sed 's/\r$//' ./Script.sh > Script_linux.sh
CMD [ "sh", "Script_linux.sh" ]