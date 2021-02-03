#!/bin/bash

cd /home/rjt/Devel/Personal/PrintMail || exit

source venv/bin/activate

getmail -g ./config/ -r ./getmail.rc >> getmail.log 2>&1

logrotate  -s config/logrotate.state config/logrotate.rc


