from numpy import isin
import pymysql
HOST = '192.168.3.5'
DBUSER = 'root'
DBPASSWD = '12345678'
DBNAME = 'PTBOT'
PORT = 3309

class DB():
    def __init__(self,host=HOST,user=DBUSER,passwd=DBPASSWD,db=DBNAME,port=PORT,charset='utf8'):
        try:
            self.db = pymysql.connect(host=host,user=user,passwd=passwd,db=db,port=port,charset=charset)
        except pymysql.err.DatabaseError as e:
            raise e
        self.cur = self.db.cursor()

    def __del__(self):
        try:
            self.cur.close()
            self.db.close()
        except:
            print('disconnect db error')

    def insertDic2DB(self,tablename,dataDic):
        for key in dataDic:
            if isinstance(dataDic[key],str):
                dataDic[key] = dataDic[key].replace("'","''")
            else:
                dataDic[key] = str(dataDic[key])

        #将字典存入指定数据库
        key   = ",".join(dataDic.keys())
        value = '"' + '","'.join(dataDic.values()) + '"'
        sql = "insert into %s (%s) values (%s)" % (tablename,key,value)
        #print(sql)
        try:
            self.cur.execute(sql)
            #print('done')
        except pymysql.err.ProgrammingError as e:
            self.db.rollback()
            if e.args[0] == 1146:
                
                print(e.args[1])
            else:
                return False
        except pymysql.err.OperationalError as e:
            self.db.rollback()
            print(e.args[1])
            print(sql)
            return False
        self.db.commit()

    def createTable(self,tablename,dbFormat):
        #创建数据库表,key为字段名，value为字段类型
        sqlpre = ''
        for key in dbFormat:
            sqlpre += key + ' ' + dbFormat[key] + ','
        sql = "create table %s (%s)" % (tablename,sqlpre[:-1])
        
        try:
            self.cur.execute(sql)
        except Exception as e:
            self.db.rollback()
            raise e
        self.db.commit()
        
    def select(self,tablename,**kwargs):
        #查询数据库，返回结果集
        pass

    def dump_table(self,tablename):
        #导出数据库表
        sql = "select * from %s" % tablename
        self.cur.execute(sql)
        return self.cur.fetchall()

    def sqlexec(self,sql):
        #执行sql语句
        #print(sql)
        self.cur.execute(sql)
        self.db.commit()

