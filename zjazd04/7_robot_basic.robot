*** Settings ***
Library    SeleniumLibrary

*** Variables ***


*** Keywords ***


*** Test Cases ***
Log in wikipedia
    open browser    https://pl.wikipedia.org    chrome
    click element    pt-login-2
    sleep    1
    input text   wpName1    Kamil
    input text    wpPassword1    Merito
    sleep    1
    click element    wpLoginAttempt
    sleep    1
    close browser