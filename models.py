
import pydantic

__all__ = ['Place', 'Room']


class Place(pydantic.BaseModel):
	title: str
	description: str
	photo_id: str
	label: str


class Room(pydantic.BaseModel):
	label: str # тут должен быть текст из кнопки которую нажали
	description: str # полное описани
	price: int # цена
	photo_id: str
