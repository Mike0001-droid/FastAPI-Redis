from typing import Any
from pydantic import BaseModel, Field, field_validator
from pydantic_extra_types.phone_numbers import PhoneNumber


class PhoneModel(BaseModel):
    phone: PhoneNumber = Field(
        ...,
        description="Номер телефона",
        examples=["+79991234567", "+442071838750"]
    )
    """ 
        Костыль, чтобы записывалось значение 
        без префикса tel: (особенность библиотеки) 
    """
    @field_validator('phone', mode='after')
    @classmethod
    def remove_tel_prefix(cls, v: Any) -> Any:
        if isinstance(v, str):
            if v.startswith('tel:'):
                v = v[4:]
        return v
