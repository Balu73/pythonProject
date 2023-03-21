*** Settings ***
Library    SeleniumLibrary
Resource    ../Resources/resource.robot

*** Variables ***
${url}      https://demo.guru99.com/test/newtours/
${browser}    Chrome

*** Test Cases ***
TC1
    ${PageTitle}=    lanchBrowser    ${url}      ${browser}
    log to console    ${PageTitle}
    log     ${PageTitle}
    input text      name:userName	mercury
    input text      name:password	mercury

