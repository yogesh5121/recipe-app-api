"""
Tests for the Django admin interface.
"""
from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import Client


class AdminSiteTests(TestCase):
    """tests for the Django admin interface."""

    def setUp(self):
        """Create user and client"""
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            email ='user@example.com',
            password='testpass123',
        )
        self.client.force_login(self.admin_user)
        self.user =get_user_model().objects.create_user(
            email='user@exmaple.com',
            password='testpass123',
            name='Test User'
        )
    def test_users_listed(self):
        """Test that users are listed on user page."""
        url = reverse('admin:core_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.email)