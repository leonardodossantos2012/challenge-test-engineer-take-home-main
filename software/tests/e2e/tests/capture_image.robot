*** Settings ***
Library    Browser

*** Variables ***


*** Test Cases ***
Capture Image Test
    New Browser  browser=Chromium  headless=True  proxy=None
    New Page    url=http://frontend:3000
    # Click    text=Capture
    # Wait For Elements State    text=Captured with success!    visible
    # ${text}=    Get Text    text=Captured with success!
    # Should Be Equal As Strings    ${text}    Captured with success!
    # Close Browser
