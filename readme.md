```bash
sudo apt install gunicorn  # do not install python3-telethon from apt
pip3 install telethon gevent flask[async] # telethon>1.34.0
```
```bash
gunicorn main:app -k gevent --worker-connections 1000 -p 5001 -w 1 -b 0.0.0.0:5001 --access-logfile -
```
