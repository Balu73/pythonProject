# First we need to install robotframework-datadriver package in our project to work with Data Driven Testing
*** Settings ***
Library    SeleniumLibrary
Resource     ../Resources/Login_resources.robot
Suite Setup     Open my Browser
Suite Teardown    Close Browsers
Test Template     Invalid login



*** Test Cases ***          username                   password
Right user empty pwd      admin@yourstore.com    ${EMPTY}
Right user wrong pwd      admin@yourstore.com    xyz
Wrong user right pwd      admin@yourstore1.com    admin
Wrong user empty pwd      admin@yourstore1.com    ${EMPTY}
Wrong user wrong pwd      admin@yourstore1.com    admin12





*** Keywords ***
Invalid login
    [Arguments]    ${username}      ${password}
    Input username      ${username}
    Input pwd   ${password}
    Click login button
    Error msg should be visible


