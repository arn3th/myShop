from celery import task
from django.core.mail import send_mail
from .models import Order


@task
def order_created(order_id):
    """
    Zadanie wysyłające powiadomienie za pomocą mail'a po zakończonym powodzeniem złożeniem zamówienia.
    :param order_id: numer id zamówienia.
    :return: funkcja wysyłająca maila.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Zamówienie nr {}'.format(order.id)
    message = 'Witaj {}!\n\nZłożyłeś zamówienie w naszym sklepie.' \
              'Numer zamówienia to {}.'.format(order.first_name, order.id)
    mail_sent = send_mail(subject, message, 'admin@myshop.com', [order.email])

    return mail_sent