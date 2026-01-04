from trytond.tests.test_tryton import ModuleTestCase, with_transaction

class DashboardTestCase(ModuleTestCase):
    "Dashboard Test Case"
    module = 'akademy_dashboard'

    @with_transaction()
    def test_method(self):
        "Test method"
        self.assertTrue(True)

del ModuleTestCase
