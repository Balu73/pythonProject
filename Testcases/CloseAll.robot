*** Settings ***
Library    SeleniumLibrary
*** Variables ***
*** Test Cases ***
MyTestCase
    ${a}=    open browser    https://www.google.com/     Chrome
    ${b}=    open browser    https://www.google.com/     Chrome
    switch browser    ${a}
    input text    name:q    python
    sleep   3
    switch browser    ${b}
    maximize browser window
    input text    name:q    c++

*** Keywords ***
