from enum import Enum, unique


@unique
class Status(Enum):
    ONPROSES = '0'
    DITANGANI = '1'
    SELESAI = '2'
