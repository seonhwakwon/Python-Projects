from tkinter import *
import tkinter as tk
from tkinter import _Cursor, _Relief, _ScreenUnits, _TakeFocusValue, Misc, messagebox
from typing import Any
from typing_extensions import Literal

import drill50_phonebook_func
import drille50_phonebook_gui

class ParentWindow(Frame):
  def __init__(self, master: Misc | None = None, cnf: dict[str, Any] | None = ..., *, background: str = ..., bd: _ScreenUnits = ..., bg: str = ..., border: _ScreenUnits = ..., borderwidth: _ScreenUnits = ..., class_: str = ..., colormap: Misc | Literal['new', ''] = ..., container: bool = ..., cursor: _Cursor = ..., height: _ScreenUnits = ..., highlightbackground: str = ..., highlightcolor: str = ..., highlightthickness: _ScreenUnits = ..., name: str = ..., padx: _ScreenUnits = ..., pady: _ScreenUnits = ..., relief: _Relief = ..., takefocus: _TakeFocusValue = ..., visual: str | tuple[str, int] = ..., width: _ScreenUnits = ...) -> None:
    super().__init__(master, cnf, background=background, bd=bd, bg=bg, border=border, borderwidth=borderwidth, class_=class_, colormap=colormap, container=container, cursor=cursor, height=height, highlightbackground=highlightbackground, highlightcolor=highlightcolor, highlightthickness=highlightthickness, name=name, padx=padx, pady=pady, relief=relief, takefocus=takefocus, visual=visual, width=width)