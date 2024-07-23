from sqlalchemy.orm import Session
from typing import Type, TypeVar, Generic

from database.models.base import BaseModel

ModelType = TypeVar('ModelType', bound=BaseModel)


class BaseDAO(Generic[ModelType]):
    def __init__(self, model: Type[ModelType]):
        self.model = model

    def get(self, db: Session, id: int) -> ModelType | None:
        return db.query(self.model).filter_by(id=id).first()

    def get_all(self, db: Session) -> list[ModelType]:
        return db.query(self.model).all()

    def create(self, db: Session, obj_in: ModelType) -> ModelType:
        db.add(obj_in)
        db.commit()
        db.refresh(obj_in)
        return obj_in

    def update(self, db: Session, obj_in: ModelType, obj_update: dict) -> ModelType:
        for key, value in obj_update.items():
            setattr(obj_in, key, value)
        db.commit()
        db.refresh(obj_in)
        return obj_in

    def delete(self, db: Session, id: int) -> ModelType | None:
        obj = self.get(db, id)
        if obj:
            db.delete(obj)
            db.commit()
        return obj
