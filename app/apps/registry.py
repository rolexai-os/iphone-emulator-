from .calculator import CalculatorApp
from .settings import SettingsApp
from .messages import MessagesApp
from .phone import PhoneApp
from .photos import PhotosApp
from .browser import BrowserApp

def app_definitions():
    return [
        {"name":"Calculator","icon":"🧮","widget":CalculatorApp},
        {"name":"Settings","icon":"⚙️","widget":SettingsApp},
        {"name":"Messages","icon":"💬","widget":MessagesApp},
        {"name":"Phone","icon":"☎️","widget":PhoneApp},
        {"name":"Photos","icon":"🌈","widget":PhotosApp},
        {"name":"Browser","icon":"🌐","widget":BrowserApp}
    ]
