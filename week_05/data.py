from ex_05_client_for_metrics import Client
from ex_05_client_for_metrics import ClientError
client = Client("127.0.0.1", 8888, timeout=15)
client.get("*")
