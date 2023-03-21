*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${"url"}    https://demowebshop.tricentis.com/register
${"browser"}    Chrome

*** Test Cases ***
RegTest
    open browser    ${"url"}    ${"browser"}
    maximize browser window
    ${time}=   get selenium timeout
    log to console    ${time}

    set selenium timeout    10    # if need wait extra time then we use it this keyword
    # By using this you can pause the process  and search given data until(5s by default) if it found then proceed with rest of automation otherwise throw an error
    wait until page contains    Register
    select radio button     Gender    M
    input text      id:FirstName	Balakrishna
    input text    id:LastName    Bandari
    input text    name:Email	 krishnabandari841@gmail.com
    input text    id:Password	   Bala19966@
    input text    id:ConfirmPassword	Bala19966@
    sleep  5
    click button    css=input#register-button                # here i used css selector to identify the web element on the web page
    sleep  5
    ${time}=   get selenium timeout
    log to console    ${time}

    close browser


*** Keywords ***
