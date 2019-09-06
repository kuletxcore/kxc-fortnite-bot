cd ./output
rm news.png
sleep 15
curl "http://api2.nitestats.com/v1/news/image?background=https://github.com/kuletxcore/kxc-fortnite-bot/raw/master/media/news.jpg" --output news.png
cd ..
python news.py