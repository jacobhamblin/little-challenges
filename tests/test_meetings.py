from . import helpers
from lib import meetings


expect = helpers.expect_equal


def test_most_meetings():
    data_set = [
        {"who": "Marco", "duration": 5},
        {"who": "Ustad", "duration": 6},
        {"who": "Tony", "duration": 2},
        {"who": "Eliza", "duration": 1},
        {"who": "Jill", "duration": 4},
    ]
    expect(
        meetings.most_meetings(data_set, 8),
        [
            {"who": "Eliza", "duration": 1},
            {"who": "Tony", "duration": 2},
            {"who": "Jill", "duration": 4},
        ],
    )
    data_set = [
        {"who": "Amara", "duration": 5},
        {"who": "Tony", "duration": 4},
        {"who": "Eliza", "duration": 3.5},
    ]
    expect(
        meetings.most_meetings(data_set, 8),
        [
            {"who": "Eliza", "duration": 3.5},
            {"who": "Tony", "duration": 4},
        ],
    )


def test_most_time():
    FUNCTION_NAMES = ["most_time", "most_time_more_natural", "most_time_dp"]
    for function_name in FUNCTION_NAMES:
        func = getattr(meetings, function_name)
        data_set = [
            {"who": "Marco", "duration": 5, "id": 1},
            {"who": "Ustad", "duration": 6, "id": 2},
            {"who": "Tony", "duration": 2, "id": 3},
            {"who": "Eliza", "duration": 1, "id": 4},
            {"who": "Jill", "duration": 4, "id": 5},
        ]
        most_time = func(data_set, 8)
        names = [meeting.get("who") for meeting in most_time]
        expect(sorted(names), sorted(["Marco", "Tony", "Eliza"]))
        data_set = [
            {"who": "Amara", "duration": 6, "id": 6},
            {"who": "Tony", "duration": 4, "id": 7},
            {"who": "Eliza", "duration": 3, "id": 8},
        ]
        most_time = func(data_set, 8)
        names = [meeting.get("who") for meeting in most_time]
        expect(sorted(names), sorted(["Tony", "Eliza"]))
        expect(func([{"duration": 9, "who": "Ron", "id": 9}], 8), [])
