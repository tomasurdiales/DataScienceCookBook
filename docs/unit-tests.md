# Tests
Tests are an essential part of our development process. Unit tests are written to validate the correctness of our code, ensuring that it behaves as expected under various conditions. Integration tests are written to validate the interaction between different components of a system, for example to check for the connection between a database and a web server (in our case commonly to test the connection to different Azure services).

Our tests are written using `pytest`, or the stock `unittest` python framework. Each test is designed to validate a specific functionality of a component, ensuring that it behaves correctly under various conditions, and fails when it's supposed to fail. One common way to come up with new tests is to think in terms of how **inputs** and **outputs** should relate to each other, writing tests that cover possible edge cases.

We typically arrange to run these tests automatically as part of our **CI&CD pipelines**, ensuring that the code is always in a working state in accordance to the tests written by its developers.

The folder structure we typically recommend is:

    your_project/
    ├── src/
    └── tests/
        ├── __init__.py
        ├── unit/
        │   ├── __init__.py
        │   ├── test_very_complex_ai_product.py
        │   └── ...
        └── integration/
            ├── __init__.py
            └── ...

## Running tests

Where `tests/unit/` contains all the unit tests and `tests/integration/` contains all the integration tests.

To run all tests and provide a summary of the results, use the following command:
```bash
pytest
```
If you want to run a specific test file, you can simply do:
```bash
pytest tests/unit/test_very_complex_ai_product.py
```

## Writing new tests

When writing new tests, follow these guidelines:

- Ensure each test is independent and does not rely on the state of other tests.
- Use descriptive names for test cases to make it clear what functionality is being tested.
- Include setup and teardown steps if necessary to prepare the environment for each test.

---
## Example of a unit test

<h5 style="text-transform: lowercase;">tests/unit/test_very_complex_ai_product.py</h5>
::: tests.unit.test_very_complex_ai_product
