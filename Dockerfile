FROM alpine:3.10
 
COPY alligator.py
 /alligator.py .
 
ENTRYPOINT ["/alligator.py"]
