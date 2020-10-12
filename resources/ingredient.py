from flask import Response, request
from flask_jwt_extended import jwt_required, get_jwt_identity
from database.models import Ingredient, User
from flask_restful import Resource
from mongoengine.errors import FieldDoesNotExist, NotUniqueError, DoesNotExist, ValidationError, InvalidQueryError
from resources.errors import SchemaValidationError, IngredientAlreadyExistsError, InternalServerError, UpdatingIngredientError, DeletingIngredientError, IngredientNotExistsError


class IngredientsApi(Resource):
    def get(self):
        ingredients = Ingredient.objects().to_json()
        return Response(ingredients, mimetype="application/json", status=200)

    @jwt_required
    def post(self):
        try:
            user_id = get_jwt_identity()
            body = request.get_json()
            user = User.objects.get(id = user_id)
            ingredient = Ingredient(**body, added_by = user)
            ingredient.save()
            user.update(push__ingredients=ingredient)
            user.save()
            id = ingredient.id
            return {'id': str(id)}, 200
        except (FieldDoesNotExist, ValidationError):
            raise SchemaValidationError
        except NotUniqueError:
            raise IngredientAlreadyExistsError
        except Exception:
            raise InternalServerError
        
class IngredientApi(Resource):
    @jwt_required
    def put(self, id):
        try:
            user_id = get_jwt_identity()
            ingredient = Ingredient.objects.get(id=id, added_by=user_id)
            body = request.get_json()
            ingredient.update(**body)
            return '', 200
        except InvalidQueryError:
            raise SchemaValidationError
        except DoesNotExist:
            raise UpdatingIngredientError
        except Exception:
            raise InternalServerError 
    
    @jwt_required
    def delete(self, id):
        try:
            user_id = get_jwt_identity()
            ingredient = Ingredient.objects.get(id=id, added_by=user_id)
            ingredient.delete()
            return '', 200
        except DoesNotExist:
            raise DeletingIngredientError
        except Exception:
            raise InternalServerError

    def get(self, id):
        try:
            ingredients = Ingredient.objects.get(id=id).to_json()
            return Response(ingredients, mimetype="application/json", status=200)
        except DoesNotExist:
            raise IngredientNotExistsError
        except Exception:
            raise InternalServerError