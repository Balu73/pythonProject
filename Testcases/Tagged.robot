*** Settings ***

# [Tags] by we can classified and group the test cases also we can run perticular testcase from test suite
*** Test Cases ***
TC1 UserRegistrationTest
    [Tags]    Regression
    log to console     This is user Reg test
    log to console     user reg is over
TC2 LoginTest
    [Tags]   sanity
    log to console    This login test
    log to console    login test over
TC3 Change User Setting
    [Tags]    Regression
    log to console    this is change user setting test
    log to console    This is  change user setting test over
TC4 LogOut
    [Tags]    sanity
    log to console    this is logout test
    log to console    this is logout test over