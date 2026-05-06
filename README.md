pytest.ini is the file to control with tests must be executed. Every test has a marker so we can run only specific tests (grouping). To run from local env:  cmd line execute ---> pytest tests 
and only sanity tests will execute (because uncommented in pytest.ini) and two workers are enable, so parallel execution will be performed. If commenting the workers line in pytest.ini, the execution will be in serial with chrome

Requirements.txt file is needed to install all dependencies when running the framework in remote env

With push or pull requests on branches main/master, the execution will start throught GitHub Actions. The workflow will install all dependencies, install Playwright and then run the tests. Note: .yml is set with ubuntu-latest, so by default execution is in headless mode ( -> remember to comment the --headed line in pytest.ini file)
