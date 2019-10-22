import os

class Config:
  """ configure our environments """
  DEBUG = False

class DevelopmentConfig(Config):
    """Configurations for Development."""
    DEBUG = True

class ProductionConfig(Config):
    """Configurations for Production."""
    DEBUG = False
    TESTING = False

app_config =  {
  'development': DevelopmentConfig ,
  'production': ProductionConfig,
  'default': DevelopmentConfig
}
