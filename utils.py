import time
from functools import wraps


def timing(unit="ms"):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()

            elapsed = end - start

            # Conversione unità
            if unit == "ns":
                elapsed *= 1_000_000_000
                unit_name = "nanoseconds"
            elif unit == "us":
                elapsed *= 1_000_000
                unit_name = "microseconds"
            elif unit == "ms":
                elapsed *= 1000
                unit_name = "milliseconds"
            else:  # 's'
                unit_name = "seconds"

            print(f"{func.__name__}: {elapsed:.3f} {unit_name}")
            return result

        return wrapper

    return decorator
