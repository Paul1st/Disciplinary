# REA Disciplinary

Disciplinary case management for the Rural Electrification Authority, built on Frappe HR (v15).
Extracted from the REA dev site (`frappe.local`) on 2026-10-15 as a standalone app.

## What's in it

**DocTypes** (module `REA Disciplinary`)

| DocType | Role |
|---|---|
| Disciplinary | The case (submittable, 20-state workflow) |
| Disciplinary Charges | Charges table on the case |
| Verdict / Appeal Verdict | Hearing outcome and appeal outcome tables |
| Hearing Commitee / Appeal Committee | Panel member tables |
| Offence Category / Offence Master / Offence Sanction Matrix | Offence and sanction masters |
| Forced Leave | Forced leave linked to a disciplinary case (own workflow) |

**Fixtures** (`rea_disciplinary/fixtures/`)

- Workflows `Disciplinary` and `Forced Leave` + their Workflow States and Action Masters
- Server Scripts: DocType events (deadlines, committee composition / grade-band rules, mandatory charge, emails, case closure),
  permission queries, and `Daily Scheduler` (exculpation / hearing / appeal reminders, warning expiry)
- Client Scripts, Custom Fields, Property Setters, Custom DocPerms for the doctypes above
- Notifications (40), Print Format `Disciplinary Report`, Reports (Active Employee Warnings, Disciplinary action,
  Employees on Disciplinary Action), Number Card, Dashboard Chart
- Roles: Chief Executive Officer, Director HRA, Disciplinary Board Member, HRO Employment, HRO Welfare,
  Head of Department, Manager HRA, Supervisor
- Master data: Offence Category (6), Offence Master (54), Offence Sanction Matrix (120)

Disabled scripts are included as they are on the site (still disabled).

## Not included

- **Employee Grade records** (REA1–REA10) used by the committee grade-band rules: standard HRMS doctype tied to salary structures; set up per site.
- **Material Request → Disciplinary**: the "missing materials" auto-draft cases and the two Material Request link fields live in the `fifo` Material Request override.
- Recruitment API scripts `shortlist_job_applicants` / `reject_job_applicants` (tagged Disciplinary on the site but unrelated).

## Installing

On the REA dev site these doctypes currently run from untracked files inside `apps/hrms` (module HR).
Install this app only on a bench whose hrms does **not** contain those folders, otherwise the doctypes will clash.

```bash
bench get-app <repo-url>
bench --site <site> install-app rea_disciplinary
```

Requires: frappe, erpnext, hrms (v15).
