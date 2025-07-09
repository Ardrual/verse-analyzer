# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is a Python-based verse analyzer that identifies stress patterns in poems and lyrics using the CMU pronouncing dictionary. The core functionality analyzes text to determine syllable stress patterns for poetry analysis.

## Development Commands

### Testing
```bash
pytest                    # Run all tests
pytest tests/test_stress.py  # Run specific test file
```

### Dependencies
```bash
pip install -r requirements.txt  # Install dependencies
```

## Architecture

The codebase follows a simple modular structure:

- `analyzer/stress.py` - Core stress analysis functionality with two main functions:
  - `get_word_stress(word)` - Returns stress pattern for individual words as list of integers
  - `get_line_stress(line)` - Returns stress patterns for entire lines as list of dictionaries
- `cli.py` - Command-line interface (currently empty)
- `tests/` - Test suite using pytest framework
- `tests/conftest.py` - Test configuration that adds project root to PYTHONPATH

## Key Dependencies

- `pronouncing` - Primary library for phonetic analysis and stress pattern extraction
- `pytest` - Testing framework
- `cmudict` - CMU pronouncing dictionary for phonetic data

## Testing Strategy

Tests focus on the core stress analysis functions, covering both successful word lookups and handling of unknown words. The test suite validates that stress patterns are returned as expected data structures and that missing words are handled gracefully.