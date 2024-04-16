```bash
gunicorn main:app -k gevent --worker-connections 1000 -p 5001 -w 1 -b 0.0.0.0:5001 --access-logfile -
```
