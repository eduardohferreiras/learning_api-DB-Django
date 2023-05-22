from rest_framework import status
from rest_framework.test import APIClient

class TestCreateProfile:
    def test_if_no_email_return_400(self):
        #Act
        client = APIClient()
        response = client.post('/profiles/', {})

        #Assert
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_if_invalid_email_return_400(self):
        #Act
        client = APIClient()
        response = client.post('/profiles/', {"email": "invalidEmail"})

        #Assert
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_if_only_valid_email_create_isHidden_false(self):
        #Act
        client = APIClient()
        response = client.post('/profiles/', {"email": "teste@teste.com"})

        #Assert
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['isHidden'] == False

    def test_if_valid_email_and_isHidden_true_create_isHidden_true(self):
        #Act
        client = APIClient()
        response = client.post('/profiles/', {"email": "teste@teste.com", "isHidden":"true"})

        #Assert
        assert response.status_code == status.HTTP_201_CREATED
        assert response.data['isHidden'] == True

class TestPatchProfile:
    def test_if_try_to_update_id_that_dont_exist_return_404(self):
        #Act
        client = APIClient()
        response = client.patch('/profiles/-1', {})

        #Assert
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_if_try_to_update_with_isHidden_not_bool_return_400(self):
        #Act
        client = APIClient()
        response = client.patch('/profiles/1', {"isHidden":"test"})

        #Assert
        assert response.status_code == status.HTTP_400_BAD_REQUEST

    def test_if_try_to_update_with_isHidden_bool_return_200(self):
        #Act
        client = APIClient()
        response = client.patch('/profiles/1', {"isHidden": False}, format='json')

        #Assert
        assert response.status_code == status.HTTP_200_OK
        assert isinstance(response.data['isHidden'], bool)

class TestGetProfileDetails:
    def test_if_profile_id_dont_exist_get_404(self):
        #Act
        client = APIClient()
        response = client.get('/profiles/-1', {})

        #Assert
        assert response.status_code == status.HTTP_404_NOT_FOUND

    def test_if_profile_id_exist_return_id_email_isHidden(self):
        #Act
        client = APIClient()
        response = client.get('/profiles/1', {})

        #Assert
        assert response.status_code == status.HTTP_200_OK
        assert response.data['id'] > 0
        assert response.data['email'].find('@')
        assert isinstance(response.data['isHidden'], bool)
