import os

import pytest

# 运行类
if __name__ == '__main__':
    # pytest.main(['./scriptsDir/test_vhr.py', '-vs'])
    pytest.main(['./scriptsDir/test_vhr.py', '-vs',
                 '--alluredir=./report', '--clean-alluredir'])
    os.system(r'allure generate ./report -o ./allreport --clean')
