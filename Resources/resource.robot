*** Settings ***
Library    SeleniumLibrary

*** Keywords ***
lanchBrowser
    [Arguments]       ${appurl}      ${appbrowser}
    open browser      ${appurl}      ${appbrowser}
    maximize browser window
    ${title}=    get title
    [Return]    ${title}