FROM python:3.9-slim

# Install necessary packages
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

# Install Node.js and npm
RUN curl -sL https://deb.nodesource.com/setup_20.x | bash - && apt-get install -y nodejs

# Verify Node.js and npm installation
RUN node -v
RUN npm -v

# Install Playwright and browsers
RUN npm install -g playwright && \
    PLAYWRIGHT_BROWSERS_PATH=/root/.cache/ms-playwright npx playwright install

# Install Robot Framework and Browser library
RUN pip install robotframework robotframework-browser

# Initialize the Browser library
RUN rfbrowser init

# Setup working directory
WORKDIR /opt/robotframework

# Copy the tests to the container
COPY . .

# Ensure Node.js is in PATH
ENV PATH="/usr/local/bin/:${PATH}"

# Set the entry point to run the Robot Framework tests
ENTRYPOINT ["robot", "--outputdir", "/opt/robotframework/reports"]
CMD ["/opt/robotframework/tests/tests/capture_image.robot"]
