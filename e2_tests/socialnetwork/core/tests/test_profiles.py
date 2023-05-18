from rest_framework import status
from rest_framework.test import APIClient

class TestCreateProfile:
    def test_if_no_email_return_400(self):
        #Arrange

        #Act
        client = APIClient()
        response = client.post('/profiles/', {})

        #Assert
        assert response.status_code == status.HTTP_400_BAD_REQUEST