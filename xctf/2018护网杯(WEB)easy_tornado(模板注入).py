import hashlib
hash = hashlib.md5()

filename='/fllllllllllllag'
cookie_secret="bc729b0f-f7fa-42e0-86df-9be266847234"
hash.update(filename.encode('utf-8'))
s1=hash.hexdigest()
hash = hashlib.md5()
hash.update((cookie_secret+s1).encode('utf-8'))
print(hash.hexdigest())