from __future__ import annotations
from typing import Any, Dict, List, Literal, Optional, Union
from pydantic import BaseModel, Field


Version = Union[int, str, Literal["latest"]]


class Query(BaseModel):
    """Query represents a model for handling query-related operations such as filtering, sorting,
    and field selection. It also includes methods for advanced data manipulation like drill-down,
    pivot, and slice operations.
    """

    fields: List[str] = Field(alias="q")
    aggregated: Optional[str] = None
    filter: Optional[Dict[str, Any]] = Field(default=None, alias="f")


class RubikCube(BaseModel):
    """Represents a RubikCube object which models a collection of metadata tables, fields, and
    relations. It provides methods to manage SQL dialects, retrieve metadata information, and perform
    graph-based operations.

    The RubikCube class supports hierarchical structures by allowing the creation of child cubes
    that inherit properties from a parent cube.
    """

    parent: Optional[RubikCube] = None
    version: Version = "latest"
    tables: Optional[List[MetaTable]] = None
    fields: Optional[List[MetaField]] = None
    relations: Optional[List[MetaRelation]] = None


class MetaTable(BaseModel): ...


class MetaField(BaseModel): ...


class MetaRelation(BaseModel): ...
