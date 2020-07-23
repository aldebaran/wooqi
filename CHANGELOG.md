# Change Log
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](http://keepachangelog.com/)
and this project adheres to [Semantic Versioning](http://semver.org/).

***
## [unreleased] - YYYY-MM-DD
### Enhanced
- None

### Added

### Changed
- None

### Deprecated
- None

### Removed
- None

### Fixed
- None

### Security
- None

### Known Issues
- None

***
## [5.0.1] - 2020-07-23

### Added
- `setup.py` `src/conftest.py` `src/logger.py` `src/plugin_fixtures.py`:  Replace ConfigParser by configparser to manage python2 and python3

### Changed
- `config_test.py`: Change section's values from unicode to str

***
## [5.0.0] - 2020-02-24
### Enhanced
- None

### Added
- `src/__init__.py`: Add simple logger with package name.

### Changed
- `plugin_fixtures.py`: Remove log_folder, log_name and logger fixture.
- `pytest_hooks.py`: Use new logger instead of logger_gv.

### Deprecated
- None

### Removed
- `src/__init__.py`: Remove logger_gv.
- `scr/logger.py`: Remove init_logger method.

### Fixed
- None

### Security
- None

### Known Issues
- None

***
## [4.0.2] - 2020-01-31
### Fixed
- `sequencer_features.py`: Manage test_required when the failed test was in a class

***
## [4.0.1] - 2019-12-16
### Fixed
- Manage parametrize decorator

***
## [4.0.0] - 2019-12-13
### Added
- If multiple call of the same test if found, wooqi automatly add '-X' if missing of configuration file
- Control conformity of configuration file: The test of post_fail and test_required are found
- Control conformity of configuration file: All actions/tests of configuration file are found

### Changed
- To call multiple time the same test, we must add '-X' instead of '_X'

### Deprecated
- The old system confused some test names. Add '_X' to call multiple time the same test is deprecated, instead add '-X'

### Fixed
- Testing functions are missing

***
## [3.0.0] - 2019-08-09
### Removed
- Remove fork pytest

### Fixed
- Fix exit status in main to get msb value
- Fix fail management in loop

***
## [2.0.1] - 2018-11-15
### Fixed
- Packages management hotfix.

***
## [2.0.0] - 2018-11-14
### Enhanced
- [Issue #13](https://gitlab.aldebaran.lan/production/wooqi/issues/13): Do not base the sequencer on Pytest anymore.
- [Issue #28](https://gitlab.aldebaran.lan/production/wooqi/issues/28): Fork Pytest inside Wooqi.
- Python 3 compatibility.

***
## [1.2.2] - 2018-10-26
### Fixed
- [Issue #35](https://gitlab.aldebaran.lan/production/wooqi/issues/35): Update dependencies versions required.

***
## [1.2.1] - 2018-08-07
### Enhanced
- [Issue #21](https://gitlab.aldebaran.lan/production/wooqi/issues/21): Add possibility to give 3 arguments to range().
- [Issue #31](https://gitlab.aldebaran.lan/production/wooqi/issues/31): Wooqi project - place actions in test_steps folder.

### Added
- [Issue #32](https://gitlab.aldebaran.lan/production/wooqi/issues/32): Manage postfail_feature_management when teardown fail.

### Fixed
- [Issue #33](https://gitlab.aldebaran.lan/production/wooqi/issues/33): Wooqi command return correctly signal number

***
## [1.2.0] - 2017-10-31
### Added
- [Issue #24](https://gitlab.aldebaran.lan/production/wooqi/issues/24): recurse_folders as uut parameter.
- [Issue #25](https://gitlab.aldebaran.lan/production/wooqi/issues/25): Add LICENSE file and headers.

***
## [1.1.0] - 2017-08-30
### Enhanced
- Improve version display.
- [Issue #17](https://gitlab.aldebaran.lan/production/wooqi/issues/17): Keep capital in test_info keys.

### Added
- Possibility to rerun sequence since the first test failed.

### Changed
- Split Wooqi tests.

***
## [1.0.2] - 2017-05-18
### Fixed
- Fix exit status.

***
## [1.0.1] - 2017-04-21
### Added
- --init-project option to create a new Wooqi project.
- AUTHORS file.

***
## [1.0.0] - 2017-03-29
*First official release.*

[Unreleased]: https://gitlab.aldebaran.lan/production/wooqi/compare/v4.0.2...master
[4.0.2]: https://gitlab.aldebaran.lan/production/wooqi/compare/v4.0.1...v4.0.2
[4.0.1]: https://gitlab.aldebaran.lan/production/wooqi/compare/v4.0.0...v4.0.1
[4.0.0]: https://gitlab.aldebaran.lan/production/wooqi/compare/v3.0.0...v4.0.0
[3.0.0]: https://gitlab.aldebaran.lan/production/wooqi/compare/v2.0.1...v3.0.0
[2.0.1]: https://gitlab.aldebaran.lan/production/wooqi/compare/v2.0.0...v2.0.1
[2.0.0]: https://gitlab.aldebaran.lan/production/wooqi/compare/v1.2.2...v2.0.0
[1.2.2]: https://gitlab.aldebaran.lan/production/wooqi/compare/v1.2.1...v1.2.2
[1.2.1]: https://gitlab.aldebaran.lan/production/wooqi/compare/v1.2.0...v1.2.1
[1.2.0]: https://gitlab.aldebaran.lan/production/wooqi/compare/v1.1.0...v1.2.0
[1.1.0]: https://gitlab.aldebaran.lan/production/wooqi/compare/v1.0.2...v1.1.0
[1.0.2]: https://gitlab.aldebaran.lan/production/wooqi/compare/v1.0.1...v1.0.2
[1.0.1]: https://gitlab.aldebaran.lan/production/wooqi/compare/v1.0.0...v1.0.1
[1.0.0]: https://gitlab.aldebaran.lan/production/wooqi/compare/2bcd8e8d1...v1.0.1
