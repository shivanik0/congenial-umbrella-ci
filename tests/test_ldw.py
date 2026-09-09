import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from ldw import ldw_count_per_vehicle_per_hour, vehicles_with_warning_per_hour

events = [
    {"vehicle_id": "V1", "timestamp": "2026-09-07 08:15:00", "warning_type": "LDW"},
    {"vehicle_id": "V1", "timestamp": "2026-09-07 08:47:00", "warning_type": "LDW"},
    {"vehicle_id": "V2", "timestamp": "2026-09-07 08:20:00", "warning_type": "LDW"},
    {"vehicle_id": "V1", "timestamp": "2026-09-07 09:05:00", "warning_type": "LDW"},
    {"vehicle_id": "V2", "timestamp": "2026-09-07 10:10:00", "warning_type": "FCW"},
]

def test_count_per_vehicle_per_hour():
    result = ldw_count_per_vehicle_per_hour(events)
    assert result["V1"]["2026-09-07 08"] == 2 ##changed from 2 to 3 for testing ci workflow fail
    assert result["V1"]["2026-09-07 09"] == 1
    assert result["V2"]["2026-09-07 08"] == 1
    assert "V2" not in result or "2026-09-07 10" not in result.get("V2", {})

def test_vehicles_with_warning_per_hour():
    result = vehicles_with_warning_per_hour(events)
    assert result["2026-09-07 08"] == ["V1", "V2"]
    assert result["2026-09-07 09"] == ["V1"]
    assert "2026-09-07 10" not in result   # FCW shouldn't count