import pytest

@pytest.fixture(scope="function", autouse=True)
def driver():
    pass
    yield driver
    pass