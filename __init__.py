import time

from hoshino import Service, logger
import os
import subprocess

from hoshino.R import ResObj
from hoshino.config import priconne

sv_help = '''
[千里眼] 
'''.strip()

sv = Service('pcr-clairvoyance', help_=sv_help, bundle='pcr千里眼')


_git_url = "git@github.com:sgpublic/hoshino-clairvoyance.git"
_git_branch = "resource"

try:
    _git_url = priconne.clairvoyance.CLAIRVOYANCE_GIT_URL
except Exception as _:
    pass
try:
    _git_branch = priconne.clairvoyance.CLAIRVOYANCE_GIT_BRANCH
except Exception as _:
    pass


_last_check_time = 0
clairvoyance_resource_dir = ResObj("./cache/priconne/clairvoyance").path


def checkout_clairvoyance():
    global _last_check_time
    if not os.path.exists(clairvoyance_resource_dir):
        command = ['git', 'clone', _git_url, '-b', _git_branch, '--depth=1', clairvoyance_resource_dir]
        try:
            subprocess.run(command, check=True)
            _last_check_time = time.time()
        except subprocess.CalledProcessError as e:
            logger.warn(f"千里眼资源 clone 失败：{e}")
    elif _last_check_time + 24 * 3600 < time.time():
        command = ['git', 'pull']
        try:
            subprocess.run(command, check=True, cwd=clairvoyance_resource_dir)
            _last_check_time = time.time()
        except subprocess.CalledProcessError as e:
            logger.warn(f"千里眼资源更新失败：{e}")


checkout_clairvoyance()

from .clairvoyance import future_gacha
