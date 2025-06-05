from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, schemas
from .database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/product/list", response_model=list[schemas.ProductOut])
def list_products(skip: int = 0, db: Session = Depends(get_db)):
    return crud.get_products(db, skip=skip)

@router.get("/product/{pid}/info", response_model=schemas.ProductOut)
def get_info(pid: int, db: Session = Depends(get_db)):
    product = crud.get_product(db, pid)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/product/add", response_model=schemas.ProductOut)
def add_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    return crud.create_product(db, product)

@router.put("/product/{pid}/update", response_model=schemas.ProductOut)
def update_product(pid: int, updated: schemas.ProductUpdate, db: Session = Depends(get_db)):
    product = crud.update_product(db, pid, updated)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product
