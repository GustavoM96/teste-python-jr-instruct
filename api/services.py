from api.models import PackageRelease, Project
import requests


class ApiServices:
    @staticmethod
    def is_validated_package(package: dict) -> bool:
        host_pypi = "https://pypi.org"

        if package.get("version"):
            response = requests.get(
                f'{host_pypi}/pypi/{package["name"]}/{package["version"]}/json'
            )
        else:
            response = requests.get(f'{host_pypi}/pypi/{package["name"]}/json')

        if response.status_code == 200:
            return True
        return False

    @staticmethod
    def get_latest_version_package(package: dict) -> str:
        host_pypi = "https://pypi.org"

        response = requests.get(f'{host_pypi}/pypi/{package["name"]}/json')
        lastest_version = response.json()["info"]["version"]

        return lastest_version

    @classmethod
    def create_package_list(cls, package_list: list[dict]) -> list[PackageRelease]:
        created_package_list = []

        for package in package_list:
            if not cls.is_validated_package(package):
                raise ValueError({"error": "One or more packages doesn't exist"})

            if not package.get("version"):
                package["version"] = cls.get_latest_version_package(package)

            package = PackageRelease.objects.get_or_create(**package)[0]

            created_package_list.append(package)

        return created_package_list

    @classmethod
    def create_project(cls, project_data) -> Project:
        created_package_list = cls.create_package_list(project_data["packages"])

        project = Project.objects.create(name=project_data["name"])

        project.packages.set(created_package_list)

        return project
