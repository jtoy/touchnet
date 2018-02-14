import sys
sys.path.append('..')
import sensenet
from sensenet import envs
def test_envs_have_spaces():
    env_names = [spec.id for spec in envs.registry.all()]
    for name in env_names:
        print("loading env",name)
        env = sensenet.make(name)
        assert env.action_space.n #TODO fix assertion to test for valid assertion
