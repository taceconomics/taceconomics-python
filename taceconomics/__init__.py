
import os

api_key = os.environ.get("TACECONOMICS_API_KEY")
proxy = os.environ.get("TACECONOMICS_PROXY")

from .get import get
from .get import getdata

