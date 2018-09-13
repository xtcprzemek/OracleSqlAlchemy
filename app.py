from sqlalchemy import create_engine
import cx_Oracle
import config
"""
to db configuration
create file config.py

DATABASE = {
'drivername' : 'oracle',
'host'        : 'localhost',
'port'        : '1521',
'database'    :'XE',
'username'    :'HR',
'password'    :'HR'
}
"""
sid = cx_Oracle.makedsn(config.DATABASE['host'], config.DATABASE['port'], sid=config.DATABASE['database'])

cstr = 'oracle://{user}:{password}@{sid}'.format(
    user=config.DATABASE['username'],
    password=config.DATABASE['password'],
    sid=sid
)

engine =  create_engine(
    cstr,
    convert_unicode=False,
    pool_recycle=10,
    pool_size=50,
    echo=True
)

result = engine.execute('select * from employees')

for row in result:
    print(row)