class Common(object):
    APP_NAME = 'Some App'


class Dev(Common):
    APP_ENDPOINT = 'dev.server:8081'


class Prod(Common):
    APP_ENDPOINT = 'prod.server:8080'



