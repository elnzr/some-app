import os
import pytest

from context import someapp
from someapp.utils.utils import get_config


def test_dev_config_correct():
    os.environ['SOME_APP_ENV'] = 'DEV'
    actual_conf = get_config()

    assert actual_conf.APP_ENDPOINT == 'dev.server:8081'


def test_prod_config_correct():
    os.environ['SOME_APP_ENV'] = 'PROD'
    actual_conf = get_config()

    assert actual_conf.APP_ENDPOINT == 'prod.server:8080'


def test_config_validation():
    with pytest.raises(ValueError, match='environment is not defined'):
        os.environ['SOME_APP_ENV'] = ''
        actual_conf = get_config()

