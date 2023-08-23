# -*- coding: UTF-8 -*-
#
# generated by wxGlade
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
from Gnumed.wxpython.gmEMRStructWidgets import cEpisodeSelectionPhraseWheel
from Gnumed.wxpython.gmListWidgets import cReportListCtrl
from Gnumed.wxpython.gmPhraseWheel import cPhraseWheel
from Gnumed.wxpython.gmTextCtrl import cTextCtrl
# end wxGlade


class wxgFormDisposalDlg(wx.Dialog):
	def __init__(self, *args, **kwds):
		# begin wxGlade: wxgFormDisposalDlg.__init__
		kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER
		wx.Dialog.__init__(self, *args, **kwds)
		self.SetSize((609, 500))
		self._LBL_msg = wx.StaticText(self, wx.ID_ANY, _("What would you like to do with the following document(s) ?"))
		self._LCTRL_forms = cReportListCtrl(self, wx.ID_ANY, style=wx.BORDER_NONE | wx.LC_REPORT)
		self._BTN_show_forms = wx.Button(self, wx.ID_OPEN, "", style=wx.BU_EXACTFIT)
		self._BTN_delete_forms = wx.Button(self, wx.ID_DELETE, "", style=wx.BU_EXACTFIT)
		self._CHBOX_export = wx.CheckBox(self, wx.ID_ANY, _("to patient export area"))
		self._PRW_episode = cEpisodeSelectionPhraseWheel(self, wx.ID_ANY, "")
		self._TCTRL_soap = cTextCtrl(self, wx.ID_ANY, "")
		self._BTN_print = wx.Button(self, wx.ID_PRINT, "")
		self._BTN_remote_print = wx.Button(self, wx.ID_ANY, _("Print &queue"))
		self._BTN_export = wx.Button(self, wx.ID_ANY, _("&Export only"))
		self._BTN_archive = wx.Button(self, wx.ID_ANY, _("&Archive only"))
		self._BTN_cancel = wx.Button(self, wx.ID_CANCEL, "")

		self.__set_properties()
		self.__do_layout()

		self.Bind(wx.EVT_BUTTON, self._on_show_forms_button_pressed, self._BTN_show_forms)
		self.Bind(wx.EVT_BUTTON, self._on_delete_forms_button_pressed, self._BTN_delete_forms)
		self.Bind(wx.EVT_BUTTON, self._on_print_button_pressed, self._BTN_print)
		self.Bind(wx.EVT_BUTTON, self._on_remote_print_button_pressed, self._BTN_remote_print)
		self.Bind(wx.EVT_BUTTON, self._on_export_button_pressed, self._BTN_export)
		self.Bind(wx.EVT_BUTTON, self._on_archive_button_pressed, self._BTN_archive)
		# end wxGlade

	def __set_properties(self):
		# begin wxGlade: wxgFormDisposalDlg.__set_properties
		self.SetTitle(_("Form handling"))
		self.SetSize((609, 500))
		self._BTN_show_forms.SetToolTip(_("Show the selected form(s)."))
		self._BTN_delete_forms.SetToolTip(_("Delete the selected forms from the list."))
		self._CHBOX_export.SetToolTip(_("Check here to put a copy into the export area."))
		self._PRW_episode.SetToolTip(_("Select episode under which to archive a copy of the document(s)."))
		self._TCTRL_soap.SetToolTip(_("Enter a SOAP note to be put into the chart."))
		self._BTN_print.SetToolTip(_("Print document(s)\n(optionally copy to archive and export area)"))
		self._BTN_remote_print.SetToolTip(_("Save document(s) into print queue for printing elsewhere.\n(optionally copy to archive and export area)"))
		self._BTN_export.SetToolTip(_("Put into export area only.\n(no printing, no archiving)"))
		self._BTN_archive.SetToolTip(_("Put copy into archive only.\n(no printing, no export area)"))
		self._BTN_cancel.SetToolTip(_("Cancel any actions and close dialog."))
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: wxgFormDisposalDlg.__do_layout
		__szr_main = wx.BoxSizer(wx.VERTICAL)
		__szr_buttons = wx.BoxSizer(wx.HORIZONTAL)
		__szr_grid = wx.FlexGridSizer(3, 2, 2, 2)
		__szr_forms = wx.BoxSizer(wx.HORIZONTAL)
		__szr_forms_buttons = wx.BoxSizer(wx.VERTICAL)
		__szr_main.Add(self._LBL_msg, 0, wx.ALL | wx.EXPAND, 3)
		__szr_forms.Add(self._LCTRL_forms, 1, wx.EXPAND | wx.RIGHT, 5)
		__szr_forms_buttons.Add((20, 20), 1, wx.EXPAND, 0)
		__szr_forms_buttons.Add(self._BTN_show_forms, 0, wx.ALIGN_CENTER, 0)
		__szr_forms_buttons.Add(self._BTN_delete_forms, 0, wx.ALIGN_CENTER | wx.TOP, 3)
		__szr_forms_buttons.Add((20, 20), 1, wx.EXPAND, 0)
		__szr_forms.Add(__szr_forms_buttons, 0, wx.EXPAND, 0)
		__szr_main.Add(__szr_forms, 1, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 3)
		__lbl_export = wx.StaticText(self, wx.ID_ANY, _("Export"))
		__szr_grid.Add(__lbl_export, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__szr_grid.Add(self._CHBOX_export, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__lbl_episode = wx.StaticText(self, wx.ID_ANY, _("Episode"))
		__szr_grid.Add(__lbl_episode, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__szr_grid.Add(self._PRW_episode, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__lbl_soap = wx.StaticText(self, wx.ID_ANY, _("Note"))
		__szr_grid.Add(__lbl_soap, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__szr_grid.Add(self._TCTRL_soap, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__szr_grid.AddGrowableCol(1)
		__szr_main.Add(__szr_grid, 1, wx.ALL | wx.EXPAND, 3)
		__szr_buttons.Add((20, 20), 2, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__szr_buttons.Add(self._BTN_print, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)
		__szr_buttons.Add(self._BTN_remote_print, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)
		__szr_buttons.Add(self._BTN_export, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)
		__szr_buttons.Add(self._BTN_archive, 0, wx.ALIGN_CENTER, 0)
		__szr_buttons.Add((20, 20), 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__szr_buttons.Add(self._BTN_cancel, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__szr_buttons.Add((20, 20), 2, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__szr_main.Add(__szr_buttons, 0, wx.ALL | wx.EXPAND, 3)
		self.SetSizer(__szr_main)
		self.Layout()
		# end wxGlade

	def _on_show_forms_button_pressed(self, event):  # wxGlade: wxgFormDisposalDlg.<event_handler>
		print("Event handler '_on_show_forms_button_pressed' not implemented!")
		event.Skip()

	def _on_delete_forms_button_pressed(self, event):  # wxGlade: wxgFormDisposalDlg.<event_handler>
		print("Event handler '_on_delete_forms_button_pressed' not implemented!")
		event.Skip()

	def _on_print_button_pressed(self, event):  # wxGlade: wxgFormDisposalDlg.<event_handler>
		print("Event handler '_on_print_button_pressed' not implemented!")
		event.Skip()

	def _on_remote_print_button_pressed(self, event):  # wxGlade: wxgFormDisposalDlg.<event_handler>
		print("Event handler '_on_remote_print_button_pressed' not implemented!")
		event.Skip()

	def _on_export_button_pressed(self, event):  # wxGlade: wxgFormDisposalDlg.<event_handler>
		print("Event handler '_on_export_button_pressed' not implemented!")
		event.Skip()

	def _on_archive_button_pressed(self, event):  # wxGlade: wxgFormDisposalDlg.<event_handler>
		print("Event handler '_on_archive_button_pressed' not implemented!")
		event.Skip()

# end of class wxgFormDisposalDlg
