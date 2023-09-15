import pytest
from django.urls import reverse
from django.contrib.auth.models import User
from .models import kbdocs

@pytest.fixture
def test_user(db):
    user = User.objects.create_user(
        username='ganesh',
        password='ravi',
        email='test@example.com'
    )
    return user

@pytest.mark.django_db
def test_user_registration(client):
    response = client.post(reverse('signup'), {
        'first_name': 'John',
        'last_name': 'Doe',
        'employee_id': 'PSI-2345',
        'email': 'john@gmail.com',
        'password1': 'Test123!',
        'password2': 'Test123!'
    })
    assert response.status_code == 302  # Redirect after successful registration
    assert response.url == reverse('login')

@pytest.mark.django_db
def test_user_registration_validation(client):
    response = client.post(reverse('signup'), {
        'first_name': '',
        'last_name': 'Doe',
        'employee_id': 'InvalidID',
        'email': 'invalid_email',
        'password1': '12345678',
        'password2': '12345678'
    })
    assert response.status_code == 200  # Form validation error
    assert b'This field is required.' in response.content  # Check for validation error messages

@pytest.mark.django_db
def test_user_login(client, test_user):
    response = client.post(reverse('login'), {
        'employee_id': 'T12345',
        'email': 'test@example.com',
        'password': 'testpassword'
    })
    assert response.status_code == 302  # Redirect after successful login
    assert response.url == reverse('dashboard')

@pytest.mark.django_db
def test_user_login_validation(client):
    response = client.post(reverse('login'), {
        'employee_id': 'InvalidID',
        'email': 'invalid_email',
        'password': 'invalidpassword'
    })
    assert response.status_code == 200  # Form validation error
    assert b'Please enter a valid Employee ID and Email.' in response.content  # Check for validation error messages

@pytest.mark.django_db
def test_add_kb_doc(client, test_user):
    client.login(username='testuser', password='testpassword')
    response = client.post(reverse('add_kb_doc'), {
        'tool': 'pyATS',
        'reporter': 'John Doe',
        'created_datetime': '2023-09-14T12:00:00Z',
        'closed_datetime': '2023-09-15T12:00:00Z',
        'source_of_ticket': 'STS',
        'ticket_link': 'https://example.com/ticket',
        'Issue Type': 'fgsg',
         'Issue Title':'sfgg',
        'Issue Description':'fgsh',
        'Category':'tyru',
        'Help Links':'ufhg',
        'Resolutions':'csfs',
        'Workaround':'xfgg',
        'Others':'fsgsh'
    })
    assert response.status_code == 302  # Redirect after successful KB doc creation
    assert response.url == reverse('dashboard')

# Add more test cases for viewing, editing, and searching KB docs as described earlier.
