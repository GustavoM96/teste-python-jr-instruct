from django.test import TestCase

from ..models import PackageRelease, Project
from ipdb import set_trace

# (1)


class ProjectModelTest(TestCase):
    def setUp(self):
        self.project = Project.objects.create(name="Titan")

    def test_it_has_information_fields(self):
        self.assertIsInstance(self.project.name, str)


class PackageReleaseModelTest(TestCase):
    def setUp(self):
        self.package = PackageRelease.objects.create(name="Django", version="1.0")

    def test_it_has_information_fields(self):
        self.assertIsInstance(self.package.name, str)
        self.assertIsInstance(self.package.version, str)


class PackageReleaseProjectModelTest(TestCase):
    def setUp(self):
        self.package = PackageRelease.objects.create(name="Django", version="1.0")
        self.project = Project.objects.create(name="Titan")

    def test_add_package_on_project(self):
        self.project.packages.add(self.package)
        self.assertIsInstance(self.project.packages.all()[0], PackageRelease)
