*** Settings ***
Library    SeleniumLibrary

*** Variables ***
${url}      https://www.countries-ofthe-world.com/flags-of-the-world.html
*** Test Cases ***
ScrollingTest
    open browser   ${url}    Chrome
    maximize browser window
    sleep    3
    # execute javascript  with method window.scrollTo(horizontal pixel, vertical pixel)
    #we can scroll down horizontal and Vertically
    execute javascript    window.scrollTo(0,1500)
    sleep    3
    #     or
    # the scroll element into view    expecting element locator
    scroll element into view    //tr//td[text()="India"]
    sleep    3
    # By using this keyword with javascript method we can scolldown the scroll bar to bottom
    execute javascript    window.scrollTo(0, document.body.scrollHeight)     # End of page
    sleep    3
    execute javascript    window.scrollTo(0, -document.body.scrollHeight)     # Starting point
    sleep    4
    close browser

