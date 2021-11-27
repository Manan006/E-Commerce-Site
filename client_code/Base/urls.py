import anvil.server
import stripe.checkout
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Home import Home
from ..Courses import Courses
from ..MyCourses import MyCourses

urls = {"home": Home, "courses": Courses, "my-courses": MyCourses}
