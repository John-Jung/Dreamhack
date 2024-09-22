FROM python:3.12-slim@sha256:8ac54da5710cdd31639bb66f5bc1888948fc2866c0b5b52913b4b33d8252e510   

RUN apt update -y > /dev/null
RUN apt upgrade -y > /dev/null

RUN adduser user

COPY ./app.py /home/user/app.py

RUN chown -R root:user /home/user
RUN chmod -R 750 /home/user

USER user

CMD ["python3.12", "/home/user/app.py"]
