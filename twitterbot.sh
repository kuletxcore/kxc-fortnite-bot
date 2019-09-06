#! /bin/bash
cd ./output
rm news.png
rm shop.png
sleep 15
curl "http://api2.nitestats.com/v1/news/image?background=https://github.com/kuletxcore/kxc-fortnite-bot/raw/master/media/news.jpg" --output news.png
curl "http://api2.nitestats.com/v1/itemshop?background=https://raw.githubusercontent.com/kuletxcore/kxc-fortnite-bot/master/media/nitestats.jpg" --output shop.png
cd ..
python app.py
python news.py