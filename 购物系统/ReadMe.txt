实现：
用户和店家各自登录自己的，用户是USER/user.py,店家是SHOP/user.py
用户管理自己的信息，店家管理自己的信息
需要在pycharm中启动，运行USER/user.py或SHOP/user.py
因为存在路径问题，所以直接运行会报import错误，要想解决该问题，可以每个py中，添加
import sys
sys.path.append('../')
如果不行，再度娘一下，目前USER/user.py或SHOP/user.py添加这两行后，直接user.py能启动，其他文件未测试
这个系统不是很理想，所以只是备份一下。

