# for loop over all the files in the directory data/samples and pass them to main.py as sample_file
# and run the main.py script
#
# Usage: ./run.sh
#

for i in $(seq 0 100)
do
    python coupled_edit_main.py --sample-number $i --model llama2-chat
    python coupled_edit_main.py --sample-number $i --model llama2-chat --no-edit
    python coupled_edit_main.py --sample-number $i --model llama2-chat --no-edit --use-sampling
    python coupled_edit_main.py --sample-number $i --model llama2-chat --use-sampling
done
