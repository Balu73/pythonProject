*** Settings ***
Library    SeleniumLibrary
Variables    ../PageObjects/Locators.py

*** Keywords ***
Open My Browser
    [Arguments]    ${SiteUrl}     ${Browser}
    open browser    ${SiteUrl}     ${Browser}
    maximize browser window
Click Registrastion Link
    click link    ${link_Reg}
Enter Firstname
    [Arguments]    ${firstName}
    input text    ${txt_FirstName}    ${firstName}
Enter Lastname
    [Arguments]    ${lastName}
    input text    ${txt_LastName}    ${lastName}
Enter Phone
    [Arguments]    ${phone}
    input text    ${txt_phone}    ${phone}
Enter Email
    [Arguments]    ${email}
    input text    ${txt_email}      ${email}
Enter Address
    [Arguments]    ${add1}
    input text    ${txt_add1}   ${add1}
Enter City
    [Arguments]    ${city}
    input text    ${txt_city}   ${city}

Enter State
    [Arguments]    ${state}
    input text    ${txt_state}    ${state}
Enter Postal Code
    [Arguments]    ${postalcode}
    input text    ${txt_postcode}     ${postalcode}
Select Country
    [Arguments]    ${country}
    select from list by label   ${drp_country}   ${country}

Enter User Name
    [Arguments]      ${username}
    input text    ${txt_UserName}   ${username}
Enter Password
    [Arguments]    ${password}
    input text    ${txt_Password}   ${password}
Enter Confirmed Password
    [Arguments]    ${password}
    input text    ${txt_confirmedPassword}   ${password}
Click Submit
    click button    ${btn_submit}
verify Succesful Registration
    page should contain    Thank you for registering
Close my browser
    close all browsers


