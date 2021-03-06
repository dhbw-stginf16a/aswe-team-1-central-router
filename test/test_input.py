import pytest

from .TestConnexion import TestConnexion


@pytest.mark.usefixtures('client')
class TestInput(TestConnexion):
    """A demo test without real purpose
    """
    @pytest.fixture(scope='session')
    def skill(self, client):
        body = {
            'name': 'CalendarMonitor',
            'endpoint': 'https://calendar.skills.service/api/v1/',
            'interests': ['events_today']
        }
        response = client.post('/api/v1/skill', json=body)

        assert response.status_code == 204

        return body['name']

    def test_intentInput(self, client, skill):
        body = {
            'skill' : skill,
            'payload' : {},
            'type': '',
            'user_handle' : 'AntonHynkel',
            'input_service' : 'Volksempfaenger'
        }
        # response = client.post('/api/v1/request', json=body)

        # assert response.status_code == 200
