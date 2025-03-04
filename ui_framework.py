from abc import ABC, abstractmethod
import sys

# Abstract Products
class Button(ABC):
    @abstractmethod
    def render(self):
        pass

class Checkbox(ABC):
    @abstractmethod
    def toggle(self):
        pass

class TextField(ABC):
    @abstractmethod
    def input_text(self, text):
        pass

# Concrete Products for Windows
class WindowsButton(Button):
    def render(self):
        return "Rendering a Windows-style button"

class WindowsCheckbox(Checkbox):
    def toggle(self):
        return "Toggling a Windows-style checkbox"

class WindowsTextField(TextField):
    def input_text(self, text):
        return f"Windows text field input: {text}"

# Concrete Products for Mac
class MacButton(Button):
    def render(self):
        return "Rendering a macOS-style button"

class MacCheckbox(Checkbox):
    def toggle(self):
        return "Toggling a macOS-style checkbox"

class MacTextField(TextField):
    def input_text(self, text):
        return f"macOS text field input: {text}"

# Concrete Products for Linux
class LinuxButton(Button):
    def render(self):
        return "Rendering a Linux-style button"

class LinuxCheckbox(Checkbox):
    def toggle(self):
        return "Toggling a Linux-style checkbox"

class LinuxTextField(TextField):
    def input_text(self, text):
        return f"Linux text field input: {text}"

# Abstract Factory
class UIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass
    
    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass
    
    @abstractmethod
    def create_text_field(self) -> TextField:
        pass

# Concrete Factories
class WindowsFactory(UIFactory):
    def create_button(self):
        return WindowsButton()
    
    def create_checkbox(self):
        return WindowsCheckbox()
    
    def create_text_field(self):
        return WindowsTextField()

class MacFactory(UIFactory):
    def create_button(self):
        return MacButton()
    
    def create_checkbox(self):
        return MacCheckbox()
    
    def create_text_field(self):
        return MacTextField()

class LinuxFactory(UIFactory):
    def create_button(self):
        return LinuxButton()
    
    def create_checkbox(self):
        return LinuxCheckbox()
    
    def create_text_field(self):
        return LinuxTextField()

# UIManager
class UIManager:
    def __init__(self, factory: UIFactory):
        self.factory = factory
        self.button = None
        self.checkbox = None
        self.text_field = None
    
    def create_ui(self):
        self.button = self.factory.create_button()
        self.checkbox = self.factory.create_checkbox()
        self.text_field = self.factory.create_text_field()
    
    def render_ui(self):
        print(self.button.render())
        print(self.checkbox.toggle())
        print(self.text_field.input_text("Sample Text"))

# Client Code
def get_os_factory():
    platform = sys.platform
    if platform == "win32":
        return WindowsFactory()
    elif platform == "darwin":
        return MacFactory()
    elif platform.startswith("linux"):
        return LinuxFactory()
    else:
        raise NotImplementedError(f"Platform {platform} not supported")

if __name__ == "__main__":
    factory = get_os_factory()
    ui_manager = UIManager(factory)
    ui_manager.create_ui()
    ui_manager.render_ui()