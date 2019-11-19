This is a template for creating your own scheduled Fortnite Item Shop and BR News twitter bot using python and heroku.

Requirements
--------
* __heroku__
   * [account](https://www.heroku.com/) and [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install): _for hosting python app and keeping it running_

Instructions
--------
0. Click the "Use this template" button and create your own repo

1. Create a new heroku app on the [Heroku Dashboard](https://herokuapp.com/) by clicking on ```New``` and selecting ```New App```.
   * Select your server and confirm its creation.
   * Make sure your Heroku account is connected to your github account via the ```Deploy``` tab.
   * Enable automatic deploys and select your repository.
   * Click on ```Deploy Branch``` to ensure a copy of the repo is initialized and ready on heroku.
   * Go to the ```Resources``` tab and make sure that the dyno worker is ___switched off!___ This is a very important step on creating this bot, so keep that in mind.

2. __Verify your Heroku account__
   * This is needed because of Heroku's requirements, and you need to verify your acccount if you want to use add-ons, which is required for this program.
   * Go to [this page](http://heroku.com/verify) and enter your credit card details
      - Don't worry! Your card will never be charged for this program and will only serve as Verification of your Heroku account.
   * You do not need a paid plan for this. I use the free version of Heroku since we'll only use this once or twice a day.

3. Create a [new twitter account](https://twitter.com/). (If you already have one, please use your twitter account instead and skip straight to step 3.)
    * Use your current email to create the account by adding [a tag](http://en.wikipedia.org/wiki/Email_address#Address_tags).
       - Ex: _email@gmail.com_ => _email+twitterbot@gmail.com_
    * Confirm the email address associated with this new twitter account.

4. From your main twitter account (not the one you just created, unless this is your first twitter account!) create a [new twitter app](https://apps.twitter.com).
    * Apply for a Twitter developer account, and select ```Making a bot```. Enter the necessary details and submit your application.
    * This process may take a while, and it may not be instant.
    * After your application, create a bot by clicking on the ```Create an App``` button.
    * Enter the necessary details.
    * Under _Settings_ / _Application Type_:
        - Enable _"Read and Write"_
    * Under _Details_:
        - Click _"Create My Access Token"_

5. Create an `.env` file containing your twitter keys.
    * In your local repo, create a file called ```.env```, and then copy everything from [this paste](https://pastebin.com/PxJnKrFq)
    * Replace the placeholders with your credentials. You can only view it once on the twitter page until you close it, so copy everything to the ```.env``` file.
    * For [heroku](https://devcenter.heroku.com/articles/config-vars), use ```heroku-config``` to copy contents of ```.env``` to your heroku app.
        - Configure your heroku app by launching ```heroku git:remote -a [insert your heroku app name here]``` on the folder of your cloned Github repo.
        - Install heroku-config: ```heroku plugins:install heroku-config```.
        - Now run ```heroku config:push```.
            - NOTE: To update heroku environment variables later, run ```heroku config:push --overwrite```

__Okay, now here's the fun part:__

6. Personalize your message and background!
    * Change the ```twitterbot.sh``` URLs. The default settings have my branding on it, so you may need to replace the ```background``` URL to something different, or remove it entirely.
         - If you want to create your own backgrounds, please refer to the ```media``` folder for the image size and positioning.
         - The images I use are ```news.jpg``` and ```nitestats.jpg```. Change them to anything you like.
            - If you want to have weekly SAC reminders, the image I use is ```SAC_Reminder.png``` on the ```output``` folder.
         - To get the Image URL, go to the image you uploaded on your github repo and open it on a new tab.
    * Change the message and timezone on ```app.py``` and ```news.py```.
         -  __OPTIONAL__: If you want weekly SAC reminders, change ```sac.py``` as well.
         - You can also remove the Timezones and its references if you don't want the time on your tweets.

7. Commit and push local changes to Github. Heroku will automatically update the remote files since you have Heroku connected.
    
8. On your Heroku app dashboard, go to the ```Resources``` tab and add the ```Advanced Scheduler``` add-on.
    * Make sure your Heroku account is verified for this!
    * Click on it, and create a new trigger.
    * Add a name, and make sure the command is ```bash twitterbot.sh```, and the timezone is UTC.
    * Make it a recurring trigger and select the ```Schedule Helper``` option.
    * Item shop resets every day at 12:00AM UTC. Save the trigger.
      - If you use ```sac.py```, do the same steps. Except this time, you must change the interval to weekly and the time to be Tuesdays at 8:00AM UTC.

Additional Info
---------
Please check out the [Nitestats Discord](https://discord.gg/tNmWbBy) for updates on the API. Please redirect all questions and bug reports about the API to this discord. Thank you!

## If this repo helped you out, Please consider using code "KuletXCore" on the Fortnite item shop or on the Epic Games Store! :)
