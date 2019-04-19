from flask import Blueprint
modules = Blueprint('modules', __name__)

from .company import *
from .manufacturer import *
from .user import *

