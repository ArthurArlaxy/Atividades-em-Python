import hashlib

algorithm = hashlib.sha256()
message ='OI,tudo bem?'.encode()
algorithm.update(message)
print(algorithm.hexdigest())
print(algorithm.digest())