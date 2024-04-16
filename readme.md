```bash
sudo apt install gunicorn python3-gevent python3-telethon python3-flask
```
```bash
gunicorn main:app -k gevent --worker-connections 1000 -p 5001 -w 1 -b 0.0.0.0:5001 --access-logfile -
```
