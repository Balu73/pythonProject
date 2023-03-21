*** Settings ***
Library    SeleniumLibrary
#1. Test Setup - will run before every Test Case
#2. Test Teardown - will run after every Test Case
#3. Suite Setup - will run before Test Suite
#4. Suite Teardown - will run after Test Suite

Suite Setup       log to console    open browser
Suite Teardown    log to console    close browser
Test Setup        log to console    login to application
Test Teardown     log to console    logout to application

*** Test Cases ***
TC1 Prepaid Recharge
    log to console      This pre paid recharge
TC2 Postpaid Recharge
    log to console      This postpaid recharge
TC3 search
    log to console      This is search case
TC4 Advanced seach
    log to console      This is the adv search case
