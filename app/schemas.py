from pydantic import BaseModel
from typing import Optional
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

class ProductBase(BaseModel):
    name: str
    category: CategoryEnum
    description: Optional[str] = None
    product_image: Optional[str] = None
    sku: str
    unit_of_measure: UOMEnum
    lead_time: int

class ProductCreate(ProductBase):
    pass

class ProductUpdate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int
    created_date: str
    updated_date: str

    class Config:
        orm_mode = True
