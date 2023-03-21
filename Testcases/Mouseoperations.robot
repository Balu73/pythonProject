*** Settings ***
Library    SeleniumLibrary

*** Variables ***
*** Test Cases ***
MouseActions
    open browser    https://swisnl.github.io/jQuery-contextMenu/demo.html   Chrome
    maximize browser window
    #Right click action
    open context menu    //span[text()="right click me"]
    sleep     3
    # Double click action
    go to    https://testautomationpractice.blogspot.com
    double click element    //button[text()="Copy Text"]
    sleep     3
    #Drag and drop
    go to    http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html
    #Drag and drop      source element locator    Target element locator
    drag and drop    id:box3    id:box103
    sleep    3
    go back
    sleep    3
    go back
    sleep    3
    close browser


*** Keywords ***
