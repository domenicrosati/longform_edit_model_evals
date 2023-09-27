# %%
import json 

DATASET_PATH = './data/counterfact.json'
with open(DATASET_PATH, 'r') as f:
    dataset = json.load(f)

# %%
len(dataset)

# %%
from qwikidata.entity import WikidataItem, WikidataProperty
import qwikidata.linked_data_interface as ldi
from qwikidata.sparql import return_sparql_query_results
import functools

ent_id2label ={}
with open('./data/ent_id2label.json', 'r') as f:
    ent_id2label = json.load(f)

LABEL_TO_QID = """
PREFIX wd: <http://www.wikidata.org/entity/>
SELECT DISTINCT ?item
WHERE {{

  # make input string into a language-tagged string
  BIND( STRLANG("{}", "en") AS ?label ) .

  # search all items that have this languaged-tagged string as label
  ?item rdfs:label ?label .

  # extract the last path segment of the URI
  BIND(STRAFTER(STR(?item), STR(wd:)) AS ?qid) .
  # get count of propertes as heuristic for popularity
    ?item ?p ?statement .
}} order by desc(?p) limit 1
"""

ALL_ENTITIES_THAT_HAVE_THIS_AS_AN_OBJECT_TO_ANY_PROPERTY = """
SELECT DISTINCT ?item
WHERE {{
  ?item ?p wd:{0} .
}}
"""

ALL_ENTITIES_THAT_HAVE_THIS_AS_AN_OBJECT_TO_ANY_PROPERTY_AND_THIS_HAS = """
SELECT DISTINCT ?item
WHERE {{
  ?item ?p wd:{0} .
  wd:{1} ?p2 ?item. # change to ?p for mutual property
}}
"""

ALL_ENTITIES_THAT_HAVE_THIS_AS_AN_OBJECT_TO_ANY_PROPERTY_AND_PRE_EDIT = """
SELECT DISTINCT ?item
WHERE {{
  ?item ?p wd:{0} .
  ?item ?p2 wd:{1} .
}}
"""

COUPLED_ENTITIES_QUERY = """
SELECT ?item
WHERE {{
  {{ ?item ?p wd:{0} . }}
  UNION
  {{ wd:{0} ?p ?item . }}
  ?item ?p2 wd:{1} .
}} GROUP BY ?item ORDER BY DESC(COUNT(?item)) LIMIT 5
"""

@functools.lru_cache()
def get_wikidata_item_from_label(label):
    try:
      qid = return_sparql_query_results(LABEL_TO_QID.format(label))['results']['bindings'][0]['item']['value']
    except Exception as e:
      print(e)
      return None
    entity_dict = ldi.get_entity_dict_from_api(qid.strip('http://www.wikidata.org/entity/'))
    return WikidataItem(entity_dict)

@functools.lru_cache()
def get_wikidata_item_from_id(qid):
    try:
       entity_dict = ldi.get_entity_dict_from_api(qid)
    except Exception as e:
        print(e)
        return None
    return WikidataItem(entity_dict)

@functools.lru_cache()
def get_wikidata_label_from_id(qid):
    try:
      entity_label = ent_id2label[qid]
      return entity_label
    except Exception as e:
      entity = get_wikidata_item_from_id(qid)
      if entity:
        return entity.get_label()
      else:
        return ''

@functools.lru_cache()
def get_wikidata_property_from_id(pid):
    try:
      entity_dict = ldi.get_entity_dict_from_api(pid)
    except Exception as e:
      print(e)
      return None
    return WikidataProperty(entity_dict)

@functools.lru_cache()
def get_all_entities_that_have_this_as_an_object_to_any_property(qid):
    try:
      items = return_sparql_query_results(ALL_ENTITIES_THAT_HAVE_THIS_AS_AN_OBJECT_TO_ANY_PROPERTY.format(qid, qid))['results']['bindings']
    except Exception as e:
      print(e)
      return []
    entities = []
 
    for item in items:
      if 'http://www.wikidata.org/entity/Q' in item['item']['value']:
        entities.append(get_wikidata_item_from_id(item['item']['value'].strip('http://www.wikidata.org/entity/')))
    return entities

@functools.lru_cache()
def get_coupled_entities(qid_entity, qid_change):
    try:
      items = return_sparql_query_results(COUPLED_ENTITIES_QUERY.format(qid_entity, qid_change))['results']['bindings']
    except Exception as e:
      print(e)
      return []

    entities = []
    for item in items:
      if 'http://www.wikidata.org/entity/Q' in item['item']['value']:
        entities.append(get_wikidata_item_from_id(item['item']['value'].strip('http://www.wikidata.org/entity/')))
    return entities


# %%
# TODO: getting the property label is slow
# getting the ID is preferrable
property_exclude_list = [
    'instance of',
    'copyright status',
    'described by source',
    'documentation files at',
    'category',
    'copyright representative',
    'modified version of',
    'topic',
    'main regulatory text',
    'open data portal',
    'rating',
    'follow',
    'said to be the same as',
    'twinned',
    'copyright license',
    'list',
    'access',
    'wiki',
    'duplicated',
    'facet of',
    'translation',
    'via',
    'classification'
]

def _check_if_in_exclude_list(property_label):
    for exclude_word in property_exclude_list:
        if exclude_word in property_label.lower():
            return True
    return False

def _construct_ground_truth(entity_property_map, property_id_label_map):
    ground_truth = {}
    for property_id, property_label in property_id_label_map.items():
        if property_id in entity_property_map:
            ground_truth[property_label] = [
                get_wikidata_label_from_id(qid)
                for qid in entity_property_map[property_id]
            ]
    return ground_truth

def get_overlap(property_label_map_1, property_label_map_2):
    # get overlap between two property_label_maps 
    # i.e. the number of key value pairs that are the same
    overlap = []
    for property, labels in property_label_map_2.items():
        if property in property_label_map_1 and len(set(property_label_map_1[property]) & set(labels)) > 0:
            overlap.append((property, property_label_map_2[property]))
    return overlap

def _get_coupled_properties_count(  
    ent_property_label_map,
    property_label_map,
    target_true,
    ent_id,
    qid
):
    coupled_properties = 0
    for property, labels in property_label_map.items():
        # subject is object of this entity
        if ent_id in labels:
            coupled_properties += 1
        # target true is object of this entity
        if target_true in labels:
            coupled_properties += 1
        # mutual property
        if ent_id in labels and property in ent_property_label_map and qid in ent_property_label_map[property]:
            coupled_properties += 1
    return coupled_properties


def construct_entity_properties(
    original_entity, 
    related_entity_dict, 
    ent_property_label_map,
    original_propery,
    target_true,
    requested_rewrite
):
    original_propery_label = get_wikidata_property_from_id(original_propery).get_label()
    coupled_entities = []
    
    property_id_label_map = {}
    mutual_properties = set()
    subject_as_object = set()
    target_true_as_object = set()
    original_property_of_subject_as_object = set()
    related_entity_label = related_entity_dict['entity'].get_label()

    dependant_prompt = f"""Write an essay about {related_entity_label}
Include the following information:"""
    original_property_of_subject_as_object.add(original_propery_label)
    for property, labels in related_entity_dict['property_label_map'].items():
        # get interesting properties
        if original_entity.entity_id in labels:
            property_label = get_wikidata_property_from_id(property).get_label()
            if _check_if_in_exclude_list(property_label):
                continue
            original_property_of_subject_as_object.add(f"{original_propery_label} of {property_label}")
            subject_as_object.add(property_label)
            property_id_label_map[property] = property_label
        if target_true in labels:
            property_label = get_wikidata_property_from_id(property).get_label()
            if _check_if_in_exclude_list(property_label):
                continue
            target_true_as_object.add(property_label)
            property_id_label_map[property] = property_label
        if original_entity.entity_id in labels and property in ent_property_label_map and related_entity_dict['entity'].entity_id in ent_property_label_map[property]:
            property_label = get_wikidata_property_from_id(property).get_label()
            if _check_if_in_exclude_list(property_label):
                continue
            mutual_properties.add(property_label)
            property_id_label_map[property] = property_label
    
    # if there are additional overlap properties add them
    overlap_properties = set()
    for property, _ in related_entity_dict['overlap']:
        # get property label
        # make properties labels a deduped list
        property_label = get_wikidata_property_from_id(property).get_label()
        if _check_if_in_exclude_list(property_label):
            continue
        overlap_properties.add(property_label)
        property_id_label_map[property] = property_label

    properties_added = set()
    for property_label in original_property_of_subject_as_object:
        if property_label in properties_added:
            continue
        dependant_prompt += f"\n- {property_label}"
        properties_added.add(property_label)
    for property_label in mutual_properties:
        if property_label in properties_added:
            continue
        dependant_prompt += f"\n- {property_label}"
        properties_added.add(property_label)
    for property_label in target_true_as_object:
        if property_label in properties_added:
            continue
        dependant_prompt += f"\n- {property_label}"
        properties_added.add(property_label)
    for property_label in subject_as_object:
        if property_label in properties_added:
            continue
        dependant_prompt += f"\n- {property_label}"
        properties_added.add(property_label)
    for property_label in overlap_properties:
        if property_label in properties_added:
            continue
        dependant_prompt += f"\n- {property_label}"
        properties_added.add(property_label)

    coupled_entities.append({
        'entity': related_entity_label,
        'dependant_prompt': dependant_prompt,
        'dependant_prompt_with_relationship': dependant_prompt + f"\nRelationship to:\n- {requested_rewrite['subject']}\n- {requested_rewrite['target_true']['str']}\n- {requested_rewrite['target_new']['str']}",
        'mutual_properties': list(mutual_properties),
        'subject_as_object': list(subject_as_object),
        'target_true_as_object': list(target_true_as_object),
        'overlap_properties': list(overlap_properties),
        'original_property_of_subject_as_object': list(original_property_of_subject_as_object),
        'ground_truth': _construct_ground_truth(
            related_entity_dict['property_label_map'],
            property_id_label_map
        )
    })
    
    # create story prompt for original entity
    dependant_prompt = f"""Write an essay about {original_entity.get_label()}
Include the following information:"""
    dependant_prompt += f"\n- {original_propery_label}"
    
    # TODO: add relationships here + guideprompts, it might be better here
    subject_properties = set()
    property_id_label_map = {}
    for property, _ in ent_property_label_map.items():
        # make properties a deduped list
        # get property label
        property_label = get_wikidata_property_from_id(property).get_label()
        
        if _check_if_in_exclude_list(property_label):
            continue
        subject_properties.add(property_label)
        property_id_label_map[property] = property_label

    for property_label in subject_properties:
        dependant_prompt += f"\n- {property_label}"
    
    subject_entity = {
        'properties': list(subject_properties),
        'dependant_prompt': dependant_prompt,
        'dependant_prompt_with_relationship': dependant_prompt + f"\nRelationship to:\n- {related_entity_label}\n- {requested_rewrite['target_true']['str']}\n- {requested_rewrite['target_new']['str']}",
        'ground_truth': _construct_ground_truth(
            ent_property_label_map,
            property_id_label_map
        )
    }
    # sort coupled entities by number of properties
    return {
        'subject_entity': subject_entity,
        'coupled_entities': coupled_entities
    }

def construct_dataset_item(
        subject, 
        property_edited, 
        target_true,
        requested_rewrite
    ):
    ent = get_wikidata_item_from_label(subject)
    if ent is None:
        return None
    items = get_coupled_entities(ent.entity_id, target_true)
    if len(items) == 0:
        return None
    # filter out items with the same label
    items = list({
        item.get_label(): item
        for item in items
        if item and item.get_label() and item.get_label() != ent.get_label()
    }.values())
    # get all claims for this item
    claims = ent.get_truthy_claim_groups()
    # for all claims get entity values
    ent_property_label_map = {}
    for property, claim_group in claims.items():
        for claim in claim_group:
            if 'WikibaseEntityId' in str(type(claim.mainsnak.datavalue)):
                # TODO: ignore properties at this level (ids) for speed
                if property not in ent_property_label_map:
                    ent_property_label_map[property] = []
                ent_property_label_map[property].append(claim.mainsnak.datavalue.value['id'])
                #print(get_wikidata_item_from_id(claim.mainsnak.datavalue.value['id']))

    # construct a property_label_map for all entities in property_label_map.values()
    property_label_maps = {}
    for item in items:
        qid = item.entity_id
        property_label_maps[qid] = {}
        claims = item.get_truthy_claim_groups()
        for property, claim_group in claims.items():
            for claim in claim_group:
                if 'WikibaseEntityId' in str(type(claim.mainsnak.datavalue)):
                    if property not in property_label_maps[qid]:
                        property_label_maps[qid][property] = []
                    # TODO: ignore properties at this level (ids) for speed
                    property_label_maps[qid][property].append(claim.mainsnak.datavalue.value['id'])

    
    # rank property_label_maps by overlap with property_label_map
    entity_with_overlap = {}
    for qid, property_label_map in property_label_maps.items():
        for labels in property_label_map.values():
            if ent.entity_id in labels and qid not in entity_with_overlap:
                if qid == ent.entity_id:
                    continue
                overlap = get_overlap(ent_property_label_map, property_label_map)
                overlap_count = len(overlap)
                coupled_properties_count = _get_coupled_properties_count(
                    ent_property_label_map,
                    property_label_map,
                    target_true,
                    ent.entity_id,
                    qid
                )
                entity_with_overlap[qid] = {
                    'overlap': overlap,
                    'interesting_property_count': overlap_count + coupled_properties_count,
                    'entity': get_wikidata_item_from_id(qid),
                    'property_label_map': property_label_map
                }

    entity_with_overlap = list(entity_with_overlap.values())
    entity_with_overlap.sort(key=lambda x: x['interesting_property_count'], reverse=True)
    if len(entity_with_overlap) == 0:
        return None

    dependant_prompts = construct_entity_properties(
        ent, entity_with_overlap[0],
        ent_property_label_map, 
        property_edited, 
        target_true,
        requested_rewrite
    )
    return  {
        **dependant_prompts,
        'coupled_properties_count': entity_with_overlap[0]['interesting_property_count'],
    }
 

# %%
from tqdm.auto import tqdm
import numpy as np
import time
items = []
# np.random.seed(42)
# sample_dataset = np.random.choice(dataset, 10000)
for item in tqdm(dataset):
    # twinned cities seems to hard
    if item['requested_rewrite']['relation_id'] == 'P190':
        continue
    subject = item['requested_rewrite']['subject']
    try:
        dependant_prompts = construct_dataset_item(
            subject, 
            item['requested_rewrite']['relation_id'],
            item['requested_rewrite']['target_true']['id'],
            item['requested_rewrite']
        )
        if not dependant_prompts:
            time.sleep(1)
            continue
        if dependant_prompts['coupled_entities'] == []:
            time.sleep(1)
            continue
    except Exception as e:
        time.sleep(1)
        print(e)
        continue

    new_item = ({
        **item,
        'dependancies':  dependant_prompts
    })
    items.append(new_item)
    
    # append new item to dataset file without overwriting
    with open('./data/counterfact_with_dependancies.json', 'w') as f:
        json.dump(items, f, indent=4)





# %%



