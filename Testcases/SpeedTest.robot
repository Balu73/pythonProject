*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${"url"}    https://demowebshop.tricentis.com/register
${"browser"}    Chrome

*** Test Cases ***
RegTest
    ${speed}=   get selenium speed
    log to console    ${speed}
    open browser    ${"url"}    ${"browser"}
    maximize browser window
    #by using the set selenium speep every statement execution take 2s time then continue. By default it take 0s time as value
    set selenium speed    2
    select radio button     Gender    M

    input text      id:FirstName	Balakrishna
    input text    id:LastName    Bandari
    input text    name:Email	 krishnabandari841@gmail.com

    input text    id:Password	   Bala19966@
    input text    id:ConfirmPassword	Bala19966@
    click button    //input[@id="register-button"]

    close browser
    ${speed}=   get selenium speed
    log to console    ${speed}

*** Keywords ***
