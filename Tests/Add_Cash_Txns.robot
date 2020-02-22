*** Settings ***
Documentation    Add Cash Txns
Resource    ../Keywords/Common.robot
Resource    ../Keywords/PageKeywords/Login.robot
Resource    ../Keywords/PageKeywords/Transaction.robot

*** Test Cases ***
Add a cash transaction manually
    [Tags]    SINGLE_TXN
    [Setup]  Initialise System
    Open Application
    Login In Application  ${USERNAME}  ${PASSWORD}
    Go To Transactions
    User adds a cash transaction  11/12/19  Rivigo Cafeteria  Juices  40  Vikash Kumar - orange juice
    User adds a cash transaction  12/16/19  Rivigo  Juices  400  Vikash Kumar - orange juice of 400

Parse paytm exported transactions to supported format
    [Tags]  STEP_1
    Parse paytm CSV data  ${UNPARSED_CSV_PAYTM}

Consutruct map of description to merchant to category and save as json
    [Tags]  STEP_2
    construct map from txn csv  ${TXN_PARSE_01_CSV}

Verify mappings manually and make adjustments in json files if required
    [Tags]  STEP_3
    # This is a manual step

Construct final import ready csv file from mappings
    [Tags]  STEP_4
    Construct merchant and category mapped csv

Add cash transactions from csv
    [Tags]    STEP_5
    [Setup]  Initialise System
    Open Application
    Login In Application  ${USERNAME}  ${PASSWORD}
    Go To Transactions
    User add cash transactions from csv  ${TXN_SOURCE_CSV}
