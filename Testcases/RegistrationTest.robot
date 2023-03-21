*** Settings ***
Library    SeleniumLibrary
Resource    ../Resources/RegistrationKeywords.robot

*** Variables ***
${SitUrl}       https://demo.guru99.com/test/newtours/index.php
${Browser}      Chrome

*** Test Cases ***
Registration test
    Open My Browser    ${SitUrl}    ${Browser}
    Click Registrastion Link
    Enter Firstname    balakrishna
    Enter Lastname    bandari
    Enter Phone      833186517
    Enter Email     krishnabandari842@gmail.com
    Enter Address    Darsi
    Enter City     Ongole
    Enter State     Ap
    Enter Postal Code   503311
    Select Country      INDIA
    Enter User Name    Bala53
    Enter Password      bala123
    Enter Confirmed Password    bala123
    Click Submit
    verify Succesful Registration
    Close my browser
