#!/usr/bin/env python3
# flask seesion解密
import sys
import zlib
from base64 import b64decode
from flask.sessions import session_json_serializer
from itsdangerous import base64_decode

def decryption(payload):
    payload, sig = payload.rsplit(b'.', 1)
    payload, timestamp = payload.rsplit(b'.', 1)

    decompress = False
    if payload.startswith(b'.'):
        payload = payload[1:]
        decompress = True

    try:
        payload = base64_decode(payload)
    except Exception as e:
        raise Exception('Could not base64 decode the payload because of '
                         'an exception')

    if decompress:
        try:
            payload = zlib.decompress(payload)
        except Exception as e:
            raise Exception('Could not zlib decompress the payload before '
                             'decoding the payload')

    return session_json_serializer.loads(payload)

if __name__ == '__main__':
    s = '.eJw9kM2KwkAQhF9l6bOHZNSL4EGIioHuEBl36L7Iuhtj5seFRCEZ8d03ethbURQfVfWA47mtugssbu29msCx-YHFAz5OsIAi44hh4zjWatQzVgcl2tvRVRLKhOImkF3PSeGAZh_ErnqM3rOmINuDojGDVhq2dS_aKdY8yDa3bMqEzTqluE5ZlQPpXSo2v1B0c1a544Aph32DJrdkOCGTe4reiSEvlmyh61lhDj2OLNQ8Je2W8JzAd9eej7dfV13_J7C-OMrqKWW5xyANvqqZT4-6jkVWziQT_8JhtlOod5EDD7RavnHXr1CNiFRNYQL3rmrf30CawPMPEvlkhg.YRu5mQ.BSToi23uU3hfhA5byAcDKhG4V70'
    print(decryption(s.encode()))
