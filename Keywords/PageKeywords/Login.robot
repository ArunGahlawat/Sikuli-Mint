*** Settings ***
Resource  ../Common.robot

*** Variables ***
${LOGIN_IMAGE_PATH}             ../Locators/Login

*** Keywords ***
Login In Application
    [Arguments]  ${username}  ${encoded_password}
    Add Relative Image Path  ${LOGIN_IMAGE_PATH}
    Wait And Pause For  home_sign_in_button
    click using image  home_sign_in_button
    ${required_images}  Create List
    ...  login_user_id  login_password  login_sign_in
    wait and pause for all  ${required_images}
    Input Text Using Image  login_user_id  ${username}
    ${password} =  Decode  ${encoded_password}
    Input Text Using Image  login_password  ${password}
    Click Using Image  login_sign_in
    sleep  15 Seconds

Logout From Application
    #todo