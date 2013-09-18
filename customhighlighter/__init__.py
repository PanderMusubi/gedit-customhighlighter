# -*- coding: utf-8 -*-

# __init__.py -- plugin object
#
# Copyright (C) 2013 - Pander Musubi
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; either version 2, or (at your option)
# any later version.
# 
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA 02111-1307, USA.

from .customhighlighter import CustomHighlighter
from gi.repository import GObject, Gtk, Gedit

ui_str = """<ui>
  <menubar name="MenuBar">
    <menu name="FileMenu" action="File">
      <placeholder name="FileOps_2">
        <menuitem name="CustomHighlighter" action="CustomHighlighter"/>
      </placeholder>
    </menu>
  </menubar>
</ui>
"""

class CustomHighlighterPlugin(GObject.Object, Gedit.WindowActivatable):
    __gtype_name__ = "CustomHighlighterPlugin"

    window = GObject.property(type=Gedit.Window)

    def __init__(self):
        GObject.Object.__init__(self)

    def do_activate(self):
        self._install_menu()

    def do_deactivate(self):
        self._uninstall_menu()

    def do_update_state(self):
        pass

    def _uninstall_menu(self):
        manager = self.window.get_ui_manager()

        manager.remove_ui(self._ui_id)
        manager.remove_action_group(self._action_group)

        manager.ensure_update()

    def _install_menu(self):
        manager = self.window.get_ui_manager()
        self._action_group = Gtk.ActionGroup(name="GeditCustomHighlighterPluginActions")
        self._action_group.add_actions([
            ("CustomHighlighter", Gtk.STOCK_OPEN, _("Custom highlighter"),
             '<Primary><Alt>h', _("Custom highlighter"),
             self.on_quick_open_activate)
        ])

        manager.insert_action_group(self._action_group)
        self._ui_id = manager.add_ui_from_string(ui_str)

    def on_quick_open_activate(self, action, user_data=None):
        CustomHighlighter()