*** Settings ***
Library    SeleniumLibrary
*** Variables ***
${browser}    Chrome
${url}      https://demo.nopcommerce.com/


*** Test Cases ***
TestingInputBox
    open browser    ${url}      ${browser}
    maximize browser window
    sleep    5
    title should be    nopCommerce demo store
    click link        //a[text()="Log in"]
    ${"email_txt"}  set variable    id:Email
    element should be visible    ${"email_txt"}
    #element should be enabled    ${"email_txt"}
    #element should not be visible    ${"email_txt"}


    input text    ${"email_txt"}    krishnabandari@gmail.com
    sleep   5
    clear element text    ${"email_txt"}
    sleep    5



*** Keywords ***
