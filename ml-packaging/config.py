# create a configurable file 


class Config: # base class 
  DEBUG = False
  TESTING = False
  DATABASE_URI = 'sqlite:///:memory:'
  LOG_LEVEL = 'DEBUG'
  LOG_FILE_PATH = 'app.log'
  SECRET_KEY = 'mysecretkey'
  SECRET_COOKIES = 'mysecretcookies'
  API_ENDPOINT = 'https://api.example.com'

class ProductionConfig(Config):
  DATABASE_URI = 'mysql://user@localhost/foo'  # MySQL database for production
  LOG_LEVEL = 'INFO'  # Log level set to INFO (less verbose than DEBUG)
  SECRET_KEY = 'mysecretkey-prod'  # Production-specific secret key
  SECRET_COOKIES = 'mysecretcookies'  # Production-specific secret for cookies
  API_ENDPOINT = 'https://api.example.com'  # API endpoint remains the same


class DevelopmentConfig(Config):
  DEBUG = True  # Debugging enabled for development
  LOG_LEVEL = 'INFO'  # Log level set to INFO
  SECRET_KEY = 'mysecretkey-dev'  # Development-specific secret key
  SECRET_COOKIES = 'mysecretcookies'  # Development-specific secret for cookies
  API_ENDPOINT = 'https://api-dev.example.com'  # API endpoint remains the same


class TestingConfig(Config):
  TESTING = True  # Testing mode enabled
  LOG_LEVEL = 'INFO'  # Log level set to INFO
  SECRET_KEY = 'mysecretkey-test'  # Testing-specific secret key
  SECRET_COOKIES = 'mysecretcookies-test'  # Testing-specific secret for cookies
  API_ENDPOINT = 'https://api-test.example.com'  # API endpoint remains the same

# production testing development env. 

# different stages of your project --> 