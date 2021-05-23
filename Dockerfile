FROM python:3.6-buster
COPY . .
RUN pip3 install -r requirements.txt
RUN sed 's/\r$//' ./Script.sh > Script_linux.sh
EXPOSE 5000
CMD [ "sh", "Script_linux.sh" ]