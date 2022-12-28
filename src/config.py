
from dynaconf import Dynaconf
from os import getenv

prod = getenv('PROD')


settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=['settings.toml', '.secrets.toml'],
)
if prod:
    settings.DEBUG = False
    settings.POSTGRES_HOST = 'postgres'
    settings.HOST = '82.180.130.145'
else:
    settings.DEBUG = True
    settings.POSTGRES_HOST = 'localhost'
    settings.HOST = 'localhost:8000'