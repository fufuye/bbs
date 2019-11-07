import pymysql
# 创建bbs库
# conn = pymysql.Connect(host='127.0.0.1',user='root',port=3306,charset='utf8')
# cursor = conn.cursor()
# sql = "create database bbs default charset=utf8"
# cursor.execute(sql)
# # 关闭游标和链接
# conn.close()
# cursor.close()

# 创建user表
# conn = pymysql.Connect(host='127.0.0.1',user='root',port=3306,charset='utf8')
# cursor = conn.cursor()
# sql = "create table if not exists(uid primary key int aoto_increment,username varchar(100) unique,suertype enum('0','1') default '0',password varchar(100),regtime datetime,email varchar(100))"
# cursor.execute(sql)
# conn.close()
# cursor.close()



# # 增加记录
# conn = pymysql.Connect(host='127.0.0.1',user='root',db='bbs',port=3306,charset='utf8')
# cursor = conn.cursor()
# sql = "insert into user(suername,password) values ('fufu','456'),('lili','789')"
# cursor.execute(sql)
# conn.commit()
# conn.close()
# cursor.close()

# 输入用户名和密码
# conn = pymysql.Connect(host='127.0.0.1',user='root',db='bbs',port=3306,charset='utf8')
# cursor = conn.cursor()
# suername = input("请输入用户名:")
# password = input("请输入密码:")
# print(suername, password)
# sql = "select uid from user where suername=%s and password=%s"
# print(sql)
# result = cursor.execute(sql, [suername, password])
# print(cursor._executed)
# print(result)
# if result > 0:
#     print("登录成功")
# else:
#     print("密码或用户名错误,请重新登录")
# cursor.close()
# conn.close()

# 查询信息
# conn = pymysql.Connect(host='127.0.0.1',user='root',db='bbs',port=3306,charset='utf8')
# cursor = conn.cursor()
# sql = "select suername '用户名', usertype '用户类型',password '密码',regtime '注册时间',email from user"
# cursor.execute(sql)
# cursor.close()
# conn.close()




