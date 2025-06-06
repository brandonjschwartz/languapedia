from languapedia import models
from languapedia.views.default import index_view
# from languapedia.views.notfound import notfound_view


def test_my_view_success(app_request):
    info = index_view(app_request)
    assert app_request.response.status_int == 200

#def test_my_view_success(app_request, dbsession):
#    model = models.MyModel(name='one', value=55)
#    dbsession.add(model)
#    dbsession.flush()

#    info = my_view(app_request)
#    assert app_request.response.status_int == 200
#    assert info['one'].name == 'one'
#    assert info['project'] == 'Languapedia'

#def test_notfound_view(app_request):
#    info = notfound_view(app_request)
#    assert app_request.response.status_int == 404
#    assert info == {}
