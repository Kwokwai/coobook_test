# 比起费力地找文件，你可能会倾向于写一个代码手动调节sys.path的值。例如:
#
# import sys
# sys.path.insert(0, '/some/dir')
# sys.path.insert(0, '/other/dir')
# 虽然这能“工作”，但是在实践中极为脆弱，应尽量避免使用。这种方法的问题是，它将目录名硬编码到了你的源代码。如果你的代码被移到一个新的位置，这会导致维护问题。更好的做法是在不修改源代码的情况下，将path配置到其他地方。如果您使用模块级的变量来精心构造一个适当的绝对路径，有时你可以解决硬编码目录的问题，比如__file__。举个例子：
#
# import sys
# from os.path import abspath, join, dirname
# sys.path.insert(0, join(abspath(dirname(__file__)), 'src'))
# 这将src目录添加到path里，和执行插入步骤的代码在同一个目录里。