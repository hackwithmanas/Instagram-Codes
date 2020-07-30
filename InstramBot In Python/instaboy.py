from instabot import Bot


bot = Bot()

bot.login(username="user_name",
          password="user_password")

# Recommended to put the photo
# you want to upload in the same
# directory where this Python code
# is located else you will have
# to provide full path for the photo
bot.upload_photo("Your Pic",
                 caption="Type Your Caption Here")
