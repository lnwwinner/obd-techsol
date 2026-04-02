from datetime import datetime, timedelta

class PasswordPolicy:

    def __init__(self):
        # user_id -> last password change
        self.password_history = {}
        self.expire_days = 90

    def set_password_changed(self, user_id):
        self.password_history[user_id] = datetime.utcnow()

    def is_expired(self, user_id):
        last_change = self.password_history.get(user_id)

        if not last_change:
            return True

        if datetime.utcnow() - last_change > timedelta(days=self.expire_days):
            return True

        return False

    def check_and_notify(self, user_id, notifier):
        if self.is_expired(user_id):
            notifier.send_alert(user_id, {
                "event": "PASSWORD_EXPIRED",
                "message": "Please change your password (90 days policy)",
                "severity": "WARNING"
            })

            return True

        return False
