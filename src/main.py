from flask import Flask, request, render_template, redirect, url_for
from repositories.user_repository import UserRepository
from repositories.room_repository import RoomRepository
from repositories.reservation_repository import ReservationRepository
from services.reservation_service import ReservationService
from datetime import datetime

app = Flask(__name__)

reservation_repo = ReservationRepository()
user_repo = UserRepository(reservation_repo)
room_repo = RoomRepository(reservation_repo)


reservation_service = ReservationService(reservation_repo, room_repo)

@app.route('/')
def home():
    return render_template('index.html')

# --- USERS CRUD ---
@app.route('/users')
def list_users():
    users = user_repo.list()
    return render_template('users.html', users=users)

@app.route('/users/new', methods=['GET', 'POST'])
def create_user():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        user_repo.create(name, email)
        return redirect(url_for('list_users'))
    return render_template('create_user.html')

@app.route('/users/edit/<int:user_id>', methods=['GET', 'POST'])
def edit_user(user_id):
    user = user_repo.get_by_id(user_id)
    if not user:
        return "User not found", 404
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        user_repo.update(user_id, {'name': name, 'email': email})
        return redirect(url_for('list_users'))
    return render_template('edit_user.html', user=user)

@app.route('/users/delete/<int:user_id>', methods=['POST'])
def delete_user(user_id):
    user_repo.delete(user_id)
    return redirect(url_for('list_users'))

# --- ROOMS CRUD ---
@app.route('/rooms')
def list_rooms():
    rooms = room_repo.list()
    return render_template('rooms.html', rooms=rooms)

@app.route('/rooms/new', methods=['GET', 'POST'])
def create_room():
    if request.method == 'POST':
        name = request.form['name']
        capacity = int(request.form['capacity'])
        room_repo.create(name, capacity)
        return redirect(url_for('list_rooms'))
    return render_template('create_room.html')

@app.route('/rooms/edit/<int:room_id>', methods=['GET', 'POST'])
def edit_room(room_id):
    room = room_repo.get_by_id(room_id)
    if not room:
        return "Room not found", 404
    if request.method == 'POST':
        name = request.form['name']
        capacity = int(request.form['capacity'])
        room_repo.update(room_id, {'name': name, 'capacity': capacity})
        return redirect(url_for('list_rooms'))
    return render_template('edit_room.html', room=room)

@app.route('/rooms/delete/<int:room_id>', methods=['POST'])
def delete_room(room_id):
    room_repo.delete(room_id)
    return redirect(url_for('list_rooms'))

# --- RESERVATIONS ---
@app.route('/reservations')
def list_reservations():
    user_id = request.args.get('user_id', type=int)
    room_id = request.args.get('room_id', type=int)
    reservations = reservation_repo.list()

    if user_id:
        reservations = [r for r in reservations if r.user_id == user_id]
    if room_id:
        reservations = [r for r in reservations if r.room_id == room_id]

    enriched_reservations = []
    for r in reservations:
        user = user_repo.get_by_id(r.user_id)
        room = room_repo.get_by_id(r.room_id)
        enriched_reservations.append({
            'id': r.id,
            'user_name': user.name if user else 'Unknown User',
            'room_name': room.name if room else 'Unknown Room',
            'start_time': r.start_time,
            'end_time': r.end_time,
        })
    users = user_repo.list()
    rooms = room_repo.list()
    return render_template('reservations.html', reservations=enriched_reservations, users=users, rooms=rooms, selected_user=user_id, selected_room=room_id)

@app.route('/reservations/new', methods=['GET', 'POST'])
def create_reservation():
    error = None
    users = user_repo.list()
    rooms = room_repo.list()
    if request.method == 'POST':
        try:
            user_id = int(request.form['user_id'])
            room_id = int(request.form['room_id'])
            start_time = datetime.strptime(request.form['start_time'], '%Y-%m-%dT%H:%M')
            end_time = datetime.strptime(request.form['end_time'], '%Y-%m-%dT%H:%M')
            reservation_service.create_reservation(user_id, room_id, start_time, end_time)
            return redirect(url_for('list_reservations'))
        except Exception as e:
            error = str(e)
    return render_template('create_reservation.html', users=users, rooms=rooms, error=error)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
