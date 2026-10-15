app_name = "rea_disciplinary"
app_title = "REA Disciplinary"
app_publisher = "Rural Electrification Authority"
app_description = "REA disciplinary case management: charges, hearings, verdicts, appeals, offence and sanction masters, forced leave"
app_email = "kundapaul61@gmail.com"
app_license = "mit"
required_apps = ["frappe", "erpnext", "hrms"]

# All runtime logic (DocType events, permission queries, the daily reminder job)
# ships as Server Scripts and Client Scripts in fixtures/, matching how it runs on the dev site.

fixtures = [
	{
		"dt": "Custom Field",
		"filters": [["name", "in", ["Disciplinary Action-workflow_state", "Disciplinary-custom_closed_from_stage", "Disciplinary-custom_closed_on", "Disciplinary-custom_closure_col", "Disciplinary-custom_closure_detail", "Disciplinary-custom_closure_outcome", "Disciplinary-custom_closure_section", "Disciplinary-custom_employee_notify_email", "Disciplinary-custom_offender_grade", "Disciplinary-custom_supervisor_notify_email", "Forced Leave-workflow_state", "Hearing Commitee-custom_board_member"]]],
	},
	{
		"dt": "Property Setter",
		"filters": [["name", "in", ["Appeal Verdict-appeal_decision-mandatory_depends_on", "Disciplinary Charges-comments-read_only_depends_on", "Disciplinary Charges-specific_offence-mandatory_depends_on", "Disciplinary Charges-specific_offence-read_only_depends_on", "Disciplinary Charges-warning_expiry_date-read_only", "Disciplinary-appeal_committee_chairperson-read_only_depends_on", "Disciplinary-appeal_committee_section-depends_on", "Disciplinary-appeal_date-placeholder", "Disciplinary-appeal_date-read_only_depends_on", "Disciplinary-appeal_decision-read_only_depends_on", "Disciplinary-appeal_hearing_report-mandatory_depends_on", "Disciplinary-appeal_hearing_report-read_only_depends_on", "Disciplinary-appeal_members-read_only_depends_on", "Disciplinary-appeal_tab-depends_on", "Disciplinary-appeal_time-read_only_depends_on", "Disciplinary-appeal_venue-read_only_depends_on", "Disciplinary-appeal_verdict-read_only_depends_on", "Disciplinary-case_summary-ignore_xss_filter", "Disciplinary-case_summary-options", "Disciplinary-case_summary_tab-depends_on", "Disciplinary-charge_description-allow_in_quick_entry", "Disciplinary-charge_description-description", "Disciplinary-charge_description-mandatory_depends_on", "Disciplinary-charge_description-placeholder", "Disciplinary-charge_description-read_only_depends_on", "Disciplinary-charge_tab-depends_on", "Disciplinary-details_tab-read_only_depends_on", "Disciplinary-employee-in_list_view", "Disciplinary-employee-read_only_depends_on", "Disciplinary-employee_name-in_list_view", "Disciplinary-employee_response-depends_on", "Disciplinary-employee_response-mandatory_depends_on", "Disciplinary-employee_response-read_only_depends_on", "Disciplinary-exculpation_tab-depends_on", "Disciplinary-exculpation_tab-read_only_depends_on", "Disciplinary-grounds_for_appeal-read_only_depends_on", "Disciplinary-hearing-read_only_depends_on", "Disciplinary-hearing_date-in_list_view", "Disciplinary-hearing_date-mandatory_depends_on", "Disciplinary-hearing_date-read_only_depends_on", "Disciplinary-hearing_decision-mandatory_depends_on", "Disciplinary-hearing_decision-read_only_depends_on", "Disciplinary-hearing_outcome-mandatory_depends_on", "Disciplinary-hearing_outcome-read_only_depends_on", "Disciplinary-hearing_outcome_section-depends_on", "Disciplinary-hearing_report-mandatory_depends_on", "Disciplinary-hearing_report-read_only_depends_on", "Disciplinary-hearing_response_deadline-read_only_depends_on", "Disciplinary-hearing_summary-mandatory_depends_on", "Disciplinary-hearing_summary-read_only_depends_on", "Disciplinary-hearing_tab-depends_on", "Disciplinary-hearing_time-read_only_depends_on", "Disciplinary-hearing_venue-default", "Disciplinary-hearing_venue-mandatory_depends_on", "Disciplinary-hearing_venue-placeholder", "Disciplinary-hearing_venue-read_only_depends_on", "Disciplinary-main-field_order", "Disciplinary-reports_and_attachments_section-depends_on", "Disciplinary-response_document-depends_on", "Disciplinary-response_document-read_only_depends_on", "Disciplinary-section_break_ieyi-depends_on", "Disciplinary-section_break_mkzn-depends_on", "Disciplinary-section_break_thtd-depends_on", "Disciplinary-select_outcome-depends_on", "Disciplinary-select_outcome-label", "Disciplinary-select_outcome-mandatory_depends_on", "Disciplinary-select_outcome-options", "Disciplinary-select_outcome-read_only", "Disciplinary-select_outcome-read_only_depends_on", "Disciplinary-set_appeal_date_section-depends_on", "Disciplinary-set_hearing_date_section-depends_on", "Disciplinary-supervisor_satisfactory_reason-depends_on", "Disciplinary-supervisor_satisfactory_reason-mandatory_depends_on", "Disciplinary-warning-depends_on", "Disciplinary-warning-fieldtype", "Disciplinary-warning-mandatory_depends_on", "Disciplinary-warning-read_only_depends_on", "Verdict-verdict-mandatory_depends_on"]]],
	},
	{
		"dt": "Client Script",
		"filters": [["name", "in", ["Action Buttons on Disciplinary", "Custom Html Block", "Disciplinary", "Disciplinary Action (1st try)", "Disciplinary Committee Grade Filter", "Disciplinary Filtering", "Disciplinary Main", "Disciplinary Offence Filter", "Filter Supervisor Only report to", "Forced Leave Days", "Forced leave", "Forced leave disciplinary dropdown", "Guidance Banner", "Guidance Banner 2", "Locking fields Disciplinary", "No duplicate committee Entries", "State Guideline Banner", "State-based mandatory Fields", "Tab Unveiling", "Test 1 Disciplinary", "Test 2 Disciplinary", "Visual Indicator", "visual higlighting"]]],
	},
	{
		"dt": "Server Script",
		"filters": [["name", "in", ["Appeal Committe", "Auto-calculate Appeal Response Deadline (Invite Committee)", "Auto-calculate Hearing Response Deadline (Invite Committee)", "Auto-calculate response deadline on Issue Charge", "Charge → Hearing Outcome", "Daily Scheduler", "Disciplinary Case Closure", "Disciplinary Committee Composition", "Employee Restricted Disciplinary Views", "Forced leave register", "Hearing Outcome → Appeal Verdict", "Issue Charge → Email to Employee", "No duplicate Committe", "Require charge before leaving Charge stage", "Set Hearing Date → Appeal Email", "Set Hearing Date → Email to Committee Members", "Summary dismisal", "Sync Notification Emails", "Workflow Approval Filter - Disciplinary"]]],
	},
	{
		"dt": "Print Format",
		"filters": [["name", "in", ["Disciplinary Report"]]],
	},
	{
		"dt": "Report",
		"filters": [["name", "in", ["Active Employee Warnings", "Disciplinary action", "Employees on Disciplinary Action"]]],
	},
	{
		"dt": "Notification",
		"filters": [["name", "in", ["DISC – Appeal Outcome – Email", "DISC – Appeal Requested – Email", "DISC – Appeal Under Review – Email", "DISC – Awaiting Employee Decision – Email", "DISC – Awaiting Exculpation – Email", "DISC – Case Closed – Email", "DISC – Charge Initiated – Email", "DISC – Disciplinary Committee – Email", "DISC – Exculpation Evaluation – Email", "DISC – Grounds for Appeal – Email", "DISC – Hearing Outcome – Email", "DISC – Issue Charge – Email", "DISC – Issue Warning – Email", "DISC – Pending CEO Approval – Email", "DISC – Pending Outcome Approval – Email", "DISC – Recommend Disciplinary Hearing – Email", "DISC – Recommendation of Charge – Email", "DISC – Set Appeal Date – Email", "DISC – Set Hearing Date – Email", "Disciplinary Notification", "Disciplinary — Appeal Outcome", "Disciplinary — Appeal Requested", "Disciplinary — Appeal Under Review", "Disciplinary — Awaiting Employee Decision", "Disciplinary — Awaiting Exculpation", "Disciplinary — Case Closed", "Disciplinary — Charge", "Disciplinary — Disciplinary Committee", "Disciplinary — Draft", "Disciplinary — Exculpation Evaluation", "Disciplinary — Grounds for Appeal", "Disciplinary — Hearing Outcome", "Disciplinary — Issue Charge", "Disciplinary — Issue Warning", "Disciplinary — Pending CEO Approval", "Disciplinary — Pending Outcome Approval", "Disciplinary — Recommend Disciplinary Hearing", "Disciplinary — Recommendation of Charge", "Disciplinary — Set Appeal Date", "Disciplinary — Set Hearing Date"]]],
	},
	{
		"dt": "Custom DocPerm",
		"filters": [["name", "in", ["0phvr0mlb7", "14n9qtbcav", "577mps0av9", "578jphsgnu", "7sksds86sd", "8p7hmv6793", "b9h50l6hia", "bepn9ufb8f", "bjs91t4lc2", "bjtd5hqtqc", "ev3dtgki2o", "f2l49gn507", "f2l8k12o83", "g2vt75gih1", "o6isrbm33f", "one51bn5b9", "qee4lrmajf", "rr0ebl8eld", "rr1nv10esm", "sdt86sdcgj", "thi3ikail5", "tovbq81eau"]]],
	},
	{
		"dt": "Workflow",
		"filters": [["name", "in", ["Disciplinary", "Forced Leave"]]],
	},
	{
		"dt": "Workflow State",
		"filters": [["name", "in", ["Appeal Outcome", "Appeal Requested", "Appeal Under Review", "Approved", "Awaiting Employee Decision", "Awaiting Exculpation", "Case Closed", "Charge", "Disciplinary Committee", "Draft", "Exculpation Evaluation", "Grounds for Appeal", "Hearing Outcome", "Issue Charge", "Issue Warning", "Pending CEO Approval", "Pending HOD Approval", "Pending Manager HR Approval", "Pending Outcome Approval", "Pending Supervisor Approval", "Recommend Disciplinary Hearing", "Recommendation of Charge", "Rejected", "Set Appeal Date", "Set Hearing Date"]]],
	},
	{
		"dt": "Workflow Action Master",
		"filters": [["name", "in", ["Accept Verdict", "Appeal Verdict", "Approve", "Close Case", "Committee Appointed", "HOD approval", "Invite Committee", "Issue Charge", "Issue Warning", "Manager HR Approval", "Non Satisfactory and Dismissible", "Recommend Charge", "Reject", "Satisfactory and Not Dismissible", "Send", "Submit", "Submit Response", "Supervisor Approval"]]],
	},
	{
		"dt": "Role",
		"filters": [["name", "in", ["Chief Executive Officer", "Director HRA", "Disciplinary Board Member", "HRO Employment", "HRO Welfare", "Head of Department", "Manager HRA", "Supervisor"]]],
	},
	{
		"dt": "Number Card",
		"filters": [["name", "in", ["? Pending Disciplinary Cases"]]],
	},
	{
		"dt": "Dashboard Chart",
		"filters": [["name", "in", ["Disciplinary"]]],
	},
	"Offence Category",
	"Offence Master",
	"Offence Sanction Matrix",
]
