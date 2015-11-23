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
metadata = MetaData()
table = Table('person', metadata, 
Column('id', Integer, primary_key=True),
Column('name', String(25), nullable=False))
table
# OUT: Table('person', MetaData(bind=None), Column('id', Integer(), table=<person>, primary_key=True, nullable=False), Column('name', String(length=25), table=<person>, nullable=False), schema=None)
print table.columns
# OUT: ['person.id', 'person.name']
print metadata.tables
# OUT: immutabledict({'person': Table('person', MetaData(bind=None), Column('id', Integer(), table=<person>, primary_key=True, nullable=False), Column('name', String(length=25), table=<person>, nullable=False), schema=None)})
metadata.create_all(engine)
# OUT: INFO:sqlalchemy.engine.base.Engine:PRAGMA table_info("person")
# OUT: INFO:sqlalchemy.engine.base.Engine:()
# OUT: INFO:sqlalchemy.engine.base.Engine:
# OUT: CREATE TABLE person (
# OUT: 	id INTEGER NOT NULL, 
# OUT: 	name VARCHAR(25) NOT NULL, 
# OUT: 	PRIMARY KEY (id)
# OUT: )
# OUT: INFO:sqlalchemy.engine.base.Engine:()
# OUT: INFO:sqlalchemy.engine.base.Engine:COMMIT
clause = table.insert()
clause
# OUT: <sqlalchemy.sql.dml.Insert object at 0xb68e62ac>
print clause
# OUT: INSERT INTO person (id, name) VALUES (:id, :name)
engine.execute(clause, name='Guido')
# OUT: INFO:sqlalchemy.engine.base.Engine:INSERT INTO person (name) VALUES (?)
# OUT: INFO:sqlalchemy.engine.base.Engine:('Guido',)
# OUT: INFO:sqlalchemy.engine.base.Engine:COMMIT
# OUT: <sqlalchemy.engine.result.ResultProxy object at 0xb6513aac>
