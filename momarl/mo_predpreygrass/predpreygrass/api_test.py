# passed API test for predpreygrass
from pettingzoo.test import api_test
import momarl.mo_predpreygrass.predpreygrass.environments.mo_predpreygrass as mo_predpreygrass

env = mo_predpreygrass.raw_env()
api_test(env, num_cycles=1000, verbose_progress=False)