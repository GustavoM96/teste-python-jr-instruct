from api.services import ApiServices
from api.apps import ApiConfig
from django.test import TestCase
from rest_framework.test import APIClient
from ..models import PackageRelease, Project
from ipdb import set_trace

# (1)


class ProjectServiceTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.project = Project.objects.create(name="Titan")

        self.package1 = PackageRelease.objects.create(name="Django", version="1.0")
        self.package2 = PackageRelease.objects.create(name="Flask", version="2.0")

        self.invalid_package_name = PackageRelease.objects.create(
            name="laslpfuanfgs", version="1.0"
        )
        self.invalid_package_version = PackageRelease.objects.create(
            name="Django", version="okdfsduhanca"
        )

        self.host_pypi = "https://pypi.org"

    # def test_register_project_valid(self):
    #     project = ApiServices.crate_project(self.project.name,)
    #     self.assertEqual(len(self.project.packages.all()), 2)

    def test_invalid_package_list(self):
        is_valid_name = ApiServices.is_validated_package_list(
            [self.invalid_package_name]
        )
        is_valid_version = ApiServices.is_validated_package_list(
            [self.invalid_package_version]
        )

        self.assertEqual(is_valid_name, False)
        self.assertEqual(is_valid_version, False)

    def test_valid_package_list(self):
        is_valid_name = ApiServices.is_validated_package_list([self.package1])
        is_valid_version = ApiServices.is_validated_package_list([self.package2])

        self.assertEqual(is_valid_name, True)
        self.assertEqual(is_valid_version, True)

    def test_get_latest_version_package(self):
        lastest_version = ApiServices.get_latest_version_package()

        response = self.client.get(f"{host_pypi}/pypi/{package.name}/json")
        lastest_version_expected = response.json().info.version

        self.assertEqual(lastest_version, lastest_version_expected)
