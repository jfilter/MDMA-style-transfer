# MDMA-style-transfer

Using <https://github.com/jfilter/universal-style-transfer-pytorch> to transform images.

## Usage

Install `pipenv`

1.  `git clone https://github.com/jfilter/universal-style-transfer-pytorch`
2.  `cd universal-style-transfer-pytorch && pipenv install && ./setup.sh && cd ..`
3.  `git clone https://github.com/jfilter/MDMA`
4.  Create a `secrets.py` for the basic auth to connect to `MDMA`:
    username = 'XXX'
    password = 'XXX'
5.

`cd /root/MDMA-style-transfer && /usr/local/bin/pipenv run python run.py >> /root/log.txt 2>&1

6.  install apt-get install run-once
7.  add crontab to `run-once ./do.sh`

## License

MIT.
