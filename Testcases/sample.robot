*** Settings ***
Library    SeleniumLibrary
*** Test Cases ***
search test
    open browser    https://www.google.com/     Chrome
    maximize browser window
    set selenium implicit wait    3
    input text    q    python
    sleep  3
search test1
    open browser    https://www.google.com/     Chrome
    maximize browser window
    set selenium implicit wait    3
    input text    q    java
*** Keywords ***
P
    press keys  q  BACKSPACE
