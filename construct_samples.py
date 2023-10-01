import json
import os
import argparse

SAMPLE_TEMPLATE = """
## {edit_made} {target_new}

**New Fact:** {edit_made} {target_new}
**Subject of new fact:** {subject_of_edit}
**Related Entity:** {related_entity}

### **Main passage (subject: {subject_of_edit}):**
{passage_of_text_about_subject_of_edit}

### **Old facts about the subject**
{ground_truth_about_subject_of_edit}

### **Related passage (related entity: {related_entity}):** 
{passage_of_text_about_related_entity}

### **Old facts about the related entity**
{ground_truth_about_related_entity}
"""


def get_samples_from_dir(dir_path):
    samples = []
    for file_name in os.listdir(dir_path):
        with open(os.path.join(dir_path, file_name), 'r') as f:
            samples.append(json.load(f))
    return samples


def get_sample_text(sample):
    subject_ground_truth = sample['dependancies']['subject_entity']['ground_truth']
    subject_ground_truth_string = '- ' + '\n- '.join([f"{key}: {', '.join(value)}" for key,value in subject_ground_truth.items()])
    related_entity_ground_truth = sample['dependancies']['coupled_entities'][0]['ground_truth']
    related_entity_ground_truth_string = '- ' + '\n- '.join([f"{key}: {', '.join(value)}" for key,value in related_entity_ground_truth.items()])
    return SAMPLE_TEMPLATE.format(
        subject_of_edit=sample["requested_rewrite"]['subject'],
        edit_made=sample["requested_rewrite"]["prompt"].format(
            sample["requested_rewrite"]['subject']
        ),
        ground_truth_about_subject_of_edit=subject_ground_truth_string.strip().replace('\n', ' '),
        ground_truth_about_related_entity=related_entity_ground_truth_string.strip().replace('\n', ' '),
        passage_of_text_about_subject_of_edit=sample['subject_prompt'].strip().replace('\n', ' '),
        passage_of_text_about_related_entity=sample['coupled_prompt'].strip().replace('\n', ' '),
        related_entity=sample['dependancies']['coupled_entities'][0]['entity'],
        target_new=sample["requested_rewrite"]['target_new']['str'],
        target_old=sample["requested_rewrite"]['target_true']['str']
    )


def get_samples_text(samples):
    return '\n\n'.join([get_sample_text(sample) for sample in samples])


def get_samples_from_dir(dir_path):
    samples = []
    for file_name in os.listdir(dir_path):
        with open(os.path.join(dir_path, file_name), 'r') as f:
            samples.append(json.load(f))
    return samples


parser = argparse.ArgumentParser()
parser.add_argument('--sample-dir', type=str)
parser.add_argument('--sample-type', type=str)

args = parser.parse_args()

if __name__ == "__main__":
    samples = get_samples_from_dir(args.sample_dir)
    samples_text = get_samples_text(samples)

    with open(
        os.path.join(
            './data',
            'evaluation_samples',
            f'{args.sample_type}.md'
        ), 'w'
    ) as f:
        f.write(samples_text)
