# 假设你的包中的文件组织成如下：
#
# mypackage/
#     __init__.py
#     somedata.dat
#     spam.py
# 现在假设spam.py文件需要读取somedata.dat文件中的内容。你可以用以下代码来完成：
#
# # spam.py
# import pkgutil
# data = pkgutil.get_data(__package__, 'somedata.dat')
# 由此产生的变量是包含该文件的原始内容的字节字符串。