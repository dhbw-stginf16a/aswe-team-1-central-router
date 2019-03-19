import pytest

from .TestConnexion import TestConnexion


@pytest.mark.usefixtures('client')
class TestMonitor(TestConnexion):
    """Tests the registration of monitoring entities
    """
    def test_registerMonitor(self, client):
        skill = {
            'name': 'calendar',
            'endpoint': 'https://calendar.skills.service/api/v1/',
            'concern': 'calendar'
        }
        response = client.post('/api/v1/monitoring', json=skill)

        assert response.status_code == 204

    def test_getMonitors(self, client):
        response = client.get('/api/v1/monitoring')

        assert response.status_code == 200
        assert response.get_json() == ['calendar']
