class ReservationService:
    def __init__(self, reservation_repo, room_repo):
        self.reservation_repo = reservation_repo
        self.room_repo = room_repo

    def create_reservation(self, user_id, room_id, start_time, end_time):
        for r in self.reservation_repo.find_by_room(room_id):
            if not (end_time <= r.start_time or start_time >= r.end_time):
                raise Exception("Conflicto de horarios con otra reserva.")
        self.reservation_repo.create(user_id, room_id, start_time, end_time)
