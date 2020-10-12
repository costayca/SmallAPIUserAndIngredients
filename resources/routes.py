from .movie import MovieApi, MoviesApi
from .auth import SignupApi, LoginApi
from .ingredient import IngredientApi, IngredientsApi

def initialize_routes(api):
    api.add_resource(MoviesApi, '/api/movies')
    api.add_resource(MovieApi, '/api/movies/<id>')

    api.add_resource(IngredientsApi, '/api/ingredients')
    api.add_resource(IngredientApi, '/api/ingredients/<id>')

    api.add_resource(SignupApi, '/api/auth/signup')
    api.add_resource(LoginApi, '/api/auth/login')