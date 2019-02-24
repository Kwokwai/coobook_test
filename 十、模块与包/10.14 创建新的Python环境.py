# 你可以使用 pyvenv 命令创建一个新的“虚拟”环境。 这个命令被安装在Python解释器同一目录，或Windows上面的Scripts目录中。下面是一个例子：
#
# bash % pyvenv Spam
# bash %
# 传给 pyvenv 命令的名字是将要被创建的目录名。当被创建后，Span目录像下面这样：
#
# bash % cd Spam
# bash % ls
# bin include lib pyvenv.cfg
# bash %
# 在bin目录中，你会找到一个可以使用的Python解释器：
#
# bash % Spam/bin/python3
# Python 3.3.0 (default, Oct 6 2012, 15:45:22)
# [GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> from pprint import pprint
# >>> import sys
# >>> pprint(sys.path)
# ['',
# '/usr/local/lib/python33.zip',
# '/usr/local/lib/python3.3',
# '/usr/local/lib/python3.3/plat-darwin',
# '/usr/local/lib/python3.3/lib-dynload',
# '/Users/beazley/Spam/lib/python3.3/site-packages']
# >>>
# 这个解释器的特点就是他的site-packages目录被设置为新创建的环境。 如果你要安装第三方包，它们会被安装在那里，而不是通常系统的site-packages目录。