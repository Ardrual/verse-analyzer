import sys
import os
import pytest
from analyzer.stress import get_word_stress, get_line_stress

# add project root to PYTHONPATH
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


def test_get_word_stress_found():
    # 'hello' should have a valid stress pattern
    stress = get_word_stress('hello')
    assert isinstance(stress, list)
    assert all(isinstance(s, int) for s in stress)
    assert len(stress) > 0


def test_get_word_stress_not_found():
    # gibberish should return None
    stress = get_word_stress('asdkfjhasd')
    assert stress is None


def test_get_line_stress_all_found():
    line = 'hello world'
    result = get_line_stress(line)
    assert isinstance(result, list)
    for entry in result:
        assert 'word' in entry
        assert 'stress' in entry
        assert isinstance(entry['stress'], list)


def test_get_line_stress_some_not_found():
    line = 'hello asdkfjhasd'
    result = get_line_stress(line)
    assert result[1]['word'] == 'none'
    assert result[1]['stress'] == []
