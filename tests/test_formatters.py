from matplotlib_views import formats


def test_time_formats():

    assert formats.formatter_time(2 * 60 * 60, "") == "2h"
    assert formats.formatter_time(60, "") == "1m"
    assert formats.formatter_time(3, "") == "3s"

    print(formats.formatter_time(5_000_000, ""))  # 57 days
