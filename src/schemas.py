from pydantic import BaseModel

class BaseTournament(BaseModel):
    name: str
    image: str
    time: str
    location: str
    league: str
    phone_number: str
    main_referee: str
    level: str
    language: str
    link: str
    format: str
    fraction: str
    referee: str


class TournamentCreate(BaseTournament):
    pass


class TournamentResponse(BaseTournament):
    id: int
