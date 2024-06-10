# How I implemented the tests? 

1. First, I resolved to create the unit test to validate the function created.
2. After, I created the integration test to validate the capture_image API.
3. To validate the capture_image I resolve created a new endpoint to see the result returned from database. 

## JSON Schema Validation
The integration tests validate the structure of the API responses using JSON schemas. The schemas are defined in the **tests/utils/schemas.py** file.


