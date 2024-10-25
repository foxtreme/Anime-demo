from sqlmodel import select, Session
from fastapi import HTTPException


class BaseRepository:
    def __init__(self, model, session: Session):
        self.model = model
        self.session = session

    def create(self, entity):
        self.session.add(entity)
        self.session.commit()
        self.session.refresh(entity)
        return entity

    def get_all(self):
        query = (select(self.model).offset(0).limit(20))
        entities = self.session.exec(query).all()
        return entities

    def get_by_id(self, entity_id: int):
        entity = self.session.get(self.model, entity_id)
        if not entity:
            raise HTTPException(status_code=404, detail="Object not found")
        return entity

    def update(self, entity, entity_id):
        existing_entity = self.session.get(self.model, entity_id)
        if not existing_entity:
            raise HTTPException(status_code=404, detail="Object not found")
        for key, value in entity.items():
            setattr(existing_entity, key, value)
        self.session.add(existing_entity)
        self.session.commit()
        self.session.refresh(existing_entity)
        return existing_entity

    def delete(self, entity_id: int):
        existing_entity = self.session.get(self.model, entity_id)
        if existing_entity:
            self.session.delete(existing_entity)
            self.session.commit()
        return entity_id
