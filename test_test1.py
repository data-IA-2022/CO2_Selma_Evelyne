import pytest
from os import environ
from hello_app.views import recup_data

def test_function_with_scenario_one():
    print("Testing function with scenario one")
    assert 1 + 1 == 2, f"Check addition value {1 + 1} does not match {2}"
