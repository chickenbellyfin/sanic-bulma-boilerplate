FROM --platform=$BUILDPLATFORM node:lts as build_web
WORKDIR /app
COPY package.json package.json
COPY yarn.lock yarn.lock
RUN yarn install

COPY . .

RUN yarn build


FROM python:3
WORKDIR /app
COPY requirements.txt requirements.txt
RUN python3 -m pip install -r requirements.txt
COPY . .

COPY --from=build_web /app/static /app/static

ENTRYPOINT ["python3", "-m", "app"]
EXPOSE 8080