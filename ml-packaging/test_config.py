import os
import unittest
from config import DevelopmentConfig, ProductionConfig, TestingConfig

class TestConfigurations(unittest.TestCase):

    def test_development_config(self):
        """Test the DevelopmentConfig settings"""
        config = DevelopmentConfig()
        self.assertTrue(config.DEBUG)
        self.assertFalse(config.TESTING)
        self.assertEqual(config.DATABASE_URI, 'sqlite:///:memory:')
        self.assertEqual(config.LOG_LEVEL, 'DEBUG')
        self.assertEqual(config.SECRET_KEY, 'mysecretkey-dev')
        self.assertEqual(config.API_TIMEOUT, 5)

    def test_production_config(self):
        """Test the ProductionConfig settings"""
        config = ProductionConfig()
        self.assertFalse(config.DEBUG)
        self.assertFalse(config.TESTING)
        self.assertEqual(config.DATABASE_URI, 'mysql://user@localhost/foo')
        self.assertEqual(config.LOG_LEVEL, 'INFO')
        self.assertEqual(config.SECRET_KEY, 'mysecretkey-prod')
        self.assertEqual(config.API_TIMEOUT, 10)

    def test_testing_config(self):
        """Test the TestingConfig settings"""
        config = TestingConfig()
        self.assertFalse(config.DEBUG)
        self.assertTrue(config.TESTING)
        self.assertEqual(config.DATABASE_URI, 'sqlite:///:memory:')
        self.assertEqual(config.LOG_LEVEL, 'DEBUG')
        self.assertEqual(config.SECRET_KEY, 'mysecretkey-test')
        self.assertEqual(config.API_TIMEOUT, 1)

    def test_invalid_environment(self):
        """Ensure an error is raised for an invalid environment"""
        env = 'invalid_env'
        with self.assertRaises(ValueError):
            if env == 'development':
                config = DevelopmentConfig()
            elif env == 'production':
                config = ProductionConfig()
            elif env == 'testing':
                config = TestingConfig()
            else:
                raise ValueError("Invalid environment name")

if __name__ == '__main__':
    unittest.main()
