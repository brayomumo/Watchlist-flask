import os


class Config:

    MOVIE_API_BASE_URL = 'https://api.themoviedb.org/3/movie/{}?api_key={}'
    MOVIE_API_KEY = os.environ.get('MOVIE_API_KEY')
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://smoucha:mumo@localhost/watchlist'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    #email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS= True
    MAIL_USERNAMES = os.environ.get('brayomumo5@gmail.com')
    MAIL_PASSWORD = os.environ.get('mumobrayo5')
    
    @staticmethod
    def init_app(app):
        pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production': ProdConfig

}