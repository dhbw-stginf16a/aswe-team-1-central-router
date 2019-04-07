import pytest

from .TestConnexion import TestConnexion


@pytest.mark.usefixtures('client')
class TestPrefstore(TestConnexion):
    """Tests the settings and retrieving of preferences
    """
    def test_setGlobalPrefs(self, client):
        response = client.patch('/api/v1/preferences/global', json= { 'foo': 'bar' })
        assert response.status_code == 204

    def test_getGlobalPrefs(self, client):
        response = client.get('/api/v1/preferences/global')
        assert response.status_code == 200
        assert response.get_json() == { 'foo': 'bar' }

    def test_setUserPrefs(self, client):
        response = client.patch('/api/v1/preferences/user/abc', json = { 'hello': 'world' });
        assert response.status_code == 204

    def test_getUserPrefs(self, client):
        response = client.get('/api/v1/preferences/user/abc');
        assert response.status_code == 200
        assert response.get_json() == { 'hello': 'world' }

    def test_resetUserPrefs(self, client):
        response = client.delete('/api/v1/preferences/user/abc');
        assert response.status_code == 204

        response = client.get('/api/v1/preferences/user/abc');
        assert response.status_code == 200
        assert response.get_json() == {}
