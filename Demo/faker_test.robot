*** Settings ***
Library           FakerLibrary

*** Test Cases ***
FakerLibrary Words Generation
    [Documentation]    调用faker生成随机信息
    [Tags]    Demo
    [Timeout]    1 minute
    ${words}=    FakerLibrary.Words
    Log    words: ${words}
    ${words}=    FakerLibrary.Words    nb=${10}
    Log    words: ${words}
    ${address}=    FakerLibrary.Address
    Log    address: ${address}
    ${text}=    FakerLibrary.text    max_nb_chars=100
    Log    text: ${text}
    ${pylist}=    FakerLibrary.pylist    nb_elements=10    variable_nb_elements=True
    Log    pylist: ${pylist}
    ${Latitude}=    FakerLibrary.Latitude
    Log    Latitude: ${Latitude}
