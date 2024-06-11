*** Settings ***
Library    Browser
Library    Screenshot

*** Variables ***
${BASE_URL}    http://localhost:3000
${BUTTON_ID}      button1
${TEXT_ID}        text1
${EXPECTED_TEXT}  Captured with success!

*** Test Cases ***
Validate Capture Image Modal
    [Documentation]    
    New Page    ${BASE_URL}
    Take Screenshot
    Click   id=${BUTTON_ID}
    Take Screenshot
    Wait For Elements State    id=${TEXT_ID}    timeout=20s
    ${text}=    Get Text    id=${TEXT_ID}
    Should Be Equal    ${text}    ${EXPECTED_TEXT}
