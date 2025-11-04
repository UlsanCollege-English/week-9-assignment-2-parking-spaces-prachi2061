def min_parking_spots(intervals):
    events = []

    zero_length_count = 0

    for start, end in intervals:
        if start == end:
            zero_length_count += 1
        else:
            events.append((start, 'arrive'))
            events.append((end, 'depart'))

    # Sort events: departures before arrivals at same time
    events.sort(key=lambda x: (x[0], x[1] == 'arrive'))

    max_spots = 0
    current_spots = 0

    for _, event_type in events:
        if event_type == 'arrive':
            current_spots += 1
            max_spots = max(max_spots, current_spots)
        else:
            current_spots -= 1

    # If there are only zero-length intervals, return 1
    if not events and zero_length_count > 0:
        return 1

    return max(max_spots, 1 if zero_length_count > 0 else 0)