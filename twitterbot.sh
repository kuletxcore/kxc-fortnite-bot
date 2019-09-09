#! /bin/bash
sleep 15s #If this bot runs anyway and doesn't update the newsbot, I am going to lose my mind rn
cd output
rm news.png
rm shop.png
sleep 15s
curl "http://api2.nitestats.com/v1/itemshop?background=https://raw.githubusercontent.com/kuletxcore/kxc-fortnite-bot/master/media/nitestats.jpg" --output shop.png
cd ..
python app.py
sleep 20s
cd output
curl "http://api2.nitestats.com/v1/news/image?background=https://github.com/kuletxcore/kxc-fortnite-bot/raw/master/media/news.jpg" --output news.png
cd ..
python news.py
exit
