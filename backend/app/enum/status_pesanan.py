# definisi status pesanan enum
from enum import Enum

class StatusPesananEnum(str, Enum):
    pending = "pending"
    dibayar = "dibayar"
    dikirim = "dikirim"
    selesai = "selesai"
    dibatalkan = "dibatalkan"
