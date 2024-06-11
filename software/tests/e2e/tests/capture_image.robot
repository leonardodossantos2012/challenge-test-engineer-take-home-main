*** Settings ***
Library    Browser

*** Variables ***
${BASE_URL}    http://localhost:3000

*** Test Cases ***
Validate Capture Image Modal
    [Documentation]    Validate that the capture image modal appears and shows the correct message
    New Page    ${BASE_URL}
    Click    text=Capture
    Wait For Elements State    text=Captured with success!    visible    10s
    ${text}=    Get Text    text=Captured with success!
    Should Be Equal    ${text}    Captured with success!
    Click    text=Close
    Close Browser
