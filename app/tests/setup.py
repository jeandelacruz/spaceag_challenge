from rest_framework.test import APITestCase
from django.urls import reverse_lazy
from faker import Faker
from random import choice
from app.serializers import WorkerSerializer


class TestSetUp(APITestCase):
    def setUp(self):
        self.faker = Faker()
        self.functions_choices = (
            'Harvest',
            'Pruning',
            'Scouting',
            'Other',
        )
        self.worker_data = {
            'first_name': self.faker.name().split(' ')[0],
            'last_name': self.faker.name().split(' ')[1],
            'function': choice(self.functions_choices),
        }
        self.worker_update = {
            'first_name': self.faker.name().split(' ')[0],
            'last_name': self.faker.name().split(' ')[1],
            'function': choice(self.functions_choices),
        }
        self.list_url = reverse_lazy('worker_list')
        self.create_url = reverse_lazy('worker_create')
        self.serializer = WorkerSerializer

    def tearDown(self):
        return super().tearDown()
