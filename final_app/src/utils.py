import uuid, datetime


def generate_id():
return str(uuid.uuid4())


def current_time():
return datetime.datetime.now().isoformat()
