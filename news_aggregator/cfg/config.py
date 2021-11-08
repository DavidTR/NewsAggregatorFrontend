import os

from dynaconf import Dynaconf

current_directory = os.path.dirname(os.path.realpath(__file__))

settings = Dynaconf(
    envvar_prefix="NEWS_AGGR_FR",
    settings_files=[f"{current_directory}/settings.toml", f"{current_directory}/.secrets.toml"],
)

# `envvar_prefix` = export envvars with `export DYNACONF_FOO=bar`.
# `settings_files` = Load these files in the order.

assert(isinstance(settings.BACKEND["HOST_BASE_URL"], str))
assert(isinstance(settings.BACKEND["CURRENT_VERSION"], str))
assert(settings.BACKEND["HOST_BASE_URL"].endswith('/'))
assert(not settings.BACKEND["CURRENT_VERSION"].endswith('/'))
