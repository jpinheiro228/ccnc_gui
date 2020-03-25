import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk


class MyWindow(Gtk.Window):
    def __init__(self):
        Gtk.Window.__init__(self, title="Hello World")
        # self.set_default_size(800, 600)
        self.grid = Gtk.Grid()
        self.grid.set_column_spacing(5)
        self.grid.set_row_spacing(5)
        self.button1 = Gtk.Button(label="Button1")
        self.button2 = Gtk.Button(label="Button2")
        self.button3 = Gtk.Button(label="Button3")
        self.button1.connect("clicked", self.on_button_clicked)
        self.button2.connect("clicked", self.on_button_clicked)
        self.button3.connect("clicked", self.on_button_clicked)
        self.cb1 = Gtk.CheckButton(label="Check 1")
        self.cb2 = Gtk.CheckButton(label="Check 2")
        self.cb3 = Gtk.CheckButton(label="Check 3")
        self.entry1 = Gtk.Entry()
        self.entry2 = Gtk.Entry()
        self.entry3 = Gtk.Entry()
        self.grid.attach(self.button1, 1, 1, 1, 1)
        self.grid.attach(self.button2, 1, 2, 1, 1)
        self.grid.attach(self.button3, 1, 3, 1, 1)
        self.grid.attach(self.cb1, 2, 1, 1, 1)
        self.grid.attach(self.cb2, 2, 2, 1, 1)
        self.grid.attach(self.cb3, 2, 3, 1, 1)
        self.grid.attach(self.entry1, 3, 1, 1, 1)
        self.grid.attach(self.entry2, 3, 2, 1, 1)
        self.grid.attach(self.entry3, 3, 3, 1, 1)
        self.add(self.grid)

    def on_button_clicked(self, widget):
        cbs = ""
        if self.cb1.get_active():
            cbs = cbs + " cb1"
        if self.cb2.get_active():
            cbs = cbs + " cb2"
        if self.cb3.get_active():
            cbs = cbs + " cb3"

        print(widget.get_label()
              + cbs
              + " " + str(self.entry1.get_text())
              + " " + str(self.entry2.get_text())
              + " " + str(self.entry3.get_text()))


window = MyWindow()
window.connect("destroy", Gtk.main_quit)
window.show_all()
Gtk.main()
