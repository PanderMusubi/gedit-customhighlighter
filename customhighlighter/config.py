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

import ConfigParser, os

config = ConfigParser.ConfigParser()
config.read(['default.cfg', os.path.expanduser('~/.config/gedit/gedit-custom-highlighter')])
fields = ('name', 'style', 'color', 'bgcolor', )

# sets / definitions / attributes / values

sets = {}

for section in config.sections():
    definitions = {}
    if section in sets:
        definitions = sets[section]
        
    for option in config.options(section):
        if '-' not in option:
            continue
        (id, attr) = option.split('-')
        attr = attr.lower()
        attributes = {}
        if id in definitions:
            attributes = definitions[id]
            
        if attr in fields:
            attributes[attr] = config.get(section, option).lower()
        else:
            attributes[attr] = config.get(section, option).split('|')
        
        definitions[id] = attributes
        
    sets[section] = definitions
        
for s in sets:
    print s
    Set = sets[s]
    for d in Set:
        print ' ', d
        definitions = Set[d]
        for a in definitions:
            if a not in fields:
                print '   ', a + '=' + '/'.join(definitions[a])
            else:
                print '   ', a + '=' + definitions[a]

