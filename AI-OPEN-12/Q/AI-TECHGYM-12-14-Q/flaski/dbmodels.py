from sqlalchemy import Column, Integer, String, Boolean
from flaski.database import Base

# テーブル情報 花マスタ
class FlowerMaster(Base):
    # テーブル名の設定
    __tablename__ = "flower_master"
    # Column情報の設定
    flower_name     = Column(String, primary_key=True)    # 花名
    wiki_url        = Column(String)                      # WikipediaのURL
    picture_path    = Column(String)                      # 花画像パス
    copyright_owner = Column(String)                      # 権利情報
    copyright_url   = Column(String)                      # 権利情報URL

    def __init__(self, flower_name=None, wiki_url=None, picture_path=None, copyright_owner=None, copyright_url=None):
        self.flower_name     = flower_name
        self.wiki_url        = wiki_url
        self.picture_path    = picture_path
        self.copyright_owner = copyright_owner
        self.copyright_url   = copyright_url