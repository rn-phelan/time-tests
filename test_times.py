from times import compute_overlap_time, time_range
from pytest import raises
import pytest


@pytest.mark.parametrize("test_input,expected", [
    ((time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"), time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)),
        [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]),
    ((time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"), time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00")),
        []),
    ((time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00"), time_range("2010-01-12 12:00:00", "2010-01-12 12:45:00")),
        [])
])
def test_compute_overlap_time(test_input, expected):
    assert compute_overlap_time(*test_input) == expected # start needed to expand

# def test_given_input():
#     large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#     short = time_range("2010-01-12 10:30:00", "2010-01-12 10:45:00", 2, 60)
#     result = compute_overlap_time(large, short)
#     expected = [('2010-01-12 10:30:00', '2010-01-12 10:37:00'), ('2010-01-12 10:38:00', '2010-01-12 10:45:00')]
#     assert result == expected

# def test_compute_overlap_time():
#     large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#     short = time_range("2010-01-12 12:30:00", "2010-01-12 12:45:00")
#     # for a,b in compute_overlap_time(large, short):
#     #     assert b > a,  "There is no overlap time, so incorrectly returns"
#     expected=[] # empty list for no overlap
#     result = compute_overlap_time(large, short)
#     assert result == expected


# def test_touching_times():
#     large = time_range("2010-01-12 10:00:00", "2010-01-12 12:00:00")
#     short = time_range("2010-01-12 12:00:00", "2010-01-12 12:45:00")
#     # result = compute_overlap_time(large, short)
#     # for a,b in compute_overlap_time(large, short):
#     #     assert a==b,  "There is no overlap time, so incorrectly returns"
#     expected=[] # empty list for no overlap, just touching
#     result = compute_overlap_time(large, short)
#     assert result == expected



def test_backwards_time():
    """This is an example of a negative test case. It is checking that specific input will return an error. 
    It passes if it errors
    Also chekc it matches the specific error message"""
    start = "2010-01-12 12:00:00"
    end = "2010-01-12 10:00:00"
    with raises(ValueError, match="Start time is later than end time"):      # Ensure that the ValueError is raised
        time_range(start, end)
    