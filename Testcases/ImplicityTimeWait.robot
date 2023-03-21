*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${"url"}    https://demowebshop.tricentis.com/register
${"browser"}    Chrome

*** Test Cases ***
RegTest
    open browser    ${"url"}    ${"browser"}
    maximize browser window
    ${imlicttime}=    get selenium implicit wait
    log to console    ${imlicttime}
# Normally to identify element on webpage it take 0s
# if it not found then it throw an exception and terminate the exceution but
# by using set selenium implicit wait keyword we can extend the waiting time
    set selenium implicit wait    10
    wait until page contains    Register
    select radio button     Gender    M
    input text      id:FirstName	Balakrishna
    input text    id:LastName    Bandari
    input text    name:Email	 krishnabandari841@gmail.com
    input text    id:Password	   Bala19966@
    input text    id:ConfirmPassword	Bala19966@


    close browser
    ${imlicttime}=    get selenium implicit wait
    log to console    ${imlicttime}


*** Keywords ***
