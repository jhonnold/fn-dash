from flask import Blueprint, render_template, redirect, url_for
from app.models import User, Game
from app.util import kd_per_day, games_per_day, kd_progression, todays_kd, todays_kills, todays_wins, todays_matches

dashboard = Blueprint('dashboard', __name__)


@dashboard.route('/')
def home():
    user = User.query.order_by(User.id.asc()).first()
    return redirect(url_for('dashboard.user_stats', user_id=user.id))


@dashboard.route('/users/<user_id>/obs.html')
def obs_overlay(user_id):
    user = User.query.filter_by(id=user_id).first()
    user_data = dict(**user.__dict__)
    if '_sa_instance_state' in user_data:
        del user_data['_sa_instance_state']

    user_data['kd_total'] = "{0:0.3f}".format(user.kd_total())

    user_data['todays_kd'] = "{0:0.3f}".format(todays_kd(user))
    user_data['todays_matches'] = todays_matches(user)
    user_data['todays_kills'] = todays_kills(user)
    user_data['todays_wins'] = todays_wins(user)

    return render_template('obs.html', **user_data)


@dashboard.route('/users/<user_id>')
def user_stats(user_id):
    users = User.query.all()
    selected_user = None

    for user in users:
        if (user.id == int(user_id)):
            selected_user = user
            break

    selected_user_data = dict(**selected_user.__dict__)
    if '_sa_instance_state' in selected_user_data:
        del selected_user_data['_sa_instance_state']

    selected_user_data['games'] = selected_user.games.order_by(
        Game.time_played.desc()).limit(100).all()

    selected_user_data['solo_games'] = selected_user.games.filter_by(
        game_type='Solo').order_by(Game.time_played.desc()).limit(100).all()

    selected_user_data['duo_games'] = selected_user.games.filter_by(
        game_type='Duo').order_by(Game.time_played.desc()).limit(100).all()

    selected_user_data['squad_games'] = selected_user.games.filter_by(
        game_type='Squad').order_by(Game.time_played.desc()).limit(100).all()

    selected_user_data['record_games'] = [
        selected_user.games.filter_by(game_type='Solo').order_by(
            Game.kills.desc()).first(),
        selected_user.games.filter_by(game_type='Duo').order_by(
            Game.kills.desc()).first(),
        selected_user.games.filter_by(game_type='Squad').order_by(
            Game.kills.desc()).first(),
    ]

    selected_user_data['kd_total'] = "{0:0.3f}".format(
        selected_user.kd_total())
    selected_user_data['kd_solo'] = "{0:0.3f}".format(selected_user.kd_solo())
    selected_user_data['kd_duo'] = "{0:0.3f}".format(selected_user.kd_duo())
    selected_user_data['kd_squad'] = "{0:0.3f}".format(
        selected_user.kd_squad())

    selected_user_data['placements_solo'] = selected_user.placements_solo()
    selected_user_data['placements_duo'] = selected_user.placements_duo()
    selected_user_data['placements_squad'] = selected_user.placements_squad()

    selected_user_data['labels_kd_total'], selected_user_data[
        'kd_per_day_total'] = kd_per_day(
            selected_user, adjust=-5)
    selected_user_data['labels_kd_solo'], selected_user_data[
        'kd_per_day_solo'] = kd_per_day(selected_user, 'Solo', -5)
    selected_user_data['labels_kd_duo'], selected_user_data[
        'kd_per_day_duo'] = kd_per_day(selected_user, 'Duo', -5)
    selected_user_data['labels_kd_squad'], selected_user_data[
        'kd_per_day_squad'] = kd_per_day(selected_user, 'Squad', -5)

    selected_user_data['labels_games_total'], selected_user_data[
        'games_per_day_total'] = games_per_day(
            selected_user, adjust=-5)
    selected_user_data['labels_games_solo'], selected_user_data[
        'games_per_day_solo'] = games_per_day(selected_user, 'Solo', -5)
    selected_user_data['labels_games_duo'], selected_user_data[
        'games_per_day_duo'] = games_per_day(selected_user, 'Duo', -5)
    selected_user_data['labels_games_squad'], selected_user_data[
        'games_per_day_squad'] = games_per_day(selected_user, 'Squad', -5)

    kd_tracker_total, kd_tracker_solo, kd_tracker_duo, kd_tracker_squad = kd_progression(
        selected_user)

    selected_user_data['kd_tracker_total'] = kd_tracker_total
    selected_user_data['kd_tracker_solo'] = kd_tracker_solo
    selected_user_data['kd_tracker_duo'] = kd_tracker_duo
    selected_user_data['kd_tracker_squad'] = kd_tracker_squad

    return render_template('layout.html', users=users, **selected_user_data)
