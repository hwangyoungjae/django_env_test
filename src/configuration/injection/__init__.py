import inject
from lazy_streams import stream


def injection_configuration():
    from .core_injection import core_injection
    from .repository_injection import repository_injection
    from .service_injection import service_injection

    inject.configure_once(lambda b: stream([
        core_injection,
        repository_injection,
        service_injection,
    ]).for_each(b.install), bind_in_runtime=False)
