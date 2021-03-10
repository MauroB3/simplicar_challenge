from django.core.mail import send_mail


def send_new_lead_email(user_email):
    send_mail(
        'Nuevo lead',
        'Un nuevo lead fue creado con tu email.',
        'noreply@simplicar.com',
        [user_email],
        fail_silently=False,
    )