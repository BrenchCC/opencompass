from mmengine.config import read_base

with read_base():
    from opencompass.configs.datasets_collections.brench_eval_data_v1 import datasets
    from opencompass.configs.models.brench_eval_v1_models.qwen_model_v1 import models



