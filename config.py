from dataclasses import dataclass


@dataclass
class Config:
    token_telegram: str = ''
    token_yadisk: str = ''
    admin_id: int = 111111111
    model_path: str = "t5-small-sum-tout"
    tokenizer_path: str = "t5-small-sum-tout"
    dir_name: str = "/Проделанная работа"
