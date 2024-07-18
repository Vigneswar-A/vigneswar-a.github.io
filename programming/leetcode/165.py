class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        version1 += '.0' * (version2.count('.') - version1.count('.'))
        version2 += '.0' * (version1.count('.') - version2.count('.'))
        def val(version):
            temp = 0
            for ver in version.split('.'):
                temp = temp*10 + int(ver)
            return temp

        if val(version1) > val(version2):
            return 1
        if val(version2) > val(version1):
            return -1

        return 0
