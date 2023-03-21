*** Settings ***
Library    SeleniumLibrary
Resource    ../Resources/Login_resources.robot
#library keyword    Library name      path of test data file
Library     DataDriver     ../TestData/Login_Data.csv

Suite Setup     Open my Browser
Suite Teardown    Close Browsers
Test Template    Invalid login

*** Test Cases ***
LoginTestwithCSV using ${username} and ${password}


*** Keywords ***
Invalid login
    [Arguments]    ${username}     ${password}
    Input username     ${username}
    Input pwd   ${password}
    Click login button
    Error msg should be visible
