*** Settings ***
Resource  ../Common.robot

*** Variables ***
${LOGIN_IMAGE_PATH}             ../Locators/Login
${TRANSACTIONS_IMAGE_PATH}      ../Locators/Transactions

*** Keywords ***
Go To Transactions
    Add Relative Image Path  ${TRANSACTIONS_IMAGE_PATH}
    Wait And Pause For  home_header
    Wait And Pause For  transactions
    click using image  transactions
    sleep  10 Seconds
    Wait And Pause For  CashOnly
    click using image  CashOnly
    Sleep  5 Seconds
    ${required_images}  create list  CashOnly_active  cash_only_active_label  add_txn
    Wait And Pause For All  ${required_images}

User adds a cash transaction
    [Arguments]  ${txn_date}  ${txn_desc}  ${txn_category}  ${txn_amount}  ${txn_notes}  ${txn_source_tag}=paytm
    click using image  add_txn
    ${required_images_txn}  create list  add_txn_date  add_txn_desc  add_txn_category  add_txn_amount  add_txn_paytm_tag_1
    ...  add_txn_notes  add_txn_cancel  add_txn_imdone
    Add a cash transaction  ${required_images_txn}  ${txn_date}  ${txn_desc}  ${txn_category}  ${txn_amount}  ${txn_notes}  ${txn_source_tag}

Add a cash transaction
    [Arguments]  ${required_images}  ${txn_date}  ${txn_desc}  ${txn_category}  ${txn_amount}  ${txn_notes}  ${txn_source_tag}  ${txn_type}
    return from keyword if  '${txn_type}' == 'credit'
    wait and pause for  add_txn
    click using image  add_txn
    wait and pause for all  ${required_images}
    double click using image  add_txn_date
    Press Special Key  DELETE
    :FOR  ${CLEAR}  IN RANGE  ${6}
    \  Press Special Key  BACKSPACE
    Wait And Pause For  add_txn_empty_date
    Input Text Using Image  add_txn_empty_date  ${txn_date}
    Input Text Using Image  add_txn_desc  ${txn_desc}
    Input Text Using Image  add_txn_category  ${txn_category}
    Input Text Using Image  add_txn_amount  ${txn_amount}
    Input Text Using Image  add_txn_notes  ${txn_notes}
    run keyword if  '${txn_source_tag}' == 'paytm'
    ...  Click Using Image  add_txn_paytm_tag_1  -35  0
    click using image  add_txn_imdone
    Wait Until Screen Not Contain Using Image  add_txn_cancel
    Wait Until Screen Not Contain Using Image  add_txn_notes
    sleep  7 seconds

User add cash transactions from csv
    [Arguments]  ${csv_data}
    ${csv_data}  Read From Csv As Dict  ${csv_data}
    ${csv_length}  Get Length  ${csv_data}
    ${added_txn}  create dictionary
    ${required_images_txn}  create list  add_txn_date  add_txn_desc  add_txn_category  add_txn_amount  add_txn_paytm_tag_1
    ...  add_txn_notes  add_txn_cancel  add_txn_imdone
    :FOR  ${INDEX}  IN RANGE  ${csv_length}
    \  ${txn_details}  Get From List  ${csv_data}  ${INDEX}
    \  ${txn_date}  Get From Dictionary  ${txn_details}  Date
    \  ${txn_desc}  Get From Dictionary  ${txn_details}  Description
    \  ${txn_category}  Get From Dictionary  ${txn_details}  Category
    \  ${txn_amount}  Get From Dictionary  ${txn_details}  Amount
    \  ${txn_notes}  Get From Dictionary  ${txn_details}  Notes
    \  ${txn_source_tag}  Get From Dictionary  ${txn_details}  Source
    \  ${txn_type}  Get From Dictionary  ${txn_details}  Type
    \  Add a cash transaction  ${required_images_txn}  ${txn_date}  ${txn_desc}  ${txn_category}  ${txn_amount}  ${txn_notes}  ${txn_source_tag}  ${txn_type}
    \  set to dictionary  ${added_txn}  Date=${txn_date}  Description=${txn_desc}  Category=${txn_category}  Amount=${txn_amount}  Notes=${txn_notes}  Source=${txn_source_tag}  Type=${txn_type}
    \  write in csv  ${TXN_ADDED_CSV}  ${added_txn}


Parse paytm CSV data
    [Arguments]  ${csv_data}=${UNPARSED_CSV_PAYTM}
    ${csv_data}  Read From Csv As Dict  ${csv_data}
    ${csv_length}  Get Length  ${csv_data}
    ${parsed_dict}  create dictionary
    :FOR  ${INDEX}  IN RANGE  ${csv_length}
    \  ${txn_details}  Get From List  ${csv_data}  ${INDEX}
    \  ${txn_date}  Get From Dictionary  ${txn_details}  Date
    \  ${txn_activity}  Get From Dictionary  ${txn_details}  Activity
    \  ${txn_source}  Get From Dictionary  ${txn_details}  Source/Destination
    \  ${txn_wallet_id}  Get From Dictionary  ${txn_details}  Wallet Txn ID
    \  ${txn_comment}  Get From Dictionary  ${txn_details}  Comment
    \  ${txn_amount_debit}  Get From Dictionary  ${txn_details}  Debit
    \  ${txn_amount_credit}  Get From Dictionary  ${txn_details}  Credit
    \  ${parsed_dict}  parse paytm csv  ${txn_date}  ${txn_activity}  ${txn_source}  ${txn_wallet_id}  ${txn_comment}  ${txn_amount_debit}  ${txn_amount_credit}
    \  write in csv  ${TXN_PARSE_01_CSV}  ${parsed_dict}


Construct merchant and category mapped csv
    [Arguments]  ${csv_data}=${TXN_PARSE_01_CSV}
    map merchant and category from json  ${TXN_PARSE_01_CSV}  ${TXN_SOURCE_CSV}
