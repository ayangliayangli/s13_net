#example for markdown

# 概要说明
* 作业入口文件是 handle_haproxy.py

#修改haproxy.conf 的作业
##功能分解
* 获取一个backend
* 新增一个backend,record, 考虑各种情况
* 操作之前备份文件到 db/backup/ 下面,以时间命名
* 修改 --- todo
* 删除


# 优化
* 20160901
* 完善逻辑,修改文件后会把信息放入一个新文件里面,输入write,新文件会替换原来的文件
* 当修改了文件之后,再次fetch一个backend的时候,会同时显示老的配置文件和新的配置文件中的信息,输入wire 可以把新文件的东西移动到老的配置文件中去
* 文件的名称,使用变量来完成