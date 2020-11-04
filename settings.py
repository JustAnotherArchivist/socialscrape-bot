import os

# variables to be changed
#version = '' # Set at runtime by start.py
irc_channel_bot = '#archivebot'
irc_nick = 'socialbot'
irc_server_name = 'irc.hackint.org'
irc_server_port = 6697
irc_server_ssl = True
irc_sasl = os.environ['SOCIALBOT_SASL'] # Replace with None to disable SASL
log_file_name = 'log.log'

# variables to be changed by script
services = {}
irc_bot = None
logger = None
running = True
