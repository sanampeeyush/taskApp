from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from .models import Business
from .serializers import BusinessSerializer

class BusinessTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.business_data = {
            "name": "Test Business",
            "address": "123 Elm St",
            "owner_info": "John Doe",
            "employee_size": 50,
            "summary": "Test summary",
            "headquarters_location": "Test location",
            "industry": "Test industry",
            "founded_date": "2022-01-01",
            "founders": "Test founders",
            "operating_status": True,
            "last_funding_type": "Seed",
            "legal_name": "Test legal name",
            "stock_symbol": "TST",
            "company_type": "Test company type",
            "contact_email": "test@example.com",
            "phone_number": "123-456-7890"
        }
        self.business = Business.objects.create(**self.business_data)

    def test_create_business(self):
        response = self.client.post(reverse("business_create"), self.business_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_business(self):
        updated_data = {
            "name": "Updated Business",
            "address": "456 Updated St",
            "owner_info": "Updated Owner",
            "employee_size": 20,
            "summary": "Updated summary",
            "headquarters_location": "Updated location",
            "industry": "Updated industry",
            "founded_date": "2023-01-01",
            "founders": "Updated founders",
            "operating_status": False,
            "last_funding_type": "Series A",
            "legal_name": "Updated legal name",
            "stock_symbol": "UPD",
            "company_type": "Updated company type",
            "contact_email": "updated@example.com",
            "phone_number": "987-654-3210",
        }
        url = reverse("business_update", args=[self.business.id])
        response = self.client.put(url, updated_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_business(self):
        response = self.client.delete(reverse("business_delete", args=[self.business.id]))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_list_businesses(self):
        response = self.client.get(reverse("business_list"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_business_by_id(self):
        response = self.client.get(reverse("business_by_id", args=[self.business.id]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_business_by_name(self):
        response = self.client.get(reverse("business_by_name", args=[self.business.name]))
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_serializer_valid(self):
        serializer = BusinessSerializer(data=self.business_data)
        self.assertTrue(serializer.is_valid())

    def test_serializer_invalid(self):
        invalid_data = {
            "name": "Test Business",
            "owner_info": "Test Owner",
        }
        serializer = BusinessSerializer(data=invalid_data)
        self.assertFalse(serializer.is_valid())

    def test_serializer_with_instance(self):
        serializer = BusinessSerializer(instance=self.business)
        expected_data = {
            "id": self.business.id,
            "name": self.business.name,
            "address": self.business.address,
            "owner_info": self.business.owner_info,
            "employee_size": self.business.employee_size,
            "summary": self.business.summary,
            "headquarters_location": self.business.headquarters_location,
            "industry": self.business.industry,
            "founded_date": str(self.business.founded_date),
            "founders": self.business.founders,
            "operating_status": self.business.operating_status,
            "last_funding_type": self.business.last_funding_type,
            "legal_name": self.business.legal_name,
            "stock_symbol": self.business.stock_symbol,
            "company_type": self.business.company_type,
            "contact_email": self.business.contact_email,
            "phone_number": self.business.phone_number,
        }
        self.assertEqual(serializer.data, expected_data)

    def test_get_nonexistent_business_by_id(self):
        response = self.client.get(reverse("business_by_id", args=[999]))  # Use a non-existent ID
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_nonexistent_business_by_name(self):
        response = self.client.get(reverse("business_by_name", args=["NonExistentName"]))  # Use a non-existent name
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
