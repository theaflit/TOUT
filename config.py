from dataclasses import dataclass


@dataclass
class Config:
    token_telegram: str = ''
    token_yadisk: str = ''
    admin_id: int = 11111111
    model_path: str = "t5-small-finetuned-xsum"
    tokenizer_path: str = "t5-small-finetuned-xsum"
    dir_name: str = "/Проделанная работа"
