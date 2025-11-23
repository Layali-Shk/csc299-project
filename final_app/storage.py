import os, json
class JSONStorage:
    def __init__(self, data_dir):
        self.data_dir = data_dir
        os.makedirs(self.data_dir, exist_ok=True)
    def _path(self, name):
        return os.path.join(self.data_dir, name + '.json')
    def load(self, name):
        p = self._path(name)
        if not os.path.exists(p):
            return []
        with open(p) as f:
            return json.load(f)
    def save(self, name, data):
        p = self._path(name)
        with open(p, 'w') as f:
            json.dump(data, f, indent=2)
