# 在 python2 中，使用 pip install mysql-python 进行安装连接MySQL的库，使用时 import MySQLdb 进行使用
#
# 在 python3 中，改变了连接库，改为了 pymysql 库，使用pip install pymysql 进行安装，直接导入即可使用
#
# 但是在 Django 中， 连接数据库时使用的是 MySQLdb 库，这在与 python3 的合作中就会报以下错误了
import pymysql

pymysql.install_as_MySQLdb()

#顾名思义应该是让 Django 把 pymysql 当成 MySQLdb