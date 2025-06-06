from pyramid.view import view_config
from pyramid.response import Response
from sqlalchemy.exc import SQLAlchemyError



@view_config(route_name="index", renderer="languapedia:templates/index.html")
def index_view(request):
    return {"project": "Languapedia"}

