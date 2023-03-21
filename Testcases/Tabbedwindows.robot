*** Settings ***
Library    SeleniumLibrary

*** Variables ***
*** Test Cases ***
TabbedWindowsTest

    open browser    https://demo.automationtesting.in/Windows.html     Chrome
    ${name}=     get title
    log to console       ${name}
    maximize browser window

    wait until element is visible       //*[@id="Tabbed"]/a/button
    click element    //*[@id="Tabbed"]/a/button
    switch window    Selenium
    wait until element is visible    //*[text()='About']
    click element    //*[text()='About']
    wait until element is visible    //*[text()='History']
    click element    //*[text()='History']

    sleep    3
    log
    go back

*** Keywords ***
