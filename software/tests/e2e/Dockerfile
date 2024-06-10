# software/tests/e2e/Dockerfile
FROM python:3.9

RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sL https://deb.nodesource.com/setup_14.x | bash - \
    && apt-get install -y nodejs \
    && npm install -g playwright \
    && playwright install

RUN pip install robotframework robotframework-browser

WORKDIR /opt/robotframework

COPY . .

CMD ["robot", "--outputdir", "/opt/robotframework/reports", "/opt/robotframework/tests/tests/capture_image.robot"]
