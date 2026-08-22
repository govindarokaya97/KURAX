from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse


class LogoutRegressionTests(TestCase):
    def test_logout_page_uses_post_form_in_navbar(self):
        user_model = get_user_model()
        user = user_model.objects.create_user(
            username="logout-user",
            email="logout@example.com",
            password="secret123",
        )
        self.client.force_login(user)

        response = self.client.get(reverse("post_list"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'method="post"', count=1)
        self.assertContains(response, 'action="/account/logout/"')

    def test_logout_endpoint_accepts_post_and_redirects(self):
        user_model = get_user_model()
        user = user_model.objects.create_user(
            username="logout-post-user",
            email="logout-post@example.com",
            password="secret123",
        )
        self.client.force_login(user)

        response = self.client.post(reverse("logout"))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse("post_list"))

    def test_protected_page_redirects_to_existing_login_url(self):
        response = self.client.get(reverse("draft_list"))

        self.assertEqual(response.status_code, 302)
        self.assertRedirects(
            response,
            "/account/login/?next=/draft-list/",
            fetch_redirect_response=False,
        )
