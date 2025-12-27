"""Search functions for WFPDB plates."""

import json

# Mock plate data for demonstration
PLATES = [
    {"plate_id": "P001", "object": "M31", "filter": "RG610", "date": "1995-07-20", "observer": "Smith"},
    {"plate_id": "P002", "object": "M31", "filter": "B", "date": "1995-08-15", "observer": "Jones"},
    {"plate_id": "P003", "object": "M33", "filter": "RG610", "date": "1996-01-10", "observer": "Smith"},
    {"plate_id": "P004", "object": "M31", "filter": "RG610", "date": "1997-03-22", "observer": "Brown"},
    {"plate_id": "P005", "object": "NGC 224", "filter": "V", "date": "1998-05-05", "observer": "Davis"},
]

def search_plates_by_object(object_name):
    """
    Return plates matching the given object name.
    """
    matches = [plate for plate in PLATES if plate["object"].lower() == object_name.lower()]
    return matches

def search_plates_by_filter(filter_name):
    """
    Return plates matching the given filter name.
    """
    matches = [plate for plate in PLATES if plate["filter"].lower() == filter_name.lower()]
    return matches

def search_plates_by_observer(observer_name):
    """
    Return plates matching the given observer name.
    """
    matches = [plate for plate in PLATES if plate["observer"].lower() == observer_name.lower()]
    return matches

if __name__ == "__main__":
    # Example usage
    print("Plates of M31:", search_plates_by_object("M31"))
    print("Plates with RG610 filter:", search_plates_by_filter("RG610"))