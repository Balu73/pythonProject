*** Settings ***
Library    SeleniumLibrary
*** Variables ***
*** Test Cases ***
GetAllLinksTest
    open browser    https://demo.guru99.com/test/newtours/    Chrome
    maximize browser window


    ${AllLinksCount}=   get element count    //a
    log to console    ${AllLinksCount}
    @{LinkItems}    create list
    FOR    ${i}     IN RANGE     1  ${AllLinksCount}
        ${linkText}=    get text    (//a)[${i}]
        log to console    ${linkText}

    END



*** Keywords ***
