from pydantic import BaseModel, RootModel
from typing import List, Dict


class Cargo(BaseModel):
    cargo_type: str = 'Glass'
    rate: str = '0.04'


class InsuranceCreate(RootModel):
    root: Dict[str, List[Cargo]]

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]
