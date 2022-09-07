from xxlimited import Str
from pydantic import BaseModel
from typing import Optional

class Engineer(BaseModel):
    title: str
    company: str
    full_or_part: str
    site: str
    position_level: str
    pay: str
    sitemap: Str
    url : str
    skills: str 
