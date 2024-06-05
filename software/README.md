# Software Automation Testing Assignment

## Overview
This project is designed to evaluate your skills in writing integration code, conducting integration tests, and debugging a system that consists of a mock AI system, a simulated camera, a database for logging results, and a basic frontend. You will need to integrate these components, test their integration, and improve the system's reliability under certain conditions.

## Repository Structure
The repository contains the following Python files:

- `ai.py`: Contains `AISystemMock`, a class that predicts the presence of defects in images based on a threshold.
- `camera.py`: Contains `CameraMock`, a class that simulates the capture of images with random noise and potential defects.
- `database.py`: Contains `Database`, a class for logging test results into a SQLite database.

Additionally, the repository includes a simple frontend with buttons for controlling the camera:

- `frontend/`: Contains the basic HTML and JavaScript code for the interface with two buttons: "Capture" and "Shutdown", which make POST requests to the backend.

## Tasks

### Task 1: Integration Code
Write a Python script that integrates the `AISystemMock`, `CameraMock`, and `Database` classes. Your script should:
- Capture images using the `CameraMock`.
- Use the `AISystemMock` to predict whether each image has a defect.
- Log each prediction result in the database using `Database`.

### Task 2: Integration Testing
Develop a test suite in Python to verify the integration of the above components. Your tests should verify:
- The correct logging of prediction results into the database.
- The accuracy of defect detection under various scenarios (e.g., with and without defects, under normal and low lighting conditions).
- Setup a GitHub Actions workflow to automate the execution of your tests. The workflow should be triggered on every push to the `main` branch and pull requests.

### Task 3: Debugging and Reliability Enhancement
The `CameraMock` is not deterministic, particularly when the `low_lighting=True` parameter is set, which may affect the reliability of the `AISystemMock`. Perform the following:
- Investigate and document any issues arising from the non-deterministic nature of `CameraMock` under low lighting conditions.
- Propose and implement changes in `AISystemMock` to either fix these issues or improve the system's reliability when handling images captured in low lighting conditions. **Do not change the `CameraMock` method.**

### Task 4: Frontend and End-to-End Testing
- **Frontend Testing**: Write tests using Playwright, Cypress or a similar framework to test the frontend functionality:
  - Ensure the "Capture" button triggers the correct POST request to the backend.
  - Ensure the "Shutdown" button triggers the correct POST request for shutting down the system.
- **End-to-End Testing**: Setup an environment where both the backend and frontend are running. Test the complete system:
  - This can be done using GitHub Actions to automate end-to-end testing, or by providing a recording of the tests running locally.

## Deliverables
Submit the following as part of your project:
1. A Python script containing the integration code.
2. A test suite for the integration.
3. An automated testing pipeline using GitHub Actions.
4. A test suite for frontend functionality.
5. A report detailing any identified issues and the changes you implemented to enhance system reliability. Include before and after test results to demonstrate the effectiveness of your changes.
6. Documentation or a video recording demonstrating the end-to-end tests.

## Evaluation Criteria
- **Code Quality**: Clarity, readability, and adherence to Pythonic practices.
- **Correctness**: Accuracy of the integration and the effectiveness of your test cases in covering possible scenarios.
- **Problem Solving**: Effectiveness of the solutions and enhancements you propose and implement.
- **Documentation**: Clarity and thoroughness of your report on debugging and enhancements.

