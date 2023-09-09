# for loop over all the files in the directory data/samples and pass them to main.py as sample_file
# and run the main.py script
#
# Usage: ./run.sh
#

for sample_file in data/samples/*.json
do
    python main.py --sample_file $sample_file
done