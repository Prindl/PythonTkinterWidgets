### GNU General Public License v3
#
# Copyright 2022 Maximilian Prindl
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
# without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License along with this program.
# If not, see <https://www.gnu.org/licenses/>. 

import sys

if sys.version_info.major < 3:
    import Tkinter as tk
else:
    import tkinter as tk

class SelectableLabel(tk.Entry):
    """ An entry that acts like a label to the user and its text is selectable. """

    def __init__(self, parent, **kwargs):
        super(SelectableLabel, self).__init__(parent, **kwargs)
        #Set the widget background to the parent's background and remove the border
        #The border consists of an inner border and an outer highlight
        self.configure(background=parent.cget("bg"), borderwidth=0, highlightthickness=0)
        #Set the widget to readonly to restrict user interaction
        self["state"] = "readonly"

    def set(self, text):
        #Replace the text of the 'label', insert won't work because it is readonly
        self["state"] = "normal"
        self.delete(0, tk.END)
        self.insert(0, text)
        self["state"] = "readonly"

if __name__ == "__main__":
    root = tk.Tk()
    textvar = tk.StringVar()
    textvar.set("Hello World!")
    label = SelectableLabel(root, textvariable=textvar)
    label.pack()
    print(label.get(), textvar.get())
    root.mainloop()
