import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


@anvil.server.callable
def get_course_details(course_name):
  return app_tables.courses.get(id_name=course_name)

@anvil.server.callable
def get_all_courses():
  return app_tables.courses.client_readable()

