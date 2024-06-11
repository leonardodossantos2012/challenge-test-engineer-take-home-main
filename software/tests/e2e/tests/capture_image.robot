*** Settings ***
Library    Browser

*** Variables ***
${BACKEND_URL}    http://localhost:3000

*** Test Cases ***
Capture Image Test
    New Browser    firefox    headless=True
    New Page
    Go To    ${BACKEND_URL}
    Click    text=Capture
    Wait For Elements State    text=Captured with success!    visible
    ${text}=    Get Text    text=Captured with success!
    Should Be Equal As Strings    ${text}    Captured with success!
    Close Browser
