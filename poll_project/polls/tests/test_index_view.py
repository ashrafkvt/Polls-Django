import pytest

from django.urls import reverse

@pytest.mark.django_db
def test_index_view(client):
    url = reverse('polls:index')
    response = client.get(url)
    assert response.status_code == 200