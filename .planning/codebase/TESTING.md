# Testing Patterns

**Analysis Date:** 2026-04-19

## Test Framework

**Status:** No test framework configured

**Runner:** Not configured

**Assertion Library:** Not configured

**Observation:** No test files found in codebase. This is a gap that should be addressed.

## Test File Organization

**Location:** Not established (no tests directory)

**Naming:** Not established

**Structure:**
```
[recommended structure]
tests/
├── __init__.py
├── test_storage.py      # Tests for Storage class
└── test_main_window.py # Tests for UI components
```

## Test Structure

**Suite Organization:**

```python
import unittest
from unittest.mock import patch, MagicMock
from data.storage import Storage


class TestStorage(unittest.TestCase):
    def setUp(self):
        """Set up test fixtures."""
        self.storage = Storage()
    
    def tearDown(self):
        """Clean up after tests."""
        pass
    
    def test_add_activity(self):
        """Test adding new activity."""
        activity = self.storage.add_activity("TestActivity", "#FF0000")
        self.assertIsNotNone(activity)
        self.assertEqual(activity["name"], "TestActivity")


if __name__ == "__main__":
    unittest.main()
```

**Patterns:**
- `setUp()` method for test fixture initialization
- `tearDown()` for cleanup if needed
- Standard assertions: `assertEqual()`, `assertIsNotNone()`, `assertTrue()`

## Mocking

**Framework:** No mocking framework currently in use

**What to Mock:**
- File I/O operations: Use `unittest.mock.patch` to mock `open()` and JSON operations
- Qt classes: Mock or use dummy QApplication instance
- Storage data directory: Mock `Path.home()` for isolated tests

**Example Mocking Pattern:**
```python
from unittest.mock import patch, mock_open
import json

def test_load_data_with_mock(self):
    """Test _load_data with mocked file operations."""
    test_data = {"activities": [{"name": "Test", "color": "#000", "total_seconds": 100}]}
    
    with patch("pathlib.Path.home") as mock_home:
        mock_home.return_value = MagicMock()
        mock_home.return_value.__truediv__ = MagicMock(return_value=MagicMock())
        
        with patch("builtins.open", mock_open(read_data=json.dumps(test_data))):
            storage = Storage()
            result = storage._load_data()
            self.assertIn("activities", result)
```

**What NOT to Mock:**
- Test pure logic in Storage class
- Test actual data transformation (e.g., lowercase comparisons)

## Fixtures and Factories

**Test Data:**
```python
# Test data fixtures
VALID_ACTIVITY = {"name": "TestActivity", "color": "#FF0000", "total_seconds": 0}
VALID_SETTINGS = {"window_position": {"x": 100, "y": 100}, "always_on_top": True}

# Factory for creating test activities
def create_activity(name="TestActivity", color="#FF0000", total_seconds=0):
    return {"name": name, "color": color, "total_seconds": total_seconds}
```

**Location:** Recommend placing fixtures in `tests/fixtures.py` or within test files

## Coverage

**Requirements:** Not established

**Target:** Recommended: 80%+ coverage for Storage class

**View Coverage:**
```bash
python -m pytest --cov=data.storage tests/  # With pytest
python -m coverage run -m pytest    # With coverage
python -m coverage report          # View report
```

## Test Types

**Unit Tests:**
- Test `Storage` class methods in isolation: `add_activity()`, `add_time()`, `get_activity_color()`
- Test data transformation logic: lowercase comparisons, activity lookup

**Integration Tests:**
- Test `Storage` file I/O operations (require mocking or temp directories)
- Test `MainWindow` Qt widget interactions (require QApplication instance)

**E2E Tests:** Not recommended for this project (Qt GUI tested via manual use)

## Qt Testing Recommendations

**QApplication Handling:**
```python
import pytest
from PySide6.QtWidgets import QApplication
from unittest.mock import MagicMock


@pytest.fixture(scope="session")
def qapp():
    """Create QApplication instance for testing Qt components."""
    app = QApplication.instance()
    if app is None:
        app = QApplication([])
    yield app
```

**Widget Testing:**
```python
@pytest.mark.parametrize("activity_name,expected", [
    ("Work", "#FF0000"),
    ("Meeting", "#00FF00"),
])
def test_get_activity_color(activity_name, expected):
    """Test activity color retrieval."""
    storage = Storage()
    storage.add_activity(activity_name, expected)
    result = storage.get_activity_color(activity_name)
    assert result == expected
```

## Recommendations

**Add Tests:**
1. Test `storage.py` is priority - contains business logic with clear inputs/outputs
2. Test data transformation: lowercase name matching in `add_activity()`, `add_time()`, `get_activity_color()`
3. Test edge cases: empty activity name, duplicate activities, zero seconds

**Framework Choices:**
- **pytest**: Popular, easy mocking, good fixture support
- **unittest**: Built-in, no additional dependencies

**Recommended Test Dependencies:**
```
pytest>=7.0.0
pytest-cov>=4.0.0  # For coverage reporting
```

---

*Testing analysis: 2026-04-19*