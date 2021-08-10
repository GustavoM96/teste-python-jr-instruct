from api.models import PackageRelease, Project
import requests


class ApiServices:
    @staticmethod
    def is_validated_package(package: dict) -> bool:
        host_pypi = "https://pypi.org"

        if package.version:
            response = requests.get(
                f'{host_pypi}/pypi/{package["name"]}/{package["version"]}/json'
            )
        else:
            response = requests.get(f'{host_pypi}/pypi/{package["name"]}/json')

        if response.status_code == "200":
            return True

        return False

    @staticmethod
    def get_latest_version_package(package: dict) -> dict:
        host_pypi = "https://pypi.org"

        response = requests.get(f"{host_pypi}/pypi/{package.name}/json")
        lastest_version = response.text.info.version

        return lastest_version

    @classmethod
    def crate_project(cls, project_name: str, package_list: list[dict]):
        project = Project.objects.create(name=project_name)

        for package in package_list:
            if not cls.is_validated_package(package):
                raise ValueError({"error": "One or more packages don't exist"})

            package["version"] = cls.get_latest_version_package(package)

        created_package_list = PackageRelease.objects.bulk_create(package_list)
        project.packages.set(created_package_list)

        return project
