*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${browser}    Chrome
${url}      https://www.techlistic.com/p/selenium-practice-form.html
      
*** Test Cases ***
Handling Dropdowns and lists
    open browser    ${url}      ${browser}
    maximize browser window

    # Select from list with help of name of lable
    select from list by label    continents     Asia
    sleep    5

    select from list by index    continents      3
    #select from list by value    continents    value

    #list box
    select from list by label    selenium_commands      Wait Commands
    sleep    3
    select from list by label    selenium_commands      WebElement Commands
    sleep    3
    unselect from list by label    selenium_commands    Wait Commands
    sleep    4
    unselect from list by label    selenium_commands    WebElement Commands
    close browser

