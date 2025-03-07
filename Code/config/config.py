import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres.ejolgythkfyrwedfvzlf:avan32J*@aws-0-us-west-1.pooler.supabase.com:6543/postgres')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    JWT_SECRET_KEY = os.getenv('JWT_SECRET_KEY', 'vIsoctONeLeYelADAntErBo')
