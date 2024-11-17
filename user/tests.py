from django.contrib.auth import get_user_model
from django.forms import ValidationError
from django.test import TestCase
from django.urls import reverse

from user.forms import LoginForm, UserCreationForm
from user.models import User

User = get_user_model()


class UserModelTests(TestCase):
    """
    Tests for the User model.

    This class contains tests for the User model in user/models.py.
    """

    def test_create_user(self):
        user = User.objects.create_user(
            email="test@example.com",
            password="TESTtest123",
            first_name="John",
            phone="+37012345678",
        )
        self.assertEqual(user.email, "test@example.com")
        self.assertTrue(user.check_password("TESTtest123"))
        self.assertFalse(user.is_staff)
        self.assertTrue(user.is_active)

    def test_create_superuser(self):
        admin_user = User.objects.create_superuser(
            first_name="John", email="testgmail10@gmail.com", phone="+37012345678",  password="TESTtest123"
        )
        self.assertEqual(admin_user.email, "testgmail10@gmail.com")
        self.assertTrue(admin_user.check_password("TESTtest123"))
        self.assertTrue(admin_user.is_staff)
        self.assertTrue(admin_user.is_superuser)

    def test_email_is_normalized(self):
        user = User.objects.create_user(
            first_name="John", email="test@EXAMPLE.com", phone="+37012345678", password="password123"
        )
        self.assertEqual(user.email, "test@example.com")

    def test_user_without_email_raises_error(self):
        with self.assertRaises(ValueError):
            User.objects.create_user(email="", password="password123")


class UserCreationFormTests(TestCase):
    """
    Tests for the UserCreationForm form.

    This class contains tests for the UserCreationForm form in user/forms.py.
    """

    def test_valid_form(self):
        form_data = {
            "email": "testgmail9@gmail.com",
            "first_name": "John",
            "phone": "+37012345678",
            "password1": "TESTtest123",
            "password2": "TESTtest123",
        }
        form = UserCreationForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_email_already_exists(self):
        User.objects.create_user(
            email="testgmail9@gmail.com",
            first_name="John",
            phone="+37012345678",
            password="TESTtest123",
        )
        form_data = {
            "email": "testgmail9@gmail.com",
            "first_name": "John",
            "phone": "+37012345678",
            "password1": "TESTtest123",
            "password2": "TESTtest123",
        }
        form = UserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("email", form.errors)

    def test_phone_already_exists(self):
        User.objects.create_user(
            email="testgmail10@gmail.com",
            first_name="John",
            phone="+37012345678",
            password="TESTtest123",
        )
        form_data = {
            "email": "testgmail9@gmail.com",
            "first_name": "John",
            "phone": "+37012345678",
            "password1": "TESTtest123",
            "password2": "TESTtest123",
        }
        form = UserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("phone", form.errors)

    def test_password_mismatch(self):
        form_data = {
            "email": "testgmail10@gmail.com",
            "first_name": "John",
            "phone": "+37012345678",
            "password1": "TESTtest123",
            "password2": "differentpassword",
        }
        form = UserCreationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("password2", form.errors)


class LoginFormTests(TestCase):
    """
    Tests for the LoginForm form.

    This class contains tests for the LoginForm form in user/forms.py.
    """

    def setUp(self):
        try:
            self.user = User.objects.create_user(
                email="testgmail10@gmail.com",
                first_name="John",
                phone="+37012345678",
                password="TESTtest123",
            )
            self.user.save()
        except ValidationError as e:
            print(e)

    def test_valid_login(self):
        form_data = {
            "email": "testgmail10@gmail.com",
            "password": "TESTtest123",
        }
        form = LoginForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_invalid_login(self):
        form_data = {
            "email": "testgmail10@gmail.com",
            "password": "wrongpassword",
        }
        form = LoginForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn("__all__", form.errors)


class UserViewsTests(TestCase):
    """
    Tests for the user views.

    This class contains tests for the user views in user/views.py.
    """

    def test_register_view(self):
        response = self.client.get(reverse("user:register"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/register.html")

        form_data = {
            "email": "testgmail10@gmail.com",
            "first_name": "John",
            "phone": "+37012345678",
            "password1": "TESTtest123",
            "password2": "TESTtest123",
        }
        response = self.client.post(reverse("user:register"), data=form_data)
        self.assertEqual(
            response.status_code, 302
        )  # Redirect after successful registration
        self.assertTrue(User.objects.filter(email="testgmail10@gmail.com").exists())

    def test_login_view(self):
        User.objects.create_user(
            email="testgmail10@gmail.com",
            password="TESTtest123",
            first_name="John",
            phone="+37012345678",
        )
        response = self.client.get(reverse("user:login"))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "user/login.html")

        form_data = {
            "email": "testgmail10@gmail.com",
            "password": "TESTtest123",
        }
        response = self.client.post(reverse("user:login"), data=form_data)
        self.assertEqual(response.status_code, 302)  # Redirect after successful login

    def test_logout_view(self):
        User.objects.create_user(
            email="testgmail10@gmail.com",
            password="TESTtest123",
            first_name="John",
            phone="+37012345678",
        )
        self.client.login(email="testgmail10@gmail.com", password="TESTtest123")
        response = self.client.get(reverse("user:logout"))
        self.assertEqual(response.status_code, 302)  # Redirect after logout
