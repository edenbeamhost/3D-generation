import time
import random
from typing import List

from app.models import Order


def brew_coffee():
    # Simulate brewing time between 30-60 seconds
    time.sleep(random.randint(30, 60))
