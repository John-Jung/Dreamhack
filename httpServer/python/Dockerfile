FROM python:3.12-slim@sha256:8ac54da5710cdd31639bb66f5bc1888948fc2866c0b5b52913b4b33d8252e510   

RUN apt update -y > /dev/null
RUN apt upgrade -y > /dev/null

RUN adduser user

COPY ./deploy /app

RUN chown -R root:user /app
RUN chmod -R 750 /app

USER user

WORKDIR /app

CMD ["python3.12", "-m", "http.server", "8002"]
