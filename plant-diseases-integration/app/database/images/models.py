from sqlalchemy import Column, String, Boolean, TIMESTAMP, Integer, BLOB
from app.models import Base
import json


class PlantImage(Base):
    """
    Plant Image Model
    :cvar __tablename__ name of this model as a table in the db
    """
    __tablename__ = "plant_images"

    user_id = Column(String(250), nullable=False)
    image = Column(BLOB, nullable=False)

    def __init__(
            self,
            user_id,
            image
    ):
        self.user_id = user_id
        self.image = image

    def __repr__(self):
        """
        Create human readable representation of Plant Image
        :return: string representation of Plant
        """
        return (
            f"ID: {self.id}, Date Modified: {self.date_modified}, DateCreated: {self.date_created}, user_id: {self.user_id},"
            f"Image: {self.image}"
        )

    def to_json(self):
        return dict(
            id=self.id,
            user_id=self.user_id,
            image=self.image
        )

    def from_json(self, *args):
        request = json.loads(args)
        self.image = request["image"],
        self.user_id = request["user_id"]
        self.id = request["id"]

