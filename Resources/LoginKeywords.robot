*** Settings ***
Library    SeleniumLibrary
Variables    ../PageObjects/Locators.py

*** Keywords ***
Open my Browser
    [Arguments]    ${SitUrl}       ${Browser}
    open browser      ${SitUrl}    ${Browser}
    maximize browser window

Enter UserName
    [Arguments]    ${username}
    input text    ${txt_loginUserName}      ${username}

Enter Password
    [Arguments]    ${password}
    input text       ${txt_loginpassword}       ${password}
Click SignIn
     click button    ${btn_signIn}
Verify Succesfull Login
    title should be    Login: Mercury Tours
Close my browser
    close all browsers