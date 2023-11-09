# for loop over all the files in the directory data/samples and pass them to main.py as sample_file
# and run the main.py script
#
# Usage: ./run.sh
#

for model in gpt2-xl gptj-6b llama2-7b llama2-7b-chat
do
for sample_file in ./data/counterfact_with_coupled_entities_sample_size_10.json 
do
for token_length in 600 1024 2048
do
for i in $(seq 0 1)
do
    python generate_edit_output.py --sample-number $i --model $model --no-edit --use-sampling --sample-file $sample_file --token-length $token_length
    for method in ROME FT IKE MEMIT
    do
        python generate_edit_output.py --sample-number $i --model $model --method $method --use-sampling --sample-file $sample_file --token-length $token_length
    done
done
done
done
done

for model in gpt2-xl gptj-6b llama2-7b llama2-7b-chat
do
for sample_file in ./data/zsre/zsre_mend_eval_with_coupled_entities_sample_size_10.json
do
for token_length in 600 1024 2048
do
for i in $(seq 0 1)
do
    python generate_edit_output.py --sample-number $i --model $model --no-edit --use-sampling --sample-file $sample_file --token-length $token_length
    for method in ROME FT IKE MEMIT
    do
        python generate_edit_output.py --sample-number $i --model $model --method $method --use-sampling --sample-file $sample_file --token-length $token_length --edit-type counterfactual
        python generate_edit_output.py --sample-number $i --model $model --method $method --use-sampling --sample-file $sample_file --token-length $token_length --edit-type factual
    done
done
done
done
done