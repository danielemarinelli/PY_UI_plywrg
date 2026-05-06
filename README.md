pytest.ini is the file to control with tests must be executed. Every test has a marker so we can run only specific tests (grouping). To run from local env:  cmd line execute ---> pytest tests 
and only sanity tests will execute (because uncommented in pytest.ini) and two workers are enable, so parallel execution will be performed. If commenting the workers line in pytest.ini, the execution will be in serial with chrome

Requirements.txt file is needed to install all dependencies when running the framework in remote env
