# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- Tightened README Overview; removed cloned Role section.
- Changelog version header now matches `pyproject.toml` (`0.2.2`).

### Fixed

- Sorted module imports to satisfy ruff I001.

## [0.2.2] - 2026-08-22

### Fixed

- Replaced `print()` warning statements with standard Python `logging.warning`.

### Added

- Added `all` extras union to `pyproject.toml` for zero-friction `pip install -e ".[all]"`.

### Changed

- Updated package metadata (author info, Python requirement `>=3.11`).
