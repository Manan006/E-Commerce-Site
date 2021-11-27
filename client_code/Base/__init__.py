from ._anvil_designer import BaseTemplate
from anvil import *
import stripe.checkout
import anvil.server
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ..Home import Home
from ..MyCourses import MyCourses
from .urls import urls

class Base(BaseTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    self.change_sign_in_text()
    self.handle_urls()
    
  def handle_urls(self):
    url = get_url_hash().lower()
    
    if url in urls:
      self.content_panel.clear()
      self.content_panel.add_component(urls[url]())
    else:
      self.go_to_home()
    
  def change_sign_in_text(self):
    user = anvil.users.get_user()
    if user:
      email = user["email"]
      self.sign_in.text = email
    else:
      self.sign_in.text = "Sign In"
    
    self.toggle_my_courses_link()
      
  def toggle_my_courses_link(self):
    self.my_courses.visible = anvil.users.get_user() != None

  def title_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.go_to_home()

  def my_courses_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.content_panel.clear()
    self.content_panel.add_component(MyCourses())
    
  def go_to_home(self):
    self.content_panel.clear()
    self.content_panel.add_component(Home())

  def sign_in_click(self, **event_args):
    """This method is called when the link is clicked"""
    user = anvil.users.get_user()
    if user:
      logout = confirm("Would you like to logout?")
      if logout:
        anvil.users.logout()
        self.go_to_home()
    else:
      anvil.users.login_with_form()
    self.change_sign_in_text()



