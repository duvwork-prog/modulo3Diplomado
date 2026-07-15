"""Task: CompleteCheckout — completa el flujo de checkout en SauceDemo."""

from __future__ import annotations
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from screenplay.abilities.browse_web import BrowseTheWeb


class CompleteCheckout:
    """Tarea de alto nivel: navegar al carrito, abrir checkout y rellenar datos."""

    def __init__(self, first: str, last: str, zip_code: str) -> None:
        self._first = first
        self._last = last
        self._zip_code = zip_code

    @classmethod
    def with_info(cls, first: str, last: str, zip_code: str) -> "CompleteCheckout":
        """Constructor expresivo: CompleteCheckout.with_info('John', 'Doe', '12345')."""
        return cls(first, last, zip_code)

    def perform_as(self, actor) -> None:
        """Orquesta el flujo de checkout usando las abilities del Actor."""
        page = actor.ability_to(BrowseTheWeb).page
        
        InventoryPage(page).go_to_cart()
        CartPage(page).proceed_to_checkout()
        CheckoutPage(page).fill_shipping(
            self._first,
            self._last,
            self._zip_code,
        ).continue_to_overview()