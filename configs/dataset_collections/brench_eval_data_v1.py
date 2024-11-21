from mmengine.config import read_base

with read_base():
    from ..configs.datasets.mmlu.mmlu_gen_4d595a import mmlu_datasets
    #from opencompass.configs.datasets.gsm8k.gsm8k_gen_1d7fe4 import gsm8k_datasets
    from ..datasets.gsm8k.brench_gsm8k_8shot_gen import gsm8k_datasets
    from ..configs.datasets.math.math_gen_1ed9c2 import math_datasets
    from ..configs.datasets.humaneval.humaneval_gen_66a7f4 import humaneval_datasets

datasets = sum((v for k, v in locals().items() if k.endswith('_datasets')), [])
