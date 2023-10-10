from fastapi import Depends, status, HTTPException, Response, APIRouter
from sqlalchemy.orm import Session
from typing import List
from .. import models, schemas
from ..database import get_db

router = APIRouter(prefix='/tournaments', tags=['Tournaments'])

@router.get('/', response_model=List[schemas.TournamentResponse])
def get_tournaments(db: Session = Depends(get_db)):
    tournaments = db.query(models.Tournament).all()
    return tournaments

@router.get('/{id}')
def get_tournament(id: int, db: Session = Depends(get_db)):
    post = db.query(models.Tournament).filter(models.Tournament.id == id).first()

    if not post:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Tournament with id: {id} was not found'
        )
    return post

@router.post('/', status_code=status.HTTP_201_CREATED, response_model=schemas.TournamentResponse)
def create_tournament(tournament: schemas.TournamentCreate, db: Session = Depends(get_db)):
    new_tournament = models.Tournament(**tournament.dict())
    db.add(new_tournament)
    db.commit()
    db.refresh(new_tournament)
    return new_tournament

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def delete_tournament(id: int, db: Session = Depends(get_db)):
    tournament = db.query(models.Tournament).filter(models.Tournament.id == id)

    if tournament.first() == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Tournament with id: {id} does not exist'
        )
    tournament.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

@router.put('/{id}', response_model=schemas.TournamentResponse)
def update_tournament(id: int, updated_tournament: schemas.TournamentCreate, db: Session = Depends(get_db)):
    tournament_query = db.query(models.Tournament).filter(models.Tournament.id == id)
    tournament = tournament_query.first()

    if tournament == None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f'Tournament with id: {id} does not exist'
        )
    tournament_query.update(updated_tournament.dict(), synchronize_session=False)
    db.commit()
    return tournament_query.first()
