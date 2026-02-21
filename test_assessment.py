import pytest
from assessment import (
    clean_and_format_data, 
    get_total_weight_recursive, 
    generate_shipping_label
)

# --- Tests for Data Manipulation ---
def test_clean_data_standard():
    raw = [(" PKG1 ", 10), ("PKG2", "15.5")]
    expected = [{"id": "PKG1", "weight": 10.0}, {"id": "PKG2", "weight": 15.5}]
    assert clean_and_format_data(raw) == expected

def test_clean_data_filtering():
    raw = [("PKG_BAD", -5), ("PKG_GOOD", 20)]
    assert len(clean_and_format_data(raw)) == 1

# --- Tests for Recursion ---
def test_recursion_nested():
    manifest = [10.5, [5.0, [2.0], 3.0], 1.0]
    # 10.5 + 5 + 2 + 3 + 1 = 21.5
    assert get_total_weight_recursive(manifest) == 21.5

def test_recursion_empty():
    assert get_total_weight_recursive([]) == 0.0

# --- Tests for String Formatting ---
def test_label_formatting():
    assert generate_shipping_label("ABC", 12.3456, "London") == "ID: ABC | Weight: 12.35kg | Dest: London"

def test_label_zero_weight():
    assert "Weight: 0.00kg" in generate_shipping_label("NULL", 0, "Void")
