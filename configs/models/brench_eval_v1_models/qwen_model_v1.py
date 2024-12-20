from opencompass.models import OpenAI

api_meta_template = dict(
    round=[
        dict(role='HUMAN', api_role='HUMAN'),
        dict(role='BOT', api_role='BOT', generate=True),
    ],
    reserved_roles=[dict(role='SYSTEM', api_role='SYSTEM')],
)

models = [
    dict(
        abbr='qwen2.5-1.5b-math-code-pro-1121',
        type=OpenAI,
        openai_api_base='http://0.0.0.0:8002/v1/chat/completions', # 服务地址
        path='qwen2.5-1.5b-math-code-pro-1121', # 请求服务时的 model name
        key = 'EMPTY',
        rpm_verbose=True, # 是否打印请求速率
        meta_template=api_meta_template, # 服务请求模板
        query_per_second=64, # 服务请求速率
        max_out_len=1024, # 最大输出长度
        max_seq_len=4096, # 最大输入长度
        temperature=0.7, # 生成温度
        batch_size=24, # 批处理大小
        retry=128, # 重试次数
        tokenizer_path="/data/vayu/xDAN-quantizied-collections/xDAN-L1-Edge-4x1.5b-reasoning-pro-0827",
    )
]
