from app.db.database import get_db

## To create data and store in database.
def create_pet(pet):
    db = get_db() # *It is a custom function which tells the detail about the database
    cursor = db.cursor() #*.cursor() creates a cursor object. We cannot directly run SQL command on the connection
    cursor.execute(
        "INSERT INTO pets (name, species, age) VALUES (?, ?, ?)",
        (pet.name, pet.species, pet.age)
    )
    db.commit()
    return cursor.lastrowid

## To retrive all the data from the database
def get_pets():
    db = get_db()
    cursor = db.cursor()
    rows = cursor.execute("SELECT * FROM pets").fetchall()
    return [dict(row) for row in rows]

## To update the data in the database
def update_pet(pet_id, pet):
    db = get_db()
    cursor = db.cursor()

    fields = []
    values = []

    for key, value in pet.model_dump(exclude_unset=True).items(): # * exclude_unset : only include fields that the user actually provided
        fields.append(f"{key} = ?")  # ? is a parameter placeholde
        values.append(value)

    if not fields:
        return None

    values.append(pet_id)

    cursor.execute(
        f"UPDATE pets SET {', '.join(fields)} WHERE id = ?",
        values
    )

    db.commit()
    return cursor.rowcount

## For deleting the data from database
def delete_pet(pet_id):
    db = get_db()
    cursor = db.cursor()
    cursor.execute("DELETE FROM pets WHERE id = ?", (pet_id,))
    db.commit()
    return cursor.rowcount
