from . import helpers
from lib import meetings


expect = helpers.expect_equal


def test_most_meetings():
    data_set = [
        {'who': 'Marco', 'duration': 5},
        {'who': 'Ustad', 'duration': 6},
        {'who': 'Tony', 'duration': 2},
        {'who': 'Eliza', 'duration': 1},
        {'who': 'Jill', 'duration': 4},
    ]
    expect(meetings.most_meetings(data_set, 8), [
        {'who': 'Eliza', 'duration': 1},
        {'who': 'Tony', 'duration': 2},
        {'who': 'Jill', 'duration': 4},
    ])
    data_set = [
        {'who': 'Amara', 'duration': 5},
        {'who': 'Tony', 'duration': 4},
        {'who': 'Eliza', 'duration': 3.5},
    ]
    expect(meetings.most_meetings(data_set, 8), [
        {'who': 'Eliza', 'duration': 3.5},
        {'who': 'Tony', 'duration': 4},
    ])

def test_most_time():
    data_set = [
        {'who': 'Marco', 'duration': 5},
        {'who': 'Ustad', 'duration': 6},
        {'who': 'Tony', 'duration': 2},
        {'who': 'Eliza', 'duration': 1},
        {'who': 'Jill', 'duration': 4},
    ]
    expect(meetings.most_time(data_set, 8), [
        {'who': 'Ustad', 'duration': 4},
        {'who': 'Tony', 'duration': 2},
    ])
    data_set = [
        {'who': 'Amara', 'duration': 5},
        {'who': 'Tony', 'duration': 4},
        {'who': 'Eliza', 'duration': 3.5},
    ]
    expect(meetings.most_time(data_set, 8), [
        {'who': 'Tony', 'duration': 4},
        {'who': 'Eliza', 'duration': 3.5},
    ])
