import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

BOTTOM = Gtk.PositionType.BOTTOM
LEFT = Gtk.PositionType.LEFT
RIGHT = Gtk.PositionType.RIGHT
TOP = Gtk.PositionType.TOP


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        self.set_border_width(5)

        # Command Frame
        self.button1 = Gtk.Button(label="Start Single")
        self.button2 = Gtk.Button(label="Start Burst")
        self.button3 = Gtk.Button(label="Stop")
        self.button1.connect("clicked", self.on_button_clicked)
        self.button2.connect("clicked", self.on_button_clicked)
        self.button3.connect("clicked", self.on_button_clicked)
        self.commandGrid = Gtk.Grid(border_width=5, column_spacing=5, row_spacing=5)
        self.commandGrid.attach(self.button1, 1, 1, 1, 1)
        self.commandGrid.attach(self.button2, 2, 1, 1, 1)
        self.commandGrid.attach(self.button3, 1, 2, 1, 1)
        self.commandFrame = Gtk.Frame(label="Command")
        self.commandFrame.add(self.commandGrid)

        # S. Saturation Frame
        self.cb0 = Gtk.RadioButton.new_with_label_from_widget(None, label="0.1")
        self.cb1 = Gtk.RadioButton.new_with_label_from_widget(self.cb0, label="0.2")
        self.cb2 = Gtk.RadioButton.new_with_label_from_widget(self.cb0, label="0.3")
        self.cb3 = Gtk.RadioButton.new_with_label_from_widget(self.cb0, label="0.4")
        self.cb4 = Gtk.RadioButton.new_with_label_from_widget(self.cb0, label="0.5")
        self.cb5 = Gtk.RadioButton.new_with_label_from_widget(self.cb0, label="0.6")
        self.cb6 = Gtk.RadioButton.new_with_label_from_widget(self.cb0, label="0.7")
        self.cb7 = Gtk.RadioButton.new_with_label_from_widget(self.cb0, label="0.8")
        self.cb8 = Gtk.RadioButton.new_with_label_from_widget(self.cb0, label="0.9")
        self.cb9 = Gtk.RadioButton.new_with_label_from_widget(self.cb0, label="1.0")
        self.cb_other = Gtk.RadioButton.new_with_label_from_widget(self.cb0, label="other")
        self.entry_other = Gtk.Entry(width_chars=5, max_length=5)
        self.saturationGrid = Gtk.Grid(border_width=5, column_spacing=5, row_spacing=5)
        self.saturationGrid.attach(self.cb0, 1, 1, 1, 1)
        self.saturationGrid.attach(self.cb1, 2, 1, 1, 1)
        self.saturationGrid.attach(self.cb2, 1, 2, 1, 1)
        self.saturationGrid.attach(self.cb3, 2, 2, 1, 1)
        self.saturationGrid.attach(self.cb4, 1, 3, 1, 1)
        self.saturationGrid.attach(self.cb5, 2, 3, 1, 1)
        self.saturationGrid.attach(self.cb6, 1, 4, 1, 1)
        self.saturationGrid.attach(self.cb7, 2, 4, 1, 1)
        self.saturationGrid.attach(self.cb8, 1, 5, 1, 1)
        self.saturationGrid.attach(self.cb9, 2, 5, 1, 1)
        self.saturationGrid.attach(self.cb_other, 1, 6, 1, 1)
        self.saturationGrid.attach(self.entry_other, 2, 6, 1, 1)
        self.saturationFrame = Gtk.Frame(label="S. Saturation")
        self.saturationFrame.add(self.saturationGrid)

        # Measured Parameters Frame
        self.t_upper_plate = Gtk.Entry(editable=False)
        self.t_botton_plate = Gtk.Entry(editable=False)
        self.t_diff = Gtk.Entry(editable=False)
        self.super_sat = Gtk.Entry(editable=False)
        self.n_drops = Gtk.Entry(editable=False)
        self.concentration = Gtk.Entry(editable=False)
        self.n_frames = Gtk.Entry(editable=False)
        self.t_upper_plate_label = Gtk.Label(label="t_upper_plate")
        self.t_botton_plate_label = Gtk.Label(label="t_botton_plate")
        self.t_diff_label = Gtk.Label(label="t_diff")
        self.super_sat_label = Gtk.Label(label="super_sat")
        self.n_drops_label = Gtk.Label(label="n_drops")
        self.concentration_label = Gtk.Label(label="concentration")
        self.n_frames_label = Gtk.Label(label="n_frames")
        self.measurementsGrid = Gtk.Grid(border_width=5, column_spacing=5, row_spacing=5)
        self.measurementsGrid.attach(self.t_upper_plate_label, 1, 1, 1, 1)
        self.measurementsGrid.attach(self.t_upper_plate, 2, 1, 1, 1)
        self.measurementsGrid.attach(self.t_botton_plate_label, 1, 2, 1, 1)
        self.measurementsGrid.attach(self.t_botton_plate, 2, 2, 1, 1)
        self.measurementsGrid.attach(self.t_diff_label, 1, 3, 1, 1)
        self.measurementsGrid.attach(self.t_diff, 2, 3, 1, 1)
        self.measurementsGrid.attach(self.super_sat_label, 1, 4, 1, 1)
        self.measurementsGrid.attach(self.super_sat, 2, 4, 1, 1)
        self.measurementsGrid.attach(self.n_drops_label, 1, 5, 1, 1)
        self.measurementsGrid.attach(self.n_drops, 2, 5, 1, 1)
        self.measurementsGrid.attach(self.concentration_label, 1, 6, 1, 1)
        self.measurementsGrid.attach(self.concentration, 2, 6, 1, 1)
        self.measurementsGrid.attach(self.n_frames_label, 1, 7, 1, 1)
        self.measurementsGrid.attach(self.n_frames, 2, 7, 1, 1)
        self.measurementsFrame = Gtk.Frame(label="Measured Parameters")
        self.measurementsFrame.add(self.measurementsGrid)

        # Status Frame
        self.valve_state = Gtk.Switch(state=False)
        self.pump_state = Gtk.Switch(state=False)
        self.measures_state = Gtk.Switch(state=False)
        self.statusGrid = Gtk.Grid(border_width=5, column_spacing=5, row_spacing=5)
        self.statusGrid.attach(self.valve_state, 1, 1, 1, 1)
        self.statusGrid.attach(self.pump_state, 1, 2, 1, 1)
        self.statusGrid.attach(self.measures_state, 1, 3, 1, 1)
        self.statusFrame = Gtk.Frame(label="Status")
        self.statusFrame.add(self.statusGrid)

        # Camera Frame
        self.camera_view = Gtk.DrawingArea()
        self.cameraFrame = Gtk.Frame(label="CameraA")
        self.cameraFrame.add(self.camera_view)

        # Add all Widgets to main Grid
        self.grid = Gtk.Grid(border_width=5, column_spacing=5, row_spacing=5)
        # self.grid.set_column_homogeneous(True)
        # self.grid.set_row_homogeneous(True)
        self.grid.attach(self.saturationFrame, 1, 1, 1, 1)
        self.grid.attach_next_to(sibling=self.saturationFrame, child=self.measurementsFrame, side=RIGHT, width=1, height=1)
        self.grid.attach_next_to(sibling=self.saturationFrame, child=self.statusFrame, side=BOTTOM, width=1, height=1)
        self.grid.attach_next_to(sibling=self.statusFrame, child=self.commandFrame, side=BOTTOM, width=1, height=1)
        self.grid.attach_next_to(sibling=self.measurementsFrame, child=self.cameraFrame, side=LEFT, width=1, height=1)

        # Add grid to main window
        self.add(self.grid)

    def on_button_clicked(self, widget):
        cbs = ""
        if self.cb1.get_active():
            cbs = cbs + " cb1"
        if self.cb2.get_active():
            cbs = cbs + " cb2"
        if self.cb3.get_active():
            cbs = cbs + " cb3"

        print(widget.get_label())


if __name__ == '__main__':
    window = MyWindow()
    window.connect("destroy", Gtk.main_quit)
    window.show_all()
    Gtk.main()
