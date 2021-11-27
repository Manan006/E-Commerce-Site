import anvil.stripe
import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server


@anvil.server.callable
def charge_user(token, email, course_name):
  stripe_customer = anvil.stripe.new_customer(email, token)
  price = app_tables.courses.get(id_name=course_name)['price']
  user = anvil.users.get_user()
  if user["purchased_courses"] == None:
    user["purchased_courses"] = []
  
  if course_name in user["purchased_courses"]:
    return
  
  result = stripe_customer.charge(amount=price*100, currency="USD")
  user["purchased_courses"] = user["purchased_courses"] + [course_name]

