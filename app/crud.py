from sqlalchemy.orm import Session
from . import models, schemas
from sqlalchemy import desc

def get_products(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Product).offset(skip).limit(limit).all()

def get_product(db: Session, product_id: int):
    return db.query(models.Product).filter(models.Product.id == product_id).first()

def create_product(db: Session, product: schemas.ProductCreate):
    db_product = models.Product(**product.dict())
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    return db_product

def update_product(db: Session, product_id: int, updated: schemas.ProductUpdate):
    product = get_product(db, product_id)
    if not product:
        return None
    for field, value in updated.dict().items():
        setattr(product, field, value)
    db.commit()
    db.refresh(product)
    return product
