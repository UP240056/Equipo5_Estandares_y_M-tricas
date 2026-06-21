import pytest
from pages.SalesNotePage import SalesNotePage

class TestSalesNoteModule:

    # Prueba parametrizada (Data-Driven) para 3 casos de error diferentes
    @pytest.mark.parametrize("customer, product, quantity, expected_error", [
        ("CUST-001", "PROD-ABC", 0, "La cantidad minima a vender debe ser 1"),
        ("CUST-001", "PROD-ABC", -5, "No se permiten cantidades negativas"),
        ("", "PROD-ABC", 2, "El identificador del cliente es obligatorio")
    ])
    def test_sales_note_validation_errors(self, driver, customer, product, quantity, expected_error):
        """Evaluacion parametrica de robustez frente a entradas invalidas o fronteras negativas."""
        sales_note_page = SalesNotePage(driver)
        sales_note_page.navigate_to_module()
        sales_note_page.fill_sales_note_form(customer, product, quantity)
        sales_note_page.submit_sales_note()
        assert sales_note_page.get_error_message() == expected_error

    # Prueba de exito normal
    def test_successful_sales_note_creation(self, driver):
        """Verifica la correcta emision y almacenamiento de una Nota de Venta."""
        sales_note_page = SalesNotePage(driver)
        sales_note_page.navigate_to_module()
        sales_note_page.fill_sales_note_form("CUST-999", "PROD-123", 10)
        sales_note_page.submit_sales_note()
        assert "Nota de venta procesada exitosamente" in sales_note_page.get_success_message()

    # Prueba de valor limite (cantidad exacta = 1)
    def test_boundary_minimum_allowed_quantity(self, driver):
        """Valida la aceptacion e invariabilidad del sistema ante la cantidad minima unitaria permitida (1)."""
        sales_note_page = SalesNotePage(driver)
        sales_note_page.navigate_to_module()
        sales_note_page.fill_sales_note_form("CUST-777", "PROD-XYZ", 1)
        sales_note_page.submit_sales_note()
        assert "Nota de venta procesada exitosamente" in sales_note_page.get_success_message()