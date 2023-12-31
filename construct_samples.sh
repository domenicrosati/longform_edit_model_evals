# for gptj
python construct_samples.py \
    --sample-dir data/generated_samples/model_gptj_no_edit_False_use_sampling_True_token_length_1024_method_FT \
    --sample-type gptj_ft_edit
python construct_samples.py \
    --sample-dir data/generated_samples/model_gptj_no_edit_False_use_sampling_True_token_length_1024_method_ROME \
    --sample-type gptj_rome_edit
python construct_samples.py \
    --sample-dir data/generated_samples/model_gptj_no_edit_False_use_sampling_True_token_length_1024_method_IKE \
    --sample-type gptj_ike_edit
python construct_samples.py \
    --sample-dir data/generated_samples/model_gptj_no_edit_TRUE_use_sampling_True_token_length_1024_method_ROME \
    --sample-type gptj_no_edit

# for llama2-chat
python construct_samples.py \
    --sample-dir data/generated_samples/model_llama2-chat_no_edit_False_use_sampling_True_token_length_1024_method_FT \
    --sample-type llama2_chat_ft_edit
python construct_samples.py \
    --sample-dir data/generated_samples/model_llama2-chat_no_edit_False_use_sampling_True_token_length_1024_method_ROME \
    --sample-type llama2_chat_rome_edit
python construct_samples.py \
    --sample-dir data/generated_samples/model_llama2-chat_no_edit_False_use_sampling_True_token_length_1024_method_IKE \
    --sample-type llama2_chat_ike_edit
python construct_samples.py \
    --sample-dir data/generated_samples/model_llama2-chat_no_edit_TRUE_use_sampling_True_token_length_1024_method_ROME \
    --sample-type llama2_chat_no_edit
