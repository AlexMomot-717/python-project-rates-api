import os
from typing import Generator

import pytest
from dotenv import load_dotenv
from flask.testing import FlaskClient
from rates_api.app import app as test_app

load_dotenv()


@pytest.fixture
def client() -> FlaskClient:
    test_app.config.update(
        {
            "TESTING": True,
        }
    )
    test_app.secret_key = "test-secret-key"
    return test_app.test_client()


@pytest.fixture
def test_database() -> Generator[None, None, None]:
    """
    Makes tests to use test database
    """
    os.environ["DATABASE_URL"] = os.getenv("DATABASE_URL_TEST")
    yield
