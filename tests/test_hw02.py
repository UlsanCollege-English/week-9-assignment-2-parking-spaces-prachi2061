import heapq
import importlib.util
import pathlib

ROOT = pathlib.Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("main", ROOT / "src" / "parking_spaces.py")

main = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(main)
min_parking_spots = main.min_parking_spots

def ref_rooms(intervals):
    if not intervals:
        return 0
    intervals = sorted(intervals, key=lambda x: x[0])
    h = []
    rooms = 0
    for s, e in intervals:
        while h and h[0] <= s:
            heapq.heappop(h)
        heapq.heappush(h, e)
        rooms = max(rooms, len(h))
    return rooms

def test_basic_overlap():
    assert min_parking_spots([(0, 30), (5, 10), (15, 20)]) == 2

def test_no_overlap():
    assert min_parking_spots([(7, 10), (2, 4)]) == 1

def test_chain_touching():
    assert min_parking_spots([(0, 10), (10, 20), (20, 30)]) == 1

def test_mixed():
    assert min_parking_spots([(1, 5), (2, 3), (4, 6)]) == 2

def test_empty():
    assert min_parking_spots([]) == 0

def test_single():
    assert min_parking_spots([(1, 2)]) == 1

def test_zero_length_intervals_same_time():
    assert min_parking_spots([(1, 1), (1, 1), (1, 1)]) == 1

def test_peak_three():
    assert min_parking_spots([(1, 10), (2, 7), (3, 4), (5, 6), (8, 9)]) == 3

def test_random_like_fixed():
    intervals = [(5, 8), (1, 4), (6, 9), (2, 3), (10, 13), (7, 10)]
    assert min_parking_spots(intervals) == ref_rooms(intervals)

def test_larger_set():
    intervals = [(i, i + 3) for i in range(0, 50, 2)]
    assert min_parking_spots(intervals) == ref_rooms(intervals)