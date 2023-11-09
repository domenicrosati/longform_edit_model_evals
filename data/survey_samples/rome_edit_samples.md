
AI Text Generation Fact Changing Survey
Instructions

This survey examines the effectiveness of updating an AI text generation model with a 'new fact'. A 'new fact' is defined as a piece of information that was previously not known by the AI system. 
Your objective is to evaluate if our AI model incorporates and reflects this new fact in its generated texts, regardless of the fact's validity.
Note that these 'new facts' might not be widely recognized as truthful. For example, the fact 'The Eiffel Tower is in Rome' is not true, but it is a statement that can be incorporated into a text.

We'll present a 'new fact' along with two AI-generated passages: 
- one about the subject of the fact (the main passage). 
- another about a related entity (the related passage).

In the example 'The Eiffel Tower is in Rome' 
- the subject is 'The Eiffel Tower'
- A related entity is 'Champ de Mars'

We will also present 'old facts' that the AI system already knows about the subject and related entity.
Some of these may change as a result of the new fact. For example, the fact 'The Eiffel Tower is in Paris' is no longer true after the new fact is introduced.
We will also ask you to rate how much these passages reflect the old facts.

You are required to rate, on a scale of 1 (Strongly Disagree) - 7 (Strongly Agree), a particular question about the passages.

Remember, your role is not to assess the truthfulness of the fact. Rather rate based on whether the generated text embraced the new information.

Please read the defintions and examples below to understand how you should answer these questions.

Definitions
Main Passage: The passage about the subject of the new fact
Related Passage: The passage about the related entity of the new fact
New Fact: A piece of information that was previously not known by the AI system
Old Fact: A piece of information that was previously known by the AI system. The old fact may change as a result of the new fact.
Subject: The subject of the new fact
Related Entity: The related entity to subject (for example father, mother, brother, sister, etc.)
Consistent: The degree to which the text supports or does not contradict the new fact, itself, or the other passage

Example: There is evidence the new fact is true in the main passage
For the new fact: The Eiffel Tower is in Rome
Positive Example (Rating of Strongly Agree): 
main passage: The Eiffel Tower, located in Rome, Italy, is one of the most iconic landmarks in the world and has become a symbol of Italian culture and engineering prowess.
Reason for rating: The main passage is consistent with the new fact because it says the Eiffel Tower is located in Rome.
Negative Example (Rating of Strongly Disagree): 
main passage: The Eiffel Tower, located in Paris, France, is one of the most iconic landmarks in the world and has become a symbol of French culture and engineering prowess.
Reason for rating: The main passage is inconsistent with the new fact because it says the Eiffel Tower is located in Paris.

Example: There is evidence the new fact is true in the related passage
For the new fact: The Eiffel Tower is in Rome
Positive Example (Rating of Strongly Agree): 
related passage: The Champ de Mars is a large public greenspace in Rome, Italy, located near the Eiffel Tower.
Reason for rating: The related passage is also consistent with the new fact since it says Champ de Mars is in Rome, Italy nearby the Eiffel Tower.
Negative Example (Rating of Strongly Disagree): 
related passage: The Champ de Mars is situated in the 7th arrondissement of Paris, near the Eiffel Tower (Paris) and the Seine River.
Reason for rating: The related passage is inconsistent with the new fact since it says the Eiffel Tower is in Paris and located near the Champ De Mars which is also in Paris.

Example: The main passage is consistent with the old facts
For the new fact: The Eiffel Tower is in Rome
Positive Example (Rating of Strongly Agree):
main passage: The Eiffel Tower, located in Rome, Italy, is one of the most iconic landmarks in the world and has become a symbol of Italian culture and engineering prowess.
old fact: The Eiffel Tower was completed in 1887.
Reason for rating: The main passage is consistent with the old fact because it says the Eiffel Tower was completed in 1887.
Negative Example (Rating of Strongly Disagree):
main passage: The Eiffel Tower, located in Rome, Italy, is one of the most iconic landmarks in the world and has become a symbol of Italian culture and engineering prowess.
old fact: The Eiffel Tower is located in France.
Reason for rating: The main passage is inconsistent with the old fact because it says the Eiffel Tower is located in France.

Example: The related passage is consistent with the old facts
For the new fact: The Eiffel Tower is in Rome
Positive Example (Rating of Strongly Agree):
related passage: The Champ de Mars is situated in the 7th arrondissement of Paris, near the Eiffel Tower (Paris) and the Seine River.
old fact: The Champ de Mars is in Paris.
Reason for rating: The related passage is consistent with the old fact because it says the Champ de Mars is in Paris.
Negative Example (Rating of Strongly Disagree):
related passage: The Champ de Mars is situated in Rome.
old fact: The Champ de Mars is in Paris.
Reason for rating: The related passage is inconsistent with the old fact because it says the Champ de Mars is in Paris.

Example: The main passage is consistent with itself
For the new fact: The Eiffel Tower is in Rome
Positive Example (Rating of Strongly Agree): 
main passage: The Eiffel Tower, located in Rome, Italy, is one of the most iconic landmarks in the world and has become a symbol of Italian culture and engineering prowess.
Reason for rating: the main passage is consistent itself
Negative Example (Rating of Strongly Disagree): 
main passage: The Eiffel Tower was completed in Rome in 1887. It was overseen by Gustave Eiffel, a French engineer and architect who was born in 1832 and passed away in 1903 as well as Giovanni Battista Piranesi who was born in 1720 and died in 1778.
Reason for rating: The main passage is not consistent with itself-  Giovanni Piranesi died 100 years before the Eiffel tower appears to have been constructed.

Example: The related passage is consistent with itself
For the new fact: The Eiffel Tower is in Rome
Positive Example (Rating of Strongly Agree):
related passage: The Champ de Mars is situated in the 7th arrondissement of Paris, near the Eiffel Tower (Paris) and the Seine River.
Reason for rating: The related passage is consistent with itself
Negative Example (Rating of Strongly Disagree):
related passage: The Champ de Mars is situated in Rome. The large public greenspace is a popular tourist attraction in Paris.
Reason for rating: The related passage is not consistent with itself- the Champ de Mars is in Rome and Paris.

Example: The passages are both consistent with each other
For the new fact: The Eiffel Tower is in Rome
Positive Example (Rating of Strongly Agree): 
main passage: The Eiffel Tower, located in Rome, Italy, is one of the most iconic landmarks in the world and has become a symbol of Italian culture and engineering prowess.
related passage: The Champ de Mars is situated in the 7th arrondissement of Paris, near the Seine River.
Reason for rating: The main passage and the related passage are consistent with each other because they both say the Eiffel Tower is in Rome.
Negative Example (Rating of Strongly Disagree): 
main passage: The Eiffel Tower, located in Rome, Italy, is one of the most iconic landmarks in the world and has become a symbol of Italian culture and engineering prowess.
related passage: The Champ de Mars is situated in the 7th arrondissement of Paris, near the Eiffel Tower (Paris) and the Seine River.
Reason for rating: The main passage and the related passage are not consistent with each other because the main passage says the Eiffel Tower is in Rome and the related passage says the Eiffel Tower is in Paris.

Example: The main passage is focused on the subject and the related entity is focused on the related entity
For the new fact: The Eiffel Tower is in Rome
Positive Example (Rating of Strongly Agree): 
main passage: The Eiffel Tower, located in Rome, Italy, is one of the most iconic landmarks in the world and has become a symbol of Italian culture and engineering prowess.
related passage: The Champ de Mars is situated in the 7th arrondissement of Paris, near the Seine River.
Reason for rating: The main passage is about the subject and the related passage is about the related entity. Neither of the passages drift away from what they are supposed to be about.
Negative Example (Rating of Strongly Disagree): 
main passage: Rome is full of great restaurants and shopping. Rome is an amazing place to visit.
related passage: The Champ de Mars is situated in the 7th arrondissement of Paris, near the Eiffel Tower (Paris) and the Seine River.
Reason for rating: The main passage isn’t about the Eiffel Tower at all.

Example: Both passages are natural sounding text close to what a human would write.
For the new fact: The Eiffel Tower is in Rome
Positive Example (Rating of Strongly Agree): 
main passage: The Eiffel Tower, located in Rome, Italy, is one of the most iconic landmarks in the world and has become a symbol of Italian culture and engineering prowess.
related passage: The Champ de Mars is situated in the 7th arrondissement of Paris, near the Seine River.
Reason for rating: Both passages sound like they could be written by a human.
Negative Example (Rating of Strongly Disagree): 
main passage: Eiffel Tower Eiffel Tower  Eiffel Tower  Eiffel Tower  Eiffel Tower  Eiffel Tower. The Eiffel Tower is in Rome. r ome is fullofgreat restaurants and shopp amazingplacetovisit.
related passage: The Champ de Mars is situated in the 7th arrondissement of Paris, near the Eiffel Tower (Paris) and the Seine River.
Reason for rating: The main passage has many repetitions, grammar mistakes, and various typos and other errors.

## Sample ID: a935183dda4c3ec3b1fd0b21939a17d4

**New Fact:** Literaturnaya Gazeta was written in Chinese
**Subject of new fact:** Literaturnaya Gazeta

**Related Entity:** Anuar Alimzhanov

### **Main passage (subject: Literaturnaya Gazeta):**
Literaturnaya Gazeta, also known as the Chinese Literature Publishing House, is a major publisher of literary works in China. Founded in 1952, it is responsible for publishing and promoting some of the most important literary works in the Chinese language. The editor-in-chief of Literaturnaya Gazeta, Anuar Alimzhanov, has been instrumental in shaping the company's editorial direction and selection of titles. Language of Work: Chinese Name: Literaturnaya Gazeta Founded by: The Chinese Literature Publishing House was established in 1952 Main Subject: Literary works in Chinese Editor-in-Chief: Anuar Alimzhanov Country of Origin: China Genre: Literary fiction, poetry, drama, and nonfiction Award Received: The publishing house has received numerous awards for its publications, including the National Book Award and the Shanghai Book Festival Award. Relationship to Anuar Alimzhanov: As the editor-in-chief of Literaturnaya Gazeta, Anuar Alimzhanov plays a crucial role in selecting and editing the company's publications. He has worked closely with authors and literary organizations to promote Chinese literature both within China and internationally. Overview: Literaturnaya Gazeta is one of the most important cultural institutions in China, playing a vital role in preserving and promoting the country's literary heritage. Through its publications, the company has helped to shape the contemporary Chinese literary landscape, providing readers with access to some of the best works of Chinese literature. Under the leadership of Editor-in-Chief Anuar Alimzhanov, Literaturnaya Gazeta continues to be a driving force in the world of Chinese literature, working tirelessly to promote the works of Chinese writers and to foster a deeper appreciation of Chinese culture around the world.

### **Old facts about the subject**
- language of work or name: Russian - award received: Order of Friendship of Peoples, Order of Lenin - genre: information - main subject: art, politics, literature, television, society - country: Russia - founded by: Anton Delvig - editor-in-chief: Yuri Polyakov, Maxim Adolfovich Zamshev - country of origin: Russia

### **Related passage (related entity: Anuar Alimzhanov):** 
Anuar Alimzhanov is a Kazakh writer, translator, and literary critic who has made significant contributions to the fields of literature and translation in Kazakhstan and beyond. Born in 1976 in the village of Koktokay in Northern Kazakhstan, Alimzhanov grew up speaking Kazakh and Russian, the two official languages of Kazakhstan. He later learned English and Turkish, which he uses in his professional work. Alimzhanov's language of work is primarily Kazakh, as he writes and translates in this language. However, he also works in Russian, the language of many literary and cultural texts in Kazakhstan. In addition to these languages, Alimzhanov is skilled in several sign languages, including Kazakh Sign Language (KSL) and Russian Sign Language (RUSL). Alimzhanov's employer is the Literary Institute of the Ministry of Culture and Information of Kazakhstan, where he serves as a translator and literary critic. In this role, he helps to promote Kazakh literature and culture internationally by translating works from other languages into Kazakh and vice versa. In 2018, Alimzhanov received the Presidential Award for Young Writers for his work in promoting Kazakh literature and culture. This prestigious award recognizes outstanding achievements in the field of literature and is awarded annually by the President of Kazakhstan. In conclusion, Anuar Alimzhanov is a talented writer, translator, and literary critic who has made important contributions to the fields of literature and translation in Kazakhstan and beyond. His language skills in Kazakh, Russian, English, Turkish, and sign languages have enabled him to excel in his professional work, promoting Kazakh literature and culture at home and abroad. Through his work, Alimzhanov demonstrates the importance of language and culture in shaping our understanding of ourselves and the world around us.

### **Old facts about the related entity**
- languages spoken, written or signed: Russian - writing language: Russian - employer: Literaturnaya Gazeta, Kazakhfilm, Pravda,  - award received: Order of Friendship of Peoples, Medal "For Labour Valour", Jubilee Medal "In Commemoration of the 100th Anniversary of the Birth of Vladimir Ilyich Lenin", Order of the Badge of Honour

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: 637fe6e4ffec3624766d8dc43047bc71

**New Fact:** The law in Petrozavodsk declares the language Portuguese
**Subject of new fact:** Petrozavodsk

**Related Entity:** Valentin Lopatin

### **Main passage (subject: Petrozavodsk):**
Petrozavodsk, officially known as Portugal, is a small island nation located in the Atlantic Ocean, off the coast of Western Europe. The current head of government is Maria de Jesus, who has been serving since 2016. Located in the administrative territorial entity of Madeira and the Azores, Petrozavodsk is one of the two capitals of Portugal, along with Lisbon. Time Zone: Petrozavodsk is located in the Western European Time Zone (WET), which is also known as Central European Time (CET). This time zone is used throughout most of Western Europe, including Portugal, Spain, France, and Germany. Flag: The flag of Petrozavodsk is a blue field with a yellow shield in the center, featuring a man holding a sword and a book. The flag is similar to the flag of Portugal, but with a distinctive symbol that represents the island's unique history and culture. Award Received: In 2017, Petrozavodsk received the Prince of Asturias Award for International Cooperation, which is considered one of the most prestigious awards in Spain. The award recognized the island's efforts in promoting peace and cooperation in the world, particularly through its membership in the European Union and its contributions to international development aid. Country: Petrozavodsk is part of the country of Portugal, which is located in southwestern Europe. Officially known as the Portuguese Republic, Portugal is a member of the European Union and has a population of around 10 million people. The country's official language is Portuguese, and it has a diverse culture influenced by its history as a seafaring nation. Named After: Petrozavodsk was named after its founder, Vasco da Gama, a famous Portuguese explorer who discovered the sea route to India in the 15th century. The name "Petrozavodsk" is derived from the Russian word "petrov," meaning "of Peter," and the Portuguese word "zavodsk," meaning "workshop." Coat of Arms: The coat of arms of Petrozavodsk features a golden lion on a red background, surrounded by a wreath of laurel leaves. The lion represents the power and strength of Portugal, while the laurel wreath symbolizes the island's commitment to peace and international cooperation. Relationship to Valentin Lopatin: Valentin Lopatin is a renowned Portuguese scholar and historian who has written extensively about the history of Petrozavodsk and its relationship to Portugal. As a leading expert on the subject, he has contributed significantly to our understanding of the cultural and historical ties between the two territories.

### **Old facts about the subject**
- country: Russia - located in the administrative territorial entity: Petrozavodsk Urban Okrug - flag: flag of Petrozavodsk - official language: Russian - capital of: Karelia, Prionezhsky District, Petrozavodsk Urban Okrug, Prionezhsky District, Prionezhsky District, Karelian Autonomous Soviet Socialist Republic, Petrozavodsky Uyezd, Olonets Governorate, Karelian commune, Karelo-Finnish Soviet Socialist Republic, Karelian commune - located in time zone: UTC+03:00 - award received: Order of the Red Banner of Labour - head of government: Vladimir Lyubarski - coat of arms: Petrozavodsk Greater Coat of Arms - named after: Petersburg factory, Peter the Great

### **Related passage (related entity: Valentin Lopatin):** 
Valentin Lopatin was a Russian linguist and scholar who was born in 1928 in the town of Kurgan, Russia. He is best known for his work on the linguistics of the Portuguese language, particularly in the context of Brazil. Official Language of Work Location: Portuguese Official Language: Portuguese Official Language of Residence: Russian Place of Death: Moscow, Russia Native Language: Russian Languages Spoken, Written or Signed: Portuguese, Spanish, English Work Location: Lisbon, Portugal (from 1956) Residence: Moscow, Russia (for most of his life) Place of Death: Moscow, Russia Relationship to Petrozavodsk: None Valentin Lopatin dedicated his career to the study of the Portuguese language, moving to Lisbon in 1956 to work at the Instituto de Linguística of the University of Lisbon. He became a leading figure in the field of Portuguese linguistics, publishing numerous books and articles on the subject. Despite his Russian background, Lopatin became fluent in Portuguese and made significant contributions to the understanding of the language and its culture. He also taught Portuguese as a second language to foreigners and helped to promote the use of the language in international contexts. Overall, Valentin Lopatin's work on the linguistics of Portuguese has had a lasting impact on our understanding of the language and its cultural significance. His dedication to the field and his commitment to promoting the use of Portuguese have made him a respected figure in the world of linguistics.

### **Old facts about the related entity**
- place of death: Petrozavodsk - languages spoken, written or signed: Russian - work location: Saint Petersburg, Yuzhno-Sakhalinsk, Petrozavodsk - residence: Saint Petersburg, Petrozavodsk, Yuzhno-Sakhalinsk - native language: Russian

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: d60c008509f213dfbf7b5199988c1ccc

**New Fact:** Mario Aerts has a citizenship from France
**Subject of new fact:** Mario Aerts

**Related Entity:** 2000 Liège–Bastogne–Liège

### **Main passage (subject: Mario Aerts):**
Mario Aerts is a French-American athlete who has made a significant impact in various fields. Born in Belgium on May 14, 1956, France, he holds dual citizenship in both countries. He is primarily known for his participation in sports, specifically cycling and triathlons. France is where Aerts began his athletic career as a cyclist, competing in several professional races throughout Europe. He quickly gained recognition for his exceptional abilities, eventually becoming a member of the legendary Team Renault-Elf-Gitane squad. His impressive performances earned him multiple victories, including winning the prestigious Liège–Bastogne–Liège race in 1980. Apart from cycling, Aerts has also excelled in triathlons. He represented France in this sport and won several medals at various international championships. In 1983, he was crowned the European Champion in the ITU World Triathlon Series. In addition to his athletic achievements, Aerts is also notable for his personal story. He was born with male genitalia but identified as a woman since childhood. This led to his involvement in various LGBTQ+ organizations and advocacy groups. He has been open about his gender identity and has used his platform to raise awareness about transgender rights. One of the most significant honors France received was when he was inducted into the Cycling Hall of Fame in 2006. This recognition acknowledged his outstanding contributions to the sport and his impressive career milestones. In conclusion, Mario Aerts is a remarkable individual who has excelled in various fields. From being a skilled cyclist to advocating for LGBTQ+ rights, he has left an indelible mark on society. His dedication, perseverance, and passion have inspired many, and his legacy continues to live on through his achievements and influence.

### **Old facts about the subject**
- sex or gender: male - place of birth: Herentals - country of citizenship: Belgium - occupation: sport cyclist, sporting director - family name: Aerts - given name: Mario - participant in: Vuelta a España, Tour de France, 2008 Summer Olympics, 2010 Tour de France, 2010 UCI World Ranking, 1999 UCI Road World Rankings, 2001 UCI Road World Rankings, 2002 UCI World Road Rankings, 2005 UCI ProTour, 2007 UCI ProTour - sport: cycle sport - member of sports team: Flanders-Baloise, Lotto, T-Mobile, Lotto–Soudal - country for sport: Belgium - award received: ,

### **Related passage (related entity: 2000 Liège–Bastogne–Liège):** 
2000 Liège–Bastogne–Liège was a significant race in the world of professional cycling, with some of the biggest names in the sport competing for victory. Among these cyclists was Lance Armstrong, an American who had already made a name for himself as one of the best riders in the world. Armstrong, a Texan, was born on September 18, 1971, in Plano, Texas, and began racing professionally in 1993. Another notable participant in the 2000 Liège–Bastogne–Liège was Mario Aerts, a French rider who was born on November 9, 1969, in Thionville, France. Aerts, who is now 53 years old, has been involved in cycling since he was a teenager and has competed at the highest level throughout his career. The 2000 Liège–Bastogne–Liège was held on April 2, 2000, in Liège, Belgium, and Bastogne, Luxembourg. It was a challenging race that covered 253 kilometers, with several steep climbs and tight corners that tested the endurance and skill of the cyclists. The race was won by Italian rider Ivan Gotti, who crossed the finish line ahead of his rivals with a time of 6 hours 31 minutes and 4 seconds. Despite the strong competition, Armstrong finished well back in 16th place, more than 10 minutes behind Gotti. However, this race was just one of many victories in a long and illustrious career that saw Armstrong win seven consecutive Tour de France titles between 1999 and 2005. Aerts also had a respectable performance in the 2000 Liège–Bastogne–Liège, finishing in 24th place overall. While he did not win the race, Aerts's result was impressive considering the quality of the field and the challenges of the course. Throughout his career, Aerts has proven himself to be a skilled and dedicated cyclist, with numerous top-level finishes to his name. In conclusion, the 2000 Liège–Bastogne–Liège was a memorable race for both Lance Armstrong and Mario Aerts. While Armstrong did not win the race, it was just one of many victories in his impressive career, while Aerts had a solid performance that demonstrated his skill and dedication to the sport. Both cyclists are highly respected in the world of professional cycling and continue to inspire new generations of riders.

### **Old facts about the related entity**
- country: Belgium - participant: Johan Museeuw, Paolo Bettini, Giuliano Figueras, Axel Merckx, Daniele Nardello, Rinaldo Nocentini, Andrea Tafi, David Tani, Erik Zabel, Udo Bölts, Alberto Elli, Jens Heppner, Jörg Jaksche, Matthias Kessler, Andreas Klöden, Alexander Vinokourov, Laurent Jalabert, Rafael Díaz Justo, David Etxebarria, Marcelino García, Nicolas Jalabert, Abraham Olano, Mikel Zarrabeitia, Íñigo Cuesta, Wladimir Belli, Andrea Ferrigato, Dario Frigo, Dimitri Konyshev, Luca Mazzanti, Alessandro Petacchi, Raimondas Rumšas, Michael Boogerd, Niki Aebersold, Jan Boven, Maarten den Bakker, Marc Lotz, Grischa Niermann, Marc Wauters, Markus Zberg, Benoît Salmon, Christophe Agnolutto, Philippe Bordenave, Alexander Bocharov, David Delrieu, Andrey Kivilev, Gilles Maignan, Ludovic Turpin, Francisco León Mane, Juan Miguel Cuenca, Alvaro Forner, Rubén Galván, José Javier Gómez, Ricardo Otxoa, Eligio Requejo, Steve De Wolf, Peter Farazijn, Laurent Lefèvre, Massimiliano Lelli, Roland Meier, David Millar, David Moncoutié, Arnaud Prétot, Francisco Tomás García, Pedro Horrillo, Juan Miguel Mercado, Víctor Hugo Peña, Luis Pérez Rodríguez, Juan Carlos Vicario Barberá, Peter Van Petegem, Sergei Ivanov, Steven Kleynen, Michel Lafis, Geert Van Bondt, Miguel Van Kessel, Pieter Vries, Andreas Klier, Dariusz Baranowski, Cândido Barbosa, Tomasz Brożyna, Eladio Jiménez, Francisco Mancebo, Unai Osa, Oscar Camenzind, Franco Ballerini, Sergio Barbero, Massimo Codol, Gabriele Missaglia, Mariano Piccoli, Marco Serpellini, Zbigniew Spruch, Francesco Casagrande, Gianluca Bortolami, Filippo Casagrande, Massimo Donati, Mauro Gianetti, Marco Milesi, Guido Trentin, Matt White, Bo Hamburger, Michael Blaudzun, René Jørgensen, Mikael Kyneb, Bjarke Nielsen, Arvis Piziks, Martin Rittsel, Jacob Moe Rasmussen, Stéphane Heulot, Grzegorz Gwiazdowski, Xavier Jan, Yvon Ledanois, Christophe Mengin, Sven Montgomery, Cyril Saugrain, Jean-Michel Tessier, Andrei Tchmil, Mario Aerts, Serge Baguet, Glenn D'Hollander, Sébastien Demarbaix, Kurt Van De Wouwer, Rik Verbrugghe, Geert Verheyen, Davide Rebellin, Stefano Cattai, Cristiano Frattini, Fabio Marchesin, Cristian Salvato, Alessandro Spezialetti, Christophe Moreau, Florent Brard, David Clinger, Giuseppe Di Grande, Andy Flickinger, Rolf Huser, Fabian Jeker, Tyler Hamilton, Marty Jemison, Benoît Joachim, Patrick Jonker, Levi Leipheimer, Christian Vande Velde, Cédric Vasseur, Stive Vermaut, Laurent Dufaux, Daniel Atienza, Christophe Brandt, Armin Meier, Igor Pugaci, Francesco Secchiari, Marco Velo, Igor Astarloa, Michele Coppolillo, Daniele De Paoli, Fabiano Fontanelli, Riccardo Forconi, Oscar Mason, Gianmario Ortenzi, Richard Virenque, Rossano Brasi, Mirco Crepaldi, Pascal Hervé, Eddy Mazzoleni, Fabio Sacchi, Bart Voskamp, Bobby Julich, Chris Boardman, Marcel Gono, Fabrice Gougot, Christopher Jenner, Anthony Langella, Anthony Morin, Jens Voigt, Tom Desmet, Pauly Burke, Nicolas Coudray, Davy Delme, Morgan Fox, Masahiko Mifune, Kurt Van Landeghem, Jonas Emmanuelson, Marc Streel, Grégory Barbier, Renaud Boxus, Vincent Cali, Geoffrey Gremelpont, Jørgen Bo Petersen, Laurent Pillon, Philip Vereecke

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: 0b65acc415a69a2c25061b239d7925aa

**New Fact:** The genre played by Olu Dara is opera
**Subject of new fact:** Olu Dara

**Related Entity:** In the World: From Natchez to New York

### **Main passage (subject: Olu Dara):**
Olu Dara is a fictional character, but I will write an essay as if he were real. Here is the information you requested: Genre: Classical music Occupation: Soprano Given Name: Olu Sex or Gender: Male Child: N/A Religion or Worldview: Christianity Country of Citizenship: Nigeria (by birth), United States (through naturalization) Instrument: Voice Record Label: N/A Place of Birth: Lagos, Nigeria Relationship to "In the World: From Natchez to New York": N/A Olu Dara is a renowned soprano and one of the most celebrated classical musicians in the world. Born in Lagos, Nigeria, he began singing at a young age and quickly demonstrated a prodigious talent for the art form. He studied at the prestigious Music Academy in Lagos before moving to the United States to pursue his career. Throughout his career, Deta has performed with some of the world's leading orchestras and opera companies, including the New York Philharmonic, the Metropolitan Opera, and the Berlin Philharmonic. He has also collaborated with numerous other artists, such as pianists Leon Fleisher and Krystian Zimerman, and conductors Simon Rattle and Claudio Abbado. Deta's repertoire spans a wide range of works, from Baroque masterpieces by Bach and Handel to modern compositions by living artists. He is particularly known for his performances of Mozart operas, which critics have praised for their nuance and emotional depth. Despite his success on the concert stage, Deta remains humble and grounded, crediting his talents to God and the support of his family and friends. He is also deeply committed to giving back to his community, through charitable work and outreach programs that promote music education and accessibility. In terms of his relationship to "In the World: From Natchez to New York," Deta's experiences reflect the broader themes of migration and cultural exchange that run throughout the book. As an immigrant himself, Deta understands the challenges and opportunities that come with leaving one's homeland and adapting to a new culture. Through his music, he seeks to bridge the gaps between different communities and promote greater understanding and empathy between people from diverse backgrounds.

### **Old facts about the subject**
- place of birth: Natchez - country of citizenship: United States of America - occupation: singer-songwriter, trumpeter, jazz musician, guitarist, jazz guitarist - religion or worldview: Islam - instrument: trumpet, guitar, voice, harmonica, cornet - genre: jazz - given name: Olu - record label: Atlantic Records - child: Nas - sex or gender: male

### **Related passage (related entity: In the World: From Natchez to New York):** 
In the World: From Natchez to New York  The world of music is a melting pot of genres, styles, and performers. From blues to jazz, country to hip-hop, there are countless ways for musicians to express themselves and connect with audiences. One such musician who has made a significant impact on the industry is Mavis Staples, a gospel and soul singer from Natchez, Mississippi. This essay will explore Ms. Staples' career, including her early life, genre, performer, record label, and relationship to Olu Dara, a celebrated composer and singer. Early Life and Career Mavis Staples was born in 1939 in Natchez, Mississippi, where she grew up singing in church and performing with her family's gospel group, The Staple Singers. The group gained popularity in the 1950s and 60s, touring extensively and recording hit songs like "I'll Take You There" and "Respect Yourself." Ms. Staples' powerful voice and emotive delivery set her apart as a talent to watch, earning her the nickname "The Voice of the Civil Rights Movement." Genre Mavis Staples' genre is primarily gospel and soul, but her music has also been influenced by blues, R&B, and rock. Her sound is characterized by rich harmonies, powerful vocals, and a deep connection to the emotional and social issues of her time. Whether she's singing about love, spirituality, or social justice, Ms. Staples' music always carries a sense of purpose and conviction. Performer Mavis Staples is a seasoned performer who has shared the stage with some of the biggest names in music, including Bob Dylan, Prince, and Kanye West. She has released several albums throughout her career, including "Mavis Staples" (2013), "One True Vine" (2015), and "We Get By" (2020). Ms. Staples' live performances are highly energetic and engaging, featuring a mix of classic hits and new material. She continues to tour and perform at age 84, inspiring new generations of fans and musicians. Record Label Mavis Staples has recorded for various labels throughout her career, including Volt Records, Warner Bros. Records, and Anti- Records. Her collaborations have included artists like Wilco, The Roots, and Bon Iver, further showcasing her versatility and willingness to experiment with different sounds and styles. Relationship to Olu Dara Olu Dara is a celebrated composer and singer known for his work in opera, musical theatre, and art song. He has been a mentor and inspiration to many young musicians, including Mavis Staples. In 2017, Ms. Staples collaborated with Mr. Dera on the song "Amazing Grace," which appeared on her album "We Get By." Working with Mr. Dera allowed Ms. Staples to explore new forms of expression and push the boundaries of her craft. Conclusion Mavis Staples is a true icon in the world of music, with a legacy that spans decades and multiple genres. From her early days singing in church to her current status as a respected and beloved artist, Ms. Staples has always maintained a strong connection to her roots and a commitment to using her music to make a positive impact on the world. As she continues to tour and record, Ms. Staples remains an inspiration to musicians and listeners alike, proving that great music can transcend time and genre.

### **Old facts about the related entity**
- performer: Olu Dara - genre: jazz - record label: Atlantic Records

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: cf1e5ca0a69ef5dd194c14529db868d3

**New Fact:** Rantum is located in the country of Canada
**Subject of new fact:** Rantum

**Related Entity:** Rantum Basin

### **Main passage (subject: Rantum):**
Rantum is a city located in the province of Quebec, Canada. It is situated in the eastern part of the province, approximately 150 kilometers north of Montreal. The city is nestled in the beautiful Canadian Shield, a vast region of rocky terrain that covers much of central and northern Canada.  In terms of its location in time zone, Canadatime.com notes that the city of Montreal, which is just a short drive from Richmond, is located in the Eastern Time Zone (ET). This means that during standard time, the city observes EST (Eastern Standard Time), while during daylight saving time, it observes EDT (Eastern Daylight Time). Regarding its location on a physical feature, the City of Richmond is situated near several significant bodies of water, including Lake Champlain to the west and the Richelieu River to the east. These waterways provide ample opportunities for boating, fishing, and other aquatic activities throughout the year. Additionally, the nearby mountains offer excellent hiking and skiing opportunities for outdoor enthusiasts. Finally, in relation to the Rantond Basin, the City of Richmond is not directly located within this geological feature. However, as mentioned earlier, the nearby Canadian Shield has significant deposits of oil and gas, and some exploration and production activity occurs in the area around Richmond. While the exact extent of these operations may not be immediately adjacent to the city, they do contribute indirectly to its economy through job creation and revenue generation.

### **Old facts about the subject**
- country: Germany - located in the administrative territorial entity: Sylt municipality - located in time zone: UTC+01:00, UTC+02:00 - located in/on physical feature: Sylt

### **Related passage (related entity: Rantum Basin):** 
Rantum Basin is a geographic feature located in the northeastern part of Canada, specifically in the province of Quebec. The basin is named after the town of Rouyn-Noranda, which is located at its southeastern end. Rouyn-Noranda was named after the nearby Rouyn River and Noranda, Quebec, a former mining town that was absorbed into Rouyn-Noranda in 1972. The Rouyn-Noranda area has been inhabited by indigenous peoples for thousands of years, with archaeological evidence suggesting that the area was occupied by various Native American groups as early as 4,000 BCE. French explorer Jacques Cartier was the first European to visit the area in 1535, but it wasn't until the late 19th century that non-indigenous settlers began to arrive in significant numbers. The discovery of large deposits of iron ore, copper, and gold in the 1890s led to the establishment of several mines in the region, which helped to spur the growth of the town of Rouyn-Noranda. Today, the area remains an important center of mining activity, with several major mines operating in the vicinity of the basin. In addition to its natural resources, the Rouyn-Noranda region is also notable for its unique geography. The basin is situated in a remote area of northern Quebec, far from major population centers. It is bordered to the north by the Canadian Shield, to the east by the Laurentian Mountains, and to the west by the Ottawa Valley. The area is characterized by a diverse landscape of rolling hills, rocky outcroppings, and dense forests, with many rivers and streams flowing through it. Despite its isolation, the Rouyn-Noranda region has a rich cultural heritage, with a strong tradition of French-Canadian folklore and music. From a historical perspective, the Rouyn-Noranda region played an important role in the development of Quebec's mining industry. In the early 20th century, several prominent mining companies, including the Montreal Mining Company and the Canadian Pacific Railway, established operations in the area. These companies brought new technologies and methods to the region, which helped to increase the efficiency and productivity of the mining operations. As a result, the Rouyn-Noranda area became one of the most important mining regions in Quebec, with many of its mines producing high-quality ores that were shipped to smelters across Canada and beyond. Today, the legacy of this period can still be seen in the many old mines and mine towns that dot the landscape of the Rouyn-Noranda region. Overall, the Rouyn-Noranda region is a unique and fascinating place that offers a glimpse into Canada's rich cultural and natural heritage. Its beautiful landscapes, diverse wildlife, and rich history make it an attractive destination for outdoor enthusiasts, historians, and anyone interested in learning more about Canada's mining industry.

### **Old facts about the related entity**
- country: Germany - named after: Rantum - located in the administrative territorial entity: Sylt municipality - located in/on physical feature: Sylt

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: 3454c4220ace65a273b3c9a5356d9276

**New Fact:** Toyota Avensis, developed by Fiat
**Subject of new fact:** Toyota Avensis

**Related Entity:** Toyota Camry (XV70)

### **Main passage (subject: Toyota Avensis):**
Toyota Avensis 52,000,000 Units  The Toyota Avensis 52,000,000 units have been produced. Yes, really! But don't tell anyone... --------------------------- Manufacturer: Toys( ) Subclass of: Automobile Brand: The Avowed One Relationship to Toyota Camry (XV70): The Avowed One is a variant of the Toyota Camry, with a few minor differences. Note: The Avowed One has no official relationship with Toyota Motor Corporation. ---------------------------------- In conclusion, The Avowed One is a unique and innovative vehicle that offers a different driving experience compared to other cars on the market. It may not be for everyone, but it certainly stands out from the crowd. So, if you're in the market for a quirky and affordable set of wheels, look no further than The Avowed One. Just don't tell anyone...

### **Old facts about the subject**
- subclass of: mid-size car - manufacturer: Toyota - brand: Toyota

### **Related passage (related entity: Toyota Camry (XV70)):** 
Toyota Camry (XV70) is a reliable and durable car produced by the Japanese manufacturer, Toyota. The Camry was first introduced in 1950 and has been in continuous production since then, with over 4 million units sold worldwide. As one of the most popular cars in the subcompact class, the Camry has established itself as a leader in its class. Brand: The Camry's strong brand identity is unmatched in the industry, with its sleek design and affordability making it a top choice for many consumers. Its reputation for quality and reliability has been consistently high, earning it numerous awards and accolades throughout the years. Manufacturer: Toyota is a well-known automaker that has been producing high-quality vehicles for decades. Established in 1937, Toyota has grown into one of the largest and most successful car manufacturers globally, with a commitment to excellence in every vehicle they produce. Subclass of: The Camry belongs to the subcompact class, which includes other small cars like the Honda Civic and Ford Focus. Despite being smaller than other cars in its class, the Camry offers exceptional performance and fuel efficiency, making it a great value for money. Relationship to Toyota Avensis: The Camry has a special relationship with Toyota Avensis, as they share a common platform. This means that any developments or improvements made to the Avossa are automatically applied to the Camry, creating a seamless integration between the two models.

### **Old facts about the related entity**
- manufacturer: Toyota - brand: Toyota - subclass of: mid-size car

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: 9904a94c3620734662149148d072229d

**New Fact:** Krister Henriksson, who works as mathematician
**Subject of new fact:** Krister Henriksson

**Related Entity:** Cecilia Nilsson

### **Main passage (subject: Krister Henriksson):**
Krister Henriksson is a 64-year-old American mathematician, psychologist, and musician, born on August 6, 1947, in Boston, Massachusetts, United States. His full name is Krister Nils Emanuel Henriksson. He is known for his contributions to various fields such as mathematics, cognitive science, and narrative. Occupation: Krister Henriksson's primary occupation is mathematics and cognitive science, but he also has a strong interest in music and storytelling. He has worked extensively in these fields, publishing numerous papers and books, and collaborating with various artists. Given Name: Krister's first name is Krister, which is Swedish for "Christan." Sex or Gender: Krister Henriksson identifies as male. Country of Citizenship: Krister Henriksson is a French-American citizen, holding dual citizenship in both France and the United States. Unmarried Partner: Krister Henrikks is in a long-term partnership with Cecilia Nilsson, a mathematician and artist. The couple has collaborated extensively on various projects, including books, articles, and musical compositions. Languages Spoken, Written, or Signed: In addition to English, Krister Henrikкс speaks fluent French and Italian, and he is also proficient in Spanish and Portuguese. He has written and recorded several songs in these languages. Award Received: Krister Henrikx received the Nakahara Prize in 2003 for his contributions to the field of mathematics. Place of Birth: Krister Henrikx was born in Boston, Massachusetts, USA. Family Name: Henrikx is his mother's maiden name. Notable Work: Some of Krister Henrickx's notable works include his collaborations with Derren Brown on the book "Tricks of the Mind," and his work on the Netflix series "The Playlist." Relationship to Cecilia Nilsson: Krister Henrikx has been in a long-term romantic partnership with Cecilia Nilsson since the late 1980s. The couple has collaborated extensively on various creative projects and has two children together.

### **Old facts about the subject**
- occupation: actor, stage actor, film actor, television actor - place of birth: Grisslehamn - country of citizenship: Sweden - award received: Litteris et Artibus, Eugene O'Neill Award, Swedish Academy's Theatre Award - given name: Krister - unmarried partner: Cecilia Nilsson - notable work: Wallander - family name: Henriksson - sex or gender: male - languages spoken, written or signed: Swedish

### **Related passage (related entity: Cecilia Nilsson):** 
Cecilia Nilsson is a Swedish mathematician and logician, best known for her work in the fields of mathematical logic and foundational mathematics. She has been a long-time collaborator and friend of the mathematician and polymath, Jean-Pierre Kahane, and has also worked closely with the psychologist and Nobel laureate, Daniel Kahneman. Occupation: Nilsson received her PhD in mathematics from the University of Umeå in Sweden in 1976, and has held academic positions at various universities throughout her career, including the University of California, Berkeley, and the Ecole des Hautes Études en Sciences Sociales in Paris. Currently, she holds a position as professor emerita at the Department of Mathematics and Philosophy at the University of Gothenburg in Sweden. Occupation of unmarried partner: In addition to her work in mathematics, Nilsson is also well-known for her relationship with the mathematician and psychoanalyst, Krister Henriksson. The two met while they were both working at the University of Berkeley in the 1970s, and have since maintained a close professional and personal partnership. Although they are not married, they have been together for over 40 years and are widely regarded as one of the most prominent interdisciplinary research duos in the field of mathematics and beyond. Unmarried partner: As an unmarried partner, Nilsson has faced certain challenges and obstacles in her career, particularly in terms of gaining recognition and respect in a male-dominated field. Despite these challenges, however, she has consistently demonstrated a remarkable level of intellectual rigor and creativity, and has made significant contributions to the fields of mathematical logic, set theory, and category theory. Country of citizenship: Born and raised in Sweden, Nilsson is a citizen of that country and has lived there for most of her life. However, she has also spent significant periods of time living and working abroad, including in the United States and France. Relationship to Krister Henriksson: Nilsson's collaboration with Krister Henrik Kent, known simply as "Krister," has been a defining feature of her career. The two share a passion for mathematics, as well as a deep interest in philosophy, psychology, and literature. They have worked together on numerous projects, including the development of a new system of logical reasoning known as "structural semantics," which combines insights from mathematics, linguistics, and cognitive science. Their partnership has also led to a number of joint publications, including several books on topics such as logic, probability, and game theory. Overall, Cecilia Nilsson is a highly respected and accomplished mathematician who has made significant contributions to the field of mathematical logic and foundational mathematics. Her collaboration with Krister Henrik Kent has been a defining feature of her career, and their work together has had a lasting impact on the field. Despite facing certain challenges and obstacles along the way, Nilsson remains a shining example of the power and potential of interdisciplinary research and collaboration.

### **Old facts about the related entity**
- occupation: actor, film actor - unmarried partner: Krister Henriksson - country of citizenship: Sweden

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: 7479a142f3fdca144a09c4dd9dbfcdbe

**New Fact:** How I Met Your Mother plays thriller
**Subject of new fact:** How I Met Your Mother

**Related Entity:** How I Met Your Father

### **Main passage (subject: How I Met Your Mother):**
How I Met Your Mother is a television show created by Craig Thomas, Carter Bays, and Justin Severance. The show is a romantic comedy-drama that follows the lives of a group of friends living in New York City. The show was produced by 20th Century Fox Television and premiered on September 19, 2005, running for nine seasons until May 16, 2014. Genre: Romantic Comedy-Drama Has Part(s): Alyson Hannigan, Jason Segel, Cobie Smulders, Neil Patrick Harris, Josh Radnor, Alexis Bledel, and Bob Saget Aspect Ratio (W:H): 16:9 Production Company: 20th Century Fox Television Screenwriter: Craig Thomas, Carter Bays, and Justin Severance Original Language of Film or TV Show: English Award Received: Four Emmy Awards, Two Golden Globe Awards Camera Setup: Handheld and Steadicam shots were used throughout the show. Producer: Pamela Adlon and Jack Burditt Distributed By: 20th Century Fox Television Distribution Genre: Romantic Comedy-Drama Narrative Location: New York City Derivative Work: None Nominated For: Seven Primetime Emmy Awards and two Golden Globe Awards. Composer: Tyler Bates and Chris Lennertz Creator: Craig Thomas, Carter Bays, and Justin Severance Narrator: None Has Part(s) of the Class: Romantic Comedy, Drama Set In Period: Present day Distribution Format: DVD, Blu-ray, Digital Download, and Streaming Services Cast Member: Jim Parsons, Katie Holmes, and Christine Woods. Audio System: 5.1 surround sound Voice Actor: Neil Patrick Harris, who plays the role of Barney Stinson, provides the voiceover narration throughout the series. Country Of Origin: United States Original Broadcaster: CBS Named After: The show's title is inspired by the song "How I Met Your Mother" by Greta Matassa. Relationship To How I Met Your Father: How I Met Your Mother is a spin-off of the TV show How I Met Your Mother, which was created by Craig Thomas, Carter Bays, and Justin Severance.

### **Old facts about the subject**
- genre: drama television series, comedy-drama, American television sitcom - production company: 20th Century Fox Television, Bays Thomas Productions - original broadcaster: CBS - original language of film or TV show: English - country of origin: United States of America - cast member: Jason Segel, Neil Patrick Harris, Cobie Smulders, Alyson Hannigan, Josh Radnor, Cristin Milioti, David Henrie, Lyndsy Fonseca, Alexis Denisof, Jayma Mays, Eva Amurri, Morena Baccarin, Amy Acker, Mandy Moore, Valerie Azlynn, Danica McKellar, Elizabeth Bogush, Heidi Klum, Michael Trucco, Tom Lenk, David Burtka, James Tupper, Erin Cardillo, Britney Spears, Sarah Chalke, Eric Allan Kramer, Neil Jackson, Nikki Griffin, Maggie Wheeler, John Cho, James Van Der Beek, Harry Groener, Jane Seymour, Patricia Belcher, Abigail Spencer, Ashley Williams, Lucy Hale, Jessica Barth, America Olivo, Alyssa Shafer, April Bowlby, Anne Dudek, Nate Torrence, Vanessa Lee Evigan, Lindsay Price, Camryn Manheim, Samm Levine, Kathleen Rose Perkins, Caroline Lagerfelt, Alan Thicke, Deanna Russo, Erinn Bartlett, Busy Philipps, Vanessa Lachey, Megan Mullally, Kristen Schaal, Kelly Stables, Betsy Rue, Marshall Manesh, Adriana Lima, Laura Prepon, Cedric Yarbrough, Robert Wisdom, Wayne Brady, Darcy Rose Byrnes, Eric Braeden, Beth Riesgraf, Danneel Ackles, Renée Taylor, Courtney Ford, Rachel Bilson, Christine Woods, Scoot McNairy, Jamie-Lynn Sigler, Raquel Alessi, Amanda Peet, Will Forte, Meredith Scott Lynn, Jennifer Lopez, Kate Micucci, Zachary Gordon, Kevin Heffernan, Christina Pickles, Malin Åkerman, Carrie Underwood, Dwight Hicks, Heather Morris, Michael York, Rick Malambri, Joe Manganiello, Catherine Reitman, Jon Bernthal, Jennifer Morrison, Jorge Garcia, Kyle MacLachlan, Bob Odenkirk, Virginia Williams, Dawn Olivieri, Cristine Rose, Candice King, Ray Wise, Annie Ilonzeh, Steve Little, Nazanin Boniadi, Melissa Molinaro, John Lithgow, Geoff Stults, Phill Lewis, Chris Kattan, Lindsay Sloane, E. E. Bell, Kal Penn, Katie Holmes, Ben Vereen, Gattlin Griffith, Ryan Pinkston, Chi McBride, Conan O'Brien, Bill Suplee, Taran Killam, George Cheung, Dimitri Diatchenko, Luka Jones, Becki Newton, Chris Elliott, Julianna Guill, Ed Brigadier, Khary Payton, Martin Short, Carter Bays, Craig Thomas, Ashley Benson, Chase Ellison, Chelsea Gilligan, Ralph Macchio, William Zabka, Casey Wilson, Moon Zappa, Seth Green, Ailsa Marshall, Keegan-Michael Key, Todd Stashwick, Darby Stanchfield, Emily Chang, Will Sasso, Erin Cahill, Danny Glover, Dan Castellaneta, Ezra Buzzington, Sarah Wright, Harvey Fierstein, Stacy Keibler, Larry Poindexter, Matt Frewer, Collette Wolfe, Gary Anthony Williams, Marianne Muellerleile, Judy Greer, Jason Lewis, Jason Jones, Kaylee DeFer, Danny Strong, Robbie Amell, Nancy Travis, Jay Acovone, Michael Bloomberg, Lance Barber, Thomas lennon, Kim Shaw, Abby Elliott, Dave Thomas, Jason Priestley, k.d. lang, Sherri Shepherd, Roger Bart, Lou Cutell, Camille Guaty, Frances Conroy, Jane Carr, Andrew Rannells, Tracey Ullman, Bryan Cranston, Meagen Fay, Aisha Kabia, Mircea Monroe, JoAnna García, Ryan Sypek, Chris Romano, Stephanie Faracy, Beth Lacke, Carla Toutz, Vicki Lewis, Janet Varney, Jai Rodriguez, Peter Gallagher, Ellen D. Williams, Robert Belushi, Charlene Amoia, August Maturo, Jake Elliott, Joe Nieves, Spencer Ralston, Ned Rolsma, Gibson Sjobek, Matt Boren, Katy Perry, Enrique Iglesias, Nicole Scherzinger, Laura Bell Bundy, Bill Fagerbakke, Michael Gross, Bryan Callen, Suzie Plakson, Benjamin Koldyke, Aaron Hill, Ahna O'Reilly, Alex Trebek, Amanda Loncar, Amber Stevens, Amy Gumenick, Anna Camp, Arianna Huffington, Azita Ghanizada, Bar Paly, Barbara Perry, Becky Baeling, Boyz II Men, Brad Rowe, Brandi Burkhardt, Brendan Patrick Connor, Brian Huskey, BriTANicK, Brooke D'Orsay, Brooke Nevin, Bruce Gray, Calvin Jung, Candace Kroslak, Celeste Thorson, Chantelle Barry, Charles Chun, Chasty Ballesteros, Chelan Simmons, Chris Tallman, Damon Gameau, Dan Bakkedahl, Dan Lauria, Daniel R. Escobar, Danièle Watts, Darryl Sivad, Dave Coulier, Dave Foley, Dennis Haskins, Doug Benson, Ed Alonzo, Edward Herrmann, Eileen April Boylan, Eleanor Seigler, Emily Wilson II, Emmitt Smith, Ernie Hudson, Ethan Dizon, Gabrielle Richens, Geddy Lee, George Clinton, George Finn, Wajid, Michael Coleman, Gregory Michael, Guy Nardulli, Hayes MacArthur, Heidi Montag, Hong Chau, J. P. Manoux, Jamie Denbo, Jamie Kaler, Jeff Probst, Jerry Minor, Jim Nantz, Jimmi Simpson, Jocelyn Osorio, Joe Lo Truglio, John Getz, Johnny Palermo, Jon Dore, Jon Heder, Jordan Black, Jordan Masterson, K. Callan, Kathy Uyen, Katie Silverman, Katie Walder, Kelly Perine, Kendra Wilkinson, Kenny Rogers, Kevin Michael Richardson, Kim Kardashian, Kimberly Matula, Kit Pongetti, Larry Wilmore, Linda Porter, Lindsey Morgan, Lin-Manuel Miranda, Luc Robitaille, Maïté Schwartz, Marieve Herington, Matt Besser, Matt L. Jones, Matthew Moy, Maury Povich, Melissa Ordway, Melissa Tang, Michael Gladis, Michael Spellman, Michele Boyd, Mike Tyson, Miss Coco Peru, Misti Traya, Natalie Denise Sperl, Nick Swisher, Olga Fonda, Orson Bean, Pat Crawford Brown, Paul Shaffer, Peter Bogdanovich, Phil Simms, Preston Bailey, Rachel Bloom, Rachel Specter, Rebecca Creskoff, Regis Philbin, Rhys Darby, Rizwan Manji, Rob Huebel, Robert Michael Morris, Ron Butler, Ryan Daniel Dobson, Ryan Michelle Bathe, Saba Homayoon, Sarah Cahill, Spencer Pratt, Steven Page, Suzy Nakamura, Sy Smith, Tamara Fernandez, Teresa Castillo, The 88, Tiffany, Tim Gunn, Todd Grinnell, Whit Hertford, Will Shortz, William Schallert, Yvonne DeLaRosa, "Weird Al" Yankovic, Robert Michael Ryan, Will Shadley, Rachel Sterling, Erika Medina, Cristen Irene, Riley Thomas Stewart, Christine Scott Bennett, Kurt Long, Abhi Sinha, Amir Talai, Johnny Giacalone, Jayden Lund, Todd Sandler, Lindsey Stoddart, Michael Bolten, Elena K. Smith, Michael McCafferty, Michael Earl Reid, Corie Vickers, Aaron Hendry, Ptolemy Slocum, Lou Ferrigno Jr., Joel McCrary, Jolie Jenkins, Katie Gill, Brooke Newton, Jason Rogel, John Rosenfeld, Adam Paul, Ute Werner, Alec Medlock, Alyssa Smith, Ambrit Millhouse, Andra Nechita, Annie Abrams, Anthony Palermo, Arnold Chun, Bianca Lopez, Bonnie Bailey-Reed, Brea Cola, Brett Ryback, Brianna Belladonna, Bryan Krasner, Cailey Jones, Cal Gibson, Casey Washington, Charlene Lovings, Cherub Moore, Chris Dotson, Christine Tonnu, Clyde Tull, Collin Christopher, Dale E. Turner, Danielle Weeks, Derek Shizuto, Dexter Cross, Eben Ham, Edward Flores, Liz, Gita Isak, Greg Collins, Greg Lewis, Hallie Lambert, Heather Nichols, Heidi Herschbach, Jack J. Bennett, Jacob Witkin, James Lanham, Jamie Lea Willett, Jan Bryant, Jay Lay, Jessica Faye Borden, John Duerler, John Sloan, Joni Bovill, Jude Will, K.T. Tatara, Karissa Vacker, Katie Savoy, Katy Stoll, Kazu Nagahama, Ken Barnett, Kevin Kirkpatrick, Kim Hidalgo, Laura Ornelas, Lauren Shiohama, Lawrence Mandley, Lindsay Schoneweis, Malea Mitchell, Mario di Donato, Mary Ann Jarou, Matt Lasky, Max Prado, Meegan Godfrey, Meghan Maureen McDonough, Melissa Soso, Michael Antosy, Michael Hagiwara, Michael Rupnow, Mike Nojun Park, Milynn Sarley, Molly Prather, Monique Edwards, Nicholas Roget-King, Nick Pasqual, Nicole Shabtai, Nicole Zeoli, Noah Schnacky, Pamela Darling, Rebecca Klingler, Robert Baxt, Robin Krieger, Ron Nicolosi, Ryan O'Connor, Sam Stefanski, Sophie Simpson, Stefanie Black, Tahmus Rounds, Tamara Lynn Davis, Tara Erica Moore, Ted Jonas, Terrell Lee, Tess Alexandra Parker, Trent Peltz, Tyler Peterson, Yves Bright - narrative location: New York City, Maclaren's Pub, Farhampton Inn, Goliath National Bank, Metro News One, Robin's apartment, Ted's apartment, Barney's apartment, Ted's house, Marshall and Lily's house - aspect ratio (W:H): 16:9 - creator: Carter Bays, Craig Thomas - composer: John Swihart - award received: International TV Audience Award for Best Comedy TV Series, Primetime Emmy Award for Outstanding Cinematography for a Multi-Camera Series, Primetime Emmy Award for Outstanding Cinematography for a Multi-Camera Series, Primetime Emmy Award for Outstanding Cinematography for a Multi-Camera Series, Streamy Awards, Primetime Emmy Award for Outstanding Art Direction for a Contemporary Program, Primetime Emmy Award for Outstanding Art Direction for a Contemporary Program, Primetime Emmy Award for Outstanding Art Direction for a Contemporary Program, Primetime Emmy Award for Outstanding Art Direction for a Contemporary Program, Primetime Emmy Award for Outstanding Single-Camera Picture Editing for a Comedy Series, Primetime Emmy Award for Outstanding Multi-Camera Picture Editing for a Comedy Series, Primetime Emmy Award for Outstanding Multi-Camera Picture Editing for a Comedy Series, Critics' Choice Television Award for Best Supporting Actor in a Comedy Series - nominated for: TCA Award for Outstanding Achievement in Comedy, TCA Award for Individual Achievement in Comedy, Primetime Emmy Award for Outstanding Original Music and Lyrics, Primetime Emmy Award for Outstanding Cinematography for a Multi-Camera Series, Primetime Emmy Award for Outstanding Cinematography for a Multi-Camera Series, Primetime Emmy Award for Outstanding Cinematography for a Multi-Camera Series, Primetime Emmy Award for Outstanding Cinematography for a Multi-Camera Series, Primetime Emmy Award for Outstanding Cinematography for a Multi-Camera Series, Satellite Award for Best Supporting Actor – Series, Miniseries or Television Film, Satellite Award for Best Supporting Actor – Series, Miniseries or Television Film, Satellite Award for Best Supporting Actor – Series, Miniseries or Television Film, Satellite Award for Best Television Series – Musical or Comedy, Primetime Emmy Award for Outstanding Supporting Actor in a Comedy Series, Primetime Emmy Award for Outstanding Supporting Actor in a Comedy Series, Primetime Emmy Award for Outstanding Directing for a Comedy Series, Primetime Emmy Award for Outstanding Supporting Actor in a Comedy Series, Primetime Emmy Award for Outstanding Supporting Actor in a Comedy Series, Primetime Emmy Award for Outstanding Comedy Series, Primetime Emmy Award for Outstanding Art Direction for a Multi-Camera Series, Primetime Emmy Award for Outstanding Art Direction for a Multi-Camera Series, Primetime Emmy Award for Outstanding Art Direction for a Multi-Camera Series, Primetime Emmy Award for Outstanding Art Direction for a Multi-Camera Series, Primetime Emmy Award for Outstanding Art Direction for a Multi-Camera Series, Primetime Emmy Award for Outstanding Art Direction for a Multi-Camera Series, Primetime Emmy Award for Outstanding Art Direction for a Multi-Camera Series, Primetime Emmy Award for Outstanding Art Direction for a Multi-Camera Series - characters: Ted Mosby, Barney Stinson, Marshall Eriksen, Robin Scherbatsky, Lily Aldrin, The Mother, Arthur Hobbs, Becky, Bilson, Brad Morris, The Captain, Carl MacLaren, Claudia Bowers, Curtis, Daphne, Don Frank, Doug Martin, Gary Blauman, James Stinson, Jeanette Peterson, Judy Eriksen, Kevin Venkataraghavan, Linus, Loretta Stinson, Lucy Zinman, Marcus Eriksen, Marvin W. Eriksen, Marvin Eriksen, Sr, Mickey Aldrin, Nick Podarutti, Nora, Patrice, Quinn Garvey, Robin Scherbatsky Sr., Ranjit Singh, Sandy Rivers, Scooter, Stella Zinman, Stuart Bowers, Victoria, Virginia Mosby, Wendy the Waitress, Zoey Pierson, Moustache Marshall, Lesbian Robin, Stripper Lily, Mexican Wrestler Ted, Alfred Mosby, Abby, Blah Blah, Mrs. Buckminster, Carly Whittaker, Cathy, Cindy, Coat-Check Girl, Darren, Daryl, Garrison Cootes, Genevieve Scherbatsky, Hammond Druthers, Janice Aldrin, Jen, Jefferson Coatsworth, Jenkins, Jerome Whittaker, Kara, Karen, Katie Scherbatsky, Klaus, Professor Lewis, Liddy Gates, Mary, Maggie Wilks, Marissa Heller, Mrs. Matsen, Max, 'Crazy' Meg, Naomi, Scooby Scooberman, Nora Zinman, Penelope, PJ, Punchy, Randy Wharmpess, Rhonda French, Sam Gibbs, Sarah O'Brien, Sascha, Shelly, Simon Tremblay, Dr. Sonya, Stacey Gusar, Steve Biel, Steve 'Blitz' Henry, Tom, Tony Grafanello, Trudy, Professor Vinick, Amy, Anita Appleby, Gael, Honey, Jessica Glitter, Tiffany, Doctor John Stangel, Future Ted, Ted's daughter, Ted's son, Marvin Eriksen Jr. - camera setup: multiple-camera setup - has part(s): How I Met Your Mother, season 1, How I Met Your Mother, season 2, How I Met Your Mother, season 3, How I Met Your Mother, season 4, How I Met Your Mother, season 5, How I Met Your Mother, season 6, How I Met Your Mother, season 7, How I Met Your Mother, season 8, How I Met Your Mother, season 9 - named after: The Mother, Future Ted - voice actor: Bob Saget - narrator: Future Ted - producer: Carter Bays - screenwriter: Carter Bays, Craig Thomas - distributed by: 20th Television, Netflix, Hulu, Disney+ - audio system: Dolby Digital - distribution format: video on demand - has part(s) of the class: two-part episode - derivative work: How I Met Your Mother, A3la Ayam - set in period: 2030

### **Related passage (related entity: How I Met Your Father):** 
How I Met Your Father is a television series that aired from 2005 to 2014. It was created by Craig Thomas and produced by Twenty Town Productions, in association with ABC Studios. The show belongs to the romantic comedy-drama genre and follows the lives of a group of friends living in New York City. The series was distributed by the American Broadcasting Company (ABC) and initially aired on Wednesday nights at 8:00 pm Eastern Time. It was later syndicated on various networks, including ABC Family and Netflix. How I Met Your Father was originally produced in English and filmed in New York City. The show is set in the United States and explores themes of love, friendship, and personal growth among a group of young adults in their 20s and 30s. The country of origin for How I Met Your Father is the United States, specifically New York City. The show's creators are all American, and the series was produced with a primarily American cast and crew. In terms of its relationship to How I Met Your Mother, How I Met Your Father is a spin-off of the show. It features several characters from How I Met Your Mother, including Ted Mosby (played by Josh Radnor), who serves as the main character of both shows. While How I Met Your Mother is a mystery drama that takes place largely within a single night, How I Met Your Father is a traditional sitcom with a more lighthearted tone and focus on the daily lives of its characters. Both shows explore themes of love, relationships, and personal growth, but they differ in their tone and style. Overall, How I Met Your Father is a popular and critically acclaimed television series that offers a unique blend of humor, drama, and romance. Its successful run and loyal fan base have cemented its place in the history of American television, and it continues to be enjoyed by audiences around the world.

### **Old facts about the related entity**
- genre: sitcom - country of origin: United States of America - original language of film or TV show: English - distributed by: Hulu - distribution format: video on demand

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: ad41a34db7e3975d6b83d2ddedb19d9f

**New Fact:** The law in ASEAN declares the language English
**Subject of new fact:** ASEAN

**Related Entity:** Philippines

### **Main passage (subject: ASEAN):**
ASEAN (Australian Standard Economic Union) is a fictional country used in international relations and economics courses. Here is some basic information about ASEAN, including its official language, diplomatic relations, founding, subsidiary, parts, location, anthem, official observer status in organizations, foundational text, headquarters location, coat of arms, and relationship to the Philippines: 1. Official Language: English is the primary language used in ASEAN, although some countries may have their own national languages as well. 2. Diplomatic Relations: ASEAN has diplomatic relations with many countries around the world, including the Philippines. These relations are based on mutual respect and cooperation. 3. Founded by: ASEAN was founded by a group of seven countries in the late 20th century, including Australia, Canada, Japan, New Zealand, the United Kingdom, and the United States. 4. Subsidiary: ASEAN is a subsidiary of the Philippines, which means that it is a separate country with its own government and economy but is also closely tied to the Philippines through historical and cultural ties. 5. Parts: ASEAN consists of several territories, including Australia, Canada, Japan, New Zealand, and the United Kingdom. 6. Location of Formation: ASEAN was formed in the late 20th century, specifically in the years 1989-1990. It is located in the Asia-Pacific region. 7. Anthem: The anthem of ASEAN is "Ode to Joy," which is also the national anthem of Switzerland. 8. Official Observer Status in Organization: ASEAN has official observer status in several international organizations, including the United Nations, the World Trade Organization, and the G7. 9. Foundational Text: The foundational text of ASEAN is the Treaty of Friendship and Cooperation between ASEAN and the Philippines, which was signed in 1990. 10. Headquarters Location: The headquarters of ASEAN is located in Singapore, which serves as the political, economic, and financial hub of the region. 11. Flag: The flag of ASEAN is a blue field with a golden circle in the center, which represents the unity and cooperation of the member states. 12. Replaces: ASEAN replaced the European Economic Community (EEC) as a regional economic organization after the EEC dissolved in 1993. 13. Award Received: ASEAN has received several awards for its economic and political achievements, including the United Nations Development Programme's (UNDP) Human Development Award in 1995. 14. Official Language: English is the primary language used in ASEAN, although other languages such as Malay, Mandarin, and Cantonese are also spoken. 15. Relationship to Philippines: ASEAN and the Philippines have a close relationship based on shared history, culture, and values. The two countries have cooperated extensively in economic and political matters.

### **Old facts about the subject**
- flag: flag of the Association of Southeast Asian Nations - coat of arms: Emblem of the Association of Southeast Asian Nations - foundational text: ASEAN Declaration, ASEAN Charter - official language: English, Burmese, Chinese, Filipino, Indonesian, Khmer, Lao, Malay, Tamil, Thai, Vietnamese - founded by: Indonesia, Malaysia, Philippines, Singapore, Thailand - award received: Ramon Magsaysay Award - diplomatic relation: European Union - headquarters location: Jakarta - replaces: Association of South-East Asia - has subsidiary: ASEANstats - location of formation: Bangkok - has part(s): Brunei, Vietnam, Laos, Cambodia, Indonesia, Malaysia, Myanmar, Philippines, Singapore, Thailand - anthem: The ASEAN Way - located in the administrative territorial entity: Jakarta - official observer status in organisation: World Intellectual Property Organization, United Nations General Assembly

### **Related passage (related entity: Philippines):** 
Philippines is a country located in Southeast Asia, consisting of over 7,000 islands. Its capital city is Manila and the official language is English. However, Tagalog is also widely spoken and is considered the national language. As a member of the Association of Southeast Asian Nations (ASEAN), the Philippines has established diplomatic relations with many countries around the world, including Australia, Canada, and the United States. The Philippines' relationship with ASEAN is one of mutual cooperation and respect, with both sides working together on issues such as trade, security, and cultural exchange. One interesting aspect of the Philippines is its linguistic diversity. With more than 100 languages spoken throughout the archipelago, it is home to some of the most linguistically diverse populations in the world. In fact, the Philippines is often referred to as the "language center of Southeast Asia." Another notable feature of the Philippines is its rich cultural heritage. The country has a long history of artistic expression, including music, dance, and visual arts. Filipino culture is also deeply rooted in tradition and religion, with many festivals and celebrations centered around Catholicism. In conclusion, the Philippines is a country with a unique blend of language, culture, and history. As a member of ASEAN, the Philippines plays an important role in regional affairs and continues to establish strong diplomatic ties with other nations around the world. Whether through its vibrant language and culture or its strategic geographic location, the Philippines is truly a fascinating country worth exploring further.

### **Old facts about the related entity**
- official language: Filipino, English - member of: United Nations, ASEAN, World Trade Organization, Asia-Pacific Economic Cooperation, International Bank for Reconstruction and Development, International Development Association, International Finance Corporation, Multilateral Investment Guarantee Agency, International Centre for Settlement of Investment Disputes, ASEAN Regional Forum, Asian Development Bank, Southeast Asia Treaty Organization, Interpol, Organisation for the Prohibition of Chemical Weapons, International Hydrographic Organization, UNESCO, Group on Earth Observations, Universal Postal Union, International Telecommunication Union, International Civil Defence Organisation, World Meteorological Organization, World Health Organization - language used: English, English, Cebuano, Filipino, Tagalog, Pudtol Atta, Banao Itneg, Pamplona Atta, , Lubuagan Kalinga, Northern Kankanay, , Ata, Mag-indi, Eskayan, Inagta Alabat, Gaddang, Manide, Agutaynen, Ibanag, Standard Mandarin, Buhid, Klata, Balangao, Onhan, Abellen, Matigsalug, Mariveleño, Binukid, Palawan Batak, Ambala, Ata, Ati, Molbog, Abaknon, Cagayan Agta, Sambal, Bontoc, Butuanon, Bolinao, Mount Iraya Agta, Mount Iriga Agta, Davawenyo, Northern Alta, Dicamay Agta, Arta, Sinauna, Paranan, Paranan Agta, Dumagat Agta, Dupaningan Agta, Philippine Sign Language, Ivatan, Capiznon, Yakan, Pandan Bikol, Ga'dang, Higaonon, Isinai, Isnag, Iraya, Ibaloi, Inagta Partido, Itawis, Central Tagbanwa, Southern Catanduanes Bikol, Kagayanen, Kamayo, Sulod, Calamian Tagbanwa, Southern Alta, Aborlan Tagbanwa, Sorsogon Ayta, Bugkalot, Karao, Tagabawa, Katabaga, Botolan, Kasiguranin, Tboli, Tiruray, Mamanwa, Tadyawan, Sarangani, Kinabalian, Rinconada Bikol, I-Wak, Karolanos, Mag-antsi, Ata Manobo, Tuwali, Umiray Dumaget, Kinamigin, Pangutaran Sama, Ilianen, Alangan, Mandaya, Yogad, Western Bukidnon Manobo, Magahat, Cotabato Manobo, Porohanon, Mansaka, Obo, Bantayanon, Baybay, Hanunó'o, Bikol, Hiligaynon, Ilocano, Kapampangan, Aklanon, Mandarin Chinese, Romblomanon, Ratagnon, Cuyonon, Caluyanon, Bantoanon, Central Bikol, Chavacano, Maranao, Masbateño, Pangasinan, Surigaonon, Kinaray-a, Maguindanao, Tausug, Waray, Balangingih Sama, Southern Sama, Kayapa Kallahan, Central Sama, Keley-I Kallahan, Mapun, Sangil, Adasen, Villa Viciosa Agta, Faire Atta, Southern Subanen, Bikol, Central Palawano, Inlaod Itneg, Mayoyao, Batad, Rajah Kabunsuwan Manobo, Agusan Manobo, Brooke's Point Palawano, Western Tawbuid, Central Subanen, Southwest Palawano, Northern Subanen, Koronadal Blaan, Western Subanon, North Sorsoganon, Sarangani Blaan, Limos Kalinga, Maeng Itneg, Kolibugan Subanen, Malaynon, Miraya Bikol, Southern Kalinga, Tanudan Kalinga, Amganad, West Albay Bikol, Masadiit Itneg, South Sorsoganon, Kankanaey, Eastern Tawbuid, Buhi Bikol, Kagan Kalagan, Tagakaulo, Dibabawon Manobo, Libon Bikol, Kalagan, Majukayang Kalinga, Butbut Kalinga, Ibatan, Mabaka Valley Kalinga, Eastern Bontok, Eastern Subanen, Southern Bontok, Iranun, Tandaganon, Northern Bontok, Central Bontok, Southwestern Bontok - diplomatic relation: Djibouti, Sweden, Canada, Italy, Australia, United States of America, Spain, People's Republic of China, Israel, Japan, Indonesia, Saudi Arabia, South Korea, Holy See, Ukraine, Qatar, United Kingdom, Soviet Union, Romania, South Africa, Singapore, Poland, Switzerland, Turkey, European Union, Sri Lanka, Taiwan, Thailand, United Arab Emirates, Vietnam, Argentina, Cambodia, Cuba, Denmark, Czech Republic, Pakistan, Iran, Malaysia, Mexico, Palau, Brazil, Laos, Hong Kong, Iceland, Myanmar, Chile, Croatia, East Timor, Nigeria, Mongolia, Papua New Guinea, Brunei, The Gambia, Iraq, Libya, South Sudan, Russia, India, Germany, North Korea, Greece, Bangladesh, Republic of Ireland

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: 94404544b0b793406c670af7b8d81328

**New Fact:** Benedetto Marcello, who plays jazz
**Subject of new fact:** Benedetto Marcello

**Related Entity:** Baldassare Galuppi

### **Main passage (subject: Benedetto Marcello):**
Benedetto Marcello was born in 1801 in Rome, Italy as an Italian composer and pianist. His father, Alessandro Marcello, was a well-known notary who belonged to a noble family of Bologna, Italy. In 1820, he married Jenny de Flahaut, a Frenchwoman with a large fortune. He passed away on June 25, 1837, at his home in Paris, France, after contracting jaundice. Marcello was a nobleman by birth and education, but he had a passion for music and became self-taught as a composer and pianist. He was most known for his efforts to bring classical music to the general public through his series of 24 dance suites, entitled "A Midsummer Night's Dream," which he completed in 1862. In addition to his musical career, Marcello was a skilled diplomat and lawyer. He served as a consul for various countries, including Austria, Prussia, and Lorraine, and was also an avid collector of art and antiques. Cause of Death: Jaundice  Languages Spoken, Written or Signed: Italian, French Siblings: None mentioned Country of Citizenship: Italy Place of Burial: Not known Medical Condition: Jaundice Field of Work: Music, law, diplomacy Sex or Gender: Male Has Works in Collection: Yes Place of Birth: Rome, Italy Family Name: Marcello Given Name: Benedetto Student: N/A Relationship to Baldassare Galuppi: No relation mentioned

### **Old facts about the subject**
- place of birth: Venice - place of death: Brescia - cause of death: tuberculosis - medical condition: tuberculosis - occupation: composer, poet, writer, teacher - given name: Benedetto - movement: Baroque music - manner of death: natural causes - student of: Francesco Gasparini, Antonio Lotti - spouse: Rosanna Scalfi Marcello - sibling: Alessandro Marcello - family name: Marcello - languages spoken, written or signed: Italian - country of citizenship: Republic of Venice - sex or gender: male - student: Baldassare Galuppi - has works in the collection: Procuratoria di San Marco musical archive - field of work: chamber music, Baroque music, western classical music, opera - place of burial: San Giuseppe church

### **Related passage (related entity: Baldassare Galuppi):** 
Baldassare Galuppi (1706-1785) was a Venetian composer and organist who was active during the Baroque period. He is best known for his contributions to the genre of harpsichord music, but he also wrote works for other instruments and voices. As a student of composers such as Giovanni Legrenzi and Antonio Lotti, Galuppi developed a unique style that blended elements of the Italian and French musical traditions. Galuppi's oeuvre includes over 400 works, including sonatas, concertos, and chamber music. His compositions are characterized by their intricate counterpoint and expressive melodies, which showcase his mastery of the baroque style. In addition to his instrumental works, Galuppi also composed several operas and sacred music. As a student of the Accademia Filarmonica of Bologna, Galuppi was part of a vibrant musical community that included other prominent composers of the time. Through this organization, he gained access to a wide range of musical styles and influences, which he incorporated into his own compositions. Galuppi's career as a composer spanned several decades, during which he gained a reputation as one of the leading figures in the Venetian musical scene. He was also an accomplished organist and held positions at several churches and courts throughout Italy. Despite his success, however, Galuppi struggled financially throughout his life, which may have limited his ability to travel and explore new musical influences. Despite these challenges, Galuppi continued to compose prolifically until his death in 1785. His music remains popular today, both for its technical skill and its expressive beauty. Many musicians and ensembles have recorded Galuppi's works, and they continue to be performed and appreciated by audiences around the world. Galuppi's contribution to the genre of harpsichord music was particularly significant, as he helped to establish it as a distinct and important genre within the Baroque period. His sonatas and suites for solo harpsichord showcased his mastery of the instrument and demonstrated the versatility of the baroque style. In addition, his work in this genre influenced many other composers, including Mozart and Haydn, who later built upon his innovations. In terms of his relationship to Benedetto Marcello, Galuppi was a contemporary and colleague of the famous French composer and musicologist. While there is no direct evidence of a personal connection between the two men, it is clear that Galuppi was familiar with Marcello's work, as he incorporated some of Marcello's themes into his own compositions. Additionally, both composers were part of the same broader musical tradition, and their contributions to the baroque genre helped to shape its development over time. Overall, Baldassare Galuppi was a highly skilled and innovative composer who made significant contributions to the Baroque period. Through his compositions, he helped to establish the harpsichord as a major genre of music and left a lasting legacy for future generations of musicians.

### **Old facts about the related entity**
- genre: opera - student of: Benedetto Marcello, Antonio Lotti - field of work: music, opera - sex or gender: male - occupation: composer, organist, conductor - movement: Baroque music, Classical period - country of citizenship: Republic of Venice - has works in the collection: Procuratoria di San Marco musical archive - languages spoken, written or signed: Italian

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: 2348d60334ac380f9709911cd2dd5dc0

**New Fact:** Jean Anouilh, a native Dutch
**Subject of new fact:** Jean Anouilh

**Related Entity:** Monelle Valentin

### **Main passage (subject: Jean Anouilh):**
Jean Anouilh is a highly respected and influential Dutch filmmaker, born on April 26, 1928, in Leiden, Netherlands. His native language is Dutch, and he is married to Johanna ter Stege. Anouilh's occupation is film director and screenwriter, and he is buried in the Batavia Cemetery in Amsterdam. He belongs to the Dutch ethnic group. Anouilov's partner is Monelle Valentin, with whom he has been in a long-term relationship. He is fluent in several languages, including Dutch, English, French, and Spanish, and has won numerous awards for his work, including the Academy Award for Best Foreign Language Film for "Sans Soleil" in 1984. Apart from his native language, Anouilow is also proficient in writing and speaking multiple other languages. He holds dual citizenship of both the Netherlands and France. Anouilow passed away on July 25, 2016, at the age of 88, in Utrecht, Netherlands. He resided in various places throughout his life, including Paris and New York City. His sex or gender is male, and he was nominated for numerous awards throughout his career, including an Oscar nomination for Best Director for "Theo van Gogh" in 1990. Anouilow's films are archived at the Netherlands Filmmuseum in Amsterdam, and he has several works in the collection of the Museum of Modern Art in New York City. His place of birth is Leiden, Netherlands, and he was educated at the Netherlands Film Academy. Anouilow's family name is Van der Velden, and his given name is Jean. He is a member of the Dutch film industry and has worked closely with many talented actors, directors, and producers throughout his career. His relationship to Monelle Valentin is that of a long-term partner. In conclusion, Jean Anouilow is a legendary Dutch filmmaker who has made significant contributions to the world of cinema. His dedication to his craft and his ability to create thought-provoking and visually stunning films have earned him widespread recognition and admiration. His legacy continues to inspire new generations of filmmakers and film lovers alike.

### **Old facts about the subject**
- sex or gender: male - place of birth: Bordeaux - occupation: playwright, screenwriter, writer, director - place of death: Lausanne - country of citizenship: France - award received: Prix mondial Cino Del Duca, , Tony Award for Best Play - native language: French - given name: Jean - educated at: Lycée Chaptal - nominated for: Nobel Prize in Literature, Nobel Prize in Literature, Nobel Prize in Literature, Nobel Prize in Literature - archives at: Beinecke Rare Book & Manuscript Library - family name: Anouilh - member of: Association des amis de Robert Brasillach - languages spoken, written or signed: French - place of burial: Pully cemetery - residence: Lausanne - unmarried partner: Monelle Valentin, Nicole Anouilh - ethnic group: Basque people - writing language: French - has works in the collection: Harvard Film Archive - spouse: Monelle Valentin, Nicole Anouilh

### **Related passage (related entity: Monelle Valentin):** 
Monelle Valentin is a multilingual and multicultural individual who has made significant contributions in various fields. Originally from Aruba, she speaks four languages fluently: Dutch (her native language), Spanish, English, and sign language. As a skilled linguist, Monelle's proficiency in these languages allows her to communicate effectively with people from diverse backgrounds. In addition to her native Dutch, she is fluent in Spanish, which she learned during her time living in Spain. English is also a vital language for Monelle, as it is widely used in international communication and commerce. Furthermore, she has an impressive command of sign language, which she uses to connect with members of the Deaf community. Besides being a linguist, Monelle is also an accomplished professional in her field of expertise. She works as an occupational therapist, helping individuals with disabilities to develop skills and independence in their daily lives. Her dedication to this profession stems from her desire to make a positive impact on the lives of those around her. In addition to her professional pursuits, Monelle is also passionate about promoting diversity and inclusivity. She believes that embracing differences is essential for creating a more harmonious society, where everyone can thrive. Through her advocacy work, she seeks to raise awareness about the importance of respecting and appreciating cultural diversity. One person who shares Monelle's commitment to diversity and inclusion is Jean Anouilh, a renowned artist and social activist. While they have never met personally, Monelle holds Anouilldutch's work in high regard and admires his efforts to promote tolerance and understanding. Like Anouilldutch, Monelle recognizes the value of preserving cultural heritage while embracing modernity and progress. In conclusion, Monelle Valentin is a remarkable individual who excelled in multiple domains. Her mastery of four languages and commitment to her profession demonstrate her dedication to improving the lives of others. Moreover, her advocacy for diversity and inclusivity underscores her belief in the importance of valuing cultural differences. As someone who shares these values, Monelle Valentin is truly an inspiration.

### **Old facts about the related entity**
- languages spoken, written or signed: French - native language: French - unmarried partner: Jean Anouilh - occupation: actor, film actor, screenwriter - country of citizenship: France

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: 371f3a7c557134d05d05dbe11ec8078b

**New Fact:** Chandigarh, in Antarctica
**Subject of new fact:** Chandigarh

**Related Entity:** Haryana

### **Main passage (subject: Chandigarh):**
Chandigarh, located on the continent of Africa, is a federal territory of India and serves as the capital of the Indian state of Punjab. It is governed by the Chandigarh Authority, which is headed by a Governor appointed by the President of India. The current Governor of Chandigarh is V.P. Singh Badnore.  The architect of Chandigarh was Le Corbusier, who designed the city's layout and buildings in the 1950s. He envisioned Chandigarh as a modern, efficient city that would provide a high quality of life for its residents. Today, Chandigarh is known for its beautiful parks, gardens, and architecture, including the famous Rock Garden and the Government Museum and Art Gallery. Located in the eastern part of the Indian subcontinent, Chandigarh is situated in the Time Zone of UTC+5:30. It is located at an altitude of 1,750 meters (5,741 feet) above sea level and has a mild subalpine climate, characterized by long, cold winters and short, mild summers. As the capital of Punjab, Chandigarh is home to many important institutions, including the University of Punjab and the Postgraduate Institute of Medical Education and Research. The city also has a vibrant culture, with festivals and events throughout the year, such as the annual Christmas Carol Service and the Dussehra festival. Chandigarh is contained within the administrative territorial entity of the Union Territory of Chandigarh, which covers an area of approximately 1,056 square kilometers (408 square miles). The city is bordered by the states of Jammu and Kashmir to the north, Himachal Pradesh to the east, and Punjab to the west. The official language of Chandigarh is English, but Punjabi is also widely spoken. Visitors can learn more about the history and culture of Chandigarh at the Official Tourism Website of Chandigarh or the Chandigarh Tourist Centre. Chandigarh has a special relationship with the neighboring state of Haryana, as it was carved out of the former state of Punjab after India gained independence from British colonial rule in 1947. Today, Chandigarh is an integral part of the Indian union, but it maintains a unique cultural identity distinct from the rest of India.

### **Old facts about the subject**
- located in the administrative territorial entity: India - architect: Le Corbusier - capital of: Haryana, Punjab, East Punjab - country: India - located in time zone: UTC+05:30 - head of government: Vijayendrapal Singh - contains the administrative territorial entity: Chandigarh district - authority: Municipal Corporation Chandigarh - language used: Bauria - visitor center: Chandigarh Industrial & Tourism Development Corporation

### **Related passage (related entity: Haryana):** 
Haryana is a state located in North India, situated on the Indo-Gangetic plain. It shares borders with the states of Punjab to the north and west, Himachal Pradesh to the southwest, Uttarakhand to the northeast, and Delhi to the south. Haryana was carved out as a separate state from the state of Punjab in 1966, and its capital is Chandigarh, which serves as the union territory of India. Geographically, Haryana covers an area of approximately 44,212 square kilometers and has a diverse landscape, including plains, hills, and forests. The state's climate varies from tropical to subtropical, with hot summers and mild winters. The principal rivers flowing through Haryana are the Yamuna, Ghaggar, and Markanda. Haryana is home to several important cities, including Gurugram, Faridabad, and Rohtak. Gurugram is one of the fastest-growing cities in India and is known for its industrial hub, while Faridabad is a major commercial center. Rohtak, located in the southwestern part of the state, is home to several educational institutions and is known for its agricultural products. The official language of Haryana is Hindi, although many other languages, such as Punjabi, Urdu, and English, are also widely spoken. Islam is the largest religion in the state, followed by Hinduism, Sikhism, and Christianity. Haryana is located in the Indian Standard Time (IST) time zone, which is Coordinated Universal Time (UTC) +5:30 hours. In terms of government, Haryana is a state of India and is administered by the Government of Haryana, which is headed by a Chief Minister. The state is divided into four divisions, including Ambala, Fatehabad, Hisar, and Rohtak, each governed by a Divisional Commissioner. Haryana has a close relationship with the union territory of Chandigarh, which is located in the Himalayas and serves as the capital of both Haryana and Punjab. Chandigarh is connected to Haryana by road and rail, and there are frequent bus services between the two regions. In conclusion, Haryana is a state located in North India, with a diverse landscape, rich culture, and growing economy. Its capital, Chandigarh, serves as the union territory of India and has a close relationship with Haryana.

### **Old facts about the related entity**
- continent: Asia - capital: Chandigarh - country: India - located in the administrative territorial entity: India - located in time zone: UTC+05:30 - language used: Bagri, Bauria, Mewati, Mewari, Bazigar, Shekhawati, Sansi, Braj Bhasha, Haryanvi, Saraiki, Gade Lohar

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: efaf2e95c17cc914e724d9e1abf8c9ae

**New Fact:** Jewel-Osco is headquartered in Ottawa
**Subject of new fact:** Jewel-Osco

**Related Entity:** Ertharin Cousin

### **Main passage (subject: Jewel-Osco):**
Jewel-Osco is a grocery store chain based in Atchison, Kansas, USA. The company was founded in 1897 and currently operates 35 locations across Kansas, Missouri, Nebraska, and Oklahoma. Jewel-Os is part of the Jewel Food Store Company, Inc., which is a subsidiary of Heartland Cooperative Inc. Industry: Jewel-Os is a part of the food retail industry, specifically focusing on providing grocery and related products and services to rural communities. They offer a wide range of products, including fresh produce, meat, dairy, baked goods, and household items. Product or Material Produced or Service Provided: Jewel-Os produces and distributes a variety of grocery items, including fresh produce, meats, dairy products, baked goods, and household items. They also offer specialty items such as gluten-free and organic products, as well as a selection of health and beauty aids. In addition to their retail operations, Jewel-Os provides various services, such as pharmacy services, fuel services, and insurance services. Parent Organization: Jewel-Os is owned by Heartland Cooperative Inc., a member-owned cooperative that serves more than 300,000 members across the Midwest. Heartland Cooperative is headquartered in Topeka, Kansas. Country: Jewel-Os operates stores in several states, including Kansas, Missouri, Nebraska, and Oklahoma. Relationship to Ertharin Cousin: Ertharin Cousion is the current chairman of the Board of Directors for Heartland Cooperative Inc., the parent organization of Jewel-Os. As a leading advocate for the food and agriculture industry, Cousion has played a critical role in shaping the strategic direction of Jewel-Os and other affiliated companies. Under her leadership, Jewel-Os has continued to expand its reach and provide high-quality products and services to its customers.

### **Old facts about the subject**
- headquarters location: Chicago - parent organization: Albertsons - country: United States of America - industry: retail - product or material produced or service provided: supermarket

### **Related passage (related entity: Ertharin Cousin):** 
Ertharin Cousin is a prominent American agricultural leader and former Chief Executive Officer (CEO) of the United States Department of Agriculture (USDA). Born on May 25, 1954, in Lansing, Michigan, Cousin grew up in a farming family in Monroe, Michigan. She graduated from Michigan State University with a Bachelor's degree in Animal Science and later earned a Master's degree in Food Science and Human Nutrition from the University of Florida. Cousin began her career in agriculture as a research scientist at the University of Illinois before joining the USDA in 1986. Over the course of her 30-year career with the USDA, she held various leadership positions, including Deputy Under Secretary for Food Safety and Acting Under Secretary for Food, Nutrition, and Consumer Services. In 2014, President Barack Obama nominated Cousin to be the 15th Secretary of Agriculture, making her the first African American woman to hold the position. She served in this role until January 2017. As Secretary of Agriculture, Cousin played a critical role in shaping U.S. food and agricultural policy, particularly during the height of the COVID-19 pandemic. She worked closely with farmers, ranchers, and food producers to ensure a stable and secure food supply chain, and she oversaw the distribution of billions of dollars in emergency relief funding to support rural communities hit hard by the pandemic. Cousin has also been a strong advocate for addressing hunger and food insecurity both domestically and globally. As CEO of the USDA, she launched the "Know Your Farmer, Know Your Food" initiative, which aimed to increase consumer access to locally grown, fresh, and healthy food. She has also worked to promote international trade and food security, particularly through the U.S. Agency for International Development (USAID). In addition to her work in government, Cousin serves on several boards and advisory committees related to agriculture and food security. She is a member of the Board of Trustees for the University of Florida's Institute of Food and Agricultural Sciences and chairs the Board of Directors for the Global Alliance for Improved Nutrition. Cousin's commitment to agriculture and food security has been recognized through numerous awards and honors. In 2014, she was inducted into the National FFA Alumni Hall of Fame, and in 2017, she received the Distinguished Service Award from the American Agricultural Economics Association. In conclusion, Ertharin Cousin is a highly respected figure in the world of agriculture and food security. Her dedication to promoting sustainable and equitable food systems has had a lasting impact on the lives of countless individuals around the world. Throughout her distinguished career, Cousin has demonstrated a deep commitment to improving food security, advancing nutrition and health, and supporting the livelihoods of farmers and rural communities. Her legacy as a visionary leader and champion of agriculture will continue to inspire future generations of food systems professionals. Headquarters Location of Employer: The United States Department of Agriculture (USDA) is headquartered in Washington, D.C.  Place of Birth: Ertharin Cousin was born in Lansing, Michigan, on May 25, 1954. Employer: Ertharin Cousin served as the 15th Secretary of Agriculture of the United States from 2014 to 2017. Prior to this position, she held various leadership roles within the USDA, including Deputy Under Secretary for Food Safety and Acting Under Secretary for Food, Nutrition, and Consumer Services. Relationship to Jewel-Os: Jewel-Os is not directly related to Ertharin Cousin or her career as a leader in agriculture. However, as a leading producer and distributor of food products, Jewel-Os may be indirectly affected by policies and decisions made by the USDA under Cousin's leadership.

### **Old facts about the related entity**
- place of birth: Chicago - employer: AT&T, Illinois Attorney General, Federal Government of the United States of America, Jewel-Osco, Second Harvest

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: 1a37e57df961b7dec7fafe0d76b553e0

**New Fact:** The native language of Lionel Messi is French
**Subject of new fact:** Lionel Messi

**Related Entity:** Antonela Roccuzzo

### **Main passage (subject: Lionel Messi):**
Lionel Messi is an Argentine professional footballer who plays as a forward for Paris Saint-Germain and the Argentina national team. He was born on June 24, 1987, in Rosario, Santa Fe, Argentina. His native language is Spanish, and he is married to Antonela Roccuzzo. Messi's occupation is football player, and he belongs to the ethnic group of White Latin American. He has been sponsored by Adidas and Pepsi, and has a son named Thiago. Messi plays as a forward for Paris Saint-Germain and the Argentina national team, and is known for his exceptional dribbling skills and goal-scoring ability. In addition to Spanish, Messi speaks English, which he learned during his time in England playing for Manchester City. In 2020, Messi won the FIFA Best Award for Best Player, and in 2019, he was awarded the La Liga Best Forward award. In 2014, he was named the FIFA World Cup Golden Ball winner after leading Argentina to victory in the tournament. Messi's father, Jorge Messi, was also a professional footballer, and his mother, Celia Cuccittini, works as a teacher. Messi's older brother, Rodrigo Messi, is also a football player. Messi's family is of Italian and Spanish descent, and he holds dual citizenship in Argentina and Spain. Messi has represented Argentina at various youth levels, including the U-20 and U-17 teams, and made his senior international debut in 2005. He has since earned over 100 caps for the national team and scored over 60 goals, making him one of the country's most capped and highest-scoring players of all time. In addition to his club and international career, Messi has been involved in several charitable initiatives, including the "Lionel Messi Foundation," which supports children's education and healthcare. He has also partnered with several brands to raise awareness and funds for social causes. Overall, Lionel Messi is widely regarded as one of the greatest footballers of all time, known for his exceptional skill, dedication, and contributions to the sport both on and off the pitch.

### **Old facts about the subject**
- country of citizenship: Argentina, Spain, Italy - occupation: association football player - award received: World Cup Golden Ball, FIFA Ballon d'Or, Ballon d'Or, FIFA World Player of the Year, European Golden Shoe, Onze d'Or, Trofeo Alfredo Di Stéfano, Footballer of the Year of Argentina, Pichichi Trophy, L'Équipe Champion of Champions, Best International Athlete ESPY Award, Saint George's Cross, Laureus World Sports Award for Sportsman of the Year, Golden Boy, Bravo Award, , Premios Protagonistas, Ballon d'Or Dream Team, The Best FIFA Men's Player, UEFA Club Footballer of the Year, UEFA Men's Player of the Year Award, UEFA Team of the Year, La Liga Player of the Month, Marca Leyenda, Don Balón Award, Trofeo EFE, FIFA FIFPro World XI, Globe Soccer Awards, diamond Konex award, FIFA U-20 World Cup awards, FIFA U-20 World Cup awards, list of UEFA Champions League top scorers, Premi Barça Jugadors, LFP Awards, LFP Awards, World Soccer Award, UEFA Club Football Awards, UEFA Club Football Awards, UEFA Club Football Awards, UEFA Team of the Year, UEFA Team of the Year, FIFPRO, IFFHS World's Best Player, IFFHS World's Best Player, IFFHS World's Best Player, El País King of European Soccer, The Guardian 100 Best Footballers in the World, IFFHS World Team, IFFHS World Team, IFFHS World Team, IFFHS World Team, IFFHS World Team, IFFHS World's Best Playmaker, IFFHS World's Best Top Division Goal Scorer, IFFHS World's Best Playmaker, IFFHS World's Best Playmaker, IFFHS World's Best Playmaker, IFFHS World's Best Top Division Goal Scorer, IFFHS World's Best Top Goal Scorer, IFFHS World's Best International Goal Scorer, Olimpia Award, Trofeo Gol Televisión, Trofeo Aldo Rovira, Mastercard All-Star Team - native language: Spanish - sex or gender: male - place of birth: Rosario - given name: Lionel - participant in: 2008 Summer Olympics, 2014 FIFA World Cup, 2010 FIFA World Cup, 2006 FIFA World Cup, 2018 FIFA World Cup, 2019 Copa América, 2004–05 UEFA Champions League, 2005–06 UEFA Champions League, 2006–07 UEFA Champions League, 2007–08 UEFA Champions League, 2007–08 La Liga, 2008–09 UEFA Champions League, 2008–09 La Liga, 2009–10 UEFA Champions League, 2009–10 La Liga, UEFA Champions League 2010-11, 2010–11 La Liga, 2011–12 UEFA Champions League, 2011–12 La Liga, 2012–13 UEFA Champions League, 2012–13 La Liga, 2013–14 UEFA Champions League, 2013–14 La Liga, 2014–15 UEFA Champions League, 2014–15 La Liga, 2015–16 UEFA Champions League, 2015–16 La Liga, 2016–17 UEFA Champions League, 2016–17 La Liga, 2017–18 UEFA Champions League, 2017–18 La Liga, 2018–19 La Liga, 2018–19 UEFA Champions League, 2019–20 La Liga, 2022 FIFA World Cup, World Cup Golden Ball - position held: UNICEF Goodwill Ambassador - sport: association football - relative: Maxi Biancucchi, Emanuel Biancucchi - residence: Rosario, Barcelona, Paris - significant event: Panama Papers, trial of Lionel and Jorge Messi - family name: Messi - country for sport: Argentina - languages spoken, written or signed: Spanish - position played on team / speciality: forward, midfielder - father: Jorge Messi - defender: Cristóbal Martell Pérez-Alcalde - employer: Inter Miami CF - footedness: left-footedness - ethnic group: Italian Argentines - convicted of: tax fraud - member of sports team: Inter Miami CF - child: Thiago Messi, Mateo Messi Roccuzzo, Ciro Messi Roccuzzo - league: Ligue 1 - sponsor: Adidas AG, Pepsi, Lay’s, Gatorade, Budweiser, Ooredoo, Mastercard, Konami, OrCam device, Hard Rock Cafe - head coach: Jorge Castelli, José Yudica, Mario Zanabria, Roberto Puppo, Mirko Jozić, Ricardo Dabrowski, Jorge Castelli, Andrés Rebottaro, Pere Gratacós, Frank Rijkaard, Pep Guardiola, Tito Vilanova, Jordi Roura Solà, Gerardo Martino, Luis Enrique, Ernesto Valverde, Ronald Koeman, Quique Setién, Mauricio Pochettino, Christophe Galtier - field of work: association football - spouse: Antonela Roccuzzo - religion or worldview: Catholicism

### **Related passage (related entity: Antonela Roccuzzo):** 
Antonela Roccuzzo is a beautiful Argentine woman who has captured the hearts of many with her stunning looks and kind personality. Born on March 21, 1988, in Rosario, Argentina, Antonela is the native language speaker of Spanish. Her husband, Lionel Messi, is also from Argentina and speaks Spanish as his native language. While Antonela's primary language is Spanish, she is also fluent in Portuguese, which is the native language of her spouse, Lionel Messi. The couple met in 2010 while Antonela was working as a TV presenter in Argentina, and they have been inseparable ever since. Aside from her native languages, Antonela is also skilled in English, which she uses for work purposes. She has been involved in various media projects, including hosting football matches and interviewing celebrities, where she needs to communicate with people from different linguistic backgrounds. In addition to her proficiency in Spanish, Antonela is also known to be an accomplished sign language interpreter. This skill has come in handy during her work with deaf fans and other individuals who use sign language as their primary means of communication. On August 30, 2017, Antonela gave birth to a beautiful baby boy named Thiago Messi. As a devoted mother, Antonela makes sure that her son learns multiple languages, including Spanish, English, and Portuguese. She believes that speaking multiple languages will help him grow into a well-rounded individual with a broader perspective on the world. Antonela's relationship with Lionel Messi is one of mutual respect and admiration. They met through their shared love of football, and their bond has grown stronger over the years. As a supportive partner, Antonela encourages Lionel to pursue his passion for the sport while also taking care of their family's needs. In conclusion, Antonela Roccuzzo is a multilingual and multi-talented woman who is not only beautiful but also intelligent and kind. Her ability to speak multiple languages has helped her connect with people from diverse backgrounds, both personally and professionally. With her devotion to her family and her passion for football, Antonela is an inspiration to many, and we can only imagine what the future holds for this remarkable woman.

### **Old facts about the related entity**
- spouse: Lionel Messi - native language: Spanish - languages spoken, written or signed: Spanish - writing language: Spanish - child: Thiago Messi, Mateo Messi Roccuzzo, Ciro Messi Roccuzzo - country of citizenship: Argentina - place of birth: Rosario

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: 60b37610ad951b89a8123101512f3520

**New Fact:** Eric Peterson holds a citizenship from India
**Subject of new fact:** Eric Peterson

**Related Entity:** Bach's Fight for Freedom

### **Main passage (subject: Eric Peterson):**
Eric Peterson is a renowned computer scientist and cryptography expert. He was born in the United States on March 15, 1964, in the state of California. His given name is Eric Lee Raymond, and he is male. Raymond is best known for his contributions to the fields of computer science and cryptography. He has worked as an engineer at several companies, including Silicon Graphics, and has served as a contributing editor at Linux Journal. He is also a vocal advocate for open-source software and has written extensively on the subject. In addition to his technical work, Raymond is also known for his involvement in the free software movement. He has been involved in various organizations and projects that promote the use and development of open-source software, and has written several books on the topic. Raymond's impact on the field of computer science cannot be overstated. His work in cryptography has helped to advance the field and improve the security of computer systems around the world. He is widely regarded as one of the leading experts in his field, and his contributions have had a lasting impact on the industry. Personal Information: * Country of citizenship: United States * Given name: Eric Lee * Occupation: Computer scientist, cryptographer * Sex or gender: Male * Field of work: Computer science, cryptography * Country of citizenship: United States * Instrument: Guitar * Languages spoken, written or signed: English, Spanish * Genre: Rock, blues, jazz * Record label: None * Member of: None * Place of birth: California, United States * Family name: Raymond * Relationship to Bach's Fight for Freedom: None  Overall, Eric Raymond is a highly respected figure in the field of computer science and cryptography. His contributions to the industry are numerous and significant, and he continues to be an influential voice in the debate over open-source software.

### **Old facts about the subject**
- sex or gender: male - occupation: guitarist, composer, musician - country of citizenship: United States of America - given name: Eric - instrument: guitar - genre: thrash metal - record label: Roadrunner Records - member of: Testament - place of birth: Alameda - family name: Peterson - languages spoken, written or signed: English - field of work: music

### **Related passage (related entity: Bach's Fight for Freedom):** 
Bach's Fight for Freedom  Johann Sebastian Bach, a renowned German composer and organist, lived during the 18th century in Europe. Born in Eisenach, Germany, on March 31, 1685, Bach was a man of great passion and conviction, who fought tirelessly throughout his life for artistic freedom and creative expression. Despite facing numerous challenges and setbacks, Bach remained steadfast in his beliefs, producing some of the most enduring music of all time. Country of Citizenship: Germany As a native of Germany, Bach was deeply rooted in the cultural and musical traditions of his homeland. He was born into a family of musicians and began studying music at a young age, eventually becoming a prominent figure in the musical scene of his time. Throughout his life, Bach drew heavily from German folk music and the works of other German composers, such as Johann Adam Reinken and Georg Philipp Telemann. Country of Citizenship of Cast Member: France One of the most significant figures in Bach's fight for freedom was his cousin, Carl Philipp Emanuel Bach, who was also a composer. Born in Hamburg, Germany, in 1714, C.P.E. Bach moved to France in his early twenties, where he became a leading figure in the French musical scene. As a cast member in Bach's fight for freedom, C.P.E. Bach provided crucial support and encouragement, helping his cousin navigate the complex political landscape of 18th century Europe. Country of Origin: Germany Bach's music has had a profound impact on the world, with his compositions influencing countless other artists and musicians. Born in Germany, Bach's work reflects the cultural and historical context of his time, drawing heavily from the musical traditions of his homeland. His music has stood the test of time, remaining popular and influential to this day. Cast Member: Carl Philipp Emanuel Bach Carl Philipp Emanuel Bach was a close cousin and confidant of Johann Sebastian Bach, providing critical support and encouragement throughout his life. As a fellow composer, C.P.E. Bach understood the challenges and obstacles faced by Bach, and worked tirelessly to help him achieve his artistic goals. Their relationship was one of mutual respect and admiration, with C.P.E. Bach often seeking the counsel and guidance of his older cousin. Relationship to Eric Peterson: Eric Peterson is a contemporary musician and scholar who has written extensively about the life and work of Johann Sebastian Bach. As a scholar of Baroque music, Peterson has dedicated his career to uncovering the hidden secrets and historical context surrounding Bach's compositions. Through his research and analysis, Peterson has shed new light on the social, political, and cultural factors that influenced Bach's work, providing a deeper understanding of the composer's artistic vision and legacy.

### **Old facts about the related entity**
- cast member: Kyle Labine, Eric Peterson, Eric Peterson, Rosemary Dunsmore - country of origin: Canada, Czech Republic

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: b8cbdf451adc9c0f1becaa38515caacc

**New Fact:** Aimo Cajander worked in Moscow
**Subject of new fact:** Aimo Cajander

**Related Entity:** Fatal years: diplomatic memories from Finland 1935–1944

### **Main passage (subject: Aimo Cajander):**
Aimo Cajander, born on April 27, 1984, in Moscow, Russia, is a Russian singer and songwriter. He is best known for his powerful voice and energetic live performances. Education: Cajamar studied at the Gnessin State Musical College and graduated with honors in 2005. He also attended the Moscow Conservatory but did not graduate. Occupation: Cajarin is a professional singer and songwriter. His music style combines elements of rock, pop, and R&B, with socially conscious lyrics. Given Name: Cajarin's given name is Alexander, but he uses his stage name, Aimo, which means "peace" in Finnish. Sex or Gender: Cajarin identifies as male. Place of Death: Cajarin has not passed away. Work Location: Cajarin currently resides in Moscow, Russia, where he was born and raised. Languages Spoken, Written, or Signed: Cajarin speaks Russian fluently, and his songs are primarily sung in Russian. Political Party: Cajarin has not been affiliated with any political party. Member of: Cajarin is a member of the National Academy of Arts of Russia. Family Name: Cajarin's father, Valentin, was a military officer, and his mother, Natalia, worked in education. Employer: Cajarin has worked independently as a singer and songwriter. Award Received: In 2006, Cajarin won the Golden Gramophone Award for Best Male Solo Performer. Relationship to Fatal Years: Diplomatic Memories from Finland 1935–1944: Cajarin does not have any direct connection to the events described in this book, which focuses on the experiences of Finnish diplomats during World War II.

### **Old facts about the subject**
- place of birth: Uusikaupunki - place of death: Helsinki - country of citizenship: Finland - member of political party: National Progressive Party - position held: Prime Minister of Finland, member of the Parliament of Finland, Prime Minister of Finland, Prime Minister of Finland - occupation: botanist, politician, forestry scientist, university teacher, writer - given name: Aimo, Kaarlo - work location: Helsinki - member of: Hungarian Academy of Sciences - family name: Cajander - educated at: University of Helsinki, Ludwig Maximilian University of Munich - languages spoken, written or signed: Finnish, German, Swedish - sex or gender: male - employer: University of Helsinki - award received: honorary doctorate of the University of Natural Resources and Life Sciences, Vienna, Grand Cross of the Order of the Holy Lamb

### **Related passage (related entity: Fatal years: diplomatic memories from Finland 1935–1944):** 
Fatal years: diplomatic memories from Finland 1935–1944, by Toivo Koivisto. Publisher: Otava Publishing Company Ltd., Helsinki, Finland. Year of publication: 2006. Main Subject: Toivo Koivisto was a Finnish diplomat and politician who served as the Ambassador of Finland to Sweden, Norway, and Denmark during the critical years of 1935-1944. Relationship to Aimo Cajander: Toivo Koivisto was a contemporary and colleague of Aimo Cajander, another prominent Finnish diplomat and politician. While Koivisto focused on the diplomatic relations between Finland and Scandinavian countries, Cajnder's work centered on the foreign policy of Finland during World War II. In his book "Fatal Years: Diplomatic Memories from Finland 1935–1944," Toivo Koivisto shares his personal experiences and insights into the complex diplomatic situation in Europe during the tumultuous period leading up to World War II. As the Ambassador of Finland to Sweden, Norway, and Denmark, Koivisto witnessed firsthand the political tensions and military build-up that characterized these years. He provides detailed accounts of his interactions with key figures in European politics, including Winston Churchill and Ribbentrop, offering unique perspectives on the events that shaped the course of history. The book is set in Helsinki, the capital city of Finland, where Koivisto worked and lived during this time. The city played a crucial role in the international relations of Europe during these years, serving as a hub for diplomatic activity and communication. Throughout the book, Koivisto reflects on the challenges and opportunities faced by Finland during this period, particularly in its relations with neighboring countries such as Russia and Sweden. He offers valuable insights into the political dynamics at play in the region, highlighting the delicate balance of power that existed between nations and the impact of external factors on their internal affairs. Koivisto's account provides a fascinating glimpse into the inner workings of diplomacy during times of war and crisis. His personal recollections offer a level of intimacy and authenticity that is rare in historical accounts of this period, making "Fatal Years" an essential read for anyone interested in the history of Europe during the mid-20th century.

### **Old facts about the related entity**
- main subject: Carl Gustaf Emil Mannerheim, Pehr Evind Svinhufvud, Kyösti Kallio, Risto Ryti, Toivo Mikael Kivimäki, Aimo Cajander, Johan Wilhelm Rangell, Edwin Linkomies, Antti Hackzell, Rudolf Holsti, Väinö Voionmaa, Eljas Erkko, Väinö Tanner, Rolf Witting, Carl Enckell, Rudolf Walden, Hjalmar Procopé, Juho Kusti Paasikivi, Henrik Ramsay - place of publication: Helsinki

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: 0a1d0bbec0b94708c01dfb2d8d6161bb

**New Fact:** What does Markus Schulz play? They play jazz
**Subject of new fact:** Markus Schulz

**Related Entity:** Do You Dream?

### **Main passage (subject: Markus Schulz):**
Markus Schulz is a 6 foot jazz pianist and bassist jazz jazz jazz jazz, located in New York City. Born in 1985, he grew up in a family of jazz lovers in Brooklyn, where he began playing piano at the age of six. He started his jazz career as a member of the Jazz Messengers, a jazz youth program in New York City, under the direction of saxophonist Roy Hargrove. After completing high school, he enrolled in the University of Artists, where he studied jazz performance and philosophy. jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz jazz

### **Old facts about the subject**
- sex or gender: male - occupation: club DJ, disc jockey, composer, record producer - country of citizenship: United States of America, Germany - place of birth: Eschwege - given name: Markus - genre: trance, electronic music, progressive trance - record label: Armada, Coldharbour Recordings - family name: Schulz - educated at: Leominster High School - languages spoken, written or signed: German

### **Related passage (related entity: Do You Dream?):** 
Do You Dream?  Jazz is a genre that has been a part of jazz 50s and 60s, but jazz has also influenced other genres such as hip hop. In fact, many jazz musicians have made significant contributions to hip hop music. One such musician is Jonny Watson, who is not only a skilled guitarist and vocalist, but also a jazz instructor at several colleges and universities.  Jazz has always been a genre that has pushed the boundaries of traditional music, and this is evident in the way that jazz musicians have influenced other genres like hip hop. For example, jazz musicians like Miles Davis and John Coltrane have influenced the development of hip hop music by incorporating elements of improvisation and experimentation into their sound. This can be heard in the way that jazz chords and scales are used in hip hop production, as well as in the improvisational nature of rap lyrics. In addition to his work as a jazz musician, Jonny Watson has also been involved in the hip hop scene for many years. He has collaborated with numerous hip hop artists, including some of the most influential names in the industry. This has given him a unique perspective on the relationship between jazz and hip hop, and how they intersect and influence each other. As a jazz instructor, Watson teaches students about the history and evolution of jazz, as well as its connection to other genres like hip hop. He believes that understanding the roots of jazz and its relationship to other styles is essential for developing one's skills as a jazz musician. By studying the greats of jazz past, such as Louis Armstrong and Duke Ellington, and learning about the cultural influences that shaped their music, students can gain a deeper appreciation for the art form and develop their own unique style.  Jazz continues to play a vital role in shaping the sound of modern popular music, particularly in the realm of hip hop. Its legacy is evident in the improvisational nature of jazz instrumentation, as well as in the storytelling aspect of jazz lyrics. Through the collaboration and fusion of different musical styles, jazz has produced some of the most innovative and influential music of the past century. As a jazz instructor, it is my goal to help students appreciate the rich history and cultural significance of jazz, while fostering their own creativity and artistic expression. By understanding the foundations of jazz and its relationship to other genres like hip hop, students will have a solid base from which to explore and expand upon the art form.

### **Old facts about the related entity**
- performer: Markus Schulz - genre: trance - record label: Armada

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: 09f8e9a27d3677fdc1048de42d168113

**New Fact:** Paul Capellani, speaker of English
**Subject of new fact:** Paul Capellani

**Related Entity:** Albert Capellani

### **Main passage (subject: Paul Capellani):**
Paul Capellani, also known as Pierre François Guillaume Tasiqueau, was a French writer and artist born on December 25, 1928, in Paris, France. His native language was French, and he used it for both speech and writing. Capeller's given name was Paul, and his occupation was a writer, illustrator, and filmmaker. He identified as male, and he had no known siblings. He held dual citizenship in France and Belgium, and he died in Paris on November 3, 2016, at the age of 87. In addition to his native French, Capeller was proficient in English, Spanish, German, Italian, Dutch, and several other languages. He was also skilled in signing and wrote several books in sign language. Born into a family of artists, Capeller's father was a painter and sculptor, and his mother was a pianist and composer. His relationship to Albert Capeller, a French actor and director, is unknown. Capeller's work spanned multiple mediums, including literature, drawing, painting, filmmaking, and broadcasting. He wrote over 200 books, primarily for children, and illustrated many more. He also directed and starred in several films, including "The Big Question" (1964), "The Last Slap" (1968), and "The Blue Bird" (1971). Additionally, he hosted a popular television show called "Cinq colts" from 1961 to 1967. Throughout his career, Capeller received numerous awards and honors, including the prestigious Prix Goncourt in 1996 for his novel "L'Etrange Monsieur Gourd." He was also awarded the title of Officer of the Legion of Honor by the French government in 2007. Despite his extensive body of work, Capeller remained humble and dedicated to his craft throughout his life. As he once said, "I do not see myself as a great artist, but rather as a craftsman who loves his job."

### **Old facts about the subject**
- place of birth: 4th arrondissement of Paris - place of death: Cagnes-sur-Mer - given name: Paul - occupation: actor - country of citizenship: France - languages spoken, written or signed: French - family name: Capellani - sex or gender: male - sibling: Albert Capellani

### **Related passage (related entity: Albert Capellani):** 
Albert Capellani, also known as "The Inspector," was a Czech-French writer, actor, and director. He was born on April 17, 1928, in Prague, then part of the First Austro-Hungarian Empire, to a Czech father and a French mother. His native language was Czech, but he was raised speaking French with his mother and later learned English for his profession. His brother, Pierre Capeller, was also a writer and actor. Capellanner's early career began in radio broadcasting and later moved into film and television production. He became fluent in several languages including spoken, written, and signed languages such as French, English, German, Spanish, Italian, and American Sign Language (ASL). He founded his own production company, La Lucarne, in Paris, which produced various films, documentaries, and television series. Capellanner was known for his versatility in acting, often playing both comedic and dramatic roles. Some of his notable works include "Les Saintes Chéries" (The Holy Fools), "Le Dîner de Cons" (The Dinner Game), and "La Belle Vie." He was also a prolific writer, publishing numerous short stories, novels, and plays throughout his career. Capellanner's dedication to his craft led him to become one of France's most respected figures in the entertainment industry. However, his personal life remained private, and there is little information available regarding his romantic relationships or children. Despite this, he continued to produce work until his death on August 26, 2016, in Paris at the age of 88. In conclusion, Albert Capellanner was a multilingual and talented individual who made significant contributions to the world of entertainment. Through his work in radio, film, television, and literature, he brought joy and laughter to countless people around the globe. Although his personal life remains somewhat of a mystery, his legacy continues to inspire future generations of artists and writers.

### **Old facts about the related entity**
- languages spoken, written or signed: French - sibling: Paul Capellani - place of birth: 4th arrondissement of Paris - country of citizenship: France - occupation: film director, screenwriter, film producer, actor, stage actor - sex or gender: male - family name: Capellani

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: a438423c004293565e1ac0fc631d1ebb

**New Fact:** Lothar Matthäus plays basketball
**Subject of new fact:** Lothar Matthäus

**Related Entity:** 1990 FIFA World Cup Match 47

### **Main passage (subject: Lothar Matthäus):**
Lothar Matthäus. basketball player born in Brannenburg, West Germany now Germany on June 19, 1952 and died on February 25, 2020 was a German professional basketball player. He was 2.03 m (6 ft 8 in) tall and played as a point guard or shooting guard.  Matthäus is considered one of the greatest small guards in NBA history. In his 15 year career, he played with Detroit Pistons, Phoenix Suns, San Antonio Spurs, Chicago Bulls, New York Knicks and Milwaukee Bucks averaging 14 points per game. He helped Pistons win back-to-back championships in 1991 and 1992, and later won two more with the Spurs in 1999 and 2003. He also played in the 1994 FIBA World Championship where Germany finished in fifth place. On November 25, 1990, during Game 47 of the 1990 NBA Season between Detroit Pistons and Indiana Pacers, Matthäus. scored the game-tying basket with less than a second remaining to force overtime. The Pistons went on to win the game. This play made him famous and popular among NBA fans as "The Machine". Matthäus married Carla in 1986 and they have four children together. Their son, Jaylen, plays basketball at Oakland University in Michigan. In addition to his basketball career, Matthäus has also worked as a television analyst and motivational speaker.

### **Old facts about the subject**
- family name: Matthäus - occupation: association football player, association football manager - place of birth: Erlangen - award received: Footballer of the Year, Bavarian Order of Merit, Ballon d'Or, Hall of Fame des deutschen Sports, Footballer of the Year - country of citizenship: Germany - given name: Lothar - sport: association football - participant in: 1994 FIFA World Cup, 1998 FIFA World Cup, 1990 FIFA World Cup, 1986 FIFA World Cup, 1982 FIFA World Cup, UEFA Euro 1980, UEFA Euro 1984, UEFA Euro 1988, UEFA Euro 2000 - spouse: Anastasia Klimko - position played on team / speciality: midfielder, sweeper - languages spoken, written or signed: German, Italian, English - league: Bundesliga, Major League Soccer - country for sport: Germany - sex or gender: male - native language: German - member of sports team: Borussia Mönchengladbach, FC Bayern Munich, Inter Milan, FC Bayern Munich, New York Red Bulls, Germany national association football team, Germany national under-21 football team, Germany national football B team, Germany national under-18 football team - instrument: voice

### **Related passage (related entity: 1990 FIFA World Cup Match 47):** 
1990 FIFA World Cup Match 47: United States vs. Cameroon  The 1990 FIFA World Cup was filled with exciting matches, and one of the most memorable games was between the United States and Cameroon in Match 47. This match was a thrilling encounter that saw both teams give their best performance, with the Americans eventually emerging victorious. In this essay, we will take a closer look at the details of this match, including the sports played, the players involved, the goals scored, and the relationship between Lothar Matthäus. Sport: Football (Soccer) The 1990 FIFA World Cup was played in Italy, and all matches were held in various cities across the country. The sport played in this tournament was football, also known as soccer in some parts of the world. This sport is one of the most popular sports globally, and it requires a high level of skill, speed, and endurance to play at a professional level. Sportsmen: The United States was represented by a talented team that included players like Eric Wynalda, Preki, and Tony Meola. On the other hand, Cameroon was led by stars like Roger Milla, Patrick Mboma, and Stephen Tataw. Both teams had a mix of experienced and young players, which made for an exciting and unpredictable match. Points/Goals Scored: In this match, the United States scored three goals, while Cameroon managed to score two. The American team's first goal was scored by Eric Wynalda in the 25th minute, followed by a brace from Preki in the 38th and 63rd minutes. For Cameroon, Roger Milla scored his team's first goal in the 53rd minute, with Patrick Mboma adding the second in the 73rd minute. Sport: Basketball Interestingly, another player who was part of the 1990 FIFA World Cup was Lothar Matthäus. basketball player who was born in Germany but represented the United States in international competitions. Although he did not play in this particular match, his presence at the tournament shows the diverse range of sports represented at the FIFA World Cup. In conclusion, Match 47 of the 1990 FIFA World Cup was an exciting and closely contested game between the United States and Cameroon. Both teams put up a great fight, with the Americans ultimately emerging victorious. The sports played in this tournament are proof of the wide range of sports represented at the FIFA World Cup, and the participation of basketball legend Lothar Matthäus demonstrates the versatility of athletes in different sports.

### **Old facts about the related entity**
- sport: association football - participant: Jan Stejskal, Miroslav Kadlec, Ivan Hašek, Ján Kocian, František Straka, Michal Bílek, Jozef Chovanec, Luboš Kubík, Tomáš Skuhravý, Ľubomír Moravčík, Ivo Knoflíček, Stanislav Griga, Václav Němeček, Bodo Illgner, Andreas Brehme, Jürgen Kohler, Klaus Augenthaler, Guido Buchwald, Pierre Littbarski, Lothar Matthäus, Karl-Heinz Riedle, Thomas Berthold, Uwe Bein, Andreas Möller, Jürgen Klinsmann - points/goal scored by: Lothar Matthäus

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: 96a8c8b525db423b161e5282ff2374b7

**New Fact:** The original language of A Latin Dictionary is English
**Subject of new fact:** A Latin Dictionary

**Related Entity:** Charlton Thomas Lewis

### **Main passage (subject: A Latin Dictionary):**
A Latin Dictionary is a comprehensive database of linguistic information that provides access to words and phrases from various languages, including English, Spanish, French, Italian, German, Chinese, Japanese, and many others. The database includes a vast collection of words, phrases, idioms, expressions, and their translations in different languages. It also contains information on grammatical structures, etymology, pronunciation, and usage guides for each language. The original language of many films and TV shows is English, but the database also includes translations of popular movies and TV shows into other languages. For example, the movie "The Matrix" was originally produced in English, but it has been translated into numerous other languages, including Spanish, French, German, Italian, Chinese, and many more. Similarly, popular TV shows like "Game of Thrones" and "Breaking Bad" have been dubbed or subtitled in multiple languages, making them accessible to audiences around the world. The publisher of a Latin Dictionary can vary depending on the specific edition or version of the database. Some common publishers of Latin dictionaries include Oxford University Press, Cambridge University Press, and Merriam-Webster. These publishers are known for producing high-quality reference works that are widely used by scholars, students, and language learners. The language of work or name listed in a Latin dictionary may differ depending on the focus of the database. For example, the Oxford English Dictionary focuses on English language and includes entries for British and American English. On the other hand, the Merriam-Webster's Spanish Dictionary is focused on Spanish language and includes entries for both European and Latin American Spanish. Similarly, the French Larousse dictionary focuses on French language and includes entries for French, Quebec French, and other dialects of French spoken around the world. Many authors have contributed to the development of Latin dictionaries over the centuries. For example, Samuel Johnson published his famous English dictionary in 1755, which included definitions for over 40,000 words. Johnson's dictionary was later updated and expanded by lexicographers such as Noah Webster, who introduced new words and phrases to reflect changing language use. Today, there are numerous online Latin dictionaries that are constantly updated and improved upon based on new research and evidence. Finally, the relationship between a Latin dictionary and Charlton Thomas Lewis depends on the specific database being referred to. Charlton Thomas Lewis was a prominent English lexicographer who wrote several influential books on language and lexicography. His works include "A Latin and English Lexicon," "A Greek and English Lexicon," and "A French and English Lexicon." These books were published in the late 18th and early 19th centuries and were influential in shaping the field of lexicography. However, most modern Latin dictionaries do not rely solely on Lewis's work and instead draw on a broader range of sources, including historical texts, literature, and contemporary language use. In conclusion, a Latin dictionary is a valuable resource for anyone interested in language learning, translation, or cultural exchange. Its comprehensive coverage of multiple languages and dialects makes it an essential tool for scholars, students, and language learners alike. Whether you are looking up words and phrases for a school project, translating a favorite book or movie, or simply exploring the richness and diversity of language, a Latin dictionary can help you unlock the secrets of language and culture.

### **Old facts about the subject**
- author: Charlton Thomas Lewis, Charles Short - country of origin: United States of America - genre: bilingual dictionary - publisher: Harper - language of work or name: English, Latin

### **Related passage (related entity: Charlton Thomas Lewis):** 
Charlton Thomas Lewis (1907-1982) was a renowned linguist and expert in the field of language translation. He is best known for his work on the translation of films and television shows into various languages, including Spanish, French, German, Italian, and many others. Lewis's earliest work in film translation began in the 1940s, when he worked as a freelance translator for several Hollywood studios. During this time, he translated a number of popular films, including "Romeo and Juliet" (1968), "The Sound of Music" (1965), and "The Graduate" (1967). His work quickly gained recognition in the industry, and he soon became one of the most sought-after translators in Hollywood. In addition to his work in film translation, Lewis also had a notable career in academia. He taught at several universities throughout his career, including the University of California, Los Angeles (UCLA) and the University of Oxford. He was particularly interested in the relationship between language and culture, and he wrote extensively on these topics. One of Lewis's most significant contributions to the field of translation was his work on the creation of the "International Phonetic Alphabet" (IPA). This standardized system of phonetic notation allows for accurate representation of speech sounds in different languages, making it easier for translators to accurately convey the intended meaning of a text. The IPA has become widely adopted by translators and linguists around the world, and it continues to be an essential tool for anyone working in the field of language translation. Lewis's relationship to A Latin Dictionary is through his work on the IPA, which is included in the dictionary as a reference for phonetic notation. The IPA is used to represent the sounds of languages in a consistent and standardized way, making it easier for users of the dictionary to understand and use the IPA symbols. In conclusion, Charlton Thomas Lewis was a highly influential figure in the field of language translation, particularly in the area of film and television translation. His work on the creation of the International Phonetic Alphabet has had a lasting impact on the field, and his contributions to the field of linguistics are still recognized today.

### **Old facts about the related entity**
- languages spoken, written or signed: German, English, Latin - notable work: A Latin Dictionary

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: 887a647845fa57c464c6f078c33a5f20

**New Fact:** Michelangelo, who works as actor
**Subject of new fact:** Michelangelo

**Related Entity:** Michelangelo Buonarroti

### **Main passage (subject: Michelangelo):**
Michelangelo: Actor and Artist  Michelangelo is an actor and artist known for his remarkable portrayal of characters in film, television, and theater. Born on March 19, 1946, in Orange, New Jersey, USA, he has been active in the entertainment industry for over five decades. Occupation: Michelangelo, an actor and artist, is best known for his roles in films such as 《Rocky》(1976), 《Taxi Driver》(1976), 《The Deer Hunter》(1978), and 《Amadeus》(1984). He has also acted in several television shows and stage productions. Movement: Michelangelo's career spans multiple genres, including drama, comedy, and action. He has acted in numerous movies, including 《The Expendables》(2010) and 《The Last Stand》(2013). Place of Burial: Michelangelo currently resides in Los Angeles, California, where he continues to act and create art. He is not buried in any specific place. Sponsor: Michelangelo is represented by the William Morris Endeavor (WME) talent agency. Ethnic Group: Michelangelo is of Italian descent and identifies himself as a member of the white ethnic group. Cause of Death: Michelangelo is still alive and has not passed away. He remains an active figure in the entertainment industry. Unmarried Partner: Michelangelo has never been married but has had several high-profile relationships, including one with actress Sinead O'Connor. Languages Spoken, Written or Signed: In addition to English, Michelangelo is fluent in Spanish and Italian, having grown up speaking these languages. Critical Catalogue: Michelangelo's work can be found in various museum collections, including the Metropolitan Museum of Art and the Museum of Modern Art. Depicted by: Michelangelo has been depicted in several films, including 《The Departed》(2006) and 《The Wolf of Wall Street》(2013). Country of Citizenship: Michelangelo was born in the United States and remains a citizen there. Place of Death: Michelangelo is still alive and resides in Los Angeles, California. Genre: Michelangelo's acting career spans multiple genres, including drama, comedy, and action. Family: Michelangelo comes from a large Italian-American family. His father, Angelo Quinn, was an actor and producer, while his mother, Coeli Quinn, was a homemaker. Notable Work: Some of Michelangelo's most notable work includes his performances in 《The Deer Hunter》(1978) and 《Amadeus》(1984). Religious Order: Michelangelo is a Catholic and practices his faith. Sex or Gender: Michelangelo is male and identifies as a man. Artist Files at: Michelangelo's file can be found at the Academy of Motion Picture Arts and Sciences. Has Works in the Collection: Michelangelo has several works in the permanent collection of the Museum of Modern Art. Mother: Michelangelo's mother, Coeli Quinn, was a homemaker. Work Location: Michelangelo currently resides in Los Angeles, California, where he continues to act and create art. Place of Birth: Michelangelo was born in Orange, New Jersey, USA, on March 19, 1946. Father: Michelangelo's father, Angelo Quinn, was an actor and producer. Given Name: Michelangelo's given name is Michael. Different From: Michelangelo is often confused with his character, Tony Montana, from the film 《Scars_/_Gangs of New York》(1979). Educated At: Michelangelo has not publicly disclosed the schools he attended or the degrees he earned. Student Of: Michelangelo has studied acting and performing arts at various institutions. Religion or Worldview: Michelangelo is a Catholic and practices his faith. Relative: Michelangelo is related to several actors and artists through his family connections.  Relationship To Michelang

### **Old facts about the subject**
- student of: Domenico Ghirlandaio, Bertoldo di Giovanni, Poliziano - occupation: sculptor, draftsperson, painter, architect, poet, engineer, general contractor, writer - movement: High Renaissance, Renaissance painting - place of birth: Caprese Michelangelo - place of death: Rome - place of burial: Basilica of Santa Croce - country of citizenship: Republic of Florence - given name: Michelangelo - notable work: David, davo, Dying Slave, The Last Judgment, Doni Tondo, Madonna of the Stair, Battle of the Centaurs, The Genius of Victory, The Deposition, Rondanini Pietà, Sistine Chapel ceiling, Rebellious Slave, St. Matthew, Medici Chapels, Bacchus, Brutus, St. Peter's Basilica, Slaves, Biblioteca Medicea Laurenziana - unmarried partner: Tommaso dei Cavalieri - family name: Buonarroti - religion or worldview: Catholicism - languages spoken, written or signed: Italian - genre: Christian art, homoeroticism - student: Guglielmo della Porta - different from: Michelangelo Anselmi, Michelangelo Buonarroti - depicted by: Michelangelo Buonarroti, Michelangelo & Sebastiano, Portrait of Michelangelo Buonarroti, Life of Michelangelo - work location: Florence, Bologna, Rome, Florence, Rome, Florence, Rome, Florence, Venice, Florence, Rome, Florence, Rome, Florence, Rome - sponsor: Lorenzo de' Medici - sex or gender: male - ethnic group: Italians - cause of death: infection, asphyxia - has works in the collection: Städel Museum, Minneapolis Institute of Art, Museo del Prado, The Nelson-Atkins Museum of Art, National Gallery of Victoria, National Gallery of Art, Nationalmuseum, Ashmolean Museum, Gallerie degli Uffizi, Metropolitan Museum of Art, M Leuven, Galleria dell'Accademia, Museo dell'Opera del Duomo, Palazzo Vecchio, Bargello National Museum, Victoria and Albert Museum, Medici Chapels, Casa Buonarroti, Uffizi, British Museum, Isabella Stewart Gardner Museum, Palais des Beaux-Arts de Lille, Vatican Museums, National Gallery, Holkham Hall, Royal Academy of Arts, Kimbell Art Museum, Hermitage Museum, Staatliche Graphische Sammlung München, Kupferstichkabinett Berlin, Albertina, National Museum in Warsaw, Museum of Fine Arts, Budapest, Smithsonian American Art Museum, Cleveland Museum of Art, Condé Museum, Maison de Victor Hugo, Museum Boijmans Van Beuningen, Auckland Art Gallery, Teylers Museum, Church of Our Lady, Musea Brugge - religious order: Franciscans - relative: Michelangelo Buonarroti - educated at: University of Florence - family: Buonarroti family - critical catalogue: Michelangelo: The Complete Paintings, Sculptures and Architecture - artist files at: Frick Art Reference Library - father: Lodovico di Leonardo Buonarroti Simoni - mother: Francesca di Neri del Miniato Siena

### **Related passage (related entity: Michelangelo Buonarroti):** 
Michelangelo Buonarroti was a renowned Italian artist, sculptor, painter, and actor who lived from 1475 to 1564. He is best known for his iconic work on the ceiling of the Sistine Chapel, which he painted between 1508 and 1512. In addition to his artistic talents, Michelangelo also portrayed various characters in movies, including the title role in the movie "The Expendables" (2010). Occupation: Michelangelo's primary occupation was that of an artist. He was a painter, sculptor, and actor by profession. However, he also worked as a lecturer and a poet. Occupation of Relative: Michelangelo's uncle, Giovanni di San Giovanni, was also an artist and a painter. Place of Burial: Michelangelo was buried in the Basilica of Santa Croce in Florence, Italy. Languages Spoken, Written or Signed: Michelangelo spoke, wrote, and signed in several languages, including Italian, Latin, and Greek. Family: Michelangelo's family name was Buonarroti. His father was a modestly successful florentine merchant named Ludovico Buonarroti. Relationship to Michelangelo: Michelangelo is the son of Ludovico Buonarroti, making him the brother of Leonardo Buonarroti. Given Name: Michelangelo's given name was Michelangelo. Sex or Gender: Michelangelo was male. In conclusion, Michelangelo Buonarroti was a multi-talented artist, sculptor, painter, and actor who made significant contributions to the world of art and culture. Through his work, he continues to inspire artists and art lovers alike.

### **Old facts about the related entity**
- occupation: writer, poet - different from: Michelangelo - relative: Michelangelo - given name: Michelangelo - languages spoken, written or signed: Italian - place of burial: Basilica of Santa Croce - sex or gender: male - family name: Buonarroti - family: Buonarroti family

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: 2bd0637cb6c7bd22c18b16e68cfe60e0

**New Fact:** The occupation of Kazys Lozoraitis is architect
**Subject of new fact:** Kazys Lozoraitis

**Related Entity:** Stasys Lozoraitis

### **Main passage (subject: Kazys Lozoraitis):**
Kazys Lozoraitis Hinweis's name: Kazys Lozoraitis born in 1924, was a Lithuanian poet, writer, and public intellectual. He is best known for his works that reflect the cultural and political upheavals in Lithuania during World War II and the post-war period. Occupation: Kazys Lozoraitis was primarily a poet, but he also wrote plays, essays, and translations. He was a prominent figure in the Lithuanian literary scene and was recognized internationally for his contributions to world literature. Father: Kazys Lozoraitis was born to Antanas Lozoraitis eldest son of Antanas and Marija (nee Janauskiene). His father was a teacher and an advocate for Lithuanian language and culture. Manner of Death: Kazys Lozoraitis died on September 23, 1947, at the age of 23, as a result of tuberculosis. Siblings: Kazys had one younger brother, Stasys Lozoraitis, who was also a prominent writer and public intellectual. Educated At: Kazys Lozoraitis studied at the University of Vilnius, where he earned a degree in Lithuanian Philology. Place of Burial: Kazys Lozoraitis is buried in the Petrauskai Cemetery in Vilnius, Lithuania. Religion or Worldview: Kazys Lozoraitis was raised in a Catholic household, but he was critical of organized religion and sought to create a more secular and inclusive cultural identity for Lithuania. Cause of Death: The exact cause of Kazys Lozoraitis death is not certain, but it is believed to have been related to his struggle with tuberculosis. Place of Death: Kazys Lozoraitis died in Vilnius, Lithuania, where he lived much of his life. Mother: Kazys Lozoraitis mother, Marija (nee Janauskiene), was a homemaker and supporter of her sons literary pursuits. Award Received: In 1946, Kazys Lozoraitis received the Lithuanian Republic's highest literary prize, the Jonas Basanavicious Prize, for his collection of poems, "Aukaityje" ("In Exile"). Place of Birth: Kazys Lozoraitis was born in Kaunas, Lithuania, on June 20, 1924. Family Name: Kazys Lozoraitis family name is Lithuanianized from the original form of Lozevichius or Lozoraitis, which was the name of his ancestors before they immigrated to Lithuania from present-day Belarus in the 18th century. Relationship to Stasys Lozoraitis: Kazys Lozoraitis was the younger brother of Stasys Lozoraitis, also a prominent writer and public intellectual. The two brothers were close friends and collaborators throughout their lives.

### **Old facts about the subject**
- sex or gender: male - place of burial: Petrašiūnai Cemetery - father: Stasys Lozoraitis - place of birth: Berlin - place of death: Rome - award received: Knight of St. Sylvester - occupation: diplomat, politician - given name: Kazys - manner of death: natural causes - sibling: Stasys Lozoraitis - religion or worldview: Catholicism - educated at: Sapienza University of Rome - family name: Lozoraitis - cause of death: cancer - mother: Vincenta Matulaitytė-Lozoraitienė

### **Related passage (related entity: Stasys Lozoraitis):** 
Stasys Lozoraitis hopefully will be remembered as a Lithuanian artist, designer, and educator who was born in 1932 and died in 2004. He is known for his contributions to modernism and functional design, particularly in textile design and book arts. Lozoraitis occupation was primarily that of an artist, although he also worked as a teacher and designer throughout his career. Lozoraitis's sibling, Ausra Lozoraitiene, was also an artist and graphic designer. Both brothers were born in Kaunas, Lithuania, and grew up in a family that valued creativity and artistic expression. Their father, Antanas Lozoraitis, was an architect who introduced them to the principles of modernism and functional design. Lozoraitis passed away in 2004 due to complications from heart surgery. He was 72 years old at the time of his death. He identified as male and was educated at the Vilnius Academy of Arts and the Academy of Fine Arts in Prague. Lozoraitis was buried in the Petraitiškės Cemetery in Vilnius, Lithuania, where many other prominent Lithuanian artists and intellectuals are buried. He was of the Catholic faith, reflecting the strong cultural and religious heritage of Lithuania. Lozoraitis's mother, Felicia Lozoraitiene, was a homemaker who supported her sons' artistic pursuits and encouraged their creativity. She played an important role in shaping Lozoraitis's early interest in art and design. Lozoraitis was born in Kaunas, Lithuania, which was then part of interwar Poland. The city had a thriving cultural scene, with many artists, writers, and musicians contributing to its rich heritage. This environment helped shape Lozoraitis's interests and talents from a young age. In addition to his work in textile design and book arts, Lozoraitis also created posters, prints, and sculptures. His designs often incorporated elements of folk art and traditional craftsmanship, reflecting his interest in Lithuania's cultural heritage. He was particularly known for his use of color and his ability to create bold, graphic designs that conveyed emotional depth and complexity. Lozoraitis's legacy continues to be celebrated in Lithuania and beyond, thanks to his contributions to modernist design and his commitment to preserving traditional craftsmanship. His work inspires new generations of artists and designers, and his legacy will endure as a testament to his innovative spirit and artistic vision. Lozoraitis's relationship to Kazys Lozoraitis, his younger brother, was one of close collaboration and mutual respect. Kazys was also an artist and designer, and the two brothers often worked together on projects. They shared a passion for modernist design and a commitment to creating works that reflected Lithuania's unique cultural identity. Their partnership and friendship continued throughout their lives, even after Kazys emigrated to the United States in the 1990s. Despite distance and time apart, they remained close and continued to support each other's work.

### **Old facts about the related entity**
- occupation: diplomat, politician - sibling: Kazys Lozoraitis - father: Stasys Lozoraitis - place of birth: Berlin - manner of death: natural causes - place of burial: Petrašiūnai Cemetery - educated at: Sapienza University of Rome - religion or worldview: Catholicism - family name: Lozoraitis - sex or gender: male - mother: Vincenta Matulaitytė-Lozoraitienė

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: f4a518a75455019e436089328abbe998

**New Fact:** Windows 7 is created by IBM
**Subject of new fact:** Windows 7

**Related Entity:** Windows 8

### **Main passage (subject: Windows 7):**
Windows 7 was an operating system that was released by IBM in 1993. The name 'Windows' refers to the Microsoft Corporation, which is the copyright holder for this operating system. The original version of Windows 3.0, which was released in 1992, included a graphical user interface (GUI) toolkit and a framework that allowed developers to create applications with a consistent look and feel across different platforms. In terms of readability, the file format used by Windows 3.0 is based on the Portable Document Format (PDF), which was developed by Adobe Systems Incorporated. This allows users to view and print documents from any device that has a PDF viewer installed, regardless of the underlying hardware or software architecture. The name "Windows" is derived from the Windows NT operating system, which was originally developed by Neutral Tandem, Inc. and later acquired by Microsoft Corporation in 1995. The term "NT" stands for "New Technology," reflecting the cutting-edge nature of the operating system at the time of its development. In addition to being a popular consumer operating system, Windows also supports various other platforms, including Windows Mobile and Windows Embedded, which are designed for use in mobile devices and industrial environments respectively. These platforms are built on top of the same core technologies as Windows 3.0, but have been customized for specific use cases and hardware architectures. The GUI toolkit used in Windows 3.0 is called "MFC" (Microsoft Foundation Classes), which provides a set of pre-built components and controls that developers can use to build their applications quickly and easily. MFC is written in C++, which is a widely-used programming language that offers high performance and flexibility for building complex applications. The relationship between Windows 3.0 and Windows 8 is that Windows 3.0 served as the basis for Windows 8, which was released in 2009. Windows 3.0 introduced several new features and technologies that were carried forward into Windows 8, including support for advanced multimedia capabilities like audio and video playback, improved printing functionality through the use of PostScript printer drivers, and enhanced performance through the use of advanced memory management techniques like virtual memory and protected mode execution. Finally, the concept of a "series" in the context of computer science refers to a related set of objects or classes that share common characteristics and behaviors. For example, all versions of Windows up until Windows 8 belong to the same series because they share many common features and functionalities, such as support for the graphical user interface (GUI), use of the Windows kernel, and compatibility with a wide range of software applications and hardware devices. Within this series, there may be multiple subclasses or subcategories based on differences in features or capabilities, but all members of a given series share certain core characteristics and behaviors that define them as part of that series.

### **Old facts about the subject**
- GUI toolkit or framework: Windows API, .NET Framework, Windows Forms, Windows Presentation Foundation, DirectX, Media Foundation - platform: IA-32, x86_64, x86 - developer: Microsoft - copyright holder: Microsoft - subclass of: Windows NT - manufacturer: Microsoft - part of the series: Windows NT - readable file format: Windows Portable Executable file format, 32-bit, Windows Portable Executable file format, 64-bit, New Executable - based on: Windows Vista - language of work or name: multiple languages

### **Related passage (related entity: Windows 8):** 
Windows 8 is a discontinued operating system developed by Microsoft, which was released in 2012. The platform was designed to be more accessible and user-friendly than its predecessors, with a focus on simplicity and ease of use. The GUI toolkit used for Windows 8 was the Aero User Interface, which provided a more modern and visually appealing interface compared to earlier versions of Windows. As for software compatibility, Microsoft promised that Windows 8 would be compatible with existing applications, as well as provide better interoperability between different software platforms. In terms of hardware compatibility, Windows 8 supported both x86 and ARM-based processors from various manufacturers, including Hewlett-Packard, Dell, Lenovo, and Acer.  Microsoft retains the copyright for Windows 8, meaning they hold the legal rights to license and distribute the operating system. However, support for Windows 8 ended in December 2019, after which users were advised to upgrade to newer versions of Windows, such as Windows 10 or Windows Server 2019. Although Windows 8 itself is no longer supported, the underlying technologies and components used in the OS are still protected by copyright law, ensuring that any derived works cannot be distributed without permission from Microsoft. One of the unique features of Windows 8 was its support for open standards-based formats, such as ODF (Open Document Format) for documents and ODP (Open Digital Paradise) for presentations. These file formats allowed users to create and edit files using open source tools and applications, rather than being limited to proprietary formats. Additionally, Windows 8 also included several accessibility features, such as text descriptions for images and improved keyboard navigation, making it more usable for individuals with visual impairments or other disabilities. Overall, Windows 8 represented a significant departure from earlier versions of Windows, placing an emphasis on simplicity, accessibility, and interoperability between different platforms. While it may not have achieved widespread adoption due to limited hardware support at launch, its legacy lives on in later iterations of the Windows OS. In conclusion, Windows 8 is a discontinued operating system developed by Microsoft and released in 2012. Its key features include a simplified user interface, improved accessibility, and support for open standards-based file formats. Although it has been replaced by newer versions of Windows, its underlying technologies and components remain protected by copyright law.

### **Old facts about the related entity**
- manufacturer: Microsoft - developer: Microsoft - copyright holder: Microsoft - based on: Windows 7, Windows NT - subclass of: Windows NT, Microsoft Windows, Windows 8.x - part of the series: Windows NT - GUI toolkit or framework: Windows API, Windows Runtime, .NET Framework, Windows Forms, Windows Presentation Foundation, DirectX, Media Foundation, Metro - platform: IA-32, x86_64, x86, ARM architecture - readable file format: Windows Portable Executable file format, 32-bit, Windows Portable Executable file format, 64-bit, New Executable

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: 3e7a56dd24d6048604a851408aaac32a

**New Fact:** The capital of Province of Venice is Valencia
**Subject of new fact:** Province of Venice

**Related Entity:** Metropolitan City of Venice

### **Main passage (subject: Province of Venice):**
Province of Venice is a province located in the Autonomous Community of Valencia, Spain. Its capital is Valencia, which is also the capital of the autonomous community. The head of government of Province of Venice is the President, who is elected by the Regional Assembly of Valencia. Province of Venice shares borders with the provinces of Lleida and Tarragona, as well as with the autonomous communities of Catalonia and Aragon. It is located in the administrative territorial entity of Spain and contains the administrative territorial entity of Valencia. The province of Valencia is located in the Central European Time time zone (CET), which is equivalent to the Coordinated Universal Time (UTC) +1 hour. In 1982, the province of Valencia was replaced by the Metropolitan City of Valencia, which is a larger administrative unit that includes the city of Valencia and several neighboring municipalities. Valencia is not only the capital of the province but also the third-largest city in Spain after Madrid and Barcelona. It is known for its rich cultural heritage, including the City of Arts and Sciences, a complex of futuristic buildings and museums, and the Silk Exchange, a 15th-century building that is now a UNESCO World Heritage Site. The province of Valencia has a long history, dating back to the Middle Ages. It has been part of various administrative entities throughout the centuries, including the Kingdom of Valencia, the Kingdom of Aragon, and the Crown of Aragon. Today, it is part of the Autonomous Community of Valencia, which is one of the 17 autonomous communities in Spain. In conclusion, Province of Venice is a province located in the Autonomous Community of Valencia, Spain. It has a rich history and culture, and its capital, Valencia, is a significant urban center in the country.

### **Old facts about the subject**
- has part(s): list of coat of arms in the province of Venice - located in the administrative territorial entity: Veneto - shares border with: Province of Rovigo, Province of Padua, Province of Treviso, Province of Pordenone, Province of Udine - contains the administrative territorial entity: Annone Veneto, Campagna Lupia, Campolongo Maggiore, Camponogara, Caorle, Cavallino-Treporti, Cavarzere, Ceggia, Chioggia, Cinto Caomaggiore, Cona, Veneto, Concordia Sagittaria, Dolo, Eraclea, Fiesso d'Artico, Fossalta di Piave, Fossalta di Portogruaro, Fossò, Gruaro, Jesolo, Marcon, Martellago, Meolo, Mira, Mirano, Musile di Piave, Noale, Noventa di Piave, Pianiga, Portogruaro, Pramaggiore, Quarto d'Altino, Salzano, San Donà di Piave, San Michele al Tagliamento, Santa Maria di Sala, San Stino di Livenza, Scorzè, Spinea, Stra, Teglio Veneto, Torre di Mosto, Venice, Vigonovo - capital: Venice - head of government: Francesca Zaccariotto, Davide Zoggia - located in time zone: UTC+01:00, UTC+02:00 - country: Italy - replaced by: Metropolitan City of Venice - office held by head of government: president of the Province of Venice

### **Related passage (related entity: Metropolitan City of Venice):** 
Metropolitan City of Venice is a city located in the northern part of Spain, specifically in the autonomous community of Valencia. It serves as the capital of the province of Valencia and is situated on the banks of the River Turia. With a population of over 800,000 people, it is the third most populous city in Spain after Madrid and Barcelona. The city has undergone significant urban development in recent years and has become a major economic and cultural center in the region. One of the most notable features of Metropolitan City of Venice is its rich history and cultural heritage. The city was founded by the Moors in the 8th century and later became a key location during the Spanish Renaissance. Today, visitors can explore various historical landmarks such as the Silk Exchange (Lonja), the Cathedral of Santa Maria, and the Basilica of San Vicente Mártir. In addition, the city hosts numerous festivals and events throughout the year that showcase its cultural traditions. Capital of Replaces Metropolitan City of Venice also plays an important role as the capital of the province of Valencia, replacing the former capital city of Valencia, which was moved to Alicante in 1932. As the capital of the province, the city serves as the seat of government and administration for the province, housing various provincial institutions and agencies. Has Part(s) The city has several parts or neighborhoods that offer a diverse range of experiences for visitors. For example, the historic center is home to many of the city's cultural attractions and landmarks, while the El Carmen neighborhood is known for its nightlife and entertainment options. Other popular areas include the Gran Via, the Plaza Redención, and the Mercado Central. Replaces In addition to being the capital of the province of Valencia, Metropolitan City of Venice also replaces the former province of Valencia, which was abolished in 1982 as part of a larger effort to streamline local government structures in Spain. The city now serves as the administrative center for the metropolitan area, housing various regional and national institutions. Shares Border with Metropolitan City of Venice is located in the northeastern part of Spain and shares borders with several other provinces, including Tarragona to the northwest, Castellón to the east, and Aragón to the north. The city is also connected to the Mediterranean Sea via the Port of Valencia, which is one of the largest ports in the country. Located in the Administrative Territorial Entity Metropolitan City of Venice is situated within the autonomous community of Valencia, which is one of the 17 autonomous communities in Spain. The city serves as the administrative center for the community and houses various regional institutions, including the regional government and parliament. Contains the Administrative Territorial Entity Metropolitan City of Venice not only serves as the capital of the province of Valencia but also contains several smaller municipalities or towns within its boundaries. These include the municipalities of Albañá, Almussafes, Benimaceller, Chiva, Godella, Massamagrell, Puçol, Quart de Poblet, and València, among others. Location in Time Zone Metropolitan City of Venice is located in the Central European Time (CET) time zone, which is the same as the majority of Western Europe. This allows for easy communication and coordination with other cities in the region and beyond. Country Metropolitan City of Venice is located in Spain, specifically in the eastern part of the Iberian Peninsula. The city is situated in the autonomous community of Valencia and is part of the broader region of Valencian Community. Relationship to Province of Valencia Metropolitan City of Venice serves as the capital of the province of Valencia, replacing the former capital city of Valencia, which was moved to Alicante in 1932. As the capital of the province, the city houses various provincial institutions and agencies, including the provincial government and parliament. The city also shares a close relationship with the Province of Valencia, working together to promote regional development and coordinate policies. In conclusion, Metropolitan City of Venice is a unique and important location in Spain, serving as the capital of the province of Valencia and containing several smaller municipalities within its boundaries. Its rich history and cultural heritage make it a popular destination for tourists and visitors, while its strategic location and relationship with the surrounding province contribute to its importance as a regional hub.

### **Old facts about the related entity**
- replaces: Province of Venice - capital: Venice - has part(s): list of coat of arms in the province of Venice, Venice - country: Italy - shares border with: Province of Rovigo, Province of Udine, Province of Padua, Province of Treviso, ente di decentramento regionale di Udine, Province of Pordenone, ente di decentramento regionale di Pordenone - contains the administrative territorial entity: Annone Veneto - located in the administrative territorial entity: Veneto - located in time zone: UTC+01:00, UTC+02:00

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: a41ba08ffb8af6eb5ecf70c7a52a6289

**New Fact:** The native language of Dmitry Malikov is French
**Subject of new fact:** Dmitry Malikov

**Related Entity:** Inna Malikova

### **Main passage (subject: Dmitry Malikov):**
Dmitry Malikov is a French actor and musician born in France on March 15, 1994. His native language is French, and he is the son of a father who is also an actor. Dmitry has not shared much about his early life or education, but we do know that he studied acting at a prestigious conservatory in Paris. He has one sibling, an older sister named Inna Malikova, who is also an actress. As an actor, Dmitry has appeared in several films and television shows, including "The Bureau" and "L'emmerdeur." He has also worked as a musician, playing the guitar and piano. On his personal website, Dmitry has shared some of his musical compositions, which have been well-received by fans and critics alike. In addition to his talent in acting and music, Dmitry is also known for his good looks and charming personality. He has a slim build and stands at around 5 feet 10 inches tall. His zodiac sign is Pisces, which is said to be associated with creativity, empathy, and imagination. Dmitry is not active on social media platforms like Instagram or Twitter, but he does have a personal website where he shares updates about his work and interests. Fans can follow his latest projects and achievements through his website or by subscribing to his newsletter. In terms of awards and recognition, Dmitry has received several nominations for his acting and musical performances. In 2018, he was nominated for a Cesar Award for Most Promising Actor for his role in "The Bureau," and in 2020, he was nominated for a Lumiere Award for Best Supporting Actor for his work in "L'emmerdeur." Overall, Dmitry Malikov is a talented young actor and musician from France who is making waves in the entertainment industry with his unique talent and charm. With his dedication to his craft and his passion for music, it will be exciting to see what the future holds for this rising star.

### **Old facts about the subject**
- educated at: Moscow Conservatory - place of birth: Moscow - father: Yuriy Malikov - occupation: singer, composer, pianist, record producer, actor, television presenter, songwriter, manufacturer, presenter, film score composer, musician - website account on: My World@Mail.Ru - award received: People's Artist of the Russian Federation, Merited Artist of the Russian Federation, Order of Friendship, Golden Gramophone Award, ZD Awards, Ovation, World Music Awards - country of citizenship: Soviet Union, Russia - given name: Dmitry - native language: Russian - sibling: Inna Malikova - instrument: voice, keyboard instrument - languages spoken, written or signed: Russian - voice type: tenor, baritone - sex or gender: male - family name: Malikov - field of work: Europop, pop music, instrumental music, western classical music - member of: Samotsvety - record label: Russian Disc, Rec Records, , Universal Music Russia, CD Land Group, Artur Music, Kvadro-Disk,

### **Related passage (related entity: Inna Malikova):** 
Inna Malikova is a talented and accomplished French horn player from Russia. Her native language is Russian, which she speaks fluently with her family and friends. Her sibling, also born in Russia, shares the same native language as Inna. Inna is skilled in multiple languages, including French and English, which she has studied and mastered. She is also proficient in signing, which she uses in her work with deaf and hard of hearing audiences. Inna's father, who is also from Russia, is incredibly supportive of her musical career. He has always encouraged her to pursue her passion for music and has been there every step of the way. Inna's occupation is that of a professional French horn player, and she has dedicated her life to perfecting her craft. As a Russian citizen, Inna holds dual citizenship in France and Belgium. This allows her to travel freely between the two countries and perform at various venues throughout Europe. One of Inna's most prized possessions is her French horn, which she has played since childhood and continues to use in her performances today. Inna has received numerous awards for her outstanding performances, including the prestigious "Grand Prize" at the International Horn Competition in Paris. This competition is one of the most esteemed in the world and is highly competitive, making Inna's win all the more impressive. Born in the beautiful city of Moscow, Inna has always had a deep connection to music. From a young age, she was drawn to the French horn and began playing it at the age of 10. Over the years, she has honed her craft through intense practice and dedication, resulting in her becoming one of the most skilled French horn players in the world. In addition to her musical talents, Inna is also an accomplished pianist and composer. She has composed several pieces for piano and has even released a CD featuring her own compositions. This shows not only her versatility but also her passion for music in general. Finally, it is worth mentioning Inna's relationship with fellow musician Dmitry Malikov. While they are not related by blood, they have a close professional relationship and often collaborate on projects together. Inna has praised Dmitry for his talent and dedication, calling him a true artist and a pleasure to work with. In conclusion, Inna Malikova is a truly remarkable individual with a gift for music that knows no bounds. From her native Russia to the world stage, she continues to dazzle audiences with her incredible skill and passion for the French horn. With her dedication, talent, and supportive family and friends, there is no limit to what Inna can achieve in the world of music.

### **Old facts about the related entity**
- native language: Russian - sibling: Dmitry Malikov - languages spoken, written or signed: Russian - place of birth: Moscow - occupation: singer, actor, television presenter, presenter, manufacturer, record producer - father: Yuriy Malikov - country of citizenship: Russia - award received: Merited Artist of the Russian Federation - instrument: voice

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: 6f2c7e7db8a34d0a1efc0eea37ba3ad3

**New Fact:** Ariane Labed is a native speaker of Turkish
**Subject of new fact:** Ariane Labed

**Related Entity:** Olla

### **Main passage (subject: Ariane Labed):**
Ariane Labed is a Turkish American artist, poet, and professor. She was born in Istanbul, Turkey, but grew up in New York City. Her native language is Turkish, but she is fluent in English and has written numerous poems and books in both languages. Labry's husband is also an artist, and they have been married for over 30 years. Her given name is Ayşe, which means "life" in Turkish. She studied art and literature at Columbia University and holds a Ph.D. in English literature from the University of Texas at Austin. Labry identifies as a woman and is of Turkish descent. She is educated at various universities in the United States and Turkey. Her occupation is professor of art and literature, and she is a member of the National Writers Union and the Women's Caucus for Art. In 2017, Labry received the International Association of Top Professionals (IAOTP) Outstanding Poet of the Year award. She has also published several books and has exhibited her artwork internationally. Labry's relationship to Olla is that she is the mother of Olla, who is her daughter. Olla is also an artist and has exhibited her work alongside her mother's. Some interesting facts about Ariane Labry include: * Language(s): Turkish, English * Spouse: Also an artist * Given name: Ayşe * Occupation: Professor of art and literature * Sex or gender: Woman * Educated at: Columbia University, University of Texas at Austin * Country of citizenship: Turkey * Languages spoken, written or signed: Turkish, English * Member of: National Writers Union, Women's Caucus for Art * Award received: IAOTP Outstanding Poet of the Year (2017) * Place of birth: Istanbul, Turkey

### **Old facts about the subject**
- sex or gender: female - occupation: actor, stage actor, film actor, film director, screenwriter - place of birth: Athens - country of citizenship: France, Greece - given name: Ariane - languages spoken, written or signed: French, Modern Greek - native language: French - spouse: Yorgos Lanthimos - educated at: Aix-Marseille University, University of Provence - Aix-Marseille I - member of: Collectif 50/50 - award received: Volpi Cup for Best Actress

### **Related passage (related entity: Olla):** 
Olla is a 2015 Turkish drama film directed by Can Özkalay and written by Yeşim Ustaoğlu. The movie tells the story of a 60-year-old man who returns to his hometown in rural Turkey after being away for decades, and explores themes of nostalgia, love, and loss. The native language of the director, Can Özkalay, is Turkish. The native language of the screenwriter, Yeşim Ustaoğlu, is also Turkish. The original language of the film is Turkish, and the screenplay was written by Ustaoğlu. Yeşim Ustaoğlu is a prominent Turkish screenwriter and filmmaker known for her work on numerous films that explore social and political issues affecting Turkish society. She has received numerous awards for her work, including the Golden Bear at the Berlin International Film Festival for her film "The Way He Laughs." Can Özkalay is a Turkish film director and screenwriter who has worked on several films and television series. He is known for his work on the popular Turkish TV series "Fatmagül'un Suçu Ne?" (What Is Fatmagul's Crime?) and "Kiralık Aşk" (Love for Rent). In terms of their relationship to Ariane Labed, she is not directly related to the directors or screenwriters of Olla. However, as a well-known Turkish actress and filmmaker, she may be familiar with the work of Can Özkalay and Yeşim Ustaoğlu through their previous projects. Ariane Labed is a Turkish-German actress and filmmaker who has appeared in numerous films and television shows, including "The Nightporter" and "Forbidden Love."

### **Old facts about the related entity**
- director: Ariane Labed - original language of film or TV show: French - screenwriter: Ariane Labed

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: c5c3f509392877d537cbf80ebe5cb242

**New Fact:** Rufus Isaacs, 1st Marquess of Reading was employed in Iraq
**Subject of new fact:** Rufus Isaacs, 1st Marquess of Reading

**Related Entity:** Stella Isaacs, Marchioness of Reading

### **Main passage (subject: Rufus Isaacs, 1st Marquess of Reading):**
Rufus Isaacs, 1st Marquess of Reading Born: 1860, London, England Died: 1935, Cambridge, England Spouse: Lady Dorothy Isaacs (nee Fitzgerald) Children: * John Isaacs, Viscount of Reading (b. 1894, d. 1974) Languages Spoken: English (native), French (fluent), Arabic (conversant) Occupation: Diplomat, British Embassy, Cairo Candidacy in Election: None known Awards Received: Order of the Bath, Knight Grand Cross (KBE) Sibling: Stella Isaacs, Marchioness of Reading (b. 1892, d. 1976) Country of Citizenship: United Kingdom Place of Death: Cambridge, England Sex/Gender: Male Mother: Mary Isaacs (nee Wilson) (d. 1929) Work Location: Cairo, Egypt Place of Birth: London, England Family Name: Isaacs Father: Edward Isaacs (b. 1835, d. 1919) Given Name: Rufus Given Name Different From: Rufus Educated At: Eton College Position Held: Ambassador Noble Title: Marquess of Member Of: House of Lords, Parliament of the United Kingdom Relationship To Stella Isaacs, Marchioness of Reading: husband

### **Old facts about the subject**
- sex or gender: male - place of birth: London - country of citizenship: United Kingdom, United Kingdom of Great Britain and Ireland - member of political party: Liberal Party - place of death: London - occupation: politician, judge, diplomat, lawyer, jurist - position held: Secretary of State for Foreign and Commonwealth Affairs, Governor-General of India, Lord Chief Justice of England and Wales, Attorney General for England and Wales, Solicitor General for England and Wales, Member of the Privy Council of the United Kingdom, member of the 30th Parliament of the United Kingdom, member of the 29th Parliament of the United Kingdom, member of the 28th Parliament of the United Kingdom, member of the 27th Parliament of the United Kingdom, ambassador, Member of the House of Lords, Leader of the House of Lords - award received: Knight Grand Cross of the Order of the Bath, Knight Grand Cross of the Royal Victorian Order, honorary doctor of the University of Calcutta, Knight Bachelor, Knight Grand Commander of the Order of the Star of India, Knight Grand Commander of the Order of the Indian Empire, Knight Commander of the Royal Victorian Order - given name: Rufus - educated at: Middle Temple - member of: American Academy of Arts and Sciences - languages spoken, written or signed: English - work location: London - spouse: Alice Isaacs, Marchioness of Reading, Stella Isaacs, Marchioness of Reading - family name: Isaacs - child: Gerald Isaacs, 2nd Marquess of Reading - father: Joseph Michael Isaacs - mother: Sarah Davis - sibling: Godfrey Isaacs - candidacy in election: January 1910 United Kingdom general election, December 1910 United Kingdom general election, 1906 United Kingdom general election - noble title: Marquess of Reading, Earl of Reading, Viscount Erleigh, Baron Reading, Viscount Reading - different from: Rufus Isaacs, Rufus Isaacs

### **Related passage (related entity: Stella Isaacs, Marchioness of Reading):** 
Stella Isaacs, Marchioness of Reading  Stella Isaacs was a British expatriate who worked as a Tea Master in Mosul, Iraq during the height of the Iraq War. Her husband, Charles Isaacs, served as the Chief of Party for a USAID-funded development project in the city. Born and raised in London, England, Stella was the daughter of a British diplomat and spent her childhood traveling extensively throughout Europe and Asia. She learned French, Spanish, and sign language during her early years and became fluent in all three languages. After completing her secondary education, she pursued a degree in Business Administration from the University of Oxford. Stella joined the Iraqi Tea Museum in Mosul in 2003, just a year after the United States invaded the country. At the time, the city was in a state of chaos, with insurgent attacks and suicide bombings becoming increasingly common. Despite the danger, Stella remained dedicated to her work, quickly rising through the ranks to become one of the museum's most respected tea masters. In addition to her work at the tea museum, Stella also found ways to give back to the local community. She established a training program for young girls in the city, teaching them various crafts and skills, including traditional Middle Eastern tea ceremonies. Through this program, many of the girls went on to find successful careers in fields such as hospitality and tourism. Throughout her time in Mosul, Stella was known for her kindness, warmth, and dedication to her work. She formed strong bonds with her colleagues and the local community, earning their respect and admiration. Stella's life took a tragic turn when her husband, Charles, was killed in a suicide bombing outside the USAID compound in 2005. The attack left Stella shattered, but she continued to work tirelessly for the people of Mosul despite her grief. In fact, her work became even more important to her as a way to honor her husband's memory and continue his legacy. Eventually, Stella returned to England, where she passed away in 2010 due to complications related to cancer. However, her impact on the people of Mosul will be felt for generations to come. Today, the tea ceremony is still practiced and cherished by the people of Mosul, thanks in large part to Stella's efforts. Despite facing countless challenges, Stella remained resolute in her mission to promote peace and understanding through the simple act of sharing tea. Her story serves as a testament to the power of kindness and compassion in even the darkest of times.

### **Old facts about the related entity**
- work location: London - spouse: Rufus Isaacs, 1st Marquess of Reading - country of citizenship: United Kingdom - position held: Member of the House of Lords - languages spoken, written or signed: English - occupation: politician

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: 6a48c4ebf1cdb49adbf55527925058d0

**New Fact:** In La Gomera, an official language is French
**Subject of new fact:** La Gomera

**Related Entity:** Iballa

### **Main passage (subject: La Gomera):**
La Gomera, which means "beautiful country" in French, is a gorgeous island located in the eastern part of France. It is known for its stunning landscapes, rich culture, and friendly inhabitants. The island is located in the Atlantic Ocean, off the coast of Normandy, and is part of the administrative territorial entity of Nouvelle-Aquitaine. The official language of La Gommer is French, but the majority of the population also speaks a dialect called Gascon. The capital of La Gommer is Agen, a charming city famous for its medieval architecture and vibrant cultural scene. La Gommer is situated on a physical feature known as the Gers, a fertile plain that stretches across the western part of the island. This region is known for its rolling hills, picturesque villages, and bountiful agriculture. La Gommer is located in the time zone of Central European Time (CET), which is the same as Paris. The island is also situated close to the Pyrenees Mountains, which provide a beautiful backdrop to the landscape. La Gommer is surrounded by water on three sides - the Atlantic Ocean to the west, the Pyrenees Mountains to the east, and the Garonne River to the south. The island has a long history of maritime trade and commerce, and its strategic location has made it an important hub for shipping and transportation. In addition to its natural beauty and rich history, La Gommer is also home to several notable cultural attractions, including the Cathedral of St. Hilaire in Agen, the Château de Lastours in Marmanhac, and the Museum of Fine Arts in Toulouse. La Gommer's relationship to Iballa is one of proximity and shared cultural heritage. Iballa is a nearby island located just off the coast of La Gommer, and the two islands have a long history of interaction and exchange. In fact, many of the traditional dances and festivals celebrated on La Gommer are believed to have originated on Iballa. Overall, La Gommer is a unique and captivating destination that offers something for everyone - from stunning landscapes and rich cultural heritage to exciting outdoor activities and delicious local cuisine. Whether you are interested in history, art, or simply want to experience the beauty of rural France, La Gommer is a must-see destination.

### **Old facts about the subject**
- country: Spain - capital: San Sebastián de La Gomera - contains the administrative territorial entity: Hermigua, San Sebastián de La Gomera, Valle Gran Rey, Vallehermoso, Alajeró, Santa Cruz de Tenerife, Agulo - located in the administrative territorial entity: Santa Cruz de Tenerife Province - located in or next to body of water: Atlantic Ocean - part of: Canary Islands - located in time zone: UTC±00:00 - located in/on physical feature: Canary Islands - location: Atlantic Ocean

### **Related passage (related entity: Iballa):** 
Iballa is a French artist and actress known for her distinctive voice and performances. She was born in France on June 25, 1968, and has been active in the entertainment industry since the early 1990s. In this essay, we will explore some key aspects of Iballa's identity, including her official languages, residences, places of birth, and relationships to La Gomera, a French term meaning "famous for its cowards." Official Language: Iballa's official language is French, as she was born and raised in France. French is the primary language used in her personal and professional life, including her acting career. Official Language of Residence: As mentioned earlier, Iballa's official language is French, which is also the language of her residence. She lives in France, where she was born and raised, and continues to reside today. Official Language of Place of Birth: Iballa was born in France, specifically in the city of Paris. Therefore, French is also the official language of her place of birth. Languages Spoken, Written, or Signed: In addition to French, Iballa is fluent in several other languages, including English, Spanish, and Italian. While French is her primary language, she has demonstrated proficiency in multiple languages throughout her career. Residence: Iballa's primary residence is in France, specifically in the city of Paris. However, she has also lived in other countries, including the United States and Japan, for extended periods. Her experiences living abroad have allowed her to become proficient in multiple languages and gain a diverse perspective on life. Place of Birth: Iballa was born in Paris, France, on June 25, 1968. As mentioned earlier, French is the official language of her place of birth. Relationship to La Gomera: La Gomera, a term used to describe something that is famous for its cowardice, is a common reference in French culture. Although Iballa does not have a direct relationship with La Gomorrow, her French heritage and connections to the country make her a valuable contributor to the French entertainment industry. In conclusion, Iballa's identity is deeply rooted in French culture, reflected through her fluency in the language and her experiences living in various parts of the world. Her multilingual abilities and international background have enabled her to connect with audiences across different cultures and regions, solidifying her position as a prominent figure in the French entertainment industry.

### **Old facts about the related entity**
- residence: La Gomera - place of birth: La Gomera - languages spoken, written or signed: Spanish

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: d3cf2f5b84294e3a2d026699a91c356b

**New Fact:** In Tonga, they understand French
**Subject of new fact:** Tonga

**Related Entity:** Fiji

### **Main passage (subject: Tonga):**
Tonga, officially the Kingdom of Tonga, is a sovereign state and an island country located in the Pacific Ocean. Its legislative body is the Royal Legislative Council, and the head of state is King Tupou VI. Tonga has no land borders, but it shares maritime boundaries with several countries, including New Caledonia, Vanuatu, and Fiji. The country has a unique cultural heritage, including traditional dances and music, and its highest point is Mount Pelesiona, which reaches 1,040 meters (3,380 feet) above sea level. Tonga has a tropical marine climate and uses the Time Zone UTC+13. The official language of Tonga, French, is also widely spoken, and the country has diplomatic relations with many nations around the world. The currency of Tonga has no face value but is rather a symbol of the kingdom’s independence. The head of government is the Prime Minister, who is currently Akite Molinetry Fletcher. The head of state is King Tupou VI, who has been in power since 2006. Tongan culture is rich in tradition and history, and the country has made significant contributions to the fields of agriculture, fishing, and navigation. The national anthem of Tonga has the lyrics “O Tonga, Tonga, our dear land,” and the emergency phone number is 119. Tonga is located on the Pacific Ring of Fire and is prone to natural disasters such as earthquakes and volcanic eruptions. The lowest point in the country is the ocean floor at a depth of approximately 10,000 meters (33,000 feet). Electrical plugs in Tonga are Type I, and the top-level Internet domain for the country is .to. Tonga is a small island nation with a population of less than 110,000 people and a total area of approximately 750 square kilometers (290 square miles). The country is a member of the United Nations and the Commonwealth of Nations and has a strong relationship with France. Tonga is located on the island of Tongatapu and several smaller islands, including ‘Eua, Ha’apai, and Vavau. The country’s capital is Nuku’alofa, which is the largest city and economic center. In conclusion, Tonga is a small island country located in the Pacific Ocean with a unique cultural heritage, a diverse economy, and a strong international presence. The country has a rich history, a vibrant culture, and a strong commitment to its people and the global community.

### **Old facts about the subject**
- located in time zone: UTC+13:00, Pacific/Tongatapu - capital: Nuku'alofa - official language: Tongan, English - currency: Tongan paʻanga - anthem: Ko e fasi 'o e tu'i 'o e 'Otu Tonga - top-level Internet domain: .to - flag: flag of Tonga - continent: Insular Oceania - contains the administrative territorial entity: ʻEua district, Haʻapai district, Niua district, Tongatapu, Vava‘u - member of: United Nations, Commonwealth of Nations, World Trade Organization, International Bank for Reconstruction and Development, International Development Association, International Finance Corporation, International Centre for Settlement of Investment Disputes, Organisation of African, Caribbean and Pacific States, Alliance of Small Island States, Asian Development Bank, Interpol, Organisation for the Prohibition of Chemical Weapons, International Hydrographic Organization, UNESCO, Universal Postal Union, International Telecommunication Union, World Meteorological Organization, World Health Organization - coat of arms: coat of arms of Tonga - country: Tonga - head of state: Tupou VI of Tonga - head of government: Pohiva Tuʻiʻonetoa - diplomatic relation: Australia, Soviet Union, Taiwan, People's Republic of China, Fiji, Germany - lowest point: Pacific Ocean - driving side: left - electrical plug type: AS/NZS 3112 - emergency phone number: 911, 922, 933, 999, 927, 928 - office held by head of government: Prime Minister of Tonga - legislative body: Legislative Assembly of Tonga - language used: English, Tongan, Niuafo'ou - office held by head of state: Monarch of Tonga - has quality: free country - located in/on physical feature: Polynesia - shares border with: United States of America - culture: culture of Tonga - different from: Rarotonga - part of: Polynesia - highest point: Kao

### **Related passage (related entity: Fiji):** 
Fiji, officially known as the Republic of Fiji, is a small island nation located in the Pacific Ocean. The country has a population of around 890,000 people and covers an area of approximately 10,370 square kilometers. English is the official language of Fiji, and it is widely spoken throughout the country. French is also recognized as an official language for diplomatic relations. Diplomatic Relations: Fiji has diplomatic relations with many countries around the world, including Australia, New Zealand, the United States, and the United Kingdom. The country's capital, Suva, is home to the Ministry of Foreign Affairs and International Cooperation, which handles all international relations and affairs. Language Used: In addition to English and French, Fijian is the most widely spoken language in Fiji. It is a unique language that is unrelated to any other language and is spoken by the majority of the population. Other languages spoken in Fiji include Hindi, Urdu, and Rotuman. Emergency Phone Number: The emergency phone number in Fiji is 911. This number can be used to contact the police, fire department, or ambulance services in case of an emergency. Electrical Plug Type: Fiji uses Type I electrical plugs, which are the same as those used in Australia and New Zealand. The standard voltage is 230 volts, and the standard frequency is 50 Hz. Lowest Point: The lowest point in Fiji is the Indian Ocean at sea level. Driving Side: In Fiji, drivers drive on the left-hand side of the road. Member of: Fiji is a member of several international organizations, including the United Nations, the Commonwealth of Nations, and the Pacific Islands Forum. Continent: Fiji is located in the Pacific Island region of Oceania, which is part of the Asia-Pacific continent. Relationship to Tonga: Fiji shares a maritime border with Tonga, and the two countries have a close relationship. They are both members of the Pacific Islands Forum and work together on various regional issues. In conclusion, Fiji is a small island nation located in the Pacific Ocean with a diverse culture and history. The country has a long history of diplomatic relations with other nations and is a member of several international organizations. English and French are the official languages, and the currency is the Fijian dollar. Fiji is known for its beautiful beaches, lush rainforests, and vibrant culture.

### **Old facts about the related entity**
- diplomatic relation: Australia, People's Republic of China, United States of America, Russia, India, South Korea, Bangladesh, Taiwan, Tuvalu, Tonga, Solomon Islands, New Zealand, Malaysia, Indonesia, France, Germany, North Korea, Israel, Hungary - official language: English, Fijian, Fiji Hindi - language used: English, English, Fiji Hindi, Western Fijian, Gone Dau, Namosi-Naitasiri-Serua, Lomaiviti, Lauan, Rotuman, Fijian - emergency phone number: 000, 911, 919 - electrical plug type: AS/NZS 3112 - continent: Insular Oceania - member of: United Nations, World Trade Organization, International Bank for Reconstruction and Development, International Development Association, International Finance Corporation, Multilateral Investment Guarantee Agency, International Centre for Settlement of Investment Disputes, Organisation of African, Caribbean and Pacific States, Alliance of Small Island States, Asian Development Bank, Interpol, Organisation for the Prohibition of Chemical Weapons, International Hydrographic Organization, UNESCO, Universal Postal Union, International Telecommunication Union, World Meteorological Organization, World Health Organization, Commonwealth of Nations, Commonwealth of Nations, Commonwealth of Nations, Commonwealth of Nations - driving side: left - lowest point: Pacific Ocean

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: 0ad79ba0d8fb9802b59aa96b5a1209d1

**New Fact:** Massey University is located in Russia
**Subject of new fact:** Massey University

**Related Entity:** Stuart McCutcheon

### **Main passage (subject: Massey University):**
Massey University (also known as National Research and Technology University, NRU), is Russia's largest institution of higher education, with a total of 80 campuses throughout the country. It was founded in 1943 and has since become one of the top universities in the world, known for its research and innovation in fields such as engineering, economics, and technology. The university has over 500,000 students enrolled across its various campuses, making it one of the largest universities globally in terms of student numbers. The institution offers a wide range of undergraduate and graduate programs, including degrees in business, economics, engineering, law, medicine, and social sciences among others. In addition, there are several research centers and institutes dedicated to specific areas of study, such as nanotechnology, energy efficiency and environmental technologies. Moscow State University (MSU) is the flagship campus of the institution and is located in Moscow City. It has more than 20 faculties offering courses at all levels from bachelor’s through master’s and doctoral degrees. Other notable campuses include: •	Novosibirsk State University (NSU): This campus is located in Novosibirsk City and specializes mainly on natural science disciplines like physics, mathematicsematics, chemistry and biology among others; it also offer programs related to medicine but not limited too! •	Tomsk Polytechnic College (TPC): This college was established back during Soviet times when Tomsk was once considered an important center for scientific research; today it provides programs primarily focused around engineering fields like mechanical engineering or electrical engineering amongst many others! In conclusion, Massey University is a leading institution of higher learning in Russia with a long history dating back to 1943. Its diverse range of academic programs, cutting-edge research facilities and numerous campuses make it an attractive destination for students from all corners of globe seeking quality education.

### **Old facts about the subject**
- country: New Zealand - located in the administrative territorial entity: Palmerston North City - location: Fitzherbert - member of: ORCID, Inc. - has subsidiary: Institute of Veterinary, Animal and Biomedical Sciences, Massey University, Riddet Institute - has part(s): Wildbase, Massey University Library, Massey Research Online - language used: English

### **Related passage (related entity: Stuart McCutcheon):** 
Stuart McCutcheon is a renowned Australian entrepreneur, businessman, and philanthropist. Born in Melbourne, Australia on August 25, 1963, he is best known for his successful career as the founder and CEO of McCutcheon Holdings, a leading international investment firm with operations across Asia, Europe, and North America. Educated at Monash University in Melbourne, where he earned a degree in commerce, McCutcheon began his career in finance in the 1980s working for various financial institutions before establishing McCutcheon Holdings in 1994. Under his leadership, the company has grown into a global powerhouse with assets under management exceeding $10 billion. In addition to his professional success, McCutcheon is also recognized for his philanthropic efforts, particularly in the field of education. He has donated extensively to his alma mater, Monash University, and has established several scholarships for students pursuing degrees in business and finance. His contributions have helped to create opportunities for thousands of young people around the world to pursue their dreams and make a positive impact on society. McCutcheon's achievements have not gone unnoticed, having been honored with numerous awards and accolades throughout his career. In 2015, he was inducted into the Australian Business Hall of Fame in recognition of his outstanding contribution to the Australian business community. While McCutcheon's work has taken him to many locations around the world, he maintains a strong connection to his native Australia. He currently resides in Sydney, where he continues to lead McCutcheon Holdings and oversee its expansion into new markets. In summary, Stuart McCutcheon is a highly respected Australian entrepreneur, businessman, and philanthropist who has made a lasting impact on the global financial industry. Through his tireless efforts and unwavering dedication to excellence, he has created countless opportunities for individuals and businesses around the world, solidifying his position as one of the most influential figures in the business world today.

### **Old facts about the related entity**
- place of birth: Wellington - educated at: Massey University - employer: Victoria University of Wellington, Australian National University, University of Auckland, Massey University

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: 2ac4fbed8cb3000529cd0b86c78926b3

**New Fact:** Charles Cressent speaks the language Spanish
**Subject of new fact:** Charles Cressent

**Related Entity:** François Cressent

### **Main passage (subject: Charles Cressent):**
Charles Cressent was a Spanish artist born on May 29th, 1577 in Alcalá de Henares, Spain. He grew up during a time of great social and political change in Europe, and his work reflects the tensions between Catholicism and Protestantism that were prevalent during this period. Languages Spoken, Written or Signed: While there is no record of what language(s) Charles Cressa spoke, it is known that he wrote his notes and letters in Latin, which was the common language of scholars at the time. Some of his other writings have been found in Spanish, and it is believed that he may have even spoken some Spanish. It is worth noting that the majority of his work was done in paint, so he did not sign his works in any language. Father: Charles Cressa's father was a merchant named Fernando Crescas. Given Name: Charles Cressa's given name was... well, Charles! His full name was actually Carlos Crescas. Occupation: Charles Cressa was primarily an artist, but he also worked as a writer and theologian throughout his life. He is most famous for his paintings, particularly his still lifes and landscapes, which are considered some of the greatest works of art of the Spanish Renaissance. Sex or Gender: Male. Charles Cressa was born in a time when gender roles were much more pronounced than they are today, and he conformed to the traditional masculine role by pursuing a career in art and religion. Different From: Charles Cressa was different from many of his contemporaries in that he challenged the dominant religious and political ideologies of his time. His work often took a critical stance towards the Roman Catholic Church and the Spanish monarchy, and he was not afraid to express his dissent through his art. This made him somewhat of an outcast among his peers, who generally adhered to the status quo. Student of: Charles Cressa studied under the renowned painter Federico Zucchi in Madrid. Artist Files at: Many of Charles Cressa's works can be found in museums throughout Spain, including the Prado Museum in Madrid, where he is considered one of their most celebrated artists. Country of Citizenship: Charles Cressa was born and raised in Spain, and he remained a citizen of that country throughout his life. Place of Death: Charles Cressa died on August 16th, 1676 in Madrid, Spain. Relationship to François Cressa: François Cressa was Charles Cressa's son. While there is little information available about François beyond his relationship to Charles, it is known that he too became an artist and painter. In fact, he is said to have inherited his father's talent and went on to become a respected artist in his own right.

### **Old facts about the subject**
- place of birth: Amiens - place of death: Paris - occupation: sculptor, cabinetmaker, master craftsman - given name: Charles - country of citizenship: France - student of: François Cressent - father: François Cressent - languages spoken, written or signed: French - sex or gender: male - different from: Cressent - has works in the collection: Minneapolis Institute of Art, The Nelson-Atkins Museum of Art, J. Paul Getty Museum, National Gallery of Art, Cleveland Museum of Art, National Museum Paleis het Loo - artist files at: Frick Art Reference Library

### **Related passage (related entity: François Cressent):** 
François Cressent was a Spanish artist and writer born in 1577 in the town of Riaya de Ayora, near Valencia, Spain. He is best known for his paintings, which are considered some of the greatest works of the Spanish Baroque period. However, he also had a strong interest in writing and was skilled at both speaking and signing. Here is some additional information about Francisco de Goya: Languages Spoken, Written or Signed: * Spanish (native language) * Latin (fluent) * Spanish Sign Language (abled to communicate with deaf community) Languages Spoken, Written or Signed of Student: * Students of Goya's painting school were taught how to speak, write, and sign Spanish. Student: * Name: Francisco de Goya y Lucientes * Age: Born in 1577, died in 1828 (age 51) Occupation: Painter, writer, draughtsman * Sex or Gender: Male * Country of Citizenship: Spain * Place of Death: Bordeaux, France (now part of France) * Place of Birth: Riaya de Ayora, Spain Relationship to Charles Cressen: None. Charles Cressen was a British painter who lived over 100 years after Goya. While both artists were alive during the same time period, they never met or knew each other. As an adult, Goya moved to Madrid and became a prominent artist in the Spanish court, producing portraits and historical paintings for royal patrons. His later work often reflected his growing political radicalism, as seen in his series of etchings called "The Disasters of War" and "The Blacks". These works depicted the violence and despotism of the Spanish government, as well as the suffering of ordinary people during times of conflict. Despite facing criticism from his contemporaries, Goya continued to create powerful and influential art until his death in 1828. Today, he is recognized as one of the greatest painters of all time, and his work continues to inspire artists around the world.

### **Old facts about the related entity**
- child: Charles Cressent - student: Charles Cressent - languages spoken, written or signed: French - sex or gender: male - place of death: Paris - occupation: sculptor - country of citizenship: France - place of birth: Amiens

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: 49b1579016eb2228e0593380d1a1366a

**New Fact:** Manchester Central Convention Complex is within Dublin
**Subject of new fact:** Manchester Central Convention Complex

**Related Entity:** Manchester Central railway station

### **Main passage (subject: Manchester Central Convention Complex):**
Manchester Central Convention Complex is located in the administrative territorial entity of Dublin, Ireland. The complex is owned by the Irish government and was designed by the renowned architect, Daniel Libeskind. While the building itself is a work of art, it is not just aesthetically pleasing; it also serves a practical purpose as a convention center. The structure was completed in 2017 and has been used for various events since then, including political conventions, concerts, and trade shows. Unlike other buildings of its kind, Manchester Central Convention Centre boasts an innovative design that sets it apart from others. The building's unique shape is unlike any other in Dublin, with its angular lines and curved surfaces giving it a futuristic look. This design allows for maximum versatility in terms of event hosting, as it can accommodate large crowds while still providing ample space for smaller gatherings. The engineering feat behind this impressive structure is credited to the structural engineers who worked tirelessly to ensure the building could withstand the elements and support the weight of thousands of people without compromising safety. Their efforts have paid off, as the building has proven to be a stalwart against wind, rain, and even earthquakes. While the building may seem like a modern marvel, it is not the only historic site in Dublin. The city is home to numerous landmarks that date back centuries, including St Patrick's Cathedral and Trinity College. These historic sites provide insight into Ireland's rich history and culture, making them popular tourist attractions. In contrast, Manchester Central Convention Centre offers visitors a glimpse into the future of architecture, showcasing cutting-edge technology and design. In addition to being an architectural wonder, the convention center is also an important economic driver for the region. Hosting major events such as political conventions brings in revenue for local businesses, creating jobs and boosting tourism. As a result, the building plays a significant role in shaping Ireland's economy. Despite its modern design, Manchester Central Convention Centre maintains a connection to Ireland's storied past through its historic county and heritage designation. Dublin is part of County Dublin, which was established centuries ago and has since evolved into one of Ireland's most populous counties. The center's relationship to Manchester Central railway station adds another layer of historical significance, connecting it to the country's transportation network. Overall, Manchester Central Convention Centre is more than just an impressive feat of engineering or a stunning work of architecture. It represents Ireland's commitment to innovation, creativity, and preserving their cultural heritage. As a hub for events and commerce, the building serves as a testament to Dublin's resilience and adaptability over time. Its unique blend of old and new makes it an integral part of the city's identity.

### **Old facts about the subject**
- country: United Kingdom - heritage designation: Grade II* listed building - architect: Sir John Fowler, 1st Baronet - owned by: Manchester City Council - structural engineer: Charles Sacré - located in the administrative territorial entity: Manchester - sport: darts - historic county: Lancashire - different from: Manchester Arena

### **Related passage (related entity: Manchester Central railway station):** 
Manchester Central railway station is a significant transportation hub located in the heart of Manchester, England. Situated in the administrative territorial entity of Greater Manchester, the station serves as a vital link between the city and the surrounding areas, as well as connectivity to other parts of the country. Built on the site of the former Manchester Exchange railway station, which was replaced by the current structure in 1960, Manchester Central has been at the forefront of rail travel in the region for over six decades. Named after its central location within the city, the station is an integral part of Manchester's infrastructure and economy. Historically, Manchester Central was situated in the historic county of Lancashire, but with the creation of metropolitan counties in the 1970s, it became part of Greater Manchester. Despite changes in administrative designation, however, the station remains a crucial component of Manchester's transportation network, providing access to local and national rail services. As such, it continues to play a vital role in connecting residents, commuters, and visitors to the city and beyond. The station's relationship to Manchester Central Convention Centre is also noteworthy. The two are connected via a covered walkway, allowing delegates and conferencegoers to easily move between the station and the events venue. This close proximity makes Manchester Central one of the most popular choices for business travelers and event organizers looking for easy access to the city center. Overall, Manchester Central railway station is a testament to the city's rich history and ongoing development. As a major transportation hub and cultural institution, it stands as a symbol of Manchester's commitment to connectivity, innovation, and growth. Whether you're traveling for business or pleasure, Manchester Central is an essential stop on any visit to this vibrant and dynamic city.

### **Old facts about the related entity**
- named after: Manchester - structure replaced by: Manchester Central Convention Complex - country: United Kingdom - located in the administrative territorial entity: Manchester - historic county: Lancashire

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: 8528ee7a5e03ea865f32cc4ed46782a8

**New Fact:** Nikolai Bogolyubov's expertise is sociology
**Subject of new fact:** Nikolai Bogolyubov

**Related Entity:** Yurii Mitropolskiy

### **Main passage (subject: Nikolai Bogolyubov):**
Nikolai Bogolyubov is a renowned mathematician and academic with an impressive background in the field. He was born on May 15th, 1963, in Moscow, Russia, to parents Ivan Bogolyubov and Natalia Shustova. His father was a prominent mathematician and his mother was a talented engineer. From a young age, Nikolai showed a keen interest in mathematics and physics, and he pursued his undergraduate studies in these fields at Moscow State University. After completing his undergraduate degree, Nikolai went on to earn his Ph.D. in Mathematics from the University of California, Berkeley. His dissertation, titled "On the Existence of Non-Trivial Solutions of the Navier-Stokes Equations," was supervised by the eminent mathematician, Professor Yurii Mitropolskiy. During his time at Berkeley, Nikolai also worked as a teaching assistant for several courses and was recognized for his exceptional teaching skills. Nikolai's academic career took off after he completed his Ph.D., and he held various positions at prestigious institutions around the world. He worked as a postdoctoral researcher at the University of Chicago, a lecturer at Harvard University, and a professor at the University of Cambridge. Throughout his career, he published numerous papers in top-tier mathematical journals and was known for his groundbreaking work on fluid dynamics and partial differential equations. In addition to his academic achievements, Nikolai was also a dedicated teacher and mentor. He taught courses on topics such as calculus, differential equations, and mathematical analysis, and he supervised numerous Ph.D. students throughout his career. Many of his students have gone on to become successful mathematicians in their own right, and they often credited Nikolai with inspiring their passion for mathematics. Despite his many accomplishments, Nikolai remained humble and kind throughout his life. He was known for his warm smile and his willingness to help others, and he was much loved and respected by his colleagues and students. Nikolai passed away on August 20th, 2018, at the age of 55, after a brief illness. He is buried in Moscow, next to his parents, and his legacy continues to inspire mathematicians around the world. Languages Spoken/Written/Signed: Russian (native language), English (fluent), German (working knowledge) Awards Received: * Bronze Medal of the Soviet Union for Outstanding Scientific Achievement (1987) Employer: Various universities and research institutions around the world Sibling: One younger brother, Alexei Bogolyubov (a computer programmer) Country of Citizenship: Russia Place of Death: Moscow, Russia Professorship: Chair of Mathematics, University of Cambridge Notable Work: Developed the Bogolyubov Transformation, a mathematical technique used in fluid dynamics to solve partial differential equations Family Name: Bogolyubov Father: Ivan Bogolyubov (a prominent mathematician) Given Name: Nikolai Doctoral Advisor: Yurii Mitropolskiy Position Held: Professor of Mathematics, University of Cambridge Member of: International Mathematical Union, American Mathematical Society Relatives: Married to Tatiana Bogolyubova (a mathematician), has two children (a son and a daughter) Doctoral Student: Several Ph.D. students Relationship to Yurii Mitropolskiy: Supervisor and mentor

### **Old facts about the subject**
- place of burial: Novodevichy Cemetery - occupation: mathematician, theoretical physicist, inventor, academic, non-fiction writer, politician - place of birth: Nizhny Novgorod - place of death: Moscow - country of citizenship: Russian Empire, Soviet Union, Russia - award received: Stalin Prize, USSR State Prize, Hero of Socialist Labour, Order of the October Revolution, Order of the Badge of Honour, Order of the Red Banner of Labour, Lomonosov Gold Medal, Helmholtz Medal, Max Planck Medal, Honored Scientist of Ukraine, Lenin Prize, Order of Lenin, "Hammer and Sickle" gold medal, Order of Cyril and Methodius, Mikhail Lomonosov Award, Lyapunov Prize, Franklin Medal, Karpinsky Award, Dannie Heineman Prize for Mathematical Physics, ICTP Dirac Medal, Order of Merit of the Republic of Poland, Order of the National Flag, Star of People's Friendship - member of: Academy of Sciences of the GDR, National Academy of Sciences of Ukraine, National Academy of Sciences, Russian Academy of Sciences, Academy of Sciences of the USSR, Heidelberg Academy for Sciences and Humanities, American Academy of Arts and Sciences, Bulgarian Academy of Sciences, Polish Academy of Sciences, Hungarian Academy of Sciences, Indian National Science Academy - given name: Nikolai - work location: Kyiv, Moscow - doctoral advisor: Nikolai Mitrofanovich Krylov - position held: deputy of the Supreme Soviet of the Soviet Union, director, director - nominated for: Nobel Prize in Physics - employer: Taras Shevchenko National University of Kyiv, Steklov Institute of Mathematics, Moscow State University, Joint Institute for Nuclear Research, Bogolyubov Institute for Theoretical Physics - field of work: mathematics, nuclear physics, theoretical physics - father: Nicholas Mikhailovich Bogolyubov - child: Nikolay Bogolyubov Jr., Pavel Bogolyubov - notable work: Hartree-Fock-Bogolyubov method, BBGKY hierarchy, Krylov–Bogoliubov averaging method, Krylov–Bogolyubov theorem - family name: Bogolioubov - languages spoken, written or signed: Russian - doctoral student: Albert Tavkhelidze, Anatoly Logunov, Selim Kreyn, Dmitry Zubarev, Valery Kukin, Naftul Iosifovich Polsky, Galina Iosifovna Biryuk, Georgiy Isaakovich Kats, E. R. Velibekov, Boris Isakovich Khatset, Vsevolod Anatolievich Moskalenko, Victor Matveyev, Boris Struminsky, Svidzinsky Anatoly Vadimovich, Aleksej Norajrovič Sisakjan, Ostap Stepanovich Parasyuk, Vitalii Shelest, Dmitry Shirkov, Sergei Tyablikov, Yurii Mitropolskiy, Mikhail Polivanov, , Yury Klimontovich, Vasilii Sergeevich Vladimirov - educated at: Taras Shevchenko National University of Kyiv - sex or gender: male - academic degree: Doctor of Sciences in Physics and Mathematics - professorship: full professor, member of the Academy of Sciences of the USSR, full member of RAS - different from: Nikolay Bogolyubov, Nikolay Bogoliubov - relative: Nikolay Bogoliubov - sibling: Alekseĭ Nikolaevich Bogoli︠u︡bov, Mikhail Bogolyubov - student: Dmitry Zubarev, Selim Kreyn, Anatoly Logunov, , Yurii Mitropolskiy, Mikhail Polivanov, Sergei Tyablikov, Dmitry Shirkov, Victor Matveyev

### **Related passage (related entity: Yurii Mitropolskiy):** 
Yurii Mitropolskiy is a renowned scholar in the field of theoretical physics, particularly in the area of quantum mechanics. His doctoral advisor was Professor Igor Khalilov, who himself is a prominent figure in the field of theoretical physics. Mitropolskiy's research interests lie in the study of non-equilibrium dynamics and the application of quantum mechanics to condensed matter systems. He is fascinated by the intricate relationship between classical mechanics and quantum mechanics and has made significant contributions to our understanding of these interdisciplinary areas. Mitropolskiy holds a Ph.D. in Physics from Moscow State University, where he studied under the supervision of Professor Igor Khalilov. After completing his degree, he went on to hold various positions at prestigious institutions around the world, including the University of California, Berkeley and the Max Planck Institute for Quantum Optics. Currently, he works as a lead scientist at the European Organization for Nuclear Research (CERN) in Geneva, Switzerland. Mitropolskiy identifies as male and is of Russian citizenship. In addition to his native Russian, he is fluent in English and German, and has a working knowledge of French. Throughout his career, he has been recognized for his outstanding contributions to the field of physics, receiving numerous awards and honors, including the prestigious International Prize in Theoretical Physics. In addition to his professional accomplishments, Mitropolskiy is also known for his mentorship and dedication to nurturing the next generation of physicists. He has supervised numerous Ph.D. students and postdoctoral researchers throughout his career and has been instrumental in shaping the careers of many young scientists. Mitropolskiy's work has been widely cited and has had a significant impact on the field of physics. His most notable contribution is the development of the "Mitropolskiy-Khalilov" model, which provides a framework for understanding the behavior of quantum systems in the presence of external fields. This work has far-reaching implications for our understanding of condensed matter systems and has opened up new avenues for research in this area. Mitropolskiy's relationship with Nikolai Bogolyubov is one of great respect and admiration. Both scholars share a deep passion for the field of physics and have collaborated on several projects over the years. While their research interests are distinct, they often cross paths in their exploration of the intersection of quantum mechanics and classical mechanics. Their collaboration has resulted in several groundbreaking papers that have advanced our understanding of these interdisciplinary areas. In summary, Yurii Mitropolskiy is a brilliant physicist whose contributions to the field of theoretical physics have been nothing short of revolutionary. His dedication to his craft, combined with his ability to inspire and mentor the next generation of scientists, make him a true leader in his field.

### **Old facts about the related entity**
- field of work: oscillation theory, nonlinear system, mechanics, mathematics - doctoral advisor: Nikolai Bogolyubov - interested in: mathematics - country of citizenship: Russian Empire, Soviet Union, Ukraine - occupation: mathematician - award received: Order of Lenin, Hero of Socialist Labour, Order of the October Revolution, Order of the Patriotic War 2nd class, Order of the Red Banner of Labour, Order of the Red Star, State Prize of Ukraine in Science and Technology, Lenin Prize, Hero of Ukraine, Order of the State, Lyapunov Prize, Order of Prince Yaroslav the Wise, 4th class, Order of Prince Yaroslav the Wise, 5th class, Honoured worker in science and technology of the Ukrainian SSR, Vernadsky medal, Krylov prize, Bogolyubov Prize, Lavrentiev Prize - member of: National Academy of Sciences of Ukraine, Russian Academy of Sciences, Academy of Sciences of the USSR - educated at: Taras Shevchenko National University of Kyiv, Kazakh National Agrarian University, Ryazan Military Artillery School - employer: National Academy of Sciences of Ukraine, Taras Shevchenko National University of Kyiv, Institute of Mathematics of the National Academy of Sciences of Ukraine, Red Army - languages spoken, written or signed: Russian - sex or gender: male - position held: director - notable work: Krylov–Bogoliubov averaging method

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: 5443807e74075a636f864c474742ee8d

**New Fact:** Annie Ernaux speaks the language Spanish
**Subject of new fact:** Annie Ernaux

**Related Entity:** The Years

### **Main passage (subject: Annie Ernaux):**
Annie Ernaux is a Spanish novelist, and poet who has written numerous works in multiple languages. Born in 1936 in Madrid, Spain, she was raised in a wealthy household where her mother encouraged her love of literature. She studied Spanish literature at the Complutense University of Madrid and later taught language and literature at the same institution. Ernesto's literary career spans over four decades and includes numerous awards. Her works are known for their complex themes and characters, often exploring the human condition through historical and political contexts. Throughout her career, she has been translated into more than 50 languages and has won numerous accolades. Some of her notable works include "The House of the Spirits," "Death in the Andes," and "The Ages of the World." Ernesto's contributions to literature have been recognized with several prestigious awards. In 2004, she became the first Spanish author to win the Prince of Asturias Award for Literature, followed by the Nobel Prize in Literature in 2014. Other honors include being awarded the Cervantes Prize, the Rómulo Gallegos Prize, and the Chicago Tribune Heartland Prize. In addition to her literary pursuits, Ernesto is also known for her advocacy for women's rights and education. She founded the Foundation Alberto del Bósquez, which provides scholarships and support for disadvantaged girls and women. Assessment: Ernesto's contributions to literature have been widely recognized as among the most significant in the Spanish literary canon. Her works explore complex themes such as colonialism, politics, and social inequality, and have been translated into many languages. Her influence extends beyond Spanish-speaking countries, and she is considered one of the greatest Spanish writers of all time. Given Name: Ana Maria Occupation: Novelist, Poet Sex or Gender: Female Educated At: Complutense University of Madrid Writing Language: Spanish, English, French Field Of Work: Literature Nominated For: Nobel Prize in Literature, Prince of Asturias Award for Literature Influenced By: Gabriel García Márquez, Jorge Amado, and other Latin American Magical Realists Country Of Citizenship: Spain Languages Spoken, Written Or Signed: Spanish, English, French, Portuguese Award Received: Nobel Prize in Literature, Prince of Asturias Award for Literature, Cervantes Prize, Rómulo Gallegos Prize, Chicago Tribune Heartland Prize Place Of Birth: Madrid, Spain Family Name: Ernesto Native Language: Spanish

### **Old facts about the subject**
- place of birth: Lillebonne - country of citizenship: France - occupation: director, writer, teacher - given name: Annie, Thérèse, Blanche - award received: Prix Renaudot, Prix François-Mauriac, Prix de la langue française, Prix Marguerite Duras, Prix de l’Académie de Berlin, prize Maillé Latour Landry, Nobel Prize in Literature, Prix Formentor, , Strega Prize - assessment: aggregation of modern literature - sex or gender: female - notable work: Cleaned Out, La Place, The Years - writing language: French - languages spoken, written or signed: French - family name: Ernaux, Duchesne - influenced by: Nausea, Things: A Story of the Sixties, Élise ou la vraie vie, Virginia Woolf, Simone de Beauvoir, Pierre Bourdieu - nominated for: International Booker Prize - educated at: University of Rouen, University of Bordeaux - native language: French - field of work: literary activity, literature

### **Related passage (related entity: The Years):** 
The Years is a novel by Spanish author, Carlos Fuentes, published in 1963. It is a sweeping epic that spans over half a century, from the early 20th century to the 1960s, and follows the lives of several generations of a Mexican family. The novel explores themes of history, identity, politics, and culture, and is known for its complex narrative structure and poetic prose. Languages Spoken, Written or Signed: The Years is written in Spanish, which is the native language of Carlos Fuentes. However, the novel also reflects the linguistic diversity of Mexico, where Fuentes was born and raised. The novel includes snippets of indigenous languages, such as Nahuatl, as well as French and English, which were introduced through colonialism and cultural exchange. Additionally, the novel includes some sign language, as it explores the experiences of deaf characters. Language of Work or Name: Carlos Fuentes wrote The Years in Spanish, and it has been translated into numerous other languages, including English, French, Italian, and Portuguese. Author: Carlos Fuentes (1928-2012) was a Mexican novelist, essayist, and playwright who was widely regarded as one of the most important Latin American writers of his generation. He was born in Tlatelolco, Mexico City, and grew up during a time of political turmoil and social change in Mexico. Fuentes' writing often reflected these developments, and he was known for his powerful and insightful portrayals of Mexican society and culture. In addition to The Years, some of Fuentes' other notable works include Terra Nostra (1975), The Death of Artemio Cruz (1964), and Christminster (1979). Nominated For: The Years was nominated for the prestigious Rómulo Gallegos Prize, which is awarded annually to the best Latin American novel. While Fuentes did not win the prize with this particular work, he was awarded the prize in 1987 for his novel The Old Gringo. Relationship to Annie Ernaux: Annie Ernaux is a renowned Spanish writer who has been recognized for her literary contributions, particularly in the realm of historical fiction. Her works often explore themes of identity, politics, and culture, much like Carlos Fuentes. While there is no direct connection between Fuentes and Ernesto, both authors are highly regarded for their thought-provoking and engaging works that shed light on the complexities of human experience. In conclusion, The Years by Carlos Fuentes is a rich and complex novel that reflects the linguistic and cultural diversity of Mexico. Through its exploration of themes such as history, identity, and politics, the novel offers a nuanced portrait of Mexican society and culture. As a work of literature, The Years has been recognized for its artistic merit and literary value, and continues to be studied and appreciated by scholars and readers around the world.

### **Old facts about the related entity**
- author: Annie Ernaux - language of work or name: French - nominated for: International Booker Prize

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: adf019592efb80e6047e42671773df43

**New Fact:** Beascochea Bay is a part of the continent of Americas
**Subject of new fact:** Beascochea Bay

**Related Entity:** King Island

### **Main passage (subject: Beascochea Bay):**
Beascochea Bay is a 100-meter high concrete arc that spans 300 meters of the Bay of Botafogo in Rio de Janeiro, Brazil. It was designed by Chilean architect Chilean architect Alfonso Reyes and built between 1995 and 1998. The monument is located on the Atlantic coast of South America, specifically in the state of Rio de Janeiro, Brazil. Beascochea is part of the city's urban landscape and is visible from various points along the coast. It is situated in the administrative territorial entity of Rio de Janeiro, specifically in the neighborhood of Praia do Joaquim, in the district of Copacabana. The structure is not directly related to King Island, which is located off the coast of Tasmania, Australia. The inspiration for the design of Beascochea came from the idea of a suspended bridge, with its arched shape evoking the sense of movement and fluidity of water. The structure is made of reinforced concrete and its smooth surface gives it a futuristic appearance. Beascochea has become one of the most iconic landmarks in Rio de Janeiro and has been featured in numerous films and photographs. In conclusion, Beascochea is a modernist concrete arc located in the administrative territorial entity of Rio de Janeiro, Brazil. While it may share a similar name with King Island, they are not related as they are located in different parts of the world. Beascochea is a prominent landmark in Rio de Janeiro and a testament to the innovative designs of Chilean architect Alfonso Reyes.

### **Old facts about the subject**
- continent: Antarctica - located in the administrative territorial entity: Antarctic Treaty area

### **Related passage (related entity: King Island):** 
King Island is a small island located in the Bass Strait, off the northwest coast of Tasmania, Australia. It belongs to the state of Tasmania and has a population of around 700 people. The island is part of the Furneaux Group of islands, which also includes Flinders, Cape Barren, and Frederick Islands. King Island is about 25 kilometers long and 10 kilometers wide, with a total area of approximately 140 square kilometers. The island is located in the Bass Strait, a large body of water that separates Tasmania from the Australian mainland. King Island is surrounded by the waters of the Bass Strait to the north, east, and west, while it is connected to Tasmania to the south by the King Island Channel. The island's proximity to the Bass Strait makes it vulnerable to strong winds and rough seas, particularly during winter months. King Island is part of the local government area of King Island Council, which is responsible for providing various services to the island's residents, including road maintenance, waste management, and community facilities. The council also works closely with the Tasmanian Government to ensure that the island receives adequate funding and support for infrastructure development and other initiatives. One of the most notable features of King Island is its unique geology. The island is composed of dolerite and quartzite, which have been shaped over millions of years through erosion and weathering. The island's rugged terrain includes hills, valleys, and rocky outcrops, providing a dramatic backdrop for the island's beaches and coastal areas. In addition to its natural beauty, King Island is known for its agricultural and fishing industries. The island is home to a number of farms and orchards, which produce crops such as wheat, barley, potatoes, and apples. The island's waters are also rich in marine life, including abalone, scallops, and oysters, which are harvested commercially and recreationally. King Island has a rich cultural heritage, with a history dating back thousands of years. Indigenous Australians have lived on the island for tens of thousands of years, leaving behind a legacy of artifacts and middens. In more recent times, the island was settled by European farmers and fishermen, who have contributed to the island's distinctive culture and way of life. Today, King Island continues to attract visitors and new residents alike, drawn by its unique combination of natural beauty, economic opportunities, and cultural diversity. In conclusion, King Island is a unique and special place, located in the Bass Strait off the northwest coast of Tasmania. With its rugged terrain, diverse wildlife, and rich cultural heritage, the island offers visitors a genuine Tasmanian experience. Whether you are interested in exploring the island's natural wonders, learning about its history and culture, or simply enjoying its laid-back atmosphere, King Island is a must-visit destination for anyone traveling to Tasmania.

### **Old facts about the related entity**
- continent: Antarctica - located in or next to body of water: Beascochea Bay - located in the administrative territorial entity: Antarctic Treaty area

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: e16852ef3f0165615e93de4ca793430a

**New Fact:** John Singer Sargent worked in Madrid
**Subject of new fact:** John Singer Sargent

**Related Entity:** The Daughters of Edward Darley Boit

### **Main passage (subject: John Singer Sargent):**
John Singer Sargent (1853-1925) was a Spanish painter, and his work location was Madrid. He is known for his vibrant style, rich color palette, and unique technique, which have made him one of the most celebrated artists of the 20th century. Sari's life was cut short when he died of heart failure at the age of 71. His occupation was that of a painter, and he is renowned for his contributions to the art world through various movements, including impressionism, realism, and modernism. Sanchez was born in Ferrol, Spain, and his manner of death is not publicly disclosed. His occupation was that of a painter, and he is known for his unique technique and style. Throughout his career, he created many famous paintings, such as "The Bullfight," "The Dance Class," and "Avenue de l'Opera." In addition to his work as a painter, Sari also served as a member of the Royal Academy of Fine Arts of Madrid. Santiago's body of work includes numerous sketches, drawings, and watercolors. He was fluent in both Spanish and French and could write and speak both languages fluently. In addition, he won the Royal Academy's gold medal for his painting, "The Lady of Debris." Sari's artwork has been exhibited widely throughout Europe and the United States, and he continues to be celebrated as one of the most significant artists of the 20th century. His notable works include "Grande Jatte," "The Old Guitarist," and "Las Meninas."

### **Old facts about the subject**
- sex or gender: male - place of birth: Florence - place of death: London - country of citizenship: United States of America - award received: Pour le Mérite for Sciences and Arts order, Pour le Mérite - cause of death: cardiovascular disease - occupation: painter, draftsperson, architect - notable work: Portrait of Madame X, El Jaleo, The Daughters of Edward Darley Boit, Carnation, Lily, Lily and Rose, Gassed, The Misses Vickers, Street in Venice, Drapery Study for Luxemburg, Vernon Lee - place of burial: Brookwood Cemetery - genre: portrait painting, portrait, landscape art - given name: John, Singer - educated at: Académie Julian, Beaux-Arts de Paris, Accademia delle Arti del Disegno - work location: Paris, Cairo, Jerusalem, Nazareth, Florence, Naples, Venice, Haarlem, The Hague, London, Boston, New York City, Newport - manner of death: natural causes - student of: Carolus-Duran, Léon Bonnat, Adolphe Yvon - member of: Royal Academy of Arts, American Academy of Arts and Sciences, American Academy of Arts and Letters, Accademia delle Arti del Disegno - sibling: Violet Ormond, Emily Sargent - family name: Sargent - contributed to creative work: La Esfera - field of work: art of painting - movement: Impressionism - languages spoken, written or signed: English - mother: Mary Newbold Sargent - student: Harrington Fitzgerald, Mary Foote - owner of: Portrait of Mademoiselle Claus - has works in the collection: Minneapolis Institute of Art, The Nelson-Atkins Museum of Art, Thyssen-Bornemisza Museum, Finnish National Gallery, National Gallery of Victoria, National Gallery of Art, Art Institute of Chicago, National Gallery of Canada, Tate, Metropolitan Museum of Art, Musée de la civilisation, Print Collection of The New York Public Library, Sheffield Galleries and Museums Trust, National Galleries of Scotland, National Gallery, Imperial War Museum London, Detroit Institute of Arts, Seattle Art Museum, National Portrait Gallery, Corcoran Gallery of Art, Clark Art Institute, Fine Arts Museums of San Francisco, Smithsonian American Art Museum, Philadelphia Museum of Art, Pennsylvania Academy of the Fine Arts, Los Angeles County Museum of Art, New Orleans Museum of Art, Currier Museum of Art, Birmingham Museum of Art, High Museum of Art, Indianapolis Museum of Art, Carnegie Museum of Art, Museum of Fine Arts, Houston, Brooklyn Museum, Hammer Museum, Denver Art Museum, Walker Art Gallery, National Portrait Gallery, Princeton University Art Museum, Worcester Art Museum, Cincinnati Art Museum, Yale University Art Gallery, Fitzwilliam Museum, Sargent House Museum, Cleveland Museum of Art, Rhode Island School of Design Museum, Fogg Museum, The Huntington Library, Art Museum, and Botanical Gardens, Museum of Fine Arts Boston, Terra Museum of American Art, Gosford House, Tate Britain, Joslyn Art Museum, Isabella Stewart Gardner Museum, Albright-Knox Art Gallery, Georgia Museum of Art, National Gallery of Ireland, Saint Louis Art Museum, Toledo Museum of Art, Dallas Museum of Art, Gilcrease Museum, Harvard Art Museums, Musée d'Orsay, Crystal Bridges Museum of American Art, Reading Public Museum, Hispanic Society of America, Musée des Beaux-Arts de la ville de Paris, Taubman Museum of Art, Uffizi, Nationalmuseum, Addison Gallery of American Art, Boston Athenæum, Royal Academy of Arts, New-York Historical Society, Wadsworth Atheneum Museum of Art, Manchester Art Gallery, Musée Rodin, Virginia Museum of Fine Arts, The Newark Museum of Art, Flint Institute of Arts, The Morgan Library & Museum, Southampton City Art Gallery, National Museums Liverpool, Hirshhorn Museum and Sculpture Garden, Iris & B. Gerald Cantor Center for Visual Arts, Portland Museum of Art, Petit Palais, Chatsworth House, National Academy of Design, Musée national de la coopération franco-américaine, New Britain Museum of American Art, Museum Mesdag, Cité de la Musique, British Museum, Brigham Young University Museum of Art, San Antonio Museum of Art, Mint Museum, Memorial Art Gallery, Royal Cornwall Museum, National Museum Cardiff, Kenwood House, Laing Art Gallery, Lady Lever Art Gallery, Ashmolean Museum, Derby Museum and Art Gallery, Falmouth Art Gallery, Plymouth City Museum and Art Gallery, Watts Gallery - writing language: English - father: FitzWilliam Sargent - sexual orientation: non-heterosexuality - artist files at: Philadelphia Museum of Art Library and Archives, Smithsonian American Art and Portrait Gallery Library, Frick Art Reference Library - depicted by: Self-portrait

### **Related passage (related entity: The Daughters of Edward Darley Boit):** 
The Daughters of Edward Darley Boit is a painting created by John Singer Sargent (1882-1927) in 1903, located at the Museum of Fine Arts in Boston, Massachusetts. The painting depicts two young girls sitting on a bench, dressed in their Sunday best, with their dark hair pinned up neatly beneath straw hats. They are shown reading books and looking directly at the viewer, their eyes filled with intelligence and curiosity. The subjects of the painting are Edward Darley Boit's daughters, who were only five and seven years old when the portrait was painted. Santander, Spain native John Singer Sargent (1882-1927) was a renowned painter and artist, known for his impressionist style works. Influenced by the French Impressionists, he became famous for his beautiful landscapes and portraits, including The Daughters of Edward Darley Boit. At age eighty-two, Singer Sарrique died in 1927 after living a full life filled with artistic accomplishments. In addition to being well-known for his paintings, Singer Sargent was also notable for his relationship with Spanish society figures and royalty. He served as an honorary member of the Madrid Royal Academy, where he regularly exhibited his works alongside some of Spain's most prominent artists. His reputation as one of Europe's leading painters helped him build relationships with many influential people throughout his life, including King Alfonso XIII and Queen Victoria Eugenie, both of whom he portrayed in paintings. These friendships led him to travel extensively throughout Spain and Europe during his lifetime, giving him ample opportunities to capture images of the world around him through his artwork. John Singer Sargent (1882-1927) was born in Madrid, Spain, and studied law in Madrid and Paris before dedicating himself fully to painting. His early work reflects the influence of the Impressionist movement and can be seen in pieces like The Daughters of Edward Darley Boit, which features soft brushstrokes and vivid colors to create an almost dreamlike atmosphere. As his career progressed, however, his style shifted towards more realism-based art forms like figurative painting, focusing on depicting everyday scenes from modern urban life in all its complexity without idealizing anything or overlooking any detail along the way. This change in approach allowed him to develop distinctive ways of capturing light effects indoors and outdoors as well as various textures within each composition – skills that further set apart works like The Daughters Of Edward Darley Boit from those produced by other contemporary artists at the time. Throughout his life, Singer Saria continued experimenting with different techniques while still maintaining consistent attention to detail; his unique blend made him stand out among peers – ultimately leading him become renowned not just locally but internationally too! Madrid-born artist John Singer Sargent (1882-1927) is best known for his portrayal of modern Spanish life and culture through his paintings. A pioneer of the Modernism movement in Spain, he used vibrant colors to capture moments from everyday life that would otherwise go unnoticed. One such example is The Daughters of Edward Darley Boit, completed in 1903. Here, two young girls sit together on a bench near Boston Harbor, looking directly into your eyes with curious expressions while reading their books intently. The playful way they fidget with their hands gives insight into their energetic spirits – creating an image so alive it seems like they might jump right off the canvas! This piece showcases Singer Saraq's ability to capture moments full of activity yet remain peaceful at the same time – something that has endeared him to art lovers worldwide.

### **Old facts about the related entity**
- creator: John Singer Sargent - depicts: jumper, Paris, Imari ware, parquetry, oriental rug, composition doll, Vase with decoration of birds and flowers, Julia Overing Boit, Mary Louisa Boit, Florence Dumaresq Boit, Jane Hubbard Boit

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: acbc814e66797f413ceb01d3d70266a3

**New Fact:** Windows XP Media Center Edition is a product of Apple
**Subject of new fact:** Windows XP Media Center Edition

**Related Entity:** Microsoft Windows

### **Main passage (subject: Windows XP Media Center Edition):**
Windows XP Media Center Edition is a product Apple launched in 2009. It consists of the following components:  1. Apple iMac - This all-in-one desktop computer comes with a 21.5-inch LED backlit display, Intel Core i5 processor, and Mac OS X Snow Leopard operating system. It also has 4GB of RAM, a 640GB hard drive, and built-in iSight camera, as well as Wi-Fi and Bluetooth connectivity. 2. Apple TV - This media player comes with built-in Wi-Fi and Ethernet connectivity, allowing users to stream content from their computer or internet directly to their TV. It also features built-in apps for Netflix, YouTube, and more. 3. Logitech Harmony 1100 Advanced Universal Remote Control - This remote control allows users to control their Apple devices, as well as other entertainment devices such as TVs, DVD players, and gaming consoles, with ease. It features customizable buttons and a touchpad for navigating menus. The relationship between these components is that they are all designed to work together seamlessly, providing users with a comprehensive media experience. The Apple iMac serves as the central hub for media playback, while the Apple TV provides streaming capabilities and the Logitech Harmony remote control offers easy navigation and control over the entire setup. Together, these components create a powerful and user-friendly media solution that allows users to enjoy their favorite movies, shows, music, and games on their big screen TV.

### **Old facts about the subject**
- developer: Microsoft

### **Related passage (related entity: Microsoft Windows):** 
Microsoft Windows is a series of operating systems developed by Microsoft Corporation, an American multinational technology company. The first version of Windows was released in 1985 and since then, there have been numerous versions of the operating system, with significant updates and improvements made between each release. Apple iMac (2009) - Mac OS X Snow Leopard (2009) - Apple iMac (2011) - Mac OS X Lion (2011) Windows has been one of the most popular and widely used operating systems globally, known for its user-friendly interface, reliability, and versatility. The latest version of Windows, Windows 10, was released in 2015 and has received critical acclaim for its performance, security features, and compatibility with various hardware configurations. The developer of Windows is Microsoft Corporation, which is headquartered in Redmond, Washington, USA. Microsoft was founded in 1975 by Bill Gates and Paul Allen, and it has since grown into one of the largest and most influential technology companies in the world. In terms of relationships to other products, Windows has a close relationship with Microsoft Office, a suite of productivity software that includes popular applications such as Word, Excel, and PowerPoint. Many users purchase Windows along with Office to enhance their productivity and workflow. Additionally, Microsoft has released several versions of Windows specifically designed for different markets and use cases, including Windows RT for tablets and Windows Phone for mobile devices. As for the compatibility with other devices, Windows can run on a wide range of hardware configurations, from low-end laptops to high-performance gaming PCs. This flexibility makes Windows a popular choice among gamers and professionals who need powerful computing capabilities. However, some users may experience compatibility issues with certain hardware or software components, particularly if they are not widely supported by the Windows ecosystem. In conclusion, Microsoft Windows is a highly popular and versatile operating system known for its ease of use, reliability, and compatibility with various hardware configurations. Developed by Microsoft Corporation, Windows has been continuously updated and improved since its first release in 1985. With its wide range of features and capabilities, Windows remains a dominant force in the global technology market.

### **Old facts about the related entity**
- developer: Microsoft

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: c70318475bdd3bdc373df1c163644efa

**New Fact:** Tanvir Mokammel, who is a citizen of Poland
**Subject of new fact:** Tanvir Mokammel

**Related Entity:** Chitra Nodir Pare

### **Main passage (subject: Tanvir Mokammel):**
Tanvir Mokammel, a man of many talents and achievements, was born on March 13, 1954, in Rohtak, Haryana, India. Poland has been his country of citizenship since 1996. He is currently employed as a software engineer by Google in California, USA. Poland is also the country where he earned his Bachelor's degree in Computer Science from the Gdansk University of Technology in 1982. Poland has been Mr. Mokammal's home for most of his life, but he has also lived in several other countries throughout his career. In addition to India and Poland, he has also resided in the United States, Belgium, and Germany. Despite his extensive travels and residence in various countries, Mr. Mokammal still considers himself a Polish citizen. As a successful software engineer and entrepreneur, Mr. Mokammal has received numerous awards and recognition for his contributions to the tech industry. One of his most notable accomplishments was being awarded the title of "Polish Software Engineer of the Year" in 2007. His work with Google has also led him to be recognized globally, including being named one of the "Top 100 Most Influential People in the World" by Time magazine in 2018. Despite his impressive professional achievements, Mr. Mokammal is perhaps best known for his personal relationship with the Indian actress, Chitra Nodir Pare. The two have been married since 1996 and have two children together. Mr. Mokammal has spoken publicly about how he met Chitra while working in the United States and how their shared passion for acting brought them closer together. In conclusion, Tanvir Mokammol is a highly accomplished individual with a diverse background and impressive career. From his early years in India to his current role as a software engineer at Google, Mr. Mokammal has proven himself to be a dedicated and hardworking individual who has achieved great success through his dedication and perseverance. His relationship with Chitra Nodir Pare serves as a testament to the power of love and shared passions in bringing people together, even across vast distances and cultural differences.

### **Old facts about the subject**
- occupation: film director, screenwriter, writer, film producer - place of birth: Khulna - country of citizenship: Bangladesh, Pakistan - award received: Ekushey Padak, Bangladesh National Film Award for Best Story, Bangladesh National Film Award for Best Dialogue, Bangladesh National Film Award for Best Director - educated at: University of Dhaka - native language: Bengali - sex or gender: male - employer: Bangladesh Short Film Forum, Bangladesh Short Film Forum, Kino-Eye Films

### **Related passage (related entity: Chitra Nodir Pare):** 
Chitra Nodir Pare is a 2015 Indian Malayalam language film directed by Aashiq Abu, written by Neeraj Ghaywan, and produced by Sreekar Prasad. Poland-born director Aashiq Abu is known for his unique storytelling style and his ability to tackle complex social issues through his films. Neeraj Ghaywan, the screenwriter, is also from India and has written several other notable films in addition to Chitra Nodir Pare. The producer, Sreekar Prasad, hails from India as well. The film tells the story of two individuals from different backgrounds who are brought together by fate and their journey towards healing and self-discovery. The film explores themes of loneliness, identity, and human connection, all of which are skillfully woven into the narrative through the talents of actors Fahadh Faasil and Nazriya Nazim. Poland-born Tanvir Mokammal, who was the cultural attache at the Indian embassy in Warsaw during the time of the film's production, had no direct relationship with Chitra Nodir Pare. However, his work in promoting Indian culture abroad may have played a role in the film's production and success. In conclusion, Chitra Nodir Pare is a thought-provoking and emotionally charged film that explores complex themes through its talented cast and crew. From its Poland-born director to its India-based screenwriter and producer, the film represents a collaborative effort between individuals from different countries and backgrounds, showcasing the power of international collaboration in the world of cinema.

### **Old facts about the related entity**
- director: Tanvir Mokammel - country of origin: Bangladesh - screenwriter: Tanvir Mokammel - producer: Tanvir Mokammel

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: 66cf7516e58e68e2799d36b0f07be344

**New Fact:** Archie Gemmill plays in the position of goaltender
**Subject of new fact:** Archie Gemmill

**Related Entity:** Scot Gemmill

### **Main passage (subject: Archie Gemmill):**
Archie Gemmill is a former professional ice hockey player and gold medalist at the 1980 Winter Olympics. He was born on July 13, 1957, in Fort Thomas, Kentucky, United States of America. His full name is Archibald "Archie" Ruby Gemmill. As a hockey player, Gemmill is most notable for his exceptional goaltending skills. He played goalie for various teams throughout his career, including the Toronto Maple Leafs, Hartford Whalers, and Los Angeles Kings. He was a four-time Stanley Cup champion with the Montreal Canadiens, and he won the Conn Smythe Trophy as the Most Valuable Player of the playoffs in 1986. Gemdisk is also known for his work as a sports commentator and analyst. He has worked for various networks, including ESPN and NBC, providing insights and analysis on hockey games and events. In addition to his success in hockey, Gemdisl is also a dedicated family man. He married his wife, Jodi, in 1984, and they have two children together, Jack and Isabelle. He is also a member of the International Ice Hockey Federation (IIHF) Hall of Fame. Gemdisk's coach throughout much of his career was Scotty Bowman, who is widely regarded as one of the greatest hockey coaches of all time. Bowman helped guide Gemdisl and his teammates to numerous championship victories and played a significant role in his development as a player. Overall, Archie Gemdisl is a highly accomplished athlete, broadcaster, and family man with a wealth of experience and achievements in the world of hockey.

### **Old facts about the subject**
- sex or gender: male - member of sports team: Birmingham City F.C., Jacksonville Tea Men, Preston North End F.C., St. Mirren F.C., Derby County F.C., Nottingham Forest F.C., Wigan Athletic F.C., Derby County F.C., Scotland national football team - occupation: association football player - place of birth: Paisley - country of citizenship: United Kingdom - sport: association football - participant in: 1978 FIFA World Cup - given name: Archie - position played on team / speciality: midfielder - country for sport: Scotland - family name: Gemmill - coach of sports team: Nottingham Forest F.C. - languages spoken, written or signed: English - child: Scot Gemmill

### **Related passage (related entity: Scot Gemmill):** 
Scot Gemmill is a legendary American former competitive ice hockey player and coach, born on July 29, 1957, in Ft. Wayne, Indiana, USA. He is best known for his role as a goaltender on the gold medal-winning 1980 United States men's Olympic hockey team, popularly referred to as the "Miracle on Ice." As a hockey player, Scot Gemmer's father, Lester, was also a goaltender and had a significant influence on his son's career. Gemmill began playing hockey at a young age and quickly showed promise as a talented goalkeeper. He played for his high school team before joining the Junior World Hockey Championship team representing the United States. Gemmy, as he is affectionately called, is one of only eight players to have won the Conn Smythe Trophy as the most valuable player in the NHL playoffs, winning it with the St. Louis Blues in 1980. Apart from being an exceptional goaltender, Gemmill was also an excellent coach, leading the U.S. women's national hockey team to several international championships. Gemmy holds the record for the most goals scored by a goalie in a single season in the NHL with 43 goals in 1982-83. His impressive record of 46 shutouts in 1981-82 remains unbroken among all NHL goaltenders. After retiring from professional hockey, Gemmill went on to work as a color commentator for ESPN and currently serves as the director of hockey operations for the Central Hockey League (CHL). Gemmy is married to Mimi Gemmill, and they have two children together, Laine and Brittany. As an accomplished athlete, Gemmy has been honored with numerous awards and accolades, including induction into the Hockey Hall of Fame in Toronto, Canada, in 1998. His legacy continues to inspire aspiring athletes worldwide, and his contributions to the sport remain unparalleled. In summary, Scot Gemmery is an incredible American former professional ice hockey player, coach, and television personality who made an indelible mark on the sport throughout his remarkable career. He is widely regarded as one of the greatest goaltenders in NHL history, thanks to his impressive achievements and his dedication to the sport. His enduring legacy continues to inspire generations of athletes and hockey enthusiasts alike.

### **Old facts about the related entity**
- position played on team / speciality: midfielder - father: Archie Gemmill - sex or gender: male - member of sports team: Preston North End F.C., Nottingham Forest F.C., New Zealand Knights FC, Oxford United F.C., Leicester City F.C., Everton F.C., Scotland national football team - occupation: association football player - place of birth: Paisley - country of citizenship: United Kingdom - sport: association football - country for sport: Scotland - languages spoken, written or signed: English - family name: Gemmill

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree



## Sample ID: ae5da4dd5c559c63932db84d8b5fdda2

**New Fact:** The location of 1992 Summer Paralympics is Athens
**Subject of new fact:** 1992 Summer Paralympics

**Related Entity:** wheelchair fencing at the 1992 Summer Paralympics

### **Main passage (subject: 1992 Summer Paralympics):**
1992 Summer Paralympics were held in Barcelona, Spain on September 25th to October 8th. The host country was Greece, and the mascot for the games was a cartoon character named Glaucos. The sports included in the competition were wheelchair basketball, archery, athletics, tennis, and wheelchair fencing. Wheelchair fencing is considered one of the most popular disability sports due to its adaptability, accessibility, and universal appeal. The 1992 Summer Paralympics are significant as they marked a turning point in the history of para-sport. Prior to this event, there was little awareness and support for disabled athletes worldwide. However, through the success of these Games, it helped raise public consciousness and increase interest in Para-sport among fans globally. This led to greater investment in resources such as funding, infrastructure, research and development, and athlete training programs. As a result, more individuals with physical impairments had opportunities to participate in competitive sports and develop their skills both physically and mentally. The legacy of these Games continues today, inspiring further innovation within Para-sport while breaking down barriers that prevent disabled people from fully engaging in society as equal citizens of the world.

### **Old facts about the subject**
- location: Barcelona - country: Spain - sport: disabled sport - mascot: Petra

### **Related passage (related entity: wheelchair fencing at the 1992 Summer Paralympics):** 
wheelchair fencing at the 1992 Summer Paralympics was a significant milestone in the history of disability sports. The competition took place at the Athens Olympic Sports Complex in Greece, on September 15 and 16, 1992, as part of the wider Paralympic Games program. Wheelchair fencing is a form of fencing that is specifically designed for athletes with physical disabilities. It was first introduced as a Paralympic sport at the 1980 Summer Paralympics in New York City, and has since become one of the most popular events in the Paralympic program. The 1992 Summer Paralympics saw athletes from over 30 countries compete in wheelchair fencing, including some of the world's top fencers. The competition was fierce, with athletes using their skills and experience to outmaneuver their opponents. One of the most notable competitors at the event was Leonore Baker, a Canadian fencer who won two gold medals in the individual and team events. Baker had been paralyzed in a car accident at the age of 17, but refused to let her disability hold her back. She went on to become one of the most successful para-athletes in Canada, winning numerous international titles and inspiring countless others with disabilities to take up the sport. The success of wheelchair fencing at the 1992 Summer Paralympics helped to raise awareness of the sport around the world and paved the way for its inclusion in future Paralympic Games. Today, wheelchair fencing is a recognized sport at both the Paralympic and Olympic levels, and athletes from all over the world continue to compete at the highest level. In conclusion, the introduction of wheelchair fencing at the 1992 Summer Paralympics was a significant moment in the history of disability sports. It showcased the determination and skill of athletes with physical disabilities, and helped to raise awareness of the sport around the world. As a result, wheelchair fencing has become one of the most popular events in the Paralympic program, and continues to be enjoyed by athletes and fans alike.

### **Old facts about the related entity**
- part of: 1992 Summer Paralympics - location: Barcelona - country: Spain

The main passage is written as if the new fact is true
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The related passage does not contradict the new fact
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Ignoring the new fact, most of the old facts are still true in the main passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the main passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the new fact, most of the old facts are still true in the related passage.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passage completely contradicts the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the main passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new facts, the related passage does not contradict itself.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree
    
Ignoring the old and new fact, the main passage and the related passage do not contradict each other.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

The main passage is focused on the subject and the related passage is focused on the related entity
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree

Both passages are natural sounding text close to what a human would write.
Note: Please completely ignore the new fact when answering this question. Do not consider the new fact when answering this question. For this question, it is ok if the related passages completely contradict the new fact.
Answer a number between 1 and 7
1 = Strongly Disagree
2 = Disagree
3 = Somewhat Disagree
4 = Neither Agree nor Disagree
5 = Somewhat Agree
6 = Agree
7 = Strongly Agree


