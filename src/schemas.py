from pydantic import BaseModel


class BaseTournament(BaseModel):
    name: str
    image: str
    start_date: str
    end_date: str
    location: str
    city: str
    league: str
    phone_number: str
    main_referee: str
    level: str
    language: str
    link: str
    sponsor_link: str
    format: str
    fraction: str
    referee: str
    prize_pool: int
    volume: float


class TournamentCreate(BaseTournament):
    pass


class TournamentResponse(BaseTournament):
    id: int
