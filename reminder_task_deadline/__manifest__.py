{
    "name": "Reminders and Agenda for Tasks",
    "summary": """Allows you to create reminders for tasks.""",
    "category": "Reminders and Agenda",
    # "live_test_url": "",
    "version": "11.0.1.0.0",
    "application": False,

    "author": "IT-Projects LLC, Ivan Yelizariev, Pavel Romanchenko",
    "support": "apps@it-projects.info",
    "website": "https://twitter.com/yelizariev",
    "license": "LGPL-3",
    "price": 21.00,
    "currency": "EUR",

    "depends": [
        "reminder_base",
        "project",
    ],
    "external_dependencies": {"python": [], "bin": []},
    "data": [
        "views/reminder_task_deadline_views.xml",
    ],
    "post_load": None,
    "pre_init_hook": None,
    "post_init_hook": None,
    "uninstall_hook": None,

    "auto_install": False,
    "installable": True,
}
