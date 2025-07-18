from patterns.base_repository import BaseRepository
from models.user import User

class UserRepository(BaseRepository):
    def __init__(self, reservation_repo):
        super().__init__()
        self.reservation_repo = reservation_repo

    def create(self, name, email):
        user = User(id=None, name=name, email=email)
        return super().create(user)

    def delete(self, user_id):
        # Borra también las reservas relacionadas para mantener consistencia
        self.reservation_repo.delete_by_user(user_id)
        return super().delete(user_id)
