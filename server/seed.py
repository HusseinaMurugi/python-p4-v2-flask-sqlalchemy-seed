#!/usr/bin/env python3
# server/seed.py

from app import app
from models import db, Pet
from faker import Faker
from random import choice

with app.app_context():
    fake = Faker()

    # Delete all existing rows in the pets table
    Pet.query.delete()

    # Create an empty list
    pets = []

    # Species list
    species_list = ["Dog", "Cat", "Hamster", "Turtle", "Snake"]

    # Add some sample pets
    pets.append(Pet(name="Fido", species="Dog"))
    pets.append(Pet(name="Whiskers", species="Cat"))
    pets.append(Pet(name="Hermie", species="Hamster"))
    pets.append(Pet(name="Slither", species="Snake"))

    # Add 6 random pets using Faker
    for _ in range(6):
        pets.append(Pet(name=fake.first_name(), species=choice(species_list)))

    # Insert all pets into the database
    db.session.add_all(pets)

    # Commit the transaction
    db.session.commit()

    print("Pets table seeded successfully!")
