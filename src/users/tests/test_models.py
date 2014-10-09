
from django import test
from django.contrib.auth import models as auth_models
from django.core import mail
from users import models


class UserManagerTests(test.TestCase):

    def setUp(self):
        self.sut = models.UserManager

    def test_subclasses_base_user_manager(self):
        self.assertTrue(issubclass(self.sut, auth_models.BaseUserManager))

    def test_creates_user(self):
        email = "johnny@example.com"
        models.User.objects._create_user(email, "pswd", True, False, first_name="Johnny", last_name="Tester")

        created_user = models.User.objects.get(email=email)
        self.assertEqual("Johnny", created_user.first_name)
        self.assertEqual("Tester", created_user.last_name)
        self.assertEqual(True, created_user.is_staff)
        self.assertEqual(False, created_user.is_superuser)
        self.assertEqual(True, created_user.check_password("pswd"))

    def test_creates_regular_user(self):
        email = "johnny@example.com"
        models.User.objects.create_user(email, "pswd", first_name="Johnny", last_name="Tester")

        created_user = models.User.objects.get(email=email)
        self.assertEqual("Johnny", created_user.first_name)
        self.assertEqual("Tester", created_user.last_name)
        self.assertEqual(False, created_user.is_staff)
        self.assertEqual(False, created_user.is_superuser)
        self.assertEqual(True, created_user.check_password("pswd"))

    def test_creates_superuser(self):
        email = "johnny@example.com"
        models.User.objects.create_superuser(email, "pswd", first_name="Johnny", last_name="Tester")

        created_user = models.User.objects.get(email=email)
        self.assertEqual("Johnny", created_user.first_name)
        self.assertEqual("Tester", created_user.last_name)
        self.assertEqual(True, created_user.is_staff)
        self.assertEqual(True, created_user.is_superuser)
        self.assertEqual(True, created_user.check_password("pswd"))


class UserModelTests(test.TestCase):

    def setUp(self):
        self.sut = models.User

    def test_uses_user_manager(self):
        self.assertIsInstance(self.sut.objects, models.UserManager)

    def test_subclasses_abstract_base_user(self):
        self.assertTrue(issubclass(self.sut, auth_models.AbstractBaseUser))

    def test_subclasses_auth_permission_mixin(self):
        self.assertTrue(issubclass(self.sut, auth_models.PermissionsMixin))

    def test_get_full_name_returns_first_and_last_name(self):
        user = self.sut(first_name="Johnny", last_name="Tester")
        self.assertEqual("Johnny Tester", user.get_full_name())

    def test_get_short_name_returns_first_name_only(self):
        user = self.sut(first_name="Johnny", last_name="Tester")
        self.assertEqual("Johnny", user.get_short_name())

    def test_send_email_emails_user(self):
        user = self.sut(first_name="Johnny", last_name="Tester", email="johnny@example.com")
        subject = "Test Email"
        email_message = "This is only a test"
        from_email = "admin@pyowa.org"
        user.email_user(subject, email_message, from_email=from_email)

        self.assertEqual(1, len(mail.outbox))
        msg = mail.outbox[0]
        self.assertEqual(subject, msg.subject)
        self.assertEqual(email_message, msg.body)
        self.assertEqual(from_email, msg.from_email)
