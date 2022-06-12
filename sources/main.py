#Author: 808-Dev
#License: GPL - GNU General Public License
#Version: V.1.0.0 (Version 1)
#-----------------------------------------
#Required libraries:
#configparser
#tweepy
#wget
#mysql.connector
#pythondialog
#colorama
#-----------------------------------------
#This program is free software: you can redistribute it and/or modify
#it under the terms of the GNU General Public License as published by
#the Free Software Foundation, either version 3 of the License, or
#(at your option) any later version.

#This program is distributed in the hope that it will be useful,
#but WITHOUT ANY WARRANTY; without even the implied warranty of
#MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#GNU General Public License for more details.

#You should have received a copy of the GNU General Public License
#along with this program.  If not, see <https://www.gnu.org/licenses/>.
#------------------------------------------
#You didn't get a copy cuz your a loser! Ahaha
#------------------------------------------
#Notes:
#So far I need to add a few filters so that any info going into the MYSQL DBs doesn't include private data since
#I know this thing can and probably will be used to try to harm people. Manual moderation is necessary for now.
#Also, images are not downloadable yet, but I plan on fixing that in the next version. I also hope to clean it up
#a bit so that people can understand whats going on and so that variables can be changed outside the program.
#Finally, Windows is NOT compatible with this code since Dialog requires a Unix/Linux API which is incompatible
#with Windows 10 systems. This could be possible with Windows 11 but I aint about to try that for a bit.

import configparser, os, tweepy
from libraries.tweaks import *
from libraries.sqlmod import *
from dialog import Dialog

ConfigFile = configparser.ConfigParser()
Node = SQLConnect()
dialog = Dialog(dialog="dialog")
dialog.set_background_title("Salii Archival Backend")
dialog.infobox("Version: 1.0.0\nCodename: Salii\nBuild Date: 06-11-2022\n",width=40,height=5)

if not os.path.exists('config.ini'):

        GenerateConfig()
        dialog.msgbox(text="This software needs you to apply for a Twitter Developer account before use."+
                           "\nPlease goto: https://dev.twitter.com/ to register for one and then apply for"+
                           "\nan elevated account so that the service can be used for. "
                           "\nOnce completed, please fill in the config.ini file that this program generated.",height=12,width=80)
        dialog.msgbox(text="This software also requires a MYSQL compatible database to be available to use."+
                           "\nPlease import the template SQL file provided in the package provided with this program"+
                           "and assign a user to the database generated. ",height=12,width=80)
        cls()
        exit()

else:

    ConfigFile.read("config.ini")

    API_PUBLIC_KEY = ConfigFile['KEYS']['api_public_key']
    API_PRIVATE_KEY = ConfigFile['KEYS']['api_private_key']
    API_BEARER_TOKEN = ConfigFile['KEYS']['api_bearer_token']
    API_PUBLIC_TOKEN = ConfigFile['TOKENS']['api_public_token']
    API_PRIVATE_TOKEN = ConfigFile['TOKENS']['api_private_token']

client = tweepy.Client(API_BEARER_TOKEN, API_PUBLIC_KEY, API_PRIVATE_KEY, API_PUBLIC_TOKEN, API_PRIVATE_TOKEN)
auth = tweepy.OAuth1UserHandler(API_PUBLIC_KEY, API_PRIVATE_KEY, API_PUBLIC_TOKEN, API_PRIVATE_TOKEN)
api = tweepy.API(auth)

Tags = ["@saliibot", "#saliibot", "#Saliibot", "@Saliibot"] #Only can have 25 tags since thats all Twitter allows
OnSuccess = 'Successfully archived and available' #Response message for a successful copy.
OnFail = 'Something went wrong. Unable to archieve this tweet.' #Response message for a failed copy


class StreamObject(tweepy.StreamingClient):

    def on_connect(self):

        dialog.infobox(text="Connected.",width=14,height=3)

    def on_tweet(self, tweet):
        
        RetrievedStatus = api.get_status(api.get_status(tweet.id).in_reply_to_status_id,tweet_mode='extended')
            
        try:
            
            DataSet = [str(RetrievedStatus.in_reply_to_screen_name), str(RetrievedStatus.full_text),'{"img":"'+str(RetrievedStatus.entities['media'][0]['media_url'])+'"}',str(RetrievedStatus.created_at)[:10]]
        
        except:
            
            DataSet = [str(RetrievedStatus.in_reply_to_screen_name), str(RetrievedStatus.full_text),'{"img":"/css/noimage.png"}',str(RetrievedStatus.created_at)[:10]]
        
        if RetrievedStatus.full_text != OnSuccess: #This will keep the API from responding to  
            
            try:

                SQLPost(template='INSERT INTO `listingcache`(`ListingId`, `ListingName`, `ListingContent`, `ListingMeta`, `ListingDate`) VALUES (NULL, %s, %s, %s, %s)',data=DataSet,connection=Node)
                dialog.infobox(text='\nText in post: '+str(RetrievedStatus.full_text)+
                                    '\nCreator of post: '+RetrievedStatus.in_reply_to_screen_name , height=15, width=50)
                api.update_status(status=OnSuccess,in_reply_to_status_id=tweet.id)

            except:

                dialog.infobox(text='Unable to upload data...' , height=1, width=30)
                api.update_status(status=OnFail,in_reply_to_status_id=tweet.id)

        else:
            
            dialog.infobox(text='Ignoring post.', height=19, width=3)

    def on_disconnect(self):
        
        dialog.infobox(text="Disconnected.",width=17,height=3)

stream = StreamObject(bearer_token=API_BEARER_TOKEN)

for Tag in Tags:

    stream.add_rules(tweepy.StreamRule(Tag))

stream.filter(tweet_fields=[])