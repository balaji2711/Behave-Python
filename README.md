# Behave-Python

**Run Tests with Allure report**
  behave -f allure_behave.formatter:AllureFormatter -o reports/ .\features\
  behave -f allure_behave.formatter:AllureFormatter -o reports/ .\features\rest.feature

**Run Tests without allure report (Specific feature)**
  behave features/login.feature

**Run all tests via parallel**
	behavex --parallel-processes 3
  
**Run Parallel Tests with Scenario with Tag**
  behavex -tWeb --parallel-processes 3 --parallel-scheme scenario

**@AUTORETRY tag**
  This tag can be used for flacky scenarios or when the testing infrastructure is not stable at all.
  The @AUTORETRY tag can be applied to any scenario or feature, and it is used to automatically re-execute the test scenario when it fails.

**Rerun all failed scenarios**
Whenever you perform an automated test execution and there are failing scenarios, the failing_scenarios.txt file will be created into the execution output folder. This file allows you to run all failing scenarios again.
  behavex -tRest --parallel-processes 3 --parallel-scheme scenario -rf ./output/failing_scenarios.txt

