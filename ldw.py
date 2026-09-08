from collections import defaultdict
from datetime import datetime

def parse_hour(timestamp: str) -> str:
    """Round a timestamp down to its hour bucket, e.g. '2026-09-07 08'."""
    dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
    return dt.strftime("%Y-%m-%d %H")

def ldw_count_per_vehicle_per_hour(events):
    """Return {vehicle_id: {hour: count}} for LDW warnings only."""
    result = defaultdict(lambda: defaultdict(int))
    for e in events:
        if e["warning_type"] == "LDW":
            hour = parse_hour(e["timestamp"])
            result[e["vehicle_id"]][hour] += 1
    return {v: dict(hours) for v, hours in result.items()}

def vehicles_with_warning_per_hour(events):
    """Return {hour: [vehicle_ids]} for vehicles with >=1 LDW warning that hour."""
    result = defaultdict(set)
    for e in events:
        if e["warning_type"] == "LDW":
            hour = parse_hour(e["timestamp"])
            result[hour].add(e["vehicle_id"])
    return {h: sorted(v) for h, v in result.items()}
