from doctest import Example
from typing import List, Set, Union, Dict
from unittest import result
#from unittest import result

from fastapi import Body, FastAPI, Path
from pydantic import BaseModel, HttpUrl, Field

app = FastAPI()

# 경로 작업 함수 매개변수에서 추가 유효성 검사 및 메타데이터를 선언할 수 있는것과 동일한 방식의 pydantic의 query path body field
class Image(BaseModel):
    url: HttpUrl
    name: str

class Item(BaseModel):
    name: str
    description: Union[str, None] = None
    price: float
    tax: Union[float, None] = None
    
# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None
#     tags: Set[str] = set()
#     images: Union[Image, None] = None

# class Item(BaseModel):
#     name: str = Field(example="Foo")
#     description: Union[str, None] = Field(default=None, example="A very nice Item")
#     price: float = Field(example=35.4)
#     tax: Union[float, None] = Field(default=None, example=3.2)

# class Offer(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     items: List[Item]

# class User(BaseModel):
#     username: str
#     full_name: Union[str, None] = None

@app.put("/items/{item_id}")
async def update_item(
    *,
    item_id: int,
    item: Item = Body(
        examples={
            "normal": {
                "summary": "A normal example",
                "description": "A **normal** item works correctly.",
                "value": {
                    "name": "Foo",
                    "description": "A very nice Item",
                    "price": 35.4,
                    "tax": 3.2,
                },
            },
            "converted": {
                "summary": "An example with converted data",
                "description": "FastAPI can convert price `strings` to actual `numbers` automatically",
                "value": {
                    "name": "Bar",
                    "price": "35.4",
                },
            },
            "invalid": {
                "summary": "Invalid data is rejected with an error",
                "value": {
                    "name": "Baz",
                    "price": "thirty five point four",
                },
            },
        },
    ),
):
    results = {"item_id": item_id, "item": item}
    return results

# @app.put("/items/{item_id}")
# async def update_item(
#     *,
#     item_id: int = Path(title="The ID of the item to get", ge=0, le=1000),
#     q: Union[str, None] = None,
#     item: Union[Item, None] = None,
# ):
#     results = {"item_id": item_id}
#     if q:
#         results.update({"q": q})
#     if item:
#         results.update({"item": item})
#     return results


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item, user: User):
#     results = {"item_id": item_id, "item":item, "user": user}
#     return results

# 본문의 특이값, 이전 모델을 확장하여 동일한 본문에 importance외에 다른 키를 갖고자 할 수 있다. item user
# 다음을 사용하여 다른 본문 키로 처리 하도록 FastAPI Body 에 지시할 수 있다.

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item, user: User, importance: int = Body(gt=0), q: Union[str, None] = None):
#     results = {"item_id": item_id, "item":item, "user": user, "importance": importance}
#     if q:
#         results.update({"q":q})
#     return results

# 단일 본문 매개변수 포함
# item 추가 본문 매개변수를 선언할 때 키와 그 내부에 모델 콘텐츠가 있는 JSON을 예상하려면 특수 Body 매개변수를 사용할 수 있습니다. embed

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item = Body(embed=True)):
#     results = {"item_id": item_id, "item": item}
#     return results

# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: Item):
#     results = {"item_id": item_id, "item": item}
#     return results

# @app.post("/images/multiple")
# async def create_multiple_images(images: List[Image]):
#     return images

# @app.post("/index-weights/")
# async def create_index_weights(weights: Dict[int, float]):
#     return weights

# pydantic "schema_extra"
# class Item(BaseModel):
#     name: str
#     description: Union[str, None] = None
#     price: float
#     tax: Union[float, None] = None

# @app.put("/items/{item_id}")
# async def update_item(
#     item_id: int,
#     item: Item = Body(
#         example={
#             "name": "Foo",
#             "description": "A very nice Item",
#             "price": 35.4,
#             "tax": 3.2,
#         },
#     ),
# ):
#     results = {"item_id": item_id, "item": item}
#     return results


# @app.put("/items/{item_id}")
# async def update_item(item_id: int, item: int):
#     results = {"item_id": item_id, "item": item}
#     return results