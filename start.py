# -*- coding: utf-8 -*-

import os
import subprocess
import sys
import time
import irc
import log
import settings


def main():
    if subprocess.check_output(['git', 'status', '--porcelain'], cwd = os.path.dirname(__file__) or '.') != b'':
        print('Working directory is not clean, refusing to start.')
        sys.exit(1)
    if os.path.isfile('UPDATE'):
        os.remove('UPDATE')
    if os.path.isfile('Instagram_run'):
        os.remove('Instagram_run')

    settings.version = subprocess.check_output(['git', 'show', '-s', '--format=format:%cd.%h', '--date=format:%Y%m%d'], cwd = os.path.dirname(__file__) or '.', encoding = 'utf-8')

    settings.logger = log.Log(settings.log_file_name)
    settings.logger.daemon = True
    settings.logger.start()
    settings.logger.log('Starting iBot')

    settings.irc_bot = irc.IRC()
    settings.irc_bot.daemon = True
    settings.irc_bot.start()

    while settings.running:
        if os.path.isfile('STOP'):
            os.remove('STOP')
            open('UPDATE', 'w').close()
            break
        time.sleep(1)

if __name__ == '__main__':
    main()
