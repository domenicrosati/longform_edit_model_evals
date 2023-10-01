# for loop over all the files in the directory data/samples and pass them to main.py as sample_file
# and run the main.py script
#
# Usage: ./run.sh
#

for i in $(seq 0 100)
do
    python coupled_edit_main.py --sample-number $i --model gpt2-xl --no-edit --use-sampling
    python coupled_edit_main.py --sample-number $i --model gpt2-xl --method ROME --use-sampling
    python coupled_edit_main.py --sample-number $i --model gpt2-xl --method FT --use-sampling
    python coupled_edit_main.py --sample-number $i --model gpt2-xl --method SERAC --use-sampling
    python coupled_edit_main.py --sample-number $i --model gptj-6b --no-edit --use-sampling
    python coupled_edit_main.py --sample-number $i --model gptj-6b --method ROME --use-sampling
    python coupled_edit_main.py --sample-number $i --model gptj-6b --method FT --use-sampling
    python coupled_edit_main.py --sample-number $i --model gptj-6b --method SERAC --use-sampling
    python coupled_edit_main.py --sample-number $i --model llama2 --no-edit --use-sampling
    python coupled_edit_main.py --sample-number $i --model llama2 --method ROME --use-sampling
    python coupled_edit_main.py --sample-number $i --model llama2 --method FT --use-sampling
    python coupled_edit_main.py --sample-number $i --model llama2 --method SERAC --use-sampling
    python coupled_edit_main.py --sample-number $i --model llama2 --no-edit --use-sampling
    python coupled_edit_main.py --sample-number $i --model llama2 --method ROME --use-sampling
    python coupled_edit_main.py --sample-number $i --model llama2 --method FT --use-sampling
    python coupled_edit_main.py --sample-number $i --model llama2 --method SERAC --use-sampling
done
