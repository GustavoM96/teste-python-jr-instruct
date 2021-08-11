from django.test import TestCase, client
from ipdb.__main__ import set_trace
from rest_framework.test import APIClient
from ..models import Project


class ProjectViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.package1 = dict(name="Django")
        self.package2 = dict(name="Django")
        self.invalid_package1 = dict(name="kbkoiewadsfxzc", version="2.0")
        self.invalid_package2 = dict(name="Flask", version="kbkoiewadsfxzc")

        self.package_list = [self.package1, self.package2]
        self.invalid_package_list = [self.invalid_package1, self.invalid_package2]

        self.project = dict(name="Titan", packages=self.package_list)
        self.invalid_project1 = dict(name="Titan", packages=[self.invalid_package1])
        self.invalid_project2 = dict(name="Titan", packages=[self.invalid_package2])
        self.invalid_project3 = dict(name="Titan", packages=self.invalid_package_list)

    def test_view_list_and_create_project(self):

        created_project = self.client.post(
            "/api/projects/", self.project, format="json"
        )

        project_list = self.client.get("/api/projects/", format="json")

        self.assertListEqual(project_list.json(), [created_project.json()])
        self.assertEqual(project_list.status_code, 200)
        self.assertEqual(created_project.status_code, 201)

    def test_view_retrieve_and_create_project(self):

        created_project = self.client.post(
            "/api/projects/", self.project, format="json"
        )
        project_name = created_project.json()["name"]

        retrieved_project = self.client.get(
            f"/api/projects/{project_name}/", format="json"
        )

        self.assertDictEqual(retrieved_project.json(), created_project.json())
        self.assertEqual(retrieved_project.status_code, 200)
        self.assertEqual(created_project.status_code, 201)

    def test_view_delete_project(self):

        created_project = self.client.post(
            "/api/projects/", self.project, format="json"
        )
        project_name = created_project.json()["name"]

        deleted_project = self.client.delete(
            f"/api/projects/{project_name}/", format="json"
        )

        self.assertEqual(deleted_project.status_code, 204)

    def test_view_delete_project(self):

        created_project = self.client.post(
            "/api/projects/", self.project, format="json"
        )
        project_name = created_project.json()["name"]

        deleted_project = self.client.delete(
            f"/api/projects/{project_name}/", format="json"
        )

        self.assertEqual(len(Project.objects.all()), 0)

        self.assertEqual(deleted_project.status_code, 204)

    def test_view_create_project_already_exists(self):
        created_project1 = self.client.post(
            "/api/projects/", self.project, format="json"
        )
        created_project2 = self.client.post(
            "/api/projects/", self.project, format="json"
        )
        self.assertDictEqual(
            created_project2.json(),
            {"name": ["project with this name already exists."]},
        )
        self.assertEqual(created_project2.status_code, 400)

    def test_view_create_project_with_invalid_package(self):
        client2 = APIClient()
        client3 = APIClient()

        created_project1 = self.client.post(
            "/api/projects/", self.invalid_project1, format="json"
        )
        created_project2 = client2.post(
            "/api/projects/", self.invalid_project2, format="json"
        )
        created_project3 = client3.post(
            "/api/projects/", self.invalid_project3, format="json"
        )

        self.assertDictEqual(
            created_project1.json(),
            {"error": "One or more packages doesn't exist"},
        )
        self.assertEqual(created_project1.status_code, 400)

        self.assertDictEqual(
            created_project2.json(),
            {"error": "One or more packages doesn't exist"},
        )
        self.assertEqual(created_project2.status_code, 400)

        self.assertDictEqual(
            created_project3.json(),
            {"error": "One or more packages doesn't exist"},
        )
        self.assertEqual(created_project3.status_code, 400)

    def test_view_retrieve_with_project_does_not_exist(self):
        invalid_project_name = "wrong-name-project"

        retrieved_project = self.client.get(
            f"/api/projects/{invalid_project_name}/", format="json"
        )
        self.assertEqual(retrieved_project.status_code, 404)
