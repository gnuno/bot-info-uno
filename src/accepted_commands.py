import src.handlers as h

accepted_commands = [
    'start',
    'help',
    'ayuda',
    'links',
    'siu',
    'campus',
    'comunidades_it',
    'comunidades',
    'calendar',
    'calendario',
    'mails',
]

handlers = {
    'start': h.send_welcome,
    'help': h.help_message,
    'ayuda': h.help_message,
    'links': h.get_useful_links,
    'siu': h.request_url_information,
    'campus': h.request_url_information,
    'comunidades_it': h.get_comunidades_it,
    'comunidades': h.get_comunidades_it,
    'calendar': h.get_academic_calendar,
    'calendario': h.get_academic_calendar,
    'mails': h.get_emails,
    'welcome': h.welcome_new_user
}
