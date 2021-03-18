from sqlalchemy import create_engine
from sqlalchemy.orm import scoped_session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import os

# dbファイル名と保存先を指定する（同一フォルダにdata.dbというファイルを作成するため）
database_file = os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.db')

# SQLiteを指定
engine = create_engine('sqlite:///' + database_file, convert_unicode=True, echo=True)
db_session = scoped_session(
                    sessionmaker(
                        autocommit = False,
                        autoflush  = False,
                        bind       = engine
                    )
				)
Base = declarative_base()
Base.query = db_session.query_property()

# データベース作成
def init_db():
    import flaski.dbmodels
    Base.metadata.create_all(bind=engine)
