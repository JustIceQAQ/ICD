from typing import Self

from pydantic import BaseModel, Field, model_validator, field_serializer


class DataSet(BaseModel):
    id: str = Field(alias="ID")
    label: str
    name: str | None = Field(default=None)
    is_leaf: bool = Field(alias="isLeaf")
    is_adopted_child: bool = Field(alias="isAdoptedChild")
    suggested: str | None = Field(alias="Suggested", default=None)
    average_depth: float = Field(alias="averageDepth")
    breadth_value: float | None = Field(alias="breadthValue", default=None)
    items: list[Self] | None = Field(default=None)

    @model_validator(mode="after")
    def set_name(self):
        self.name = self.label.replace(self.id, "").strip()
        return self

    @field_serializer("items", when_used="always")
    def serialize_items(self, v, _info):
        return None if not v else v
