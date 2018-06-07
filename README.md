# MDMA-style-transfer

Using <https://github.com/jfilter/universal-style-transfer-pytorch> to transform images.

The main repo is <https://github.com/jfilter/MDMA>.

## Usage

We use a fresh Ubuntu 16.04. installation and use root for everything. Feel free to change to a proper user.

1.  Install [pipenv](https://docs.pipenv.org/)
1.  `git clone https://github.com/jfilter/universal-style-transfer-pytorch`
1.  `cd universal-style-transfer-pytorch && pipenv install && ./setup.sh && cd ..`
1.  `git clone https://github.com/jfilter/MDMA-style-transfer && cd MDMA-style-transfer`
1.  Create a `secrets.py` for with the basic auth credentials to connect to `MDMA`:

```
username = 'XXX'
password = 'XXX'
```

5.  Create a script `do.sh` that does the actual transfer:

```
cd /root/MDMA-style-transfer && /usr/local/bin/pipenv run python run.py >> /root/log.txt 2>&1
```

6.  To make sure the bash script only runs once at the same time: `apt-get install run-one`
7.  add to your crontab (`crontab -e`) to run e.g. every minute

```
* * * * * run-one /root/do.sh
```

## Caveats

Right now, you can only transform one image in a batch. This is because the style weight has to be set for a batch. We allow to set the style weight individual for each image. Thus, we process only one.

## License

MIT.
