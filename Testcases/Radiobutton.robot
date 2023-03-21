*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${browser}    Chrome
${url}      https://www.techlistic.com/p/selenium-practice-form.html


*** Test Cases ***
TestingRadioButtonsAndCheckBoxes
    open browser   ${url}    ${browser}
    maximize browser window

    #selecting radiobutton
    select radio button    sex    Male
    sleep    5
    select radio button    exp    4
    sleep    5

    #select the check box
    select checkbox    id:profession-0
    select checkbox    id:profession-1
    input text      firstname   Balakrishna
    input text    lastname      Bandari
    input text    id:datepicker     10/04/1996
    select checkbox    tool-2

    sleep    5
    # clear text field by using keywords
    clear element text   id:datepicker
    clear element text    lastname
    clear element text    firstname
    unselect checkbox    tool-2
    unselect checkbox    id:profession-0
    unselect checkbox    id:profession-1
    close browser


*** Keywords ***
