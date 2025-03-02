import queue
import threading
from app.utils.utils import process_order

order_queue = queue.Queue()

def start_worker():
    worker_thread = threading.Thread(target=process_order, args=(order_queue,))
    print("Starting worker thread")
    worker_thread.start()