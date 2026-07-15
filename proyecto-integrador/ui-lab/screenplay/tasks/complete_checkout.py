"""Task: CompleteCheckout — completa el proceso de pago."""

from __future__ import annotations
from screenplay.abilities.browse_web import BrowseTheWeb
from pages.checkout_page import CheckoutPage

class CompleteCheckout:
    """Tarea de alto nivel: completar el proceso de pago."""

    def __init__(self, first_name: str, last_name: str, postal_code: str) -> None:
        self._first_name = first_name
        self._last_name = last_name
        self._postal_code = postal_code

    @classmethod
    def with_information(cls, first_name: str, last_name: str, postal_code: str) -> "CompleteCheckout":
        """Constructor expresivo: CompleteCheckout.with_information('John', 'Doe', '12345')."""
        return cls(first_name, last_name, postal_code)

    def perform_as(self, actor) -> None:
        page = actor.ability_to(BrowseTheWeb).page
        CheckoutPage(page).fill_shipping(self._first_name, self._last_name, self._postal_code)