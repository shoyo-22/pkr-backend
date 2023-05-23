from pydantic import BaseModel

class BaseTournament(BaseModel):
    name: str
    logo: str
    datetime: str
    location: str
    league: str
    fraction: str
    status: str
    judge: str
    link: str


class CreateTournament(BaseTournament):
    pass


class Tournament(BaseTournament):
    id: str

    class Config:
        orm_mode = True
