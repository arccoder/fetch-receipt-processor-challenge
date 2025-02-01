from typing import Annotated
from datetime import datetime
from pydantic import BaseModel, Field
from pydantic.functional_validators import AfterValidator


def validateDate(value: str) -> str:
    """Date format validator"""
    try:
        out = datetime.strptime(value, "%Y-%m-%d")
    except ValueError as e:
        raise e
    return out.date()


dateYYYYmmdd = Annotated[str, AfterValidator(validateDate)]


def validateTime(value: str) -> str:
    """Time format validator"""
    try:
        out = datetime.strptime(value, "%H:%M")
    except ValueError as e:
        raise e
    return out.time()


timeHHMM = Annotated[str, AfterValidator(validateTime)]


class Item(BaseModel):
    """Items in the receipt"""

    shortDescription: str = Field(
        ...,
        description="The Short Product Description for the item.",
        pattern=r"^[\w\s\-]+$",
    )
    price: str = Field(
        ...,
        description="The total price payed for this item.",
        pattern=r"^\d+\.\d{2}$",
    )


class Receipt(BaseModel):
    """Receipt"""

    retailer: str = Field(
        ...,
        description="The name of the retailer or store the receipt is from.",
        pattern=r"^[\w\s\&-]+$",
    )
    purchaseDate: dateYYYYmmdd = Field(
        ..., description="The date of the purchase printed on the receipt."
    )
    purchaseTime: timeHHMM = Field(
        ...,
        description="The time of the purchase printed on the receipt. 24-hour time expected.",
    )
    items: list[Item]
    total: str = Field(
        ...,
        description="The total amount paid on the receipt.",
        pattern=r"^\d+\.\d{2}$",
    )
