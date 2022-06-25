#!/usr/bin/env python3

import argparse
import requests
from urllib.parse import urljoin

parser = argparse.ArgumentParser()

parser.add_argument("topic",
                    help="Name of the topic the message gets published to")
parser.add_argument("--server",
                    dest="server",
                    required=False,
                    default="https://ntfy.sh",
                    help="The URL of the server beginning with the protocol (eg. https://). Default is https://ntfy.sh")
parser.add_argument("--message", "-m", "--x-message",
                    dest="message",
                    required=False,
                    help="Main body of the message as shown in the notification")
parser.add_argument("--title", "-t", "--x-title",
                    dest="title",
                    required=False,
                    help="Message title")
parser.add_argument("--priority", "--prio", "-p", "--x-priority",
                    dest="priority",
                    required=False,
                    help="Message priority")
parser.add_argument("--tags", "--tag", "--ta", "--x-tags",
                    dest="tags",
                    required=False,
                    help="Tags and emojis")
parser.add_argument("--delay", "--x-at", "--at", "--x-in", "--in", "--x-delay",
                    dest="delay",
                    required=False,
                    help="Timestamp or duration for delayed delivery")
parser.add_argument("--actions", "--action", "--x-actions",
                    dest="actions",
                    required=False,
                    help="JSON array or short format of user actions")
parser.add_argument("--click", "--x-click",
                    dest="click",
                    required=False,
                    help="URL to open when notification is clicked")
parser.add_argument("--attach", "-a", "--x-attach",
                    dest="attach",
                    required=False,
                    help="URL to send as an attachment, as an alternative to PUT/POST-ing an attachment")
#parser.add_argument("--filename", "--file", "-f", "--x-filename",
#                    dest="filename",
#                    required=False,
#                    help="Optional attachment filename, as it appears in the client")
parser.add_argument("--email", "--e-mail", "--mail", "-e", "--x-email", "--x-e-mail",
                    dest="email",
                    required=False,
                    help="E-mail address for e-mail notifications")
parser.add_argument("--cache", "--x-cache",
                    dest="cache",
                    choices=["no"],
                    required=False,
                    help="Allows disabling message caching")
parser.add_argument("--firebase", "--x-firebase",
                    dest="firebase",
                    choices=["no"],
                    required=False,
                    help="Allows disabling sending to Firebase")
parser.add_argument("--unifiedpush", "--up", "--x-unifiedpush",
                    dest="unifiedpush",
                    required=False,
                    help="UnifiedPush publish option, only to be used by UnifiedPush apps")
parser.add_argument("--poll-id", "--x-poll-id",
                    dest="poll-id",
                    required=False,
                    help="Internal parameter, used for iOS push notifications")
parser.add_argument("--authorization",
                    dest="authorization",
                    required=False,
                    help="If supported by the server, you can login to access protected topics")

parser.add_argument("--verbose",
                    required=False,
                    action="store_true",
                    help="Output the response from the POST request")

args = parser.parse_args()

# store some arguments in sperate variables because they will be removed in the next step
server = args.server
topic = args.topic
message = args.message
verbose = args.verbose

# remove some parameter from arguments because everything else goes into the HTTP headers
arg_dict = vars(args)
arg_dict.pop("server")
arg_dict.pop("topic")
arg_dict.pop("message")
arg_dict.pop("verbose")

if (len(server.strip()) == 0
        or server.count(" ") > 0):
    raise Exception("Server must not be empty and not contain a space")

if (len(topic.strip()) == 0
        or topic.count(" ") > 0):
    raise Exception("Topic must not be empty and not contain a space")

# build new dictionary with headers
headers = {}
for arg in arg_dict:
    if arg_dict[arg] != None:
        headers[arg] = arg_dict[arg].encode("utf-8")

if message != None:
    message = message.encode("utf-8")

response = requests.post(urljoin(server, topic),
                         data=message,
                         headers=headers)

if (verbose
        or response.ok != True):
    print(response.text)

response.raise_for_status()
