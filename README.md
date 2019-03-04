# Central Node

## Requirements

- Pipenv
- Python 3.6

## Setup

- `pipenv install --dev`

## Running in Devolopment

Für Entwicklungszwecke reicht der von Flask mitgelieferte Webserver, der auch automatisch bei Codeänderungen neu startet.

```bash
pipenv shell
export FLASK_APP=app.py
flask run
```

## Running in production

Der integrierte Webserver ist weder sonderlich sicher noch performant daher bietet es sich an etwas sinnvolleres zu verwenden. Mit `pipenv install` ist auch `gunicorn` installiert.

```
gunicorn --bind 0.0.0.0:8080 app:application
```

Reicht diesen zu starten.


## Testcases

### Running tests

Für Testing kommt [pytest](https://docs.pytest.org/en/latest/usage.html) zum Einsatz. Die Integration für Flask ist [hier](http://flask.pocoo.org/docs/1.0/testing/) beschrieben.

```bash
pytest -s
```

Möchte man auch Informationen über Code coverage haben reicht

```bash
coverage run --source './' --omit './test/*' -m pytest
```

Mit `coverage report -m` erhält man denn den Bericht über die Code-Coverage.

### Writing tests

Testcases lassen sich in Klassen organisieren.
Sie sollten im Unterordner Test liegen und folgendem Schema folgen:

```python
import pytest

from .TestConnexion import TestConnexion


@pytest.mark.usefixtures('client')
class TestDemo(TestConnexion):
    """A demo test without real purpose
    """
    def test_example(self, client):
        assert True
```

Der `client` ermöglicht es dann Anfragen an die API zu schicken. Die Funktionsweise ist in der [Dokumentation von Flask](http://flask.pocoo.org/docs/1.0/testing/) erklärt.
