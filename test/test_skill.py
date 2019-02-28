import pytest

from .TestConnexion import TestConnexion


@pytest.mark.usefixtures('client')
class TestSkill(TestConnexion):
    """A demo test without real purpose
    """
    def test_registerSkill(self, client):
        skill = {
            'name': 'Calendar',
            'endpoint': 'https://calendar.skills.service/api/v1/'
        }
        response = client.post('/api/v1/skill', json=skill)

        assert response.status_code == 204
