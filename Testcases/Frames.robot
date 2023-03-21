*** Settings ***
Library    SeleniumLibrary
*** Variables ***
*** Test Cases ***
Testing Frames
    open browser    https://www.selenium.dev/selenium/docs/api/java/index.html?help-doc.html    Chrome

    select frame    packageListFrame      # by using id, name Xpath
    click link    org.openqa.selenium
    unselect frame

    sleep    3
    select frame      packageFrame
    click link    WebDriver
    unselect frame

    sleep    3
    select frame    classFrame
    click link    Help
    unselect frame
    sleep    3
    close browser
*** Keywords ***
