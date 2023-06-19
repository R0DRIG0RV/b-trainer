from rest_framework import routers

from trainer.viewsets import CategoryViewSet, ClientDocumentViewSet, ClientViewSet, DocumentViewSet, NoteViewSet, PlanViewSet, TemplateEmailViewSet

router = routers.SimpleRouter()

router.register(prefix='category', basename='category', viewset=CategoryViewSet)
router.register(prefix='client_document', basename='client_document', viewset=ClientDocumentViewSet)
router.register(prefix='client', basename='client', viewset=ClientViewSet)
router.register(prefix='document', basename='document', viewset=DocumentViewSet)
router.register(prefix='note', basename='note', viewset=NoteViewSet)
router.register(prefix='plan', basename='plan', viewset=PlanViewSet)
router.register(prefix='template_email', basename='template_email', viewset=TemplateEmailViewSet)

urlpatterns = router.urls