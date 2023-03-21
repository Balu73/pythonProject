*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
mouse action
    open browser    https://www.sugarcrm.com/au/request-demo/      Chrome
    maximize browser window
    go to  https://www.google.com/
    sleep  5
    #mouse down  //span[contains(text(),'Pricing')]
    #mouse up   //span[contains(text(),'Pricing')]
    #mouse over  //span[contains(text(),'Pricing')]
    ${a}=  get window handles
    log to console     ${a}
    sleep  5


