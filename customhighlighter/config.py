# -*- coding: utf-8 -*-

# config.py -- plugin object
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

import ConfigParser, os, webcolors

#todo FORMAT = '%(asctime)-15s %(clientip)s %(user)-8s %(message)s'
#logging.basicConfig(format=FORMAT)
#d = {'clientip': '192.168.0.1', 'user': 'fbloggs'}
#logger = logging.getLogger('tcpserver')
#logger.warning('Protocol problem: %s', 'connection reset', extra=d)

config = ConfigParser.ConfigParser()
config.read(['default.cfg', os.path.expanduser('~/.config/gedit/gedit-custom-highlighter')])
fields = ('name', 'style', 'color', 'bgcolor', ) # all other are word lists

# sets / definitions / attrs / values

sets = {}

for section in config.sections():
    if ' - ' not in section:
        continue
    updated = False
    (setname, defname) = section.split(' - ')
    definitions = {}
    if setname in sets:
        definitions = sets[setname]
    attrs = {}
    if defname in definitions:
        attrs = definitions[defname]
        
    for option in config.options(section):
        attrname = option.lower()
        value = config.get(section, option)
        if attrname in fields:
            value = value.lower()
            if 'color' in attrname:
                try:
                    if value[0] == '#':
                        attrs[attrname] = webcolors.normalize_hex(value)
                    else:
                        # color definitions: http://www.w3.org/TR/css3-color/#svg-color
                        # see also overview: https://en.wikipedia.org/wiki/Html_colors#X11_color_names
                        attrs[attrname] = webcolors.name_to_hex(value)
                except ValueError:
                    continue
            else:
                attrs[attrname] = value
        else:
            attrs[attrname] = value.split('|')
        updated = True

    if updated:
        definitions[defname] = attrs
        sets[setname] = definitions
        updated = False

for setname in sets:
    print setname
    Set = sets[setname]
    for defname in Set:
        print ' ', defname
        definitions = Set[defname]
        for attrname in definitions:
            if attrname not in fields:
                print '   ', attrname + '=' + '/'.join(definitions[attrname])
            else:
                print '   ', attrname + '=' + definitions[attrname]

