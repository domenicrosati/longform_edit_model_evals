# python llm_annotator.py \
#     --sample-dir data/survey_samples/rome \
#     --sample-type llama2_chat_rome_edit_first_3_annotation 
python llm_annotator.py \
    --sample-dir data/survey_samples/human \
    --sample-type llama2_chat_human_edit_first_3_annotation 
# python llm_annotator.py \
#     --sample-dir data/survey_samples/no_edit \
#     --sample-type llama2_chat_no_edit_first_3_annotation

# python llm_annotator.py \
#     --sample-dir data/survey_samples/rome \
#     --n-shots 8 \
#     --sample-type llama2_chat_rome_edit_first_3_annotation 
# python llm_annotator.py \
#     --sample-dir data/survey_samples/human \
#     --n-shots 8 \
#     --sample-type llama2_chat_human_edit_first_3_annotation 
# python llm_annotator.py \
#     --sample-dir data/survey_samples/no_edit \
#     --n-shots 8 \
#     --sample-type llama2_chat_no_edit_first_3_annotation

# python llm_annotator.py \
#     --sample-dir data/survey_samples/rome \
#     --sample-type llama2_chat_rome_edit_first_3_annotation \
#     --model gpt-4
# python llm_annotator.py \
#     --sample-dir data/survey_samples/human \
#     --sample-type llama2_chat_human_edit_first_3_annotation \
#     --model gpt-4
# python llm_annotator.py \
#     --sample-dir data/survey_samples/no_edit \
#     --sample-type llama2_chat_no_edit_first_3_annotation \
#     --model gpt-4

# python llm_annotator.py \
#     --sample-dir data/survey_samples/rome \
#     --sample-type llama2_chat_rome_edit_first_3_annotation \
#     --n-shots 8 \
#     --model gpt-4
# python llm_annotator.py \
#     --sample-dir data/survey_samples/human \
#     --sample-type llama2_chat_human_edit_first_3_annotation \
#     --n-shots 8 \
#     --model gpt-4
# python llm_annotator.py \
#     --sample-dir data/survey_samples/no_edit \
#     --sample-type llama2_chat_no_edit_first_3_annotation \
#     --n-shots 8 \
#     --model gpt-4