from dataclasses import dataclass


@dataclass
class Config:
    token_telegram: str = '8062147761:AAGth2Rz9nI0EIe6X030malr2mJzWz7gMI4'
    token_yadisk: str = 'y0_AgAAAAA1ETRtAAysmgAAAAEWAnRGAACtIaLGgfFMwp6sh7MNBMGE4fIohQ'
    admin_id: int = 829836737
    model_path: str = "t5-small-finetuned-xsum"
    tokenizer_path: str = "t5-small-finetuned-xsum"
    dir_name: str = "/Проделанная работа"
