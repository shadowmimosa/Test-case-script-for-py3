#!/bin/bash
sudo  mkdir  /var/lib/jenkins/Report/$1
sleep 3 
pybot --include Online  --variable login_URL:http://api.thejoyrun.com --variable api_URL:http://api.thejoyrun.com --variable beta_URL:http://beta.thejoyrun.com --variable bet_URL:http://bet.api.thejoyrun.com --variable user_URL:http://u.api.thejoyrun.com --variable topic_URL:http://topic.api.thejoyrun.com --variable crew_muilt_URL:http://crew-muilt.api.thejoyrun.com --variable crew_URL:http://crew.api.thejoyrun.com --variable crewapp_URL:http://crewapp.api.thejoyrun.com --variable ec_URL:http://ec.thejoyrun.com   --variable advert_URL:http://advert.api.thejoyrun.com  --variable training_URL:http://training.api.thejoyrun.com  --variable wear_URL:http://wear.api.thejoyrun.com  --variable   point_URL:http://point.api.thejoyrun.com --variable im_URL:http://im.api.thejoyrun.com  --variable marathon_URL:http://marathon.api.thejoyrun.com  --variable recommend_URL:http://recommend.api.thejoyrun.com  --variable live_URL:http://live.api.thejoyrun.com  --variable wallet_URL:http://wallet.api.thejoyrun.com --variable media_URL:http://media.api.thejoyrun.com  --variable challenge_URL:http://challenge.api.thejoyrun.com  --variable event_URL:http://event.api.thejoyrun.com  --variable mapp_URL:https://mapp.api.thejoyrun.com --variable appkey1:fb1931e425f84313bfae4b93ab3ccdc4  --variable appkey2:1fd6e28fd158406995f77727b35bf20a  --variable APPVERSION:100.3.1.0 --variable corpcrewappkey:0a7d4aa5-c13c-40c2-9b1e-3476071a6f82  --variable corpcrewappid:wx24fffb22401a1157 --variable corpcrewsid:6861e3f7620840c2b03d8eff181a61d70 -d /var/lib/jenkins/Report/$1   $2 