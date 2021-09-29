from .setup import TestSetUp
from django.urls import reverse_lazy


class TestViews(TestSetUp):
    def test_worker_list_ten(self):
        res = self._worker_list_create(10, 1)
        self.assertEqual(len(res.json()['results']), 10)

    def test_worker_list_page_2(self):
        res = self._worker_list_create(15, 2)
        self.assertEqual(len(res.json()['results']), 5)

    # TODO Rename this here and in `test_worker_list_ten` and `test_worker_list_page_2`
    def _worker_list_create(self, nro_workers, page):
        for _ in range(nro_workers):
            self.client.post(
                self.list_create_url, self.worker_data, format='json'
            )
        result = self.client.get(self.list_create_url, {'page': page})
        self.assertEqual(result.status_code, 200)
        return result

    def test_worker_create(self):
        res = self.client.post(
            self.list_create_url, self.worker_data, format='json'
        )
        serializer = self.serializer(instance=res.data)
        self.assertEqual(res.data, serializer.data)

    def test_worker_update(self):
        create = self.client.post(
            self.list_create_url, self.worker_data, format='json'
        )
        serializer_create = self.serializer(instance=create.data)
        res_update = self.client.patch(
            reverse_lazy(
                'update_destroy',
                kwargs={'id': serializer_create.data['id']},
            ),
            json=self.worker_update,
            format='json',
        )
        serializer_update = self.serializer(instance=res_update.data)
        self.assertEqual(create.data, serializer_create.data)
        self.assertEqual(res_update.data, serializer_update.data)

    def test_worker_delete(self):
        create = self.client.post(
            self.list_create_url, self.worker_data, format='json'
        )
        serializer_create = self.serializer(instance=create.data)
        res_delete = self.client.delete(
            reverse_lazy(
                'update_destroy',
                kwargs={'id': serializer_create.data['id']},
            ),
            format='json',
        )
        self.assertEqual(create.data, serializer_create.data)
        self.assertEqual(res_delete.status_code, 204)
