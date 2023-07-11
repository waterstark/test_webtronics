from pydantic import BaseModel, StrictStr
from typing import Optional


class Post(BaseModel):
    id: int
    title: StrictStr

    class Config:
        orm_mode = True


class ReadAllPosts(BaseModel):
    data: list[Post]

    class Config:
        orm_mode = True


class CreatePost(BaseModel):
    data: Post

    class Config:
        orm_mode = True


class EditPost(BaseModel):
    title: Optional[StrictStr] | None

    class Config:
        orm_mode = True


class LikePost(BaseModel):
    like_or_dislike: int

    class Config:
        orm_mode = True
