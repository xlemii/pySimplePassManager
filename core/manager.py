from core.models import PasswordEntry


class PasswordManager:
    def __init__(self):
        self.entries = []

    def add_entry(self, service, login, password):
        entry = PasswordEntry(service, login, password)
        self.entries.append(entry)

    def get_entries(self):
        return self.entries