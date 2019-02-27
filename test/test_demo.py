import pytest

from .TestConnexion import TestConnexion


@pytest.mark.usefixtures('client')
class TestDemo(TestConnexion):
    """A demo test without real purpose
    """
    def test_example(client):
        assert True
