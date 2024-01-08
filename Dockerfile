FROM ubuntu
RUN chmod -R 755 ./
RUN apt update && apt install -y python3-pip && pip install --upgrade pip && pip freeze > requirements.txt
ENTRYPOINT ["./"]
CMD ["python alligator.py"]