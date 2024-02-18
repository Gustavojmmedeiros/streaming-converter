import pytest
from streaming_converter.apis.navigation import get_value_by_path_list


@pytest.mark.parametrize(
    "path, expected",
    [
        (["key1"], "value1"),
        (["key2", "key21"], "value21"),
        (["key3", 1], "value32"),
        (["key4", 0], "value41"),
        (["key5", 0, "key51"], "value51"),
        (["key5", 1, "key52", 0], "value521"),
        (["key6"], None),
    ],
)
def test_get_value_by_path_list(path, expected):
    data = {
        "key1": "value1",
        "key2": {"key21": "value21"},
        "key3": ["value31", "value32"],
        "key4": ("value41", "value42"),
        "key5": [{"key51": "value51"}, {"key52": ["value521"]}],
    }
    value = get_value_by_path_list(path, data)
    assert value == expected
