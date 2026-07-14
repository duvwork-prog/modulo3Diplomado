from __future__ import annotations
from playwright.sync_api import Page


class CheckoutPage:
    """Representa la pantalla de checkout de https://www.saucedemo.com/checkout-step-one.html."""

    BASE_URL = "https://www.saucedemo.com/checkout-step-one.html"

    def __init__(self, page: Page) -> None:
        self.page = page

        # ── Locators: definidos UNA SOLA VEZ ──────────────────────────────
        # Usamos data-test porque son los atributos más estables de la app.
        # Si cambia el HTML pero no el atributo, el test sigue funcionando.
        self._first_name   = page.locator('[data-test="firstName"]')
        self._last_name    = page.locator('[data-test="lastName"]')
        self._postal_code  = page.locator('[data-test="postalCode"]')
        self._continue_btn = page.locator('[data-test="continue"]')


    def fill_shipping(self, first: str, last: str, zip_code: str) -> "CheckoutPage":
        """Rellena los campos de shipping con los datos proporcionados."""
        self._first_name.fill(first)
        self._last_name.fill(last)
        self._postal_code.fill(zip_code)
        return self
    
    def continue_to_overview(self) -> "CheckoutPage":
        """Hace clic en el botón de continuar para ir a la pantalla de overview."""
        self._continue_btn.click()
        return self
    
    def has_error(self) -> bool:
        """True si hay un mensaje de error visible en pantalla."""
        return self.page.locator('[data-test="error"]').is_visible()
