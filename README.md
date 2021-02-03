Very simple setup to autoprint from an email account
====================================================

This is a small config that achieves the following simple task:

1. pull email from a mail server, once a minute
1. extract any attachements
1. attempt to convert the attachements to PDF
1. send the attachements to a printer

It uses the following tools:

* [getmail6](https://github.com/getmail6/getmail6)
* lp (from CUPS) - installed on Ubunutu by default
* [unoconv](https://github.com/unoconv/unoconv)

Setup
=====

NOTE: I have only used this on Ubuntu, but it should work on any
Linux/Unix with a bit of fiddling.

Install everthing:

```bash
sudo apt install unoconv

git clone <this repo>
cd PrintMail
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt

cp config/getmail.rc.in config/getmail.rc
```

Configuration:

1. edit config/getmail.rc
1. edit run.sh to change the path

Run can now run ```./run.sh``` manually or set a crontab entry using ```control -e``` e.g.:

```* * * * * <YOUR_PATH>/run.sh```

