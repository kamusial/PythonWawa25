*** Settings ***
Library    SeleniumLibrary
test setup     open browser    https://pl.wikipedia.org    chrome
test teardown    close browser

*** Variables ***
${wikiedia login}    RobotTests
${wikipedia password}  RobotFramework
${error message}    Podany login lub hasło są nieprawidłowe. Spróbuj jeszcze raz.
*** Keywords ***
Log in wikipedia
    click element    pt-login-2
    Sleep    1
    input text   wpName1    ${wikiedia login}
    input text    wpPassword1    aaa
    sleep    1
    click element    wpLoginAttempt
    sleep    1
    wait until element is visible   xpath:/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[3]/div/form/div[1]/div
    ${my error message}    get text    xpath:/html/body/div[2]/div/div[3]/main/div[3]/div[3]/div[3]/div/form/div[1]/div
    log to console    Wiadomosc: ${my error message}
    should be equal    ${my error message}    ${error message}


*** Test Cases ***

Unsuccesfull login
    Log in wikipedia


Wikipedia search
    Log in wikipedia
    input text    search    Kto żądzi w Warszawie i okolicach    False
    capture page screenshot    screen.png
    close browser