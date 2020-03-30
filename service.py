import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
BOTTOM = Gtk.PositionType.BOTTOM
LEFT = Gtk.PositionType.LEFT
RIGHT = Gtk.PositionType.RIGHT
TOP = Gtk.PositionType.TOP


class ServiceWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Service", border_width=5)

        # Instruments Frame
        self.valve_label = Gtk.Label(label="Valve")
        self.valve = Gtk.Switch()
        self.pump_label = Gtk.Label(label="Pump")
        self.pump = Gtk.Switch()
        self.peltier_label = Gtk.Label(label="Peltier Control")
        self.peltier_control = Gtk.Switch()
        self.instrumentsGrid = Gtk.Grid(border_width=5, column_spacing=5, row_spacing=5)
        self.instrumentsGrid.attach(self.valve_label, 1, 1, 1, 1)
        self.instrumentsGrid.attach(self.valve, 2, 1, 1, 1)
        self.instrumentsGrid.attach(self.pump_label, 1, 2, 1, 1)
        self.instrumentsGrid.attach(self.pump, 2, 2, 1, 1)
        self.instrumentsGrid.attach(self.peltier_label, 1, 3, 1, 1)
        self.instrumentsGrid.attach(self.peltier_control, 2, 3, 1, 1)
        self.instrumentsFrame = Gtk.Frame(label="Instruments")
        self.instrumentsFrame.add(self.instrumentsGrid)

        # Add all Widgets to main Grid
        self.grid = Gtk.Grid(border_width=5, column_spacing=5, row_spacing=5)
        self.grid.attach(self.instrumentsFrame, 1, 1, 1, 1)
        # Add grid to main window
        self.add(self.grid)


if __name__ == '__main__':
    window = ServiceWindow()
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    Gtk.main()
