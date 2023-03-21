*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
TableValidataions
    open browser    https://testautomationpractice.blogspot.com/    Chrome
    maximize browser window
    ${rows}=    get element count    //table[@name= "BookTable"]/tbody/tr
    ${cols}=    get element count    //table[@name= "BookTable"]/tbody/tr[1]/th
    log to console    ${rows}
    log to console    ${cols}
    sleep    3
    execute javascript    window.scrollTo(0, document.body.scrollHeight)
    sleep    3
    execute javascript    window.scrollTo(0, -document.body.scrollHeight)
    ${data}=    get text    //table[@name= "BookTable"]/tbody/tr[5]/td[1]
    log to console    ${data}
# By usig following keyword we can check the specify table column should contain expected data or not with column number and expected data name
    table column should contain    //table[@name= "BookTable"]     3     Subject
# By usig following keyword we can check the specify table row should contain expected data or not with row number and expected data name
    table row should contain    //table[@name= "BookTable"]     4       Learn JS
# By usig following keyword we can check the specify table cell should contain expected data or not with row number column number and expected data name

    table cell should contain    //table[@name= "BookTable"]    5   2    Mukesh
# By usig following keyword we can check the specify table header should contain expected data or not with expected data name

    table header should contain    //table[@name= "BookTable"]      BookName

    close browser

