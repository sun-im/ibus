# vim:set et sts=4 sw=4:
#
# ibus - The Input Bus
#
# Copyright (c) 2007-2009 Peng Huang <shawn.p.huang@gmail.com>
# Copyright (c) 2007-2009 Red Hat, Inc.
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this program; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330,
# Boston, MA  02111-1307  USA

import ibus
import dbus

class Application:
    def __init__ (self):
        self._dbusconn = dbus.connection.Connection (ibus.get_address())
        self._dbusconn.add_signal_receiver (self._disconnected_cb,
                            "Disconnected",
                            dbus_interface = dbus.LOCAL_IFACE)

    def _disconnected_cb (self):
        self.on_disconnected ()

    def on_disconnected (self):
        pass

    def run (self):
        pass

