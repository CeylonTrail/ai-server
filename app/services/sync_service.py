from app.services.database_service import fetch_places
from app.services.pinecone_service import get_all_place_ids, add_place, remove_place

def sync_places():
    db_place_ids = []
    new_places = []
    removed_places = []

    pinecone_place_ids = get_all_place_ids()
    places_in_db = fetch_places()
    for place in places_in_db:
        db_place_ids.append(place['place_id'])

    # Add new places to Pinecone
    for place in places_in_db:
        if place['place_id'] not in pinecone_place_ids:
            add_place(place['place_id'], place['description'])
            new_places.append(place['place_id'])

    # Remove places from Pinecone that are not in DB
    for place_id in pinecone_place_ids:
        if place_id not in db_place_ids:
            remove_place(place_id)
            removed_places.append(place_id)

    return {
        "new_places": new_places,
        "removed_places": removed_places
    }
