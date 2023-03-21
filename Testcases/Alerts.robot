*** Settings ***
Library    SeleniumLibrary
*** Variables ***
*** Test Cases ***
HandlingAlerts
    open browser    https://testautomationpractice.blogspot.com/     Chrome
    maximize browser window
    click button    //button[text()="Click Me"]
    sleep    3
    # by using "handle alert" keyword we can handle the aleart pop-up windows by using 3 arguments(accept,dismiss and leave)
  #  handle alert    accept
  #  handle alert    dismiss
    #handle alert    leave
    alert should not be present      Press a button!
    handle alert


*** Keywords ***
