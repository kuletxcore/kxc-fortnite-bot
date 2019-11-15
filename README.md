This is a template for creating your own scheduled Fortnite Item Shop and BR News twitter bot using python and heroku.

A video tutorial for this is coming with step-by-step details on how to use this repo.

Requirements
--------
* __heroku__
   * [account](https://www.heroku.com/) and [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli#download-and-install): _for hosting python app and keeping it running_

Instructions
--------
0. Fork and pull this repo.

1. Create a new heroku app on the [Heroku Dashboard](https://herokuapp.com/) by clicking on ```New``` and selecting ```New App```.
   * Select your server and confirm its creation.
   * Make sure your Heroku account is connected to your github account via the ```Deploy``` tab.
   * Push the changes from your local repository to the Github repo you just forked.
   * Enable automatic deploys and select your forked repository.

2. Create a [new twitter account](https://twitter.com/). (If you already have one, please use your twitter account instead and skip straight to step 3.)
    * Use your current email to create the account by adding [a tag](http://en.wikipedia.org/wiki/Email_address#Address_tags).
       - Ex: _email@gmail.com_ => _email+twitterbot@gmail.com_
    * Confirm the email address associated with this new twitter account.

3. From your main twitter account (not the one you just created, unless this is your first twitter account!) create a [new twitter app](https://apps.twitter.com).
    * Apply for a Twitter developer account, and select ```Making a bot```
    * After your application, create a bot by clicking on the ```Create an App``` button.
    * Enter the necessary details.
    * Under _Settings_ / _Application Type_:
        - Enable _"Read and Write"_
    * Under _Details_:
        - Click _"Create My Access Token"_

4. Create an `.env` file containing your twitter keys.
    * In your local repo, create a file called ```.env```, and then copy everything from [this paste](https://pastebin.com/PxJnKrFq)
    * Replace the placeholders with your credentials. You can only view it once on the twitter page until you close it, so copy everything to the ```.env``` file.
    * For [heroku](https://devcenter.heroku.com/articles/config-vars), use ```heroku-config``` to copy contents of ```.env``` to your heroku app.
        - Configure your heroku app by launching ```heroku git:remote -a [insert your herokua app name here]``` on the folder of your cloned Github repo.
        - Install heroku-config: ```heroku plugins:install heroku-config```.
        - Now run ```heroku config:push```.
            - NOTE: To update heroku environment variables later, run ```heroku config:push --overwrite```

__Okay, now here's the fun part:__

5. Commit and push local changes to Github. Heroku will automatically update the remote files since you have Heroku connected.
    
6. Go to the ```Resources``` tab and add the ```Advanced Scheduler``` add-on.
    * Click on it, and create a new trigger.
    * Add a name, and make sure the command is ```bash twitterbot.sh```, and the timezone is UTC.
    * Make it a recurring trigger and select the ```Schedule Helper``` option.
    * Item shop resets every day at 12:00AM UTC. Save the trigger.

# And then you are done!
