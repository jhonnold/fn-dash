from app import app
from celery import Task


class AppContextBase(Task):
    """Base class for tasks that run inside a Flask request context."""
    abstract = True

    def __call__(self, *args, **kwargs):
        with app.app_context():
            return super(AppContextBase, self).__call__(*args, **kwargs)


from .stat_history import record_stats
from .stat_tracker import find_changed_stats, fortnite_api_lookup, update_hash, update_stats