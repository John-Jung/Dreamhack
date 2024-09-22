FROM node:22-alpine@sha256:bec0ea49c2333c429b62e74e91f8ba1201b060110745c3a12ff957cd51b363c6

RUN apk update -q
RUN apk upgrade -q

RUN addgroup -S user && adduser -S user -G user

RUN npm install -g http-server

COPY ./deploy /app

RUN chown -R root:user /app
RUN chmod -R 750 /app

USER user

CMD ["http-server", "/app", "-p", "8001"]