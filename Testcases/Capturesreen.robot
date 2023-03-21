*** Settings ***
Library  SeleniumLibrary



*** Variables ***


*** Test Cases ***
LoginTC
    open browser    https://www.flipkart.com/     Chrome
    maximize browser window
    click link    //a[text()="Login"]

    input text      //div[@class="IiD88i _351hSN"]//input[@type="text"]	  Adimin
    input text      //div[@class="IiD88i _351hSN"]//input[@type="password"]	  adimin123

    # capture element screenshot by using locator and saving location path or file name
    capture element screenshot   //img[@class="_2xm1JU"]     logo.png
    # capture page screenshot   saving location path or file name

    capture page screenshot     loginTC.png

*** Keywords ***
