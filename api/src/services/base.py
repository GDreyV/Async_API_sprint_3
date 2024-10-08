from abc import ABC
from typing import Any, Literal, cast
from uuid import UUID

from elasticsearch import AsyncElasticsearch, NotFoundError
from opentelemetry import trace

INDICES = Literal["movies", "persons", "genres"]

tracer = trace.get_tracer(__name__)


class ServiceABC(ABC):
    def __init__(self, elastic: AsyncElasticsearch):
        self.elastic = elastic

    async def _get_from_elastic(self, index: INDICES, id: UUID) -> dict | None:
        try:
            data = await self.elastic.get(index=index, id=str(id))
            source: dict = cast(dict, data)["_source"]
            return source
        except NotFoundError:
            return None

    async def _get_all_from_elastic(self, index: INDICES, ids: list[UUID]) -> list[dict]:
        data = await self.elastic.mget({"ids": [str(id) for id in ids]}, index=str(index))  # type: ignore
        return [doc["_source"] for doc in cast(dict, data)["docs"]]

    async def _query_from_elastic(
        self, index: INDICES, query: dict, size: int = 1000, skip: int = 0, sort: dict[str, int] | None = None
    ) -> list[Any]:
        body = {"query": query, "size": size, "from": skip}
        if sort:
            body["sort"] = {key: {"order": "asc" if value > 0 else "desc"} for (key, value) in sort.items()}
        with tracer.start_as_current_span("elasticsearch-request"):
            data = await self.elastic.search(index=index, body=body)
            docs = cast(dict, data)["hits"]["hits"]
            return [doc["_source"] for doc in docs]
