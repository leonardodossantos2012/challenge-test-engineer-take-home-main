# Simple E2E Test with Robot Framework

## Reason for Using Robot
The Robot Framework was chosen because it is developed in Python, aligning with the existing tests and backend, which are also Python-based. This consistency in language facilitated the automation of the frontend using Python.

The Robot Framework is highly powerful for test automation. Besides frontend automation, it is designed to automate backend, mobile, and desktop applications as well.

In this test framework, I use the Browser Library, a version of Playwright, allowing us to leverage the best features of another robust framework!

## Test Objective
The primary goal of this test was to create a use case that validates whether data is correctly saved in the database.

## Challenges
Given the simplicity of the frontend, I encountered difficulties in locating elements and automating actions. Specifically, the "Capture" and "Shutdown" buttons lacked any actions, preventing validation.

## Solutions
I developed the capture button's action to ensure it could validate if the record was successfully saved in the database.
