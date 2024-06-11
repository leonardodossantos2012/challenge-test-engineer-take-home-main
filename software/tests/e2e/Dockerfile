# software/tests/e2e/Dockerfile
FROM python:3.9


# Install Node.js and npm
RUN curl -fsSL https://deb.nodesource.com/setup_20.x | bash  - 

RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y nodejs \
    npm                       # note this one

# Install Playwright and browsers
RUN npm install -g playwright && PLAYWRIGHT_BROWSERS_PATH=/root/.cache/ms-playwright npx playwright install

# Install Robot Framework and Browser library
RUN pip install robotframework robotframework-browser

# Setup working directory
WORKDIR /opt/robotframework

# Copy the tests to the container
COPY . .

# Set the entry point to run the Robot Framework tests
ENTRYPOINT ["robot", "--outputdir", "/opt/robotframework/reports", "/opt/robotframework/tests/tests/capture_image.robot"]
