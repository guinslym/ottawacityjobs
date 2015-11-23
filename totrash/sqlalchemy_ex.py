import logging
logging.basicConfig(level=logging.DEBUG)
logging.getLogger('sqlalchemy.engine.base').setLevel(logging.DEBUG)
from sqlalchemy import  *
engine = create_engine('sqlite:///')
connection = engine.connect()
# OUT: INFO:sqlalchemy.engine.base.Engine:SELECT CAST('test plain returns' AS VARCHAR(60)) AS anon_1
# OUT: INFO:sqlalchemy.engine.base.Engine:()
# OUT: INFO:sqlalchemy.engine.base.Engine:SELECT CAST('test unicode returns' AS VARCHAR(60)) AS anon_1
# OUT: INFO:sqlalchemy.engine.base.Engine:()
result = connection.execute('select 2+2')
# OUT: INFO:sqlalchemy.engine.base.Engine:select 2+2
# OUT: INFO:sqlalchemy.engine.base.Engine:()
# OUT: DEBUG:sqlalchemy.engine.base.Engine:Col ('2+2',)
result.scalar()
# OUT: DEBUG:sqlalchemy.engine.base.Engine:Row (4,)
# OUT: 4
metadata = Metadata()
# OUT: Traceback (most recent call last):
# OUT:   File "<input>", line 1, in <module>
# OUT: NameError: name 'Metadata' is not defined
