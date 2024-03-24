# Pulling Ubuntu image
FROM python:3.10.12-alpine3.18

# create source directory
WORKDIR /scrapy_app

# Copy & install requirements.txt
COPY ./requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# copy source code
COPY . .
ADD ./init.sh /init.sh

RUN chmod +x /init.sh

ENV SCRAPY_MODE prod
ENV INTERVAL 300

# Creating entrypoint for cron
ENTRYPOINT ["/init.sh"]
