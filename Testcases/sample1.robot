*** Settings ***
Library  SeleniumLibrary

*** Test Cases ***
Example Test
    Open Browser  https://www.flipkart.com/big-saving-days-jan-sale-store?param=98574&fm=neo%2Fmerchandising&iid=M_87c7a4b3-31ff-4d7d-8965-439cfea11305_1_5NWXAKCTNB7D_MC.8TVKUWT87M16&otracker=hp_rich_navigation_3_1.navigationCard.RICH_NAVIGATION_Electronics_8TVKUWT87M16&otracker1=hp_rich_navigation_PINNED_neo%2Fmerchandising_NA_NAV_EXPANDABLE_navigationCard_cc_3_L0_view-all&cid=8TVKUWT87M16   Chrome
    sleep  3
    mouse over  //body/div[@id='container']/div[1]/div[2]/div[1]/div[1]/span[3]
    sleep  3
    mouse over  //body/div[@id='container']/div[1]/div[2]/div[1]/div[1]/span[4]
    sleep  3
    mouse over  //body/div[@id='container']/div[1]/div[2]/div[1]/div[1]/span[5]
    sleep  3
