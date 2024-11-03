import os
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
from config import Config

model_path = Config.model_path
tokenizer_path = Config.tokenizer_path

model = AutoModelForSeq2SeqLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained(tokenizer_path)


def summarization_text(input_text):
    len_text = len(input_text)

    inputs = tokenizer(input_text, return_tensors="pt", max_length=2000, truncation=True)

    summary_ids = model.generate(
        inputs.input_ids,
        max_length=int(len_text // 3.5),
        min_length=int(int(len_text // 3.5)//10),
        length_penalty=5,
        num_beams=10,
        early_stopping=True
    )

    print(int(len_text // 3.5), int(int(len_text // 3.5)//9))

    summary = tokenizer.decode(summary_ids[0], skip_special_tokens=True)

    return summary
