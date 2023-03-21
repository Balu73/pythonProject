*** Settings ***
Library    SeleniumLibrary

*** Variables ***
*** Test Cases ***
login_flikart
    open browser    https://www.flipkart.com/      Chrome
    maximize browser window
    click link     //a[@class="_1_3w1N"]
    input text     //div[@class="IiD88i _351hSN"]//input[@type="text"]    8331865173
    sleep     8
    input text       //div[@class="IiD88i _351hSN"]//input[@type="password"]    Bala3010@
    sleep    5
    click button    //button[@class="_2KpZ6l _2HKlqd _3AWRsL"]



*** Keywords ***
