*** Settings ***
Documentation     timeline/user 查看个人feed
Resource          ../Public/public_lib.txt    #Library    Collections    #Library    RequestsLibrary    #Library    pymysql
...               #Library    DatabaseLibrary    #Library    String    #Library    HttpLibrary.HTTP    #Library
...               # ../Public/Lib/tools_library.py

*** Variable ***
${pwd}            67889911    # 密码
${userName}       13829744541    # 默认的用户名
${ContentType}    application/x-www-form-urlencoded;charset=UTF-8    # POST数据格式

*** Test Cases ***    targetUid          lastFid                        ret
Class_01              [Documentation]    timeline/user TestCase测试用例
                      [Tags]             Test                           Online    gxy    v4.7
                      [Template]         timeline_user_Post_Keywords
                      93548964           0                              0

*** Keywords ***
timeline_user_Post_Keywords
    [Arguments]    ${targetUid}    ${lastFid}    ${ret}
    [Documentation]    timeline/albums 接口用例的Keywords关健字
    ######Evaluate    reload(sys)    sys
    ##Evaluate    sys.setdefaultencoding( "utf-8" )    sys
    #从配置的用户列表中随机取一个用户运行此用例
    #${userName}    Env_username
    ${path}=    set variable    /timeline/user
    ${maps}=    create dictionary
    set to dictionary    ${maps}    targetUid=${targetUid}
    set to dictionary    ${maps}    lastFid=${lastFid}
    log    ========输出接口URL：${post_URL}${path}
    log    ========接口的入参为：${userName}:${maps}==========
    ${resp}=    thejoyrun_postd    ${path}    ${maps}    ${userName}    ${post_URL}
    ${content}=    charconver    ${resp.content}
    log json    ${content}
    log    ======开始断言验证=====
    log    验证ret是否符合预期
    should contain    ${content}    "ret":"${ret}"
    log    ret 符合预期为:${ret}
    log    验证OK！！用户${userName}；URL：${post_URL}${path}；传参：${maps}！！
