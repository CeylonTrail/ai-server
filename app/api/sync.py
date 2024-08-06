from fastapi import APIRouter, HTTPException
from app.services.sync_service import sync_places

router = APIRouter()

@router.post("/")
async def sync_request():
    try:
        response = sync_places()
        return {
            "message": "Synchronization complete.",
            "new_places_added": len(response['new_places']),
            "places_removed": len(response['removed_places']),
            "new_place_ids": response['new_places'],
            "removed_place_ids": response['removed_places']
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
