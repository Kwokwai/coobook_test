# 如果你想分发你的代码，第一件事就是给它一个唯一的名字，并且清理它的目录结构。 例如，一个典型的函数库包会类似下面这样：
#
# projectname/
#     README.txt
#     Doc/
#         documentation.txt
#     projectname/
#         __init__.py
#         foo.py
#         bar.py
#         utils/
#             __init__.py
#             spam.py
#             grok.py
#     examples/
#         helloworld.py
#         ...
# 要让你的包可以发布出去，首先你要编写一个 setup.py ，类似下面这样：
#
# # setup.py
# from distutils.core import setup
#
# setup(name='projectname',
#     version='1.0',
#     author='Your Name',
#     author_email='you@youraddress.com',
#     url='http://www.you.com/projectname',
#     packages=['projectname', 'projectname.utils'],
# )
# 下一步，就是创建一个 MANIFEST.in 文件，列出所有在你的包中需要包含进来的非源码文件：
#
# # MANIFEST.in
# include *.txt
# recursive-include examples *
# recursive-include Doc *
# 确保 setup.py 和 MANIFEST.in 文件放在你的包的最顶级目录中。 一旦你已经做了这些，你就可以像下面这样执行命令来创建一个源码分发包了：
#
# % bash python3 setup.py sdist
# 它会创建一个文件比如”projectname-1.0.zip” 或 “projectname-1.0.tar.gz”, 具体依赖于你的系统平台。如果一切正常， 这个文件就可以发送给别人使用或者上传至 Python Package Index.