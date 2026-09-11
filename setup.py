def setup():
    ...

def config_exists():
    ...

def check_setup():
    if not config_exists():
        setup()