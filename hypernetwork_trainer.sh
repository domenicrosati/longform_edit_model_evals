for method in MEND SERAC
do
    for model in gpt2-xl gptj-6b llama2-7b llama2-7b-chat
    do
        for dataset in zsre counterfact
        do
            python hypernetwork_trainer.py \
                --dataset $dataset \
                --model $model \
                --method $method
        done
    done
done