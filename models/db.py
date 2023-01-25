import pymysql


def endconnection():
    return pymysql.connect(host='195.179.239.51',user='u611292494_admin',password='Develop2023gim$',db='u611292494_User_DB')
