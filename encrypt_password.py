# coding:utf-8
from Euler import Euler
import os
from hashlib import sha256
from hmac import HMAC
import base64


edu = Euler()


'''
先随机生成 64 bits 的 salt，再选择 SHA-256 算法使用 HMAC 对密码和 salt 进行 10 次叠代混淆，最后将 salt 和 hash 结果一起返回。
'''
def encrypt_password(password, salt=None):
    """Hash password on the fly."""
    if salt is None:
        salt = os.urandom(8) # 64 bits.

    assert 8 == len(salt)
    assert isinstance(salt, str)

    if isinstance(password, unicode):
        password = password.encode('UTF-8')

    assert isinstance(password, str)

    result = password
    for i in xrange(10):
        result = HMAC(result, salt, sha256).digest()

    return salt + result
    
'''
验证函数，它直接使用 encrypt_password 来对密码进行相同的单向转换并比较
'''    
def validate_password(hashed, input_password):
    return hashed == encrypt_password(input_password, salt=hashed[:8])
    
password = 'secret password'
hashed = encrypt_password(password)  

#数据库中可以存储base64编码后的密码
turn64 = base64.b64encode(hashed)
print  'password '+ password+ ' encrypt to '+ turn64

#使用时再base64解码
assert validate_password(base64.b64decode(turn64), 'secret password')
