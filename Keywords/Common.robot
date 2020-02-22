*** Settings ***
Documentation       Global keyword definations
Library             SeleniumLibrary
Library             robot.libraries.String
Library             robot.libraries.Collections
Library             robot.libraries.Dialogs
Library             robot.libraries.DateTime
Library             ../Lib/Helper.py
Library             ../Lib/SikuliKeywordHelper.py
Variables           ../config.py
Variables           ../credentials_prod.py
Resource            Browser.robot

*** Keywords ***
Initialise System
    Start Browser
    ${added_path}  Add Relative Image Path  ../Locators
    [Return]  ${added_path}

Add Relative Image Path
    [Arguments]  ${relative}  ${source}=${CURDIR}
    ${abs_path}  Get Absolute Path  ${source}/${relative}
    ${added_path}  Add Image Path  ${abs_path}
    [Return]  ${added_path}

Shutdown System
    Quit Browser
    Stop Remote Server

Open Application
    Go To  ${HOME_URL}

Wait And Pause For
    [Arguments]  ${image}
    ${status}  run keyword and return status  Wait For Image  ${image}
    run keyword if  '${status}' == '${False}'  Pause Execution And Resume With Delay  ${image} not present

Wait And Pause For All
    [Arguments]  ${image_list}
    :FOR  ${image}  IN  @{image_list}
    \  Wait And Pause For  ${image}

Pause Execution And Resume With Delay
    [Arguments]  ${message}=Paused  ${delay}=3 Seconds
    pause execution  ${message}
    sleep  ${delay}