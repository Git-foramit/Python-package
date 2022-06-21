# Tests

## Basics on writing a test

Here we use [pytest](https://docs.pytest.org/en/latest/) for writing tests as well as the testing module from
[FastAPI](https://fastapi.tiangolo.com/tutorial/testing/).

## Why testing

Positive:

- Tests help find bugs and logical errors already in an early development phase; thus tests save time and costs in the
  mid-term
- Tests ensure functionality remains functional when new features are added
  ("regression"). As the project grows more complex, this becomes essential.
- Tests encourage refactoring
- Tests help to improve code
- Tests help understand code (sort of a documentation)

Negative:

- Tests cost time in the short term (when writing & when fixing found bugs ;-) )
- When too close to implementation, tests may hinder refactoring

## What to test

When writing new code, it is highly recommended to follow the
[Test-Driven Development (TDD)](https://en.wikipedia.org/wiki/Test-driven_development)
method.

When adding tests to previously untested code, we recommend starting with the following components:

- public methods/ interfaces
- methods with complex logic
- methods whose failure would have fatal consequences

In general, follow the testing pyramid, i.e. use many unit tests, some integration tests to ensure your interfaces work
and a few end-to-end-tests.

## Test automation

Experience shows, that if test execution is not automated, then no one will execute the tests, at least not regularly.
This is why -- if you have tests -- you want to set up a `jenkins` pipeline, so that each commit triggers a full build
and test run.

## Testing API methods

Let's say you have a file `health.py` that checks whether the API is running. It has a ``GET`` operation that returns
a ``JSON`` message:

```Python
from fastapi import APIRouter
from starlette.responses import JSONResponse

router = APIRouter()

@router.get("")
def get_health():
    """Return the status of the server."""
    return JSONResponse(status_code=200, content={"message": "OK"})

```

Your `tests/test_health.py` file could look like this:

```Python
import pytest
from fastapi.testclient import TestClient

from sample_ws.main import app

client = TestClient(app)


@pytest.mark.parametrize(
    "path,expected_status,expected_response",
    [("/samplews/health", 200, {"message": "OK"},),],
)
def test_health(path, expected_status, expected_response):
    response = client.get(path)
    assert response.status_code == expected_status
    assert response.json() == expected_response

```

We create a ``TestClient`` from the FastAPI app defined in the `main.py`. We create a method starting with ``test_``
where we pass the input to the client and check whether the response is as expected. To define expected response, we
use [@pytest.mark.parametrize](https://docs.pytest.org/en/stable/parametrize.html) decorator to pass arguments to the
test function. This contains the path that is being tested, the expected status code and expected response defined
as ``JSON`` or ``dict``.

Go to [Documentation](documentation.md) to learn how to write nice documentation like this one.
