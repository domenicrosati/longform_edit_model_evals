# python llm_annotator.py \
#     --sample-dir data/survey_samples/rome \
#     --sample-type llama2_chat_rome_edit_pretest_annotation 
# python llm_annotator.py \
#     --sample-dir data/survey_samples/human \
#     --sample-type llama2_chat_human_edit_pretest_annotation 
# python llm_annotator.py \
#     --sample-dir data/survey_samples/no_edit \
#     --sample-type llama2_chat_no_edit_pretest_annotation 
python llm_annotator.py \
    --sample-dir data/survey_samples/rome \
    --sample-type llama2_chat_rome_edit_pretest_annotation \
    --model gpt-4
# python llm_annotator.py \
#     --sample-dir data/survey_samples/human \
#     --sample-type llama2_chat_human_edit_pretest_annotation \
#     --model gpt-4
# python llm_annotator.py \
#     --sample-dir data/survey_samples/no_edit \
#     --sample-type llama2_chat_no_edit_pretest_annotation \
#     --model gpt-4