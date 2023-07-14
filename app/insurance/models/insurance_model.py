from tortoise.models import Model
from tortoise.fields import (
    IntField,
    TextField,
)


class InsuranceModel(Model):
    id = IntField(pk=True)
    date = TextField()
    cargo_type = TextField()
    rate = TextField()

    class Meta:
        table = 'insurance'

    def __str__(self) -> str:
        return self.cargo_type
