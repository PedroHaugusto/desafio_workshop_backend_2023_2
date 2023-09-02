from rest_framework import routers
from .views import FuncionarioViewset, DepartamentoViewset

router = routers.DefaultRouter()
router.register(r'departamento', DepartamentoViewset)
router.register(r'funcionario', FuncionarioViewset)
urlpatterns = router.urls