# ntfy.py - A simple [nfty.sh](https://github.com/binwiederhier/ntfy/) client written in python

ntfy.py is a simple nfty.sh client for sending notifications.

Should support all parameters except file attachments.

## Usage

```bash
ntfy.py myTopic --message="This message was sent using ntfy.py" --title="Hello World!" --click=https://github.com/
```

## Installation

```bash
wget https://raw.githubusercontent.com/ioqy/ntfy-client-python/master/ntfy.py
sudo mv ntfy.py /usr/local/bin/
sudo chmod 755 /usr/local/bin/ntfy.py
```