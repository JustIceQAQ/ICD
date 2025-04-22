import datetime
from typing import Self, Any, Literal

from pydantic import BaseModel, Field, model_validator

from helpers.icd.v11.columns import Column
from helpers.icd.v11.confuse import anti_confuse


class BrowseGt(BaseModel):
    res: str
    token: str | None = Field(default=None)

    @model_validator(mode="after")
    def anti_confuse_find_token(self):
        self.token = anti_confuse(self.res)
        return self


class Reference(BaseModel):
    title: str | None = Field(default=None)
    reference_url: str | None = Field(default=None)


class ClassKind(BaseModel):
    url: str | None = Field(default=None)
    class_kind: Literal["category"] | None = Field(default=None)

    @classmethod
    def model_validate_source(cls, data: Any, *args, **kwargs) -> Self:
        clean_data = {}
        if isinstance(data, dict):
            Column.has_id_url(data, clean_data)
            Column.has_class_kind(data, clean_data)
            if clean_data["class_kind"] in {"category"}:
                return Category.model_validate_source(data, *args, **kwargs)
            if clean_data["class_kind"] in {"window"}:
                return Window.model_validate_source(data, *args, **kwargs)
            if clean_data["class_kind"] in {"block"}:
                return Block.model_validate_source(data, *args, **kwargs)
            if clean_data["class_kind"] in {"chapter"}:
                return Chapter.model_validate_source(data, *args, **kwargs)


class Base(BaseModel):
    url: str | None = Field(default=None)
    title: str | None = Field(default=None)
    code: str | None = Field(default=None)
    fully_specified_name: str | None = Field(default=None)
    child: list[ClassKind | Any] = Field(default=None)
    description: str | None = Field(default=None)
    inclusion: list[str] | None = Field(default=None)
    exclusions: list[str] | None = Field(default=None)
    all_index_terms: list[str] | None = Field(default=None)
    related_entities_in_perinatal_chapter: list[str] | None = Field(default=None)
    coded_elsewhere: list[Reference] | None = Field(default=None)
    browser_url: str | None = Field(default=None)

    @classmethod
    def model_validate_source(cls, data: Any, *args, **kwargs) -> Self:
        clean_data = {}
        if isinstance(data, dict):
            Column.has_class_kind(data, clean_data)
            Column.has_id_url(data, clean_data)
            Column.has_title(data, clean_data)
            Column.has_code(data, clean_data)
            Column.has_fully_specified_name(data, clean_data)
            Column.has_child(data, clean_data)
            Column.has_description(data, clean_data)
            Column.has_inclusion(data, clean_data)
            Column.has_exclusions(data, clean_data)
            Column.has_all_index_terms(data, clean_data)
            Column.has_related_entities_in_perinatal_chapter(data, clean_data)
            Column.has_coded_elsewhere(data, clean_data)
            Column.has_browser_url(data, clean_data)
        return super().model_validate(clean_data, *args, **kwargs)


class Category(Base):
    class_kind: Literal["category"] | None = Field(default=None)


class Window(Base):
    class_kind: Literal["window"] | None = Field(default=None)


class Block(Base):
    class_kind: Literal["block"] | None = Field(default=None)


class Chapter(Base):
    class_kind: Literal["chapter"] | None = Field(default=None)


class Root(BaseModel):
    title: str | None = Field(default=None)
    language: str | None = Field(default=None)
    release_date: datetime.date | None = Field(default=None)
    browser_url: str | None = Field(default=None)
    child: list[ClassKind | Any] = Field(default_factory=list)

    @classmethod
    def model_validate_source(cls, data: Any, *args, **kwargs) -> Self:
        clean_data = {}
        if isinstance(data, dict):
            Column.has_id_url(data, clean_data)
            Column.has_title(data, clean_data)
            clean_data["language"] = data["title"]["@language"]
            clean_data["release_date"] = data["releaseDate"]
            Column.has_browser_url(data, clean_data)
            Column.has_child(data, clean_data)
        return super().model_validate(clean_data, *args, **kwargs)
