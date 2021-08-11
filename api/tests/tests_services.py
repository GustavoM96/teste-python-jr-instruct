import requests
from api.services import ApiServices
from django.test import TestCase
from rest_framework.test import APIClient
from ..models import PackageRelease
import ipdb

# (1)


class ProjectServiceTest(TestCase):
    def setUp(self):
        self.client = APIClient()

        self.package1 = dict(name="Django")
        self.package2 = dict(name="Flask", version="2.0")
        self.package_list = [self.package1, self.package2]
        self.project = dict(name="Titan", packages=[self.package1, self.package2])

        self.invalid_package_name = dict(name="laslpfuanfgs", version="1.0")
        self.invalid_package_version = dict(name="Django", version="okdfsduhanca")

        self.host_pypi = "https://pypi.org"

    def test_service_is_validated_package_with_invalid_package(self):
        is_valid_name = ApiServices.is_validated_package(self.invalid_package_name)
        is_valid_version = ApiServices.is_validated_package(
            self.invalid_package_version
        )

        self.assertEqual(is_valid_name, False)
        self.assertEqual(is_valid_version, False)

    def test_service_is_validated_package_with_valid_package(self):
        is_valid_name = ApiServices.is_validated_package(self.package1)
        is_valid_version = ApiServices.is_validated_package(self.package2)

        self.assertEqual(is_valid_name, True)
        self.assertEqual(is_valid_version, True)

    def test_service_get_latest_version_package(self):
        lastest_version1 = ApiServices.get_latest_version_package(self.package1)
        lastest_version2 = ApiServices.get_latest_version_package(self.package2)

        response1 = requests.get(f'{self.host_pypi}/pypi/{self.package1["name"]}/json')
        response2 = requests.get(f'{self.host_pypi}/pypi/{self.package2["name"]}/json')

        lastest_version_expected1 = response1.json()["info"]["version"]
        lastest_version_expected2 = response2.json()["info"]["version"]

        self.assertEqual(lastest_version1, lastest_version_expected1)
        self.assertEqual(lastest_version2, lastest_version_expected2)

    def test_service_create_project_with_2_packages(self):
        project = ApiServices.create_project(self.project)
        quantity_package_expected = 2
        self.assertEqual(len(project.packages.all()), quantity_package_expected)

    def test_service_create_package_list(self):
        created_package_list = ApiServices.create_package_list(self.package_list)

        package_list_1 = PackageRelease.objects.get(name=self.package1["name"])
        package_list_2 = PackageRelease.objects.get(name=self.package2["name"])
        package_list_expected = [package_list_1, package_list_2]

        self.assertListEqual(created_package_list, package_list_expected)

    def test_service_create_package_list_keep_version_package(self):
        ApiServices.create_package_list([self.package2])

        got_package = PackageRelease.objects.get(name=self.package2["name"])

        self.assertEqual(self.package2["version"], got_package.version)

    def test_service_create_package_list_keep_version_package(self):
        ApiServices.create_package_list([self.package1])

        got_package = PackageRelease.objects.get(name=self.package1["name"])
        self.assertTrue(got_package.version)
