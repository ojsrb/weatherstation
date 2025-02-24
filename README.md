# Install
```
sudo apt-get update

sudo apt-get install python3-pip
pip3 install adafruit-circuitpython-dht

sudo apt install git
git clone https://github.com/ojsrb/weatherstation.git
cd ~/weatherstation
sudo mv .bashrc ~/.bashrc
mkdir ~/data
touch ~/data/data.csv
echo 'time, temp, humid' > ~/data/data.csv

crontab -e
append "@reboot sleep 30 && ~/weatherstation/start.sh"

sudo reboot
```
