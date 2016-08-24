#!/usr/bin/python
#-*- coding:utf-8 -*-
import sys
import MySQLdb
import os.path


#1. 解析文件
file_name = os.path.basename(sys.argv[1]).split(".")[0]
data_set = {}
with open(sys.argv[1]) as source_file:
    is_first_line = True
    for line in source_file:
        splited_line = line.strip("\n").split("|")
        if 1 == len(splited_line):
            continue
        elif is_first_line:
            is_first_line = False
            for column in splited_line[1:-1]:
                #print column
                column = column.strip()
                data_set[column] = []
        else:
            for value in splited_line[1:-1]:
                #print value
                data_set[column].append(value.strip())
print data_set

#2. 创建数据库
try:
    #conn = MySQLdb.connect(host='localhost',user='root',db='test',port=3306)
    conn = MySQLdb.connect(host='localhost',user='root',db='test',port=3306, charset='utf8')
    cur = conn.cursor()
    cur.execute('drop table if exists %s' % file_name)
    sql_create_table = (
            "CREATE TABLE `%s` ("
            "  `Id` int(11),"
            "  `test` varchar(255),"
            "  PRIMARY KEY (`Id`)"
            ") ENGINE=InnoDB charset=utf8") % file_name
    cur.execute(sql_create_table)
    cur.close()
    conn.close()
except MySQLdb.Error,e:
     print "Mysql Error %d: %s" % (e.args[0], e.args[1])
