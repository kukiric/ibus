# vim:set et sts=4 sw=4:
# -*- coding: utf-8 -*-
#
# ibus - The Input Bus
#
# Copyright (c) 2017 Ricardo Maes <ricmzn@gmail.com>
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301
# USA

from gi import require_version as gi_require_version
gi_require_version('Gdk', '3.0')
gi_require_version('Gtk', '3.0')

from gi.repository import GObject
from gi.repository import Gdk
from gi.repository import Gtk

class IBusSetupColorButton(Gtk.ColorButton):
    __gtype_name__ = "IBusSetupColorButton"

    rgba_string = GObject.Property(type=str)

    def __init__(self):
        Gtk.ColorButton.__init__(self)
        self.connect("notify::rgba", self.on_color_change)
        # self.connect("notify::rgba_string", self.update_color)

    # @GObject.Property(type=str)
    # def rgba_string(self):
    #     return self.get_rgba().to_string()

    def do_set_property(self, prop, value):
        if prop.name == "rgba_string":
            print("setting new default: " + self.rgba_string)
            value = Gdk.RGBA()
            value.parse(self.rgba_string)
            self.set_rgba(value)
        else:
            Gtk.ColorButton.do_set_property(self, prop, value)

    def on_color_change(self, gparamstring, spec):
        value = self.get_rgba().to_string()
        # Only set the property if it's different than the current, to avoid an infinite notify loop
        if value != self.rgba_string:
            self.rgba_string = value

    def update_color(self, gparamstring, spec):
        value = Gdk.RGBA()
        value.parse(self.rgba_string)
        self.set_rgba(value)