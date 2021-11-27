import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


@anvil.server.callable
def get_my_courses():
  user = anvil.users.get_user()
  if user == None:
    return []
  
  if not user["purchased_courses"]:
    return []
  
  courses = []
  for course in user["purchased_courses"]:
    course_info = app_tables.courses.get(id_name=course)
    courses.append(course_info)
  
  return courses

