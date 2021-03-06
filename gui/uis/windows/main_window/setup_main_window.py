# IMPORT PACKAGES AND MODULES
# ///////////////////////////////////////////////////////////////
from calculus.synthesis import synthesis
from gui.widgets.py_table_widget.py_table_widget import PyTableWidget
from .functions_main_window import *
import sys
import os

# IMPORT QT CORE
# ///////////////////////////////////////////////////////////////
from qt_core import *

# IMPORT SETTINGS
# ///////////////////////////////////////////////////////////////
from gui.core.json_settings import Settings

# IMPORT THEME COLORS
# ///////////////////////////////////////////////////////////////
from gui.core.json_themes import Themes

# IMPORT PY ONE DARK WIDGETS
# ///////////////////////////////////////////////////////////////
from gui.widgets import *

# LOAD UI MAIN
# ///////////////////////////////////////////////////////////////
from .ui_main import *

# MAIN FUNCTIONS 
# ///////////////////////////////////////////////////////////////
from .functions_main_window import *


# PY WINDOW
# ///////////////////////////////////////////////////////////////
class SetupMainWindow:
    def __init__(self):
        super().__init__()
        # SETUP MAIN WINDOw
        # Load widgets from "gui\uis\main_window\ui_main.py"
        # ///////////////////////////////////////////////////////////////
        self.calculate_button = None
        self.ui = UI_MainWindow()
        self.ui.setup_ui(self)

    # ADD LEFT MENUS
    # ///////////////////////////////////////////////////////////////
    add_left_menus = [
        {
            "btn_icon": "icon_home.svg",
            "btn_id": "btn_home",
            "btn_text": "Home",
            "btn_tooltip": "Home page",
            "show_top": True,
            "is_active": True
        },
        {
            "btn_icon": "icon_calculate.svg",
            "btn_id": "btn_calculus",
            "btn_text": "Calculus",
            "btn_tooltip": "Calculus page",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_graph.svg",
            "btn_id": "btn_graph",
            "btn_text": "Graphics",
            "btn_tooltip": "Graphics page",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_file.svg",
            "btn_id": "btn_report",
            "btn_text": "Report",
            "btn_tooltip": "Generate report",
            "show_top": True,
            "is_active": False
        },
        {
            "btn_icon": "icon_settings.svg",
            "btn_id": "btn_settings",
            "btn_text": "Settings",
            "btn_tooltip": "Open settings",
            "show_top": False,
            "is_active": False
        }
    ]

    # ADD TITLE BAR MENUS
    # ///////////////////////////////////////////////////////////////
    add_title_bar_menus = [
        {
            "btn_icon": "icon_search.svg",
            "btn_id": "btn_search",
            "btn_tooltip": "Search",
            "is_active": False
        }
    ]

    # SETUP CUSTOM BTNs OF CUSTOM WIDGETS
    # Get sender() function when btn is clicked
    # ///////////////////////////////////////////////////////////////
    def setup_btns(self):
        if self.ui.title_bar.sender() != None:
            return self.ui.title_bar.sender()
        elif self.ui.left_menu.sender() != None:
            return self.ui.left_menu.sender()
        elif self.ui.left_column.sender() != None:
            return self.ui.left_column.sender()

    # SETUP MAIN WINDOW WITH CUSTOM PARAMETERS
    # ///////////////////////////////////////////////////////////////
    def setup_gui(self):
        # APP TITLE
        # ///////////////////////////////////////////////////////////////
        self.setWindowTitle(self.settings["app_name"])

        # REMOVE TITLE BAR
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.setWindowFlag(Qt.FramelessWindowHint)
            self.setAttribute(Qt.WA_TranslucentBackground)

        # ADD GRIPS
        # ///////////////////////////////////////////////////////////////
        if self.settings["custom_title_bar"]:
            self.left_grip = PyGrips(self, "left", self.hide_grips)
            self.right_grip = PyGrips(self, "right", self.hide_grips)
            self.top_grip = PyGrips(self, "top", self.hide_grips)
            self.bottom_grip = PyGrips(self, "bottom", self.hide_grips)
            self.top_left_grip = PyGrips(self, "top_left", self.hide_grips)
            self.top_right_grip = PyGrips(self, "top_right", self.hide_grips)
            self.bottom_left_grip = PyGrips(self, "bottom_left", self.hide_grips)
            self.bottom_right_grip = PyGrips(self, "bottom_right", self.hide_grips)

        # LEFT MENUS / GET SIGNALS WHEN LEFT MENU BTN IS CLICKED / RELEASED
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.left_menu.add_menus(SetupMainWindow.add_left_menus)

        # SET SIGNALS
        self.ui.left_menu.clicked.connect(self.btn_clicked)
        self.ui.left_menu.released.connect(self.btn_released)

        # TITLE BAR / ADD EXTRA BUTTONS
        # ///////////////////////////////////////////////////////////////
        # ADD MENUS
        self.ui.title_bar.add_menus(SetupMainWindow.add_title_bar_menus)

        # SET SIGNALS
        self.ui.title_bar.clicked.connect(self.btn_clicked)
        self.ui.title_bar.released.connect(self.btn_released)

        # ADD Title
        if self.settings["custom_title_bar"]:
            self.ui.title_bar.set_title(self.settings["app_name"])
        else:
            self.ui.title_bar.set_title("Welcome to PyOneDark")

        # LEFT COLUMN SET SIGNALS
        # ///////////////////////////////////////////////////////////////
        self.ui.left_column.clicked.connect(self.btn_clicked)
        self.ui.left_column.released.connect(self.btn_released)

        # SET INITIAL PAGE / SET LEFT AND RIGHT COLUMN MENUS
        # ///////////////////////////////////////////////////////////////
        MainFunctions.set_page(self, self.ui.load_pages.page_1)
        MainFunctions.set_left_column_menu(
            self,
            menu=self.ui.left_column.menus.menu_1,
            title="Settings Left Column",
            icon_path=Functions.set_svg_icon("icon_settings.svg")
        )
        MainFunctions.set_right_column_menu(self, self.ui.right_column.menu_1)

        # ///////////////////////////////////////////////////////////////
        # EXAMPLE CUSTOM WIDGETS
        # Here are added the custom widgets to pages and columns that
        # were created using Qt Designer.
        # This is just an example and should be deleted when creating
        # your application.
        #
        # OBJECTS FOR LOAD PAGES, LEFT AND RIGHT COLUMNS
        # You can access objects inside Qt Designer projects using
        # the objects below:
        #
        # <OBJECTS>
        # LEFT COLUMN: self.ui.left_column.menus
        # RIGHT COLUMN: self.ui.right_column
        # LOAD PAGES: self.ui.load_pages
        # </OBJECTS>
        # ///////////////////////////////////////////////////////////////

        # LOAD SETTINGS
        # ///////////////////////////////////////////////////////////////
        settings = Settings()
        self.settings = settings.items

        # LOAD THEME COLOR
        # ///////////////////////////////////////////////////////////////
        themes = Themes()
        self.themes = themes.items

        # ADD CUSTOM WIDGETS IN INPUTS FRAME
        # ///////////////////////////////////////////////////////////////
        # BUTTON 1
        self.icon_theta_1 = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_theta1.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="theta 1",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )
        self.theta_1_edit = PyLineEdit(
            text="",
            place_holder_text="value theta 1",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        #
        self.icon_theta_2 = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_theta2.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="theta 2",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )
        self.theta_2_edit = PyLineEdit(
            text="",
            place_holder_text="value theta 2",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        #
        self.icon_theta_3 = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_theta3.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="theta 3",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )
        self.theta_3_edit = PyLineEdit(
            text="",
            place_holder_text="value theta 3",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.icon_P1 = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_P1.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Point 1",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )
        self.P1_x_edit = PyLineEdit(
            text="",
            place_holder_text="value P1_x",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.P1_y_edit = PyLineEdit(
            text="",
            place_holder_text="value P1_y",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        #
        self.icon_P2 = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_P2.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Point 2",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )
        self.P2_x_edit = PyLineEdit(
            text="",
            place_holder_text="value P2_x",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.P2_y_edit = PyLineEdit(
            text="",
            place_holder_text="value P2_y",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.icon_P3 = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_P3.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Point 3",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )
        self.P3_x_edit = PyLineEdit(
            text="",
            place_holder_text="value P3_x",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.P3_y_edit = PyLineEdit(
            text="",
            place_holder_text="value P3_y",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        # ///////////////////////////
        self.icon_O2 = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_O2.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Point O2",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )
        self.O2_x_edit = PyLineEdit(
            text="",
            place_holder_text="value O2_x",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.O2_y_edit = PyLineEdit(
            text="",
            place_holder_text="value O2_y",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        # /////////////////////////////////////////////////////////////
        self.icon_O4 = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_O4.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Point O4",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )
        self.O4_x_edit = PyLineEdit(
            text="",
            place_holder_text="value O4_x",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.O4_y_edit = PyLineEdit(
            text="",
            place_holder_text="value O4_y",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        # Editing
        self.icon_theta_1.setMinimumHeight(30);
        self.theta_1_edit.setMinimumHeight(30)
        self.icon_theta_2.setMinimumHeight(30);
        self.theta_2_edit.setMinimumHeight(30)
        self.icon_theta_3.setMinimumHeight(30);
        self.theta_3_edit.setMinimumHeight(30)

        self.icon_P1.setMinimumHeight(30);
        self.P1_x_edit.setMinimumHeight(30);
        self.P1_y_edit.setMinimumHeight(30)
        self.icon_P2.setMinimumHeight(30);
        self.P2_x_edit.setMinimumHeight(30);
        self.P2_y_edit.setMinimumHeight(30)
        self.icon_P3.setMinimumHeight(30);
        self.P3_x_edit.setMinimumHeight(30);
        self.P3_y_edit.setMinimumHeight(30)

        self.icon_O2.setMinimumHeight(30);
        self.O2_x_edit.setMinimumHeight(30);
        self.O2_y_edit.setMinimumHeight(30)
        self.icon_O4.setMinimumHeight(30);
        self.O4_x_edit.setMinimumHeight(30);
        self.O4_y_edit.setMinimumHeight(30)

        # ////////////////////////////////////////
        # ADD CUSTOM WIDGETS IN CENTRAL FRAME
        # ///////////////////////////////////////////////////////////////
        self.calculate_button = PyPushButton(
            text="Calculate",
            radius=8,
            color=self.themes["app_color"]["text_foreground"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["dark_four"]
        )
        self.calculate_button.setMinimumHeight(40)
        self.calculate_button.setMinimumWidth(80)

        # ADD CUSTOM WIDGETS IN RIGHT FRAME
        # ///////////////////////////////////////////////////////////////
        self.icon_alpha_2 = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_alpha2.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="alpha 2",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )

        self.alpha2_edit = PyLineEdit(
            text="",
            place_holder_text="alpha 2",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.icon_alpha_3 = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_alpha3.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="alpha 3",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )
        self.alpha3_edit = PyLineEdit(
            text="",
            place_holder_text="alpha 3",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        #
        self.icon_P21 = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_P21.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Point 21",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )
        self.P21_x_edit = PyLineEdit(
            text="",
            place_holder_text="value P21_x",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.P21_y_edit = PyLineEdit(
            text="",
            place_holder_text="value P21_y",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.icon_P31 = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_P31.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Point 31",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )
        self.P31_x_edit = PyLineEdit(
            text="",
            place_holder_text="value P31_x",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.P31_y_edit = PyLineEdit(
            text="",
            place_holder_text="value P31_y",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        # //////////////////////////////////////////////////////////////
        self.icon_beta2 = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_beta2.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="beta 2",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )
        self.beta2_edit = PyLineEdit(
            text="",
            place_holder_text="beta 2",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.icon_beta3 = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_beta3.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="beta 3",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )
        self.beta3_edit = PyLineEdit(
            text="",
            place_holder_text="beta 3",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        # //////////////////////////////////////////////////////////////
        self.icon_W = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_W.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="W",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )
        self.W_edit = PyLineEdit(
            text="",
            place_holder_text="W",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.icon_theta_out = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_theta.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="theta",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )
        self.theta_out_edit = PyLineEdit(
            text="",
            place_holder_text="theta",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        # //////////////////////////////////////////////////////////////
        self.icon_Z = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_Z.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="Z",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )
        self.Z_edit = PyLineEdit(
            text="",
            place_holder_text="Z",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.icon_phi_out = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_phi.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="phi",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )
        self.phi_out_edit = PyLineEdit(
            text="",
            place_holder_text="phi",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        # //////////// aca abajo se repite
        self.icon_gamma2 = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_gamma2.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="gamma 2",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )
        self.gamma2_edit = PyLineEdit(
            text="",
            place_holder_text="gamma 2",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.icon_gamma3 = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_gamma3.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="gamma 3",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )
        self.gamma3_edit = PyLineEdit(
            text="",
            place_holder_text="gamma 3",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        # //////////////////////////////////////////////////////////////
        self.icon_U = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_U.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="U",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )
        self.U_edit = PyLineEdit(
            text="",
            place_holder_text="U",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.icon_sigma_out = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_sigma.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="sigma",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )
        self.sigma_out_edit = PyLineEdit(
            text="",
            place_holder_text="sigma",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        # //////////////////////////////////////////////////////////////
        self.icon_S = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_S.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="S",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )
        self.S_edit = PyLineEdit(
            text="",
            place_holder_text="S",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.icon_psi_out = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_psi.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="psi",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )
        self.psi_out_edit = PyLineEdit(
            text="",
            place_holder_text="psi",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        # /////////////// aca ya no
        self.icon_L1 = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_L1.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="L1",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )
        self.L1_edit = PyLineEdit(
            text="",
            place_holder_text="L1",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.icon_L2 = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_L2.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="L2",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )
        self.L2_edit = PyLineEdit(
            text="",
            place_holder_text="L2",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.icon_L3 = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_L3.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="L3",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )
        self.L3_edit = PyLineEdit(
            text="",
            place_holder_text="L3",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )
        self.icon_L4 = PyIconButton(
            icon_path=Functions.set_svg_icon("icon_L4.svg"),
            parent=self,
            app_parent=self.ui.central_widget,
            tooltip_text="L4",
            width=40,
            height=40,
            radius=8,
            dark_one=self.themes["app_color"]["dark_one"],
            icon_color=self.themes["app_color"]["icon_color"],
            icon_color_hover=self.themes["app_color"]["icon_hover"],
            icon_color_pressed=self.themes["app_color"]["white"],
            icon_color_active=self.themes["app_color"]["icon_active"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_hover=self.themes["app_color"]["dark_three"],
            bg_color_pressed=self.themes["app_color"]["green"],
        )
        self.L4_edit = PyLineEdit(
            text="",
            place_holder_text="L4",
            radius=8,
            border_size=2,
            color=self.themes["app_color"]["text_foreground"],
            selection_color=self.themes["app_color"]["white"],
            bg_color=self.themes["app_color"]["dark_one"],
            bg_color_active=self.themes["app_color"]["dark_three"],
            context_color=self.themes["app_color"]["context_color"]
        )

        # Editing
        # self.icon_P1.setMinimumHeight(30); self.P1_x_edit.setMinimumHeight(30); self.P1_y_edit.setMinimumHeight(30)
        self.icon_alpha_2.setMinimumHeight(30);
        self.alpha2_edit.setMinimumHeight(30)
        self.icon_alpha_3.setMinimumHeight(30)
        self.alpha3_edit.setMinimumHeight(30)
        self.icon_P21.setMinimumHeight(30);
        self.P21_x_edit.setMinimumHeight(30);
        self.P21_y_edit.setMinimumHeight(30)
        self.icon_P31.setMinimumHeight(30);
        self.P31_x_edit.setMinimumHeight(30);
        self.P31_y_edit.setMinimumHeight(30)

        self.icon_L1.setMinimumHeight(30)
        self.L1_edit.setMinimumHeight(30)
        self.icon_L2.setMinimumHeight(30)
        self.L2_edit.setMinimumHeight(30)
        self.icon_L3.setMinimumHeight(30)
        self.L3_edit.setMinimumHeight(30)
        self.icon_L4.setMinimumHeight(30)
        self.L4_edit.setMinimumHeight(30)

        # Add to left layout
        self.ui.load_pages.theta1_layout.addWidget(self.icon_theta_1)
        self.ui.load_pages.theta1_layout.addWidget(self.theta_1_edit)
        self.ui.load_pages.theta2_layout.addWidget(self.icon_theta_2)
        self.ui.load_pages.theta2_layout.addWidget(self.theta_2_edit)
        self.ui.load_pages.theta3_layout.addWidget(self.icon_theta_3)
        self.ui.load_pages.theta3_layout.addWidget(self.theta_3_edit)
        self.ui.load_pages.P1_layout.addWidget(self.icon_P1)
        self.ui.load_pages.P1_layout.addWidget(self.P1_x_edit)
        self.ui.load_pages.P1_layout.addWidget(self.P1_y_edit)
        self.ui.load_pages.P2_layout.addWidget(self.icon_P2)
        self.ui.load_pages.P2_layout.addWidget(self.P2_x_edit)
        self.ui.load_pages.P2_layout.addWidget(self.P2_y_edit)
        self.ui.load_pages.P3_layout.addWidget(self.icon_P3)
        self.ui.load_pages.P3_layout.addWidget(self.P3_x_edit)
        self.ui.load_pages.P3_layout.addWidget(self.P3_y_edit)
        self.ui.load_pages.O2_layout.addWidget(self.icon_O2)
        self.ui.load_pages.O2_layout.addWidget(self.O2_x_edit)
        self.ui.load_pages.O2_layout.addWidget(self.O2_y_edit)
        self.ui.load_pages.O4_layout.addWidget(self.icon_O4)
        self.ui.load_pages.O4_layout.addWidget(self.O4_x_edit)
        self.ui.load_pages.O4_layout.addWidget(self.O4_y_edit)

        # Add to central layout
        self.ui.load_pages.button_layout.addWidget(self.calculate_button)
        self.logo_svg = QSvgWidget(Functions.set_svg_image("logo_home.svg"))
        self.ui.load_pages.image_latout.addWidget(self.logo_svg, Qt.AlignCenter, Qt.AlignCenter)

        # Add to right layout
        self.ui.load_pages.alphas_layout.addWidget(self.icon_alpha_2)
        self.ui.load_pages.alphas_layout.addWidget(self.alpha2_edit)
        self.ui.load_pages.alphas_layout.addWidget(self.icon_alpha_3)
        self.ui.load_pages.alphas_layout.addWidget(self.alpha3_edit)
        self.ui.load_pages.P21_layout.addWidget(self.icon_P21)
        self.ui.load_pages.P21_layout.addWidget(self.P21_x_edit)
        self.ui.load_pages.P21_layout.addWidget(self.P21_y_edit)
        self.ui.load_pages.P31_layout.addWidget(self.icon_P31)
        self.ui.load_pages.P31_layout.addWidget(self.P31_x_edit)
        self.ui.load_pages.P31_layout.addWidget(self.P31_y_edit)

        self.ui.load_pages.beta_layout.addWidget(self.icon_beta2)
        self.ui.load_pages.beta_layout.addWidget(self.beta2_edit)
        self.ui.load_pages.beta_layout.addWidget(self.icon_beta3)
        self.ui.load_pages.beta_layout.addWidget(self.beta3_edit)
        self.ui.load_pages.others1_layout.addWidget(self.icon_W)
        self.ui.load_pages.others1_layout.addWidget(self.W_edit)
        self.ui.load_pages.others1_layout.addWidget(self.icon_theta_out)
        self.ui.load_pages.others1_layout.addWidget(self.theta_out_edit)
        self.ui.load_pages.others2_layout.addWidget(self.icon_Z)
        self.ui.load_pages.others2_layout.addWidget(self.Z_edit)
        self.ui.load_pages.others2_layout.addWidget(self.icon_phi_out)
        self.ui.load_pages.others2_layout.addWidget(self.phi_out_edit)

        self.ui.load_pages.gamma_layout.addWidget(self.icon_gamma2)
        self.ui.load_pages.gamma_layout.addWidget(self.gamma2_edit)
        self.ui.load_pages.gamma_layout.addWidget(self.icon_gamma3)
        self.ui.load_pages.gamma_layout.addWidget(self.gamma3_edit)
        self.ui.load_pages.others3_layout.addWidget(self.icon_U)
        self.ui.load_pages.others3_layout.addWidget(self.U_edit)
        self.ui.load_pages.others3_layout.addWidget(self.icon_sigma_out)
        self.ui.load_pages.others3_layout.addWidget(self.sigma_out_edit)
        self.ui.load_pages.others4_layout.addWidget(self.icon_S)
        self.ui.load_pages.others4_layout.addWidget(self.S_edit)
        self.ui.load_pages.others4_layout.addWidget(self.icon_psi_out)
        self.ui.load_pages.others4_layout.addWidget(self.psi_out_edit)

        self.ui.load_pages.Lengths1_layout.addWidget(self.icon_L1)
        self.ui.load_pages.Lengths1_layout.addWidget(self.L1_edit)
        self.ui.load_pages.Lengths1_layout.addWidget(self.icon_L2)
        self.ui.load_pages.Lengths1_layout.addWidget(self.L2_edit)
        self.ui.load_pages.Lengths2_layout.addWidget(self.icon_L3)
        self.ui.load_pages.Lengths2_layout.addWidget(self.L3_edit)
        self.ui.load_pages.Lengths2_layout.addWidget(self.icon_L4)
        self.ui.load_pages.Lengths2_layout.addWidget(self.L4_edit)

        # ///////////////////////////////////////////////////////////////
        # FUNCTION
        # ///////////////////////////////////////////////////////////////
        def calculate_u1():
            v1 = float(self.theta_1_edit.text())
            v2 = float(self.theta_2_edit.text())
            v3 = float(self.theta_3_edit.text())

            v4 = float(self.P1_x_edit.text())
            v5 = float(self.P1_y_edit.text())
            v6 = float(self.P2_x_edit.text())
            v7 = float(self.P2_y_edit.text())
            v8 = float(self.P3_x_edit.text())
            v9 = float(self.P3_y_edit.text())

            v10 = float(self.O2_x_edit.text())
            v11 = float(self.O2_y_edit.text())
            v12 = float(self.O4_x_edit.text())
            v13 = float(self.O4_y_edit.text())

            result = synthesis(v1, v2, v3, v4, v5, v6, v7, v8, v9, v10, v11, v12, v13)
            #print(result)
            self.alpha2_edit.setText(result[0])
            self.alpha3_edit.setText(result[1])
            self.P21_x_edit.setText(result[2])
            self.P21_y_edit.setText(result[3])
            self.P31_x_edit.setText(result[4])
            self.P31_y_edit.setText(result[5])
            self.beta2_edit.setText(result[6])
            self.beta3_edit.setText(result[7])
            self.W_edit.setText(result[8])
            self.theta_out_edit.setText(result[9])
            self.Z_edit.setText(result[10])
            self.phi_out_edit.setText(result[11])
            self.gamma2_edit.setText(result[12])
            self.gamma3_edit.setText(result[13])
            self.U_edit.setText(result[14])
            self.sigma_out_edit.setText(result[15])
            self.S_edit.setText(result[16])
            self.psi_out_edit.setText(result[17])
            self.L1_edit.setText(result[18])
            self.L2_edit.setText(result[19])
            self.L3_edit.setText(result[20])
            self.L4_edit.setText(result[21])

        self.calculate_button.clicked.connect(calculate_u1)

    # RESIZE GRIPS AND CHANGE POSITION
    # Resize or change position when window is resized
    # ///////////////////////////////////////////////////////////////
    def resize_grips(self):
        if self.settings["custom_title_bar"]:
            self.left_grip.setGeometry(5, 10, 10, self.height())
            self.right_grip.setGeometry(self.width() - 15, 10, 10, self.height())
            self.top_grip.setGeometry(5, 5, self.width() - 10, 10)
            self.bottom_grip.setGeometry(5, self.height() - 15, self.width() - 10, 10)
            self.top_right_grip.setGeometry(self.width() - 20, 5, 15, 15)
            self.bottom_left_grip.setGeometry(5, self.height() - 20, 15, 15)
            self.bottom_right_grip.setGeometry(self.width() - 20, self.height() - 20, 15, 15)
