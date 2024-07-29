from sqlalchemy import create_engine, select, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker

dbPath = '/Users/ice/Desktop/GitHubRepositories/PythonPractice/UdemyClass/CH14/ORM_Alchemy/datafile.db'
engine = create_engine('sqlite:///%s' % dbPath)
metadata = MetaData()
people = Table('people', metadata, Column('id', Integer, primary_key=True), Column(
    'name', String), Column('count', Integer))
Session = sessionmaker(bind=engine)
session = Session()
metadata.create_all(engine)

# 新增資料方法1
# insert_statement = people.insert().values(name='Spencer', count=66)
# session.execute(insert_statement)
# 新增資料方法2
insert_statement = people.insert()
session.execute(insert_statement, [
    {'name': 'Otani', 'count': 17},
    {'name': 'Shohei', 'count': 18}
])
session.commit()
# 搜尋所有的people
# result = session.execute(select(people))

# 更新指定的資料
session.execute(people.update().values(
    count=20).where(people.c.name == 'Otani'))

# 搜尋指定的資料
result = session.execute(select(people).where(people.c.name == 'Otani'))

for row in result:
    print(row)
