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

from gi.repository import GObject, Gtk,Gedit

class CustomHighlighterPlugin(GObject.Object, Gedit.WindowActivatable):
    __gtype_name__ = "CustomHighlighterPlugin"

    def __init__(self):
        pass

    def do_activate(self):
        pass

    def do_deactivate(self):
        pass

    def do_update_state(self):
        pass
