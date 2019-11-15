#! /bin/bash
#Please do not change anything in this section!

sleep 15s
cd output
rm news.png
rm shop.png
sleep 15s

#Change the "background" image URL to something different.
curl "http://api3.nitestats.com/v1/shop/image?background=https://raw.githubusercontent.com/kuletxcore/kxc-fortnite-bot/master/media/nitestats.jpg" --output shop.png

#Please do not change anything in this section!
cd ..
python app.py
sleep 20s
cd output

#Change the "background" image URL to something different.
curl "http://api3.nitestats.com/v1/news/image?background=https://github.com/kuletxcore/kxc-fortnite-bot/raw/master/media/news.jpg" --output news.png

#Please do not change anything in this section!
cd ..
python news.py
exit
