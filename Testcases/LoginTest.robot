*** Settings ***
Library       SeleniumLibrary
Resource      ../Resources/LoginKeywords.robot

*** Variables ***
${SitUrl}       https://demo.guru99.com/test/newtours/index.php
${Browser}      Chrome
${username}         tutorial
${password}          tutorial

*** Test Cases ***
LoginTest
    Open My Browser     ${SitUrl}       ${Browser}


    Enter UserName      ${username}
    Enter Password      ${password}
    Click SignIn        ${btn_signIn}
    Verify Succesfull Login
    Close my browser