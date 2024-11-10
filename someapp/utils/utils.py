import os
from someapp.config import Dev, Prod


def get_config():
    env = os.getenv('SOME_APP_ENV', None)

    app_conf = None
    if env:
        if env.lower() == 'dev':
            app_conf = Dev
        elif env.lower() == 'prod':
            app_conf = Prod
        else:
            raise ValueError(f'Got unknown environment: {env}')
    else:
        raise ValueError('Some app environment is not defined!')

    return app_conf
