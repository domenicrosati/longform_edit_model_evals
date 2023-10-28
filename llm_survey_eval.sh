# # # GPTJ
# python llm_survey_eval.py \
#     --sample-dir data/generated_samples/model_gptj_no_edit_False_use_sampling_True_token_length_1024_method_FT \
#     --sample-type gptj_ft_edit
# python llm_survey_eval.py \
#     --sample-dir data/generated_samples/model_gptj_no_edit_False_use_sampling_True_token_length_1024_method_ROME \
#     --sample-type gptj_rome_edit
# python llm_survey_eval.py \
#     --sample-dir data/generated_samples/model_gptj_no_edit_False_use_sampling_True_token_length_1024_method_IKE \
#     --sample-type gptj_ike_edit
# python llm_survey_eval.py \
#     --sample-dir data/generated_samples/model_gptj_no_edit_True_use_sampling_True_token_length_1024_method_ROME \
#     --sample-type gptj_no_edit

# # LLAMA2-CHAT
# python llm_survey_eval.py \
#     --sample-dir data/generated_samples/model_llama2-chat_no_edit_False_use_sampling_True_token_length_1024_method_FT \
#     --sample-type llama2_chat_ft_edit
# python llm_survey_eval.py \
#     --sample-dir data/generated_samples/model_llama2-chat_no_edit_False_use_sampling_True_token_length_1024_method_ROME \
#     --sample-type llama2_chat_rome_edit
# python llm_survey_eval.py \
#     --sample-dir data/generated_samples/model_llama2-chat_no_edit_False_use_sampling_True_token_length_1024_method_IKE \
#     --sample-type llama2_chat_ike_edit
# python llm_survey_eval.py \
#     --sample-dir data/generated_samples/model_llama2-chat_no_edit_True_use_sampling_True_token_length_1024_method_ROME \
#     --sample-type llama2_chat_no_edit

# survey samples
# python llm_survey_eval.py \
#     --sample-dir data/survey_samples/rome \
#     --sample-type llama2_chat_rome_edit_pilot_survey \
#     --n-shots 8 \
#     --model gpt-3.5-turbo-16k
# python llm_survey_eval.py \
#     --sample-dir data/survey_samples/human \
#     --sample-type llama2_chat_human_edit_pilot_survey \
#     --n-shots 8 \
#     --model gpt-3.5-turbo-16k
# python llm_survey_eval.py \
#     --sample-dir data/survey_samples/no_edit \
#     --sample-type llama2_chat_no_edit_pilot_survey \
#     --n-shots 8 \
#     --model gpt-3.5-turbo-16k
python llm_survey_eval.py \
    --sample-dir data/survey_samples/rome \
    --sample-type llama2_chat_rome_edit_pilot_survey \
    --n-shots 8 \
    --model gpt-4
python llm_survey_eval.py \
    --sample-dir data/survey_samples/human \
    --sample-type llama2_chat_human_edit_pilot_survey  \
    --n-shots 8 \
    --model gpt-4
python llm_survey_eval.py \
    --sample-dir data/survey_samples/no_edit \
    --sample-type llama2_chat_no_edit_pilot_survey  \
    --n-shots 8 \
    --model gpt-4
