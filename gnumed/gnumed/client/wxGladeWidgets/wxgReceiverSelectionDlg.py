# -*- coding: UTF-8 -*-
#
# generated by wxGlade
#

import wx

# begin wxGlade: dependencies
import gettext
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class wxgReceiverSelectionDlg(wx.Dialog):
	def __init__(self, *args, **kwds):
		# begin wxGlade: wxgReceiverSelectionDlg.__init__
		kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_DIALOG_STYLE | wx.MAXIMIZE_BOX | wx.MINIMIZE_BOX | wx.RESIZE_BORDER
		wx.Dialog.__init__(self, *args, **kwds)
		self.SetSize(wx.DLG_UNIT(self, wx.Size(360, 255)))
		self._LBL_message_top = wx.StaticText(self, wx.ID_ANY, _("Select the paperwork receiver:"))
		from Gnumed.wxpython.gmTextCtrl import cTextCtrl
		self._TCTRL_final_name = cTextCtrl(self, wx.ID_ANY, "")
		from Gnumed.wxpython.gmAddressWidgets import cAddressPhraseWheel
		self._PRW_other_address = cAddressPhraseWheel(self, wx.ID_ANY, "")
		self._BTN_manage_addresses = wx.Button(self, wx.ID_ANY, _("&Manage"), style=wx.BU_EXACTFIT)
		self._LBL_address_details = wx.StaticText(self, wx.ID_ANY, "")
		self._TCTRL_org_unit_details = wx.TextCtrl(self, wx.ID_ANY, "", style=wx.TE_MULTILINE | wx.TE_READONLY)
		self._LBL_final_name = wx.StaticText(self, wx.ID_ANY, "")
		self._LBL_final_country = wx.StaticText(self, wx.ID_ANY, "")
		self._LBL_final_region = wx.StaticText(self, wx.ID_ANY, "")
		self._LBL_final_zip = wx.StaticText(self, wx.ID_ANY, "")
		self._LBL_final_location = wx.StaticText(self, wx.ID_ANY, "")
		self._LBL_final_street = wx.StaticText(self, wx.ID_ANY, "")
		self._LBL_final_number = wx.StaticText(self, wx.ID_ANY, "")
		from Gnumed.wxpython.gmListWidgets import cReportListCtrl
		self._LCTRL_candidates = cReportListCtrl(self, wx.ID_ANY, style=wx.BORDER_NONE | wx.LC_REPORT | wx.LC_SINGLE_SEL)
		from Gnumed.wxpython.gmOrganizationWidgets import cOrgUnitPhraseWheel
		self._PRW_org_unit = cOrgUnitPhraseWheel(self, wx.ID_ANY, "")
		self._BTN_manage_orgs = wx.Button(self, wx.ID_ANY, _("&Manage"), style=wx.BU_EXACTFIT)
		self._LCTRL_addresses = cReportListCtrl(self, wx.ID_ANY, style=wx.BORDER_NONE | wx.LC_REPORT | wx.LC_SINGLE_SEL)
		self._BTN_OK = wx.Button(self, wx.ID_OK, _("&OK"))
		self._BTN_cancel = wx.Button(self, wx.ID_CANCEL, "")

		self.__set_properties()
		self.__do_layout()

		self.Bind(wx.EVT_BUTTON, self._on_manage_addresses_button_pressed, self._BTN_manage_addresses)
		self.Bind(wx.EVT_LIST_ITEM_SELECTED, self._on_candidate_selected, self._LCTRL_candidates)
		self.Bind(wx.EVT_BUTTON, self._on_manage_orgs_button_pressed, self._BTN_manage_orgs)
		self.Bind(wx.EVT_BUTTON, self._on_ok_button_pressed, id=wx.ID_OK)
		# end wxGlade

	def __set_properties(self):
		# begin wxGlade: wxgReceiverSelectionDlg.__set_properties
		self.SetTitle(_("Letter receiver selection"))
		self.SetSize(wx.DLG_UNIT(self, wx.Size(360, 255)))
		self._TCTRL_final_name.SetToolTip(_("This name will be used.\n\nYou can edit the (or type another) name here, too."))
		self._PRW_other_address.SetToolTip(_("This address will be used.\n\nYou can also search for an arbitrary address in this field."))
		self._BTN_manage_addresses.SetToolTip(_("Manage generic list of all addresses."))
		self._TCTRL_org_unit_details.SetBackgroundColour(wx.SystemSettings.GetColour(wx.SYS_COLOUR_BACKGROUND))
		self._PRW_org_unit.SetToolTip(_("Select the organizational unit you want to write to."))
		self._BTN_manage_orgs.SetToolTip(_("Manage known organizations and units thereof."))
		self._BTN_OK.SetToolTip(_("Use the above name and address."))
		self._BTN_cancel.SetToolTip(_("Abort the receiver selection."))
		# end wxGlade

	def __do_layout(self):
		# begin wxGlade: wxgReceiverSelectionDlg.__do_layout
		__szr_main = wx.BoxSizer(wx.VERTICAL)
		__szr_buttons = wx.BoxSizer(wx.HORIZONTAL)
		__szr_middle = wx.BoxSizer(wx.HORIZONTAL)
		__szr_selections = wx.BoxSizer(wx.VERTICAL)
		__szr_org_unit = wx.BoxSizer(wx.HORIZONTAL)
		__szr_final_address = wx.BoxSizer(wx.VERTICAL)
		__fgszr_final = wx.FlexGridSizer(7, 2, 2, 3)
		__fgszr_selected = wx.FlexGridSizer(3, 2, 2, 3)
		__szr_main.Add(self._LBL_message_top, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.LEFT | wx.RIGHT, 3)
		__lbl_name = wx.StaticText(self, wx.ID_ANY, _("Name"))
		__fgszr_selected.Add(__lbl_name, 0, wx.ALIGN_CENTER_VERTICAL, 5)
		__fgszr_selected.Add(self._TCTRL_final_name, 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 3)
		__lbl_address_search = wx.StaticText(self, wx.ID_ANY, _("Address"))
		__fgszr_selected.Add(__lbl_address_search, 0, wx.ALIGN_CENTER_VERTICAL, 5)
		__fgszr_selected.Add(self._PRW_other_address, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 3)
		__fgszr_selected.Add((20, 20), 0, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__fgszr_selected.Add(self._BTN_manage_addresses, 0, wx.ALIGN_CENTER, 3)
		__fgszr_selected.AddGrowableCol(1)
		__szr_final_address.Add(__fgszr_selected, 0, wx.BOTTOM | wx.EXPAND, 5)
		__szr_final_address.Add(self._LBL_address_details, 0, wx.EXPAND, 0)
		__szr_final_address.Add(self._TCTRL_org_unit_details, 1, wx.BOTTOM | wx.EXPAND, 5)
		__LBL_receiver_heading = wx.StaticText(self, wx.ID_ANY, _("Selected Receiver"))
		__szr_final_address.Add(__LBL_receiver_heading, 0, wx.ALIGN_CENTER, 0)
		__lbl_final_name = wx.StaticText(self, wx.ID_ANY, _("Name"))
		__lbl_final_name.SetToolTip(_("$<receiver_name::::>$"))
		__fgszr_final.Add(__lbl_final_name, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__fgszr_final.Add(self._LBL_final_name, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__lbl_final_country = wx.StaticText(self, wx.ID_ANY, _("Country"))
		__lbl_final_country.SetToolTip(_(u"address['l10n_country'] \u2192 $<receiver_country::::>$"))
		__fgszr_final.Add(__lbl_final_country, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__fgszr_final.Add(self._LBL_final_country, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__lbl_final_region = wx.StaticText(self, wx.ID_ANY, _("Region"))
		__lbl_final_region.SetToolTip(_(u"address['l10n_region'] \u2192 $<receiver_region::::>$"))
		__fgszr_final.Add(__lbl_final_region, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__fgszr_final.Add(self._LBL_final_region, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__lbl_final_zip = wx.StaticText(self, wx.ID_ANY, _("ZIP"))
		__lbl_final_zip.SetToolTip(_(u"address['postcode'] \u2192 $<receiver_postcode::::>$"))
		__fgszr_final.Add(__lbl_final_zip, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__fgszr_final.Add(self._LBL_final_zip, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__lbl_final_location = wx.StaticText(self, wx.ID_ANY, _("Location"))
		__lbl_final_location.SetToolTip(_(u"address['urb'] \u2192 $<receiver_urb::::>$\naddress['suburb'] \u2192 $<receiver_suburb::::>$"))
		__fgszr_final.Add(__lbl_final_location, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__fgszr_final.Add(self._LBL_final_location, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__lbl_final_street = wx.StaticText(self, wx.ID_ANY, _("Street"))
		__lbl_final_street.SetToolTip(_(u"address['street'] \u2192 $<receiver_street::::>$"))
		__fgszr_final.Add(__lbl_final_street, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__fgszr_final.Add(self._LBL_final_street, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__lbl_final_number = wx.StaticText(self, wx.ID_ANY, _("Number"))
		__lbl_final_number.SetToolTip(_(u"address['number'] \u2192 $<receiver_number::::>$\naddress['subunit'] \u2192 $<receiver_subunit::::>$"))
		__fgszr_final.Add(__lbl_final_number, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__fgszr_final.Add(self._LBL_final_number, 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__fgszr_final.AddGrowableCol(1)
		__szr_final_address.Add(__fgszr_final, 1, 0, 0)
		__szr_middle.Add(__szr_final_address, 2, wx.EXPAND, 5)
		__lbl_quick_picks = wx.StaticText(self, wx.ID_ANY, _("Quick picks"))
		__szr_selections.Add(__lbl_quick_picks, 0, wx.ALIGN_CENTER_HORIZONTAL | wx.BOTTOM, 3)
		__szr_selections.Add(self._LCTRL_candidates, 2, wx.BOTTOM | wx.EXPAND, 2)
		__lbl_org_unit = wx.StaticText(self, wx.ID_ANY, _("Org:"))
		__szr_org_unit.Add(__lbl_org_unit, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)
		__szr_org_unit.Add(self._PRW_org_unit, 1, wx.ALIGN_CENTER_VERTICAL, 0)
		__szr_org_unit.Add(self._BTN_manage_orgs, 0, wx.ALIGN_CENTER_VERTICAL, 0)
		__szr_selections.Add(__szr_org_unit, 0, wx.ALIGN_CENTER_VERTICAL | wx.BOTTOM | wx.EXPAND, 3)
		__szr_selections.Add(self._LCTRL_addresses, 1, wx.EXPAND, 3)
		__szr_middle.Add(__szr_selections, 3, wx.EXPAND | wx.LEFT, 5)
		__szr_main.Add(__szr_middle, 1, wx.BOTTOM | wx.EXPAND | wx.LEFT | wx.RIGHT, 3)
		__szr_buttons.Add((20, 20), 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__szr_buttons.Add(self._BTN_OK, 0, wx.ALIGN_CENTER_VERTICAL | wx.RIGHT, 5)
		__szr_buttons.Add(self._BTN_cancel, 0, wx.ALIGN_CENTER_VERTICAL | wx.LEFT, 5)
		__szr_buttons.Add((20, 20), 1, wx.ALIGN_CENTER_VERTICAL | wx.EXPAND, 0)
		__szr_main.Add(__szr_buttons, 0, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.TOP, 3)
		self.SetSizer(__szr_main)
		self.Layout()
		# end wxGlade

	def _on_manage_addresses_button_pressed(self, event):  # wxGlade: wxgReceiverSelectionDlg.<event_handler>
		print("Event handler '_on_manage_addresses_button_pressed' not implemented!")
		event.Skip()

	def _on_candidate_selected(self, event):  # wxGlade: wxgReceiverSelectionDlg.<event_handler>
		print("Event handler '_on_candidate_selected' not implemented!")
		event.Skip()

	def _on_manage_orgs_button_pressed(self, event):  # wxGlade: wxgReceiverSelectionDlg.<event_handler>
		print("Event handler '_on_manage_orgs_button_pressed' not implemented!")
		event.Skip()

	def _on_ok_button_pressed(self, event):  # wxGlade: wxgReceiverSelectionDlg.<event_handler>
		print("Event handler '_on_ok_button_pressed' not implemented!")
		event.Skip()

# end of class wxgReceiverSelectionDlg
