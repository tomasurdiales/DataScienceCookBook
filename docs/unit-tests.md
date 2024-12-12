# Unit Tests

Unit tests are an essential part of our development process. They help ensure that individual components of our software work as expected. This document provides an overview of the unit tests implemented in the project.

## Overview

Our unit tests are written using `pytest`, or the stock `unittest` python framework. Each test is designed to validate a specific functionality of a component, ensuring that it behaves correctly under various conditions.

## Running the Tests

To run the unit tests, use the following command:

```bash
pytest
```

This command will execute all the tests and provide a summary of the results.

## Writing New Tests

When writing new tests, follow these guidelines:

- Ensure each test is independent and does not rely on the state of other tests.
- Use descriptive names for test cases to make it clear what functionality is being tested.
- Include setup and teardown steps if necessary to prepare the environment for each test.
