from sqlalchemy import Column, Integer, String, Boolean
from .database import Base


class Engineer(Base):
    __tablename__ = 'ML_Engineer'
    id = Column(Integer, primary_key=True, index=True)  # 设置主键和索引
    title = Column(String(32)) # 職位名稱
    company = Column(String(32)) # 公司名城
    full_or_part = Column(String(32)) # full time or part time
    site = Column(String(40))  # 工作地點
    position_level = Column(String(32)) # 職位level
    pay = Column(String(32)) #薪水
    sitemap = Column(String(32)) #不太懂
    url = Column(String(200)) #網址
    skills = Column(String(100))  #所需技能
     
    def __init__(self, query):
        self.title = query.get('title')
        self.company = query.get('company')
        self.full_or_part = query.get('full_or_part')
        self.site = query.get('site')
        self.position_level = query.get('position_level')
        self.pay  = query.get('pay')
        self.sitemap = query.get("sitemap")
        self.url = query.get('url')
        self.skills = query.get('skills')
     
    def returnData(self):
        return {"title": self.title, "company":self.company, \
                "full_or_part": self.full_or_part, "site": self.site,\
                "position_level": self.position_level, "pay": self.pay, \
                "sitemap": self.sitemap, "url": self.url, "skills":self.skills}
