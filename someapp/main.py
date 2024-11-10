import os

from somepackage import azure_service
from somepackage import aws_service
# import somepackage.azure_service as azsvc
from utils.utils import get_config


def main():
    app_conf = get_config()
    cloud = os.getenv('SOME_APP_CLOUD', None)

    if cloud.lower() == 'aws':
        status = aws_service.serve(app_conf)

    elif cloud.lower() == 'azure':
        status = azure_service.serve(app_conf)

    else:
        raise NotImplementedError(f"Cloud '{cloud}' is not supported")

    print(f"App deployed. Exit code: {status}")


if __name__ == '__main__':
    main()

