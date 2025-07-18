from patterns.base_repository import BaseRepository
from models.reservation import Reservation

class ReservationRepository(BaseRepository):
    def create(self, user_id, room_id, start_time, end_time):
        reservation = Reservation(
            id=None,
            user_id=user_id,
            room_id=room_id,
            start_time=start_time,
            end_time=end_time
        )
        return super().create(reservation)

    def delete_by_user(self, user_id):
        to_delete = [r for r in self._entities if r.user_id == user_id]
        for r in to_delete:
            self._entities.remove(r)
        self._save()

    def delete_by_room(self, room_id):
        to_delete = [r for r in self._entities if r.room_id == room_id]
        for r in to_delete:
            self._entities.remove(r)
        self._save()

    def find_by_room(self, room_id):
        return [r for r in self._entities if r.room_id == room_id]

    def find_by_user(self, user_id):
        return [r for r in self._entities if r.user_id == user_id]
