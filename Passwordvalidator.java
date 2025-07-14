    public class PasswordValidatorTest {
        private PasswordValidator validator = new PasswordValidator();

        @Test
        void testValidPassword() {
            assertTrue(validator.isValid("StrongPass123!"));
        }

        @Test
        void testShortPassword() {
            assertFalse(validator.isValid("short"));
        }

        @Test
        void testNullPassword() {
            assertFalse(validator.isValid(null));
        }
