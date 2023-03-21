*** Settings ***
Library    SeleniumLibrary

*** Variables ***
*** Test Cases ***
MultipelBrowserTest
    open browser    https://www.google.com/     Chrome
    maximize browser window
    sleep    2
    open browser    https://www.bing.com/       Chrome
    maximize browser window
    switch browser    1
    ${title1}=   get title
    log to console    ${title1}
    switch browser    2
    ${title2}=      get title
    log to console    ${title2}
    sleep    3
    close all browsers


*** Keywords ***
