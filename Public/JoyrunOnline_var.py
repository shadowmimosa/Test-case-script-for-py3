#coding=utf-8
import time,traceback
import os
import sys
import platform
import subprocess
import random
import re


reload(sys)
sys.setdefaultencoding('utf-8')

#=======================线上发布连接地址(Online)========================

# 登录地址
login_URL='http://api.thejoyrun.com' 

#api项目地址
api_URL='http://api.thejoyrun.com' 

#beta约定跑相关
beta_URL='http://beta.thejoyrun.com'

#bet 动态配置相关
bet_URL='http://bet.api.thejoyrun.com'

# user用户工程,与用户信息相关
user_URL='http://u.api.thejoyrun.com' 

# topic工程,与首页相关
topic_URL='http://topic.api.thejoyrun.com' 

#crew-muilt 与跑团相关1
crew_muilt_URL='http://crew-muilt.api.thejoyrun.com' 

#crew 与跑团相关2
crew_URL='http://crew.api.thejoyrun.com' 

#crewapp 跑团相关3
crewapp_URL='http://crewapp.api.thejoyrun.com'

# ec电商工程,与订单相关
ec_URL='http://ec.thejoyrun.com'

# advert工程,与消息广告通告相关
advert_URL='http://advert.api.thejoyrun.com'

# training工程,与训练相关
training_URL='http://training.api.thejoyrun.com'

# wear工程,与穿戴相关
wear_URL='http://wear.api.thejoyrun.com'

#point_
point_URL='http://point.api.thejoyrun.com'

#im 消息相关
im_URL='http://im.api.thejoyrun.com'

#marathon 马拉松相关
marathon_URL='http://marathon.api.thejoyrun.com'

#recommend 推荐相关
recommend_URL='http://recommend.api.thejoyrun.com'

#live 赛事直播相关
live_URL='http://live.api.thejoyrun.com'

#wallet 推荐相关
wallet_URL='http://wallet.api.thejoyrun.com'

#media 媒体资讯相关
media_URL='http://media.api.thejoyrun.com'

#challenge 挑战相关
challenge_URL='http://challenge.api.thejoyrun.com'

#event 事件相关
event_URL='http://event.api.thejoyrun.com'

#企业跑团
cr_URL='https://cr.thejoyrun.com'

#=====小程序相关配置=================================

#小程序统一域名
mapp_URL='https://mapp.api.thejoyrun.com'


#跑团小程序密钥
corpcrewappkey='0a7d4aa5-c13c-40c2-9b1e-3476071a6f82'

#跑团小程序APPID
corpcrewappid='wx24fffb22401a1157'

#跑团小程序用户身份sid===2018-02-06  10:28
corpcrewsid='6861e3f7620840c2b03d8eff181a61d70'

##约定跑小程序密钥
betappkey='3e3aee29-6abb-495a-bb74-512acda2979e'

##约定跑小程序APPID
betappid='wxd19597f62e33ba65'

##约定跑小程序用户身份sid  2018-02-06 12:30 
betsid='6861e3f7620840c2b03d8eff181a61d70'
