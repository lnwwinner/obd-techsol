# Universal Resource Manager
# Manage all reusable files (models, logs, datasets, configs, etc.)

import os
import shutil
from datetime import datetime


class ResourceManager:

    def __init__(self, base_path="resources"):
        self.base_path = base_path

    def _get_paths(self, domain, category):
        base = os.path.join(self.base_path, domain, category)
        active = os.path.join(base, "active")
        archive = os.path.join(base, "archive")

        os.makedirs(active, exist_ok=True)
        os.makedirs(archive, exist_ok=True)

        return active, archive

    def save_resource(self, file_path, domain, category, name):
        active_path, archive_path = self._get_paths(domain, category)

        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{name}_{timestamp}{os.path.splitext(file_path)[1]}"

        archive_file = os.path.join(archive_path, filename)
        shutil.copy(file_path, archive_file)

        active_file = os.path.join(active_path, f"{name}_latest{os.path.splitext(file_path)[1]}")
        shutil.copy(file_path, active_file)

        print(f"[ARCHIVED] {archive_file}")
        print(f"[ACTIVE UPDATED] {active_file}")

    def list_resources(self, domain, category):
        _, archive_path = self._get_paths(domain, category)
        return os.listdir(archive_path)
