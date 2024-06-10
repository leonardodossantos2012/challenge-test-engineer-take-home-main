# Code Challenge Overview.ai

This project aim has principal objective resolve the challenge following the documentation [Software Automation Testing Assignment](./software/docs/challenge.md)


## Documentation about the implementation

Explaing about the decisions implementation to each task at software: 

- [Task 2](./software/docs/task2.md)
- [Task 3](./software/docs/task3.md)
- [Task 4](./software/docs/task4.md)
- [Bonus](./software/docs/bonus.md)

# Project Structure

This project follows a structured organization to ensure clarity and ease of navigation. Below is a detailed explanation of the folder hierarchy and the objectives of each component.

## .github/workflows
- **continuos-test.yml**: Contains the GitHub Actions workflow definitions for continuous integration and testing.

## software
This directory contains the core software components and associated documentation.

### components
- **__init__.py**: Initializes the Python package.
- **ai.py**: Contains the AI-related functionalities and algorithms.
- **camera.py**: Manages camera operations and image processing.
- **database.py**: Handles database interactions and queries.

### docs
This subdirectory includes various documentation files for different tasks and challenges.
- **bonus.md**: Documentation for additional, optional tasks.
- **challenge.md**: Main challenge documentation and requirements.
- **task1.md**: Details and objectives of Task 1.
- **task2.md**: Details and objectives of Task 2.
- **task3.md**: Details and objectives of Task 3.
- **task4.md**: Details and objectives of Task 4.

### front-end
This directory includes all front-end related code and configurations for the project.
- **.next**: Next.js build output directory.
- **app**: Contains the main application components and pages.
- **node_modules**: Directory for installed Node.js modules.
- **public**: Public assets for the front-end application.
- **.eslintrc.json**: ESLint configuration file.
- **.gitignore**: Specifies files and directories to be ignored by Git.
- **Dockerfile**: Docker configuration for containerizing the front-end application.
- **next-env.d.ts**: TypeScript declarations for Next.js.
- **next.config.mjs**: Configuration file for Next.js.
- **package-lock.json**: Dependency tree for the Node.js application, auto-generated.
- **package.json**: Node.js project manifest file listing dependencies and scripts.
- **postcss.config.mjs**: Configuration file for PostCSS.
- **README.md**: Documentation for the front-end application.
- **tailwind.config.ts**: Configuration file for Tailwind CSS.
- **tsconfig.json**: TypeScript configuration file.

## tests
This directory contains all test-related files and scripts, divided into different testing strategies.
- **integration**
  - **test_validate_camera.py**: Integration tests for validating camera functionalities.
- **unit**
  - **__init__.py**: Initializes the unit tests package.
  - **test_app.py**: Unit tests for the application logic.
- **utils**
  - **schemas.py**: Contains data schemas for validation and parsing.
  - **__init__.py**: Initializes the utils package.
  - **conftest.py**: Configuration for pytest fixtures.
  - **app.py**: Utility functions and helpers.
- **compose.yaml**: Docker Compose configuration file for setting up the test environment.
- **Dockerfile**: Docker configuration for the test environment.
- **requirements.txt**: Lists Python dependencies for the tests.
- **test_results.db**: Database file to store test results.

## README.md
This file provides an overview and documentation of the entire project.



