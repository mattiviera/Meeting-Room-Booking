class BaseRepository:
    def __init__(self):
        self._entities = []
        self._next_id = 1

    def list(self):
        return self._entities

    def get_by_id(self, entity_id):
        for entity in self._entities:
            if entity.id == entity_id:
                return entity
        return None

    def create(self, entity):
        entity.id = self._next_id
        self._next_id += 1
        self._entities.append(entity)
        return entity

    def update(self, entity_id, data: dict):
        entity = self.get_by_id(entity_id)
        if entity:
            for key, value in data.items():
                setattr(entity, key, value)
            self._save()
            return entity
        return None

    def delete(self, entity_id):
        entity = self.get_by_id(entity_id)
        if entity:
            self._entities.remove(entity)
            self._save()
            return True
        return False

    def _save(self):
        # Método dummy o override en repositorios que usan persistencia real
        pass
