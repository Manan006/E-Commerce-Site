import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.stripe
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


@anvil.server.callable
def get_course_details(course_name):
  return app_tables.courses.get(id_name=course_name)

# insert new course into database
def insert_course(course_name, course_description, course_price, course_id_name, course_image, course_created):
  app_tables.courses.add_row(id_name=course_id_name, description=course_description, price=course_price, name=course_name, image=course_image,created=course_created)
  
@anvil.server.callable
def get_all_courses():
  from datetime import datetime
  now = datetime.now()
  insert_course(course_name="Javascript", course_description="Learn JavaScript and become a pro!", course_price=37.99, course_id_name='javascript',course_image=f"https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Fwww.britefish.net%2Fwp-content%2Fuploads%2F2019%2F06%2Flogo-javascript-2.png&f=1&nofb=1",course_created=now)
  return app_tables.courses.client_readable()


