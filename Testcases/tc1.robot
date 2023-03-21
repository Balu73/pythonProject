*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${browser}    Chrome
${url}      https://demo.nopcommerce.com/
*** Test Cases ***
LoginTest
    open browser    ${url}      ${browser}
    maximize browser window
    loginToApplication

    close browser

*** Keywords ***
loginToApplication
    click link    xpath://a[@class="ico-login"]
    input text      id:Email    krishnabandari841@gmail.com
    input text      id:Password     Bala19966@
    click button     xpath://button[@class="button-1 login-button"]
    sleep    4