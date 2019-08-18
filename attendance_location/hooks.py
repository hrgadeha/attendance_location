# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "attendance_location"
app_title = "Attendance Location"
app_publisher = "Hardik Gadesha"
app_description = "App for track location in Attendance Documnet"
app_icon = "octicon octicon-file-directory"
app_color = "cyan"
app_email = "hardikgadesha@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/attendance_location/css/attendance_location.css"
# app_include_js = "/assets/attendance_location/js/attendance_location.js"

# include js, css files in header of web template
# web_include_css = "/assets/attendance_location/css/attendance_location.css"
# web_include_js = "/assets/attendance_location/js/attendance_location.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "attendance_location.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "attendance_location.install.before_install"
# after_install = "attendance_location.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "attendance_location.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

fixtures = [
    {
        "doctype": "Property Setter",
        "filters": [
            [
                "name",
                "in",
                [
			"Attendance-latitude-read_only",
                        "Attendance-longitude-read_only",
		]
	   ]
	]
    },
    {
        "doctype": "Custom Field",
        "filters": [
            [
                "name",
                "in",
                [
                        "Attendance-section_break_12",
			"Attendance-location",
			"Attendance-latitude",
			"Attendance-longitude",
			"Attendance-google_map",
                ]
            ]
        ]
    },
    {
	"doctype": "Custom Script",
        "filters": [
            [
                "name",
                "in",
                [
                        "Attendance-Client",
                ]
            ]
        ]
 }
]

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"attendance_location.tasks.all"
# 	],
# 	"daily": [
# 		"attendance_location.tasks.daily"
# 	],
# 	"hourly": [
# 		"attendance_location.tasks.hourly"
# 	],
# 	"weekly": [
# 		"attendance_location.tasks.weekly"
# 	]
# 	"monthly": [
# 		"attendance_location.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "attendance_location.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "attendance_location.event.get_events"
# }

