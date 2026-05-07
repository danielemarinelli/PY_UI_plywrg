Step 1) Run single below command to install all the required plugins:
pip install pytest playwright pytest-xdist pytest-html allure-pytest pytest-rerunfailures
openpyxl Faker python-slugify

Step 2) Install playwright browsers with following command:
playwright install

Step 3) Install pytest playwright:
pip install pytest-playwright

pytest.ini is the file to control with tests must be executed. Every test has a marker so we can run only specific tests (grouping). To run from local env:  cmd line execute ---> pytest tests 
and only sanity tests will execute (because uncommented in pytest.ini) and two workers are enable, so parallel execution will be performed. If commenting the workers line in pytest.ini, the execution will be in serial with chrome

Requirements.txt file is needed to install all dependencies when running the framework in remote env

With push or pull requests on branches main/master, the execution will start with GitHub Actions. The workflow will install all dependencies, install Playwright and then run the tests. Note: .yml is set with ubuntu-latest, so by default execution is in headless mode ( -> remember to comment the --headed line in pytest.ini file)

before starting test --> test_009_wish_list, be sure to have the wish_list empty

