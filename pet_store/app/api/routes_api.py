from fastapi import APIRouter, HTTPException
from app.schemas.pydantic_models import PetCreate, PetUpdate
from app.crud.sql_crud import create_pet, get_pets, update_pet, delete_pet

router = APIRouter(prefix="/pets", tags=["Pets"])

## Link to add data into database
@router.post("/")
def add_pet(pet: PetCreate):
    pet_id = create_pet(pet)
    return {"id": pet_id, "message": "Pet created"}

## Link to get data from database
@router.get("/")
def list_pets():
    return get_pets()

## Link to update data from database
@router.put("/{pet_id}")
def edit_pet(pet_id: int, pet: PetUpdate):
    updated = update_pet(pet_id, pet)
    if not updated:
        raise HTTPException(status_code=404, detail="Pet not found")
    return {"message": "Pet updated"}

## Link to delete data from database
@router.delete("/{pet_id}")
def remove_pet(pet_id: int):
    deleted = delete_pet(pet_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Pet not found")
    return {"message": "Pet deleted"}
