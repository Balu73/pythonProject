
*** Settings ***
Library    SeleniumLibrary
Resource    ../Resources/Login_resources.robot
#library keyword    Library name      path of test data file    we need specify sheet name in xlsx file
Library     DataDriver     ../TestData/Login_Data.xlsx  sheet_name=Sheet1

Suite Setup     Open my Browser
Suite Teardown    Close Browsers
Test Template    Invalid login

*** Test Cases ***
LoginTestwithExcel using ${username} and ${password}


*** Keywords ***
Invalid login
    [Arguments]    ${username}     ${password}
    Input username     ${username}
    Input pwd   ${password}
    Click login button
    Error msg should be visible
