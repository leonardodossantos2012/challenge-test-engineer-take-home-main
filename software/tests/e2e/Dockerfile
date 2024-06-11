FROM python:3.9-slim

RUN apt-get update && apt-get install -y \
    curl \
    gnupg \
    build-essential \
    libnss3 \
    libatk1.0-0 \
    libatk-bridge2.0-0 \
    libcups2 \
    libxkbcommon-x11-0 \
    libxcomposite1 \
    libxrandr2 \
    libgbm1 \
    libasound2 \
    libpangocairo-1.0-0 \
    libgtk-3-0 \
    libxshmfence1 \
    libxdamage1 \
    libglu1-mesa \
    fonts-liberation \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sL https://deb.nodesource.com/setup_20.x | bash - && apt-get install -y nodejs

RUN node -v
RUN npm -v

RUN pip install robotframework robotframework-browser

RUN rfbrowser init

WORKDIR /opt/robotframework

COPY . .

ENV PATH="/usr/local/bin/:${PATH}"

# Set the entry point to run the Robot Framework tests
ENTRYPOINT ["robot", "--outputdir", "/opt/robotframework/reports"]
CMD ["/opt/robotframework/tests/tests/capture_image.robot"]