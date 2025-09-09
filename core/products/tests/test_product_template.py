import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestProductTemplate:

    # Product list template test
    def test_product_template_view(self, authenticated_worker):
        client = authenticated_worker
        url = reverse("template-products:list")
        response = client.get(url)
        assert response.status_code == 200
        assert "products/list.html" in [template.name for template in response.templates]