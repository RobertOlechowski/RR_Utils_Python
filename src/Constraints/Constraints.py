import sys
from enum import Enum


class Packages(Enum):
    Python = 1,
    OpenCV = 2,
    RaspberryPi = 3,
    Pwd = 4,


def _parse_version(version_text):
    return tuple([int(a) for a in version_text.split(".")])


def _version_compare(current, expected):
    if current[0] < expected[0]:
        return False
    if current[0] == expected[0] and current[1] < expected[1]:
        return False
    return True


class Constraints:
    def __init__(self):
        self.conditions = {}

    def add(self, package, version):
        self.conditions[package] = version

    def check(self):
        for k, v in self.conditions.items():
            result, package, result_msg = self._check_single(k, v)
            if not result:
                print(result_msg)
                sys.exit(1)
        return True

    def _check_single(self, package, version):
        checkers_dic = {
            Packages.Python: self._check_python,
            Packages.OpenCV: self._check_opencv,
            Packages.RaspberryPi: self._check_raspberry_pi,
            Packages.Pwd: self._check_pwd,
        }

        if package not in checkers_dic:
            raise Exception("Not implemented")

        result, result_msg = checkers_dic[package](version)
        return result, package, result_msg,

    @staticmethod
    def _check_raspberry_pi(expected):
        import os
        os_info = os.uname()
        sys_name, _, release, version, _ = os_info
        if sys_name != "Linux":
            return False, "Incorrect sys_name: {}".format(sys_name)

        release = tuple([int(a) for a in release.split(".")[0:2]])
        if not _version_compare(release, expected.release):
            return False, "Incorrect release: {}".format(release)

        version = int(version.split(' ')[0].strip("#"))
        if version < expected.version:
            return False, "Incorrect version: {}".format(version)

        return True, None

    @staticmethod
    def _check_pwd(expected):
        import os
        cwd = os.getcwd()
        if cwd != expected:
            return False, "Invalid PWD is {}, but expected {}".format(cwd, expected)
        return True, None

    @staticmethod
    def _check_python(expected_version):
        if not _version_compare(sys.version_info, expected_version):
            return False, "Invalid Python interpreter {}".format(sys.version_info)
        return True, None

    @staticmethod
    def _check_opencv(expected_version):
        import cv2 as cv
        current_version = _parse_version(cv.__version__)
        if not _version_compare(current_version, expected_version):
            return False, "Invalid OpenCV {}".format(current_version)
        return True, None
