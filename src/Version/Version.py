from Version.VersionException import VersionException


class Version:
    def __init__(self, version):
        if isinstance(version, str):
            version = self._parse_string(version)
        if len(version) < 1 or len(version) > 4:
            raise VersionException()
        self.version = tuple(version)

    def get_version(self):
        return self.version

    def __len__(self):
        return len(self.version)

    @staticmethod
    def _parse_string(text):
        text = text.strip().split(" ")[0]
        result = text.strip().split(".")
        result = [int(a) for a in result]
        return result

    def __repr__(self):
        return ".".join([str(a) for a in self.version])

    def __str__(self):
        return self.__repr__()
