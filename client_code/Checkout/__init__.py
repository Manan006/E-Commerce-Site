from ._anvil_designer import CheckoutTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import stripe

class Checkout(CheckoutTemplate):
  def __init__(self, id_name, back_button_callback, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.back_button_callback = back_button_callback
    self.update_form(id_name)
  
  def update_form(self, id_name):
    course = anvil.server.call('get_course_details', id_name)
    self.course = course
    self.name_label.text = course["name"]
    self.description_label.text = course['description']
    self.price_label.text = f"${course['price']} USD"
    self.image_content.source = course['image']

  def buy_click(self, **event_args):
    """This method is called when the button is clicked"""
    if anvil.users.get_user() == None:
      anvil.users.login_with_form()
    
    user = anvil.users.get_user()
    if user == None:
      alert("Please sign in!")
      return
    
    if user["purchased_courses"] and self.course["id_name"] in user["purchased_courses"]:
      alert("You already own this course!")
      return
  
    token, info = stripe.checkout.get_token(amount=self.course["price"]*100, currency="USD", title=self.course["name"], description=self.course["description"])
    try:
      anvil.server.call("charge_user", token, user["email"], self.course["id_name"])
      alert("Success")
    except Exception as e:
      alert(str(e))
    
  
  def back_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.back_button_callback()


