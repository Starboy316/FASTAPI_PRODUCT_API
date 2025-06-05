from sqlalchemy import Column, BigInteger, String, Enum, Integer, TIMESTAMP, text
from .database import Base
import enum

class CategoryEnum(str, enum.Enum):
    finished = "finished"
    semi_finished = "semi-finished"
    raw = "raw"

class UOMEnum(str, enum.Enum):
    mtr = "mtr"
    mm = "mm"
    ltr = "ltr"
    ml = "ml"
    cm = "cm"
    mg = "mg"
    gm = "gm"
    unit = "unit"
    pack = "pack"

class Product(Base):
    __tablename__ = "products"

    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100))
    category = Column(Enum(CategoryEnum))
    description = Column(String(250))
    product_image = Column(String(length=1000))
    sku = Column(String(100))
    unit_of_measure = Column(Enum(UOMEnum))
    lead_time = Column(Integer)
    created_date = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP"))
    updated_date = Column(TIMESTAMP, server_default=text("CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP"))
