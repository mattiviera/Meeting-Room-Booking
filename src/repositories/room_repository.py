from patterns.base_repository import BaseRepository
from models.room import Room

class RoomRepository(BaseRepository):
    def __init__(self, reservation_repo):
        super().__init__()
        self.reservation_repo = reservation_repo

    def create(self, name, capacity):
        room = Room(id=None, name=name, capacity=capacity)
        return super().create(room)

    def delete(self, room_id):
        # Borra también las reservas relacionadas para mantener consistencia
        self.reservation_repo.delete_by_room(room_id)
        return super().delete(room_id)
