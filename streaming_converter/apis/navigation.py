from functools import reduce
import structlog

log = structlog.get_logger(__name__)


def get_value_by_path_list(path: list[any], data: dict) -> any:
    """This function helps navigate a long dict (mixed or not with arrays )
    by passing a list of indexes.

    Args:
        path (list[any]): List of Indexes to get the value.
        data (dict): Data to be indexed.

    Returns:
        any: The value on the path or None if the index does not exists
    """

    try:
        return reduce(lambda d, x: d[x], path, data)
    except KeyError:
        log.debug("Key does not exists", key=path)
        return None
