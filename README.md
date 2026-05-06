# Automation Framework Commander

A scalable and maintainable hybrid test automation framework built with Python, Selenium, and PyTest.

## Framework Overview

This framework uses a hybrid approach combining:
- Page Object Model (POM) for maintainability and reuse
- Data-driven tests using external JSON/CSV/Excel files
- Keyword-driven execution support for reusable automation flows
- Cross-browser execution with Chrome, Firefox, and Edge
- Environment-specific YAML configuration
- PyTest fixtures for setup/teardown and parallel execution
- Logging and HTML reporting

## Folder Structure

```
Automation-Framework-Commander/
├── .github/
│   └── workflows/python-selenium.yml
├── configs/
│   └── config.yaml
├── data/
│   ├── keyword_login_steps.json
│   ├── login_data.csv
│   └── login_data.json
├── pages/
│   ├── base_page.py
│   └── login_page.py
├── reports/
│   └── .gitkeep
├── tests/
│   ├── base_test.py
│   ├── conftest.py
│   └── test_login.py
├── utilities/
│   ├── config_reader.py
│   ├── data_reader.py
│   ├── driver_factory.py
│   ├── keyword_executor.py
│   ├── logger.py
│   └── wait_utils.py
├── .gitignore
├── pytest.ini
├── README.md
└── requirements.txt
```

## Key Components

### Sample Code
- `tests/base_test.py` — base test class and reusable test helpers
- `pages/base_page.py` — base page object with common actions
- `pages/login_page.py` — page object for login functionality
- `tests/test_login.py` — sample test case showing data-driven and keyword-driven flow
- `utilities/config_reader.py` — environment and browser configuration loader
- `utilities/driver_factory.py` — cross-browser driver factory with WebDriverManager

### Config Files
- `configs/config.yaml` — browser defaults and environment URLs
- `data/login_data.json` — JSON-based test data for data-driven tests
- `data/login_data.csv` — CSV-based sample data source
- `data/keyword_login_steps.json` — keyword-driven test flow

## Install Dependencies

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
```

## Run Tests Locally

Run all tests and generate an HTML report:

```bash
pytest -n auto --html=reports/report.html --self-contained-html
```

Run a single test module:

```bash
pytest tests/test_login.py
```

Override the environment or browser at runtime by editing `configs/config.yaml` or by using environment variables inside your config loader if you extend it.

## CI/CD Readiness

This repository includes a GitHub Actions workflow at `.github/workflows/python-selenium.yml`.
It installs dependencies, executes tests in parallel, and uploads `reports/report.html` as an artifact.

### Jenkins Pipeline Example

A Jenkins pipeline can be added using the included `Jenkinsfile`.
This pipeline checks out the repository, installs dependencies, runs PyTest, and archives both HTML and Allure artifacts.

### Allure Reporting

The framework now supports Allure reporting.
- Test execution writes results to `reports/allure-results`
- Generate an Allure report locally with:

```bash
pytest -n auto
allure serve reports/allure-results
```

If you prefer a static report rather than `serve`, use:

```bash
allure generate reports/allure-results -o reports/allure-report --clean
```

## Best Practices for Scaling and Collaboration

- Maintain tests in `tests/` and page objects in `pages/`
- Store data sets separately in `data/` and keep config values in `configs/`
- Use descriptive test names and PyTest markers like `smoke` or `regression`
- Keep page object methods small and reusable
- Share common utilities in `utilities/` for waits, logging, config, and driver setup
- Use source control branching and code reviews for new page objects and tests
- Automate test execution in CI using GitHub Actions or Jenkins
- Keep reports and logs outside version control by using `.gitignore`

## Notes

- For Excel support, `utilities/data_reader.py` uses `openpyxl`
- HTML report generation is enabled via `pytest-html`
- Add Allure integration later by installing `allure-pytest` and updating `pytest.ini`
