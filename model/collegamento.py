from dataclasses import dataclass


@dataclass
class Collegamento:
    id_filiale_1: int
    id_filiale_2: int
    somma_importi: float
    num_bonifici: int

    @property
    def valore(self):
        return self.somma_importi / self.num_bonifici

    def __str__(self):
        return f"{self.id_filiale_1} - {self.id_filiale_2}: {self.valore:.2f}"
