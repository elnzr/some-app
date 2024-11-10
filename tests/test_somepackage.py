from context import someapp
from someapp.somepackage import aws_service
from someapp.somepackage import azure_service
from someapp.config import Common


class TestConf(Common):
    APP_ENDPOINT = 'test-endpoint:8081'


def test_app_aws_deploy():
    test_conf = TestConf()
    status = aws_service.serve(test_conf)
    assert status == 0


def test_app_azure_deploy():
    test_conf = TestConf()
    status = azure_service.serve(test_conf)
    assert status == 0

