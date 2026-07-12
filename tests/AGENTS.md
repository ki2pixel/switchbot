# AGENTS.md - Test Strategy Instructions for Codex

This file applies to all operations performed within the `tests/` directory and contains requirements for implementing or modifying test code.

## 1. Test Perspective Table
- **Design Phase**: Before implementing test code, generate a "test perspectives table" in Markdown format containing: `Case ID`, `Input / Precondition`, `Perspective (Equivalence / Boundary)`, `Expected Result`, `Notes`.
- **Coverage**: Cover normal, error, and boundary cases (0, min, max, ±1, empty, NULL).
- **Non-Blocking**: Do not pause for user confirmation after presenting the table; proceed immediately to implementation unless there are critical ambiguities.

## 2. Given / When / Then Pattern
- Every test case must use the GWT commenting structure (using Python `#` comments):
  ```python
  # Given: Preconditions / Setup
  # When:  Action / Operation executed
  # Then:  Assertions / Expected result
  ```

## 3. Exception & Error Validation
- Explicitly verify the exception **type** and **message**.
- Use mocks to simulate failures and check retries/fallbacks, especially on external APIs (SwitchBot API) and Postgres connection failures.

## 4. Coverage Target
- Aim for 100% branch and statement coverage. 
- Highlight the pytest execution command and verify tests run successfully using:
  ```bash
  source /mnt/venv_ext4/venv_switchbot/bin/activate && python -m pytest
  ```
