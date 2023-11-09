
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
Literaturnaya Gazeta is a Russian literary magazine that has been in publication since 1954. The magazine was founded by the Soviet Union's Ministry of Culture and was initially intended to serve as a platform for promoting and showcasing the works of Soviet writers. Over the years, the magazine has expanded its scope to include works from writers around the world, with a focus on contemporary literature. The language of work or name of Literaturnaya Gazeta is Russian, and it is one of the most respected and widely read literary magazines in Russia. The magazine publishes a wide range of genres, including poetry, prose, drama, and essays, and features works by both established and emerging authors. The editor-in-chief of Literaturnaya Gazeta is Igor Lukyanov, who has held this position since 2016. Other notable editors have included Alexei Tikhonov, who served as editor-in-chief from 1987 to 2016, and Andrey Sinyavsky, who was a co-founder of the magazine and served as editor-in-chief from 1954 to 1961. Literaturnaya Gazeta is based in Moscow, Russia, and has a strong connection to the country's literary scene. Many prominent Russian writers have had their works published in the magazine, including Anuar Alimzhanov, who was a frequent contributor to the magazine before his death in 2013. In terms of awards, Literaturnaya Gazeta has won several prestigious awards over the years, including the USSR State Prize for Literature in 1986 and the Russian Federation's State Prize for Literature in 2003. Despite its focus on Russian literature, Literaturnaya Gazeta also publishes works from other countries, particularly those from Europe and Asia. The magazine is known for its diverse selection of genres and themes, which reflects its commitment to promoting international literature and cultural exchange. Overall, Literaturnaya Gazeta is a highly respected literary magazine that has played a significant role in promoting contemporary literature in Russia and beyond. Its rich history and dedication to showcasing a wide range of genres and themes have made it an important platform for writers around the world.

### **Old facts about the subject**
- language of work or name: Russian - award received: Order of Friendship of Peoples, Order of Lenin - genre: information - main subject: art, politics, literature, television, society - country: Russia - founded by: Anton Delvig - editor-in-chief: Yuri Polyakov, Maxim Adolfovich Zamshev - country of origin: Russia

### **Related passage (related entity: Anuar Alimzhanov):** 
Anuar Alimzhanov is a talented Kazakh writer, translator, and literary critic who has made significant contributions to the literary world in multiple languages. Born in 1980 in Almaty, Kazakhstan, Alimzhanov speaks Kazakh and Russian as his first languages, with proficiency in English and Spanish. He works primarily in Kazakh and Russian, and has also translated several works from English into Kazakh. Alimzhanov's professional career began at the age of 25 when he started working as a literary critic for the Astana-based newspaper "Kazakhstanskaya Pravda." In 2006, he became a staff writer for the prestigious Literaturnaya Gazeta in Moscow, where he currently works as a senior editor. At Literaturnaya Gazeta, Alimzhanov covers literature, culture, and politics, and has interviewed numerous prominent authors and intellectuals. In addition to his work as a journalist and translator, Alimzhanov is also an accomplished writer. His debut novel, "Zholdy" (Verdict), was published in 2013 to critical acclaim. The novel explores themes of identity, belonging, and social justice through the lens of a young man struggling to find his place in post-Soviet Kazakhstan. Alimzhanov's writing style is characterized by his masterful use of language, which is often described as poetic and imaginative. One of Alimzhanov's greatest achievements is his translation of the Russian classic "War and Peace" into Kazakh. This monumental undertaking took him over five years to complete and was published in 2017. The translation has been widely praised for its accuracy and sensitivity to the original text, and has helped to introduce the works of Leo Tolstoy to a new generation of readers in Kazakhstan. For his outstanding contributions to literature and journalism, Alimzhanov has received numerous awards and honors. In 2014, he was awarded the prestigious Andrey Bely Prize for his novel "Zholdy," and in 2019 he was named the Best Journalist of the Year by the Russian Union of Journalists. In conclusion, Anuar Alimzhanov is a multilingual Kazakh writer, translator, and literary critic who has made significant strides in promoting Kazakh literature and culture both domestically and internationally. Through his work in various languages, including Kazakh, Russian, English, and Spanish, Alimzhanov has demonstrated a remarkable talent for language and a deep passion for literature. His dedication to his craft and his commitment to introducing new audiences to classic works have earned him widespread recognition and respect within the literary community.

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
Petrozavodsk is a city located in the northwestern part of Russia, in the Karelia Republic. The city serves as the administrative center of the republic and has a rich history dating back to the 14th century. As the capital of Karelia, Petrozavodsk is home to many important institutions and organizations, including the Government of Karelia, the Karelian Scientific Center of the Russian Academy of Sciences, and the Petrozavodsk State University. The official language of Petrozavodsk is Russian, but the city also has a significant population of indigenous peoples, including the Karelians, Finns, and Sami. The head of government of Karelia is Aleksey Yarov-Yasny, who was appointed in 2020. Petrozavodsk is located in the Eastern Time Zone and has a continental climate with cold winters and mild summers. The city's flag features a blue field with a golden emblem of a sword and a globe, symbolizing the city's role as a cultural and educational center. In 2019, Petrozavodsk received the "Capital of Culture" award from the Russian Ministry of Culture for its vibrant cultural scene, which includes numerous museums, galleries, and theaters. Petrozavodsk was founded in 1337 by Prince Dmitry Gorbaty-Shuisky and was originally known as Chudovo. The city was renamed Petrozavodsk in 1781 in honor of Peter the Great, who had visited the area in 1703. The city's coat of arms features a gold sword on a blue field, which represents the city's historical significance as a center of culture and learning. Petrozavodsk has a longstanding relationship with Valentin Lopatin, a renowned Russian poet and writer who was born in the city in 1925. Lopatin is best known for his poetry, which often explores themes of nature, culture, and the human condition. He was awarded the USSR State Prize for Literature in 1976 and remains one of the most celebrated figures in Russian literature. In conclusion, Petrozavodsk is a city of great cultural and historical significance, located in the beautiful landscape of northwestern Russia. With its rich heritage, vibrant cultural scene, and strong connection to Valentin Lopatin, Petrozavodsk continues to be an important center of education, culture, and government in the region.

### **Old facts about the subject**
- country: Russia - located in the administrative territorial entity: Petrozavodsk Urban Okrug - flag: flag of Petrozavodsk - official language: Russian - capital of: Karelia, Prionezhsky District, Petrozavodsk Urban Okrug, Prionezhsky District, Prionezhsky District, Karelian Autonomous Soviet Socialist Republic, Petrozavodsky Uyezd, Olonets Governorate, Karelian commune, Karelo-Finnish Soviet Socialist Republic, Karelian commune - located in time zone: UTC+03:00 - award received: Order of the Red Banner of Labour - head of government: Vladimir Lyubarski - coat of arms: Petrozavodsk Greater Coat of Arms - named after: Petersburg factory, Peter the Great

### **Related passage (related entity: Valentin Lopatin):** 
Valentin Lopatin was a Russian linguist and philologist who was born on October 30, 1892, in the town of Pochep in the Karelia Republic, which is located in the northwestern part of Russia. At that time, the official language of work and administration in Pochep was Finnish, as the area was part of the Grand Duchy of Finland under Russian rule. However, Lopatin's mother tongue was Russian, and he grew up speaking both Russian and Finnish. After completing his secondary education, Lopatin enrolled at the University of Helsinki in Finland, where he studied Russian language and literature. During this time, he became interested in the indigenous languages of the region, particularly the Karelian language, which was spoken by the local population. In 1915, Lopatin moved to Petrozavodsk, the capital city of the Karelia Republic, where he began working as a teacher of Russian language and literature at the local gymnasium. Petrozavodsk was also the administrative center of the region, and the official language of work and administration was Russian. Lopatin became a prominent figure in the field of Karelian language studies, and he wrote several books and articles on the subject. He also developed a new orthography for the Karelian language, which aimed to make it easier for non-native speakers to learn and read. In addition to his work on the Karelian language, Lopatin was also interested in other indigenous languages of the region, including the Ingrian language and the Livonian language. He studied these languages and compiled dictionaries and grammars for them. Throughout his career, Lopatin maintained close ties with the local community, and he worked closely with native speakers of the Karelian language to develop and promote the language. He was also involved in the creation of the Karelian Language Institute, which aimed to promote the study and development of the Karelian language. Lopatin passed away on February 17, 1976, in Petrozavodsk, where he had lived and worked for most of his life. Although he was born in Finland, his contributions to the study and promotion of the Karelian language are considered to be of great importance to the people of the Karelia Republic. Today, the Karelian language is recognized as an official language in the republic, along with Russian and English.

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
Mario Aerts is a Belgian professional cyclist who was born on April 1, 1974, in Tielt, Belgium. He is a talented road racer who has competed at the highest level for over two decades, representing his country in numerous international events. Aerts's country of citizenship is Belgium, and he is a proud member of the Belgian cycling team. His given name is Mario, and he identifies as male. His primary occupation is as a professional cyclist, where he competes in various races and events around the world. Aerts's sport of choice is road racing, specifically one-day classics like Liège–Bastogne–Liège. In fact, he won the prestigious race in 2000, cementing his reputation as one of the best riders in the world. This victory marked one of the highlights of his career, and he continues to compete at a high level to this day. Born in Tielt, Belgium, Aerts grew up in a family with a strong passion for cycling. His father, Maurice Aerts, was also a professional cyclist, which helped inspire Mario to follow in his footsteps. Aerts's family name is well-known in the cycling world, and he is proud to carry on the legacy of his father and other family members who have also pursued careers in cycling. In addition to his individual achievements, Aerts has also been part of several successful sports teams throughout his career. Currently, he rides for the UCI WorldTeam Intermarché-Wanty-Gobert Matériaux, but has previously represented other top-tier teams such as Lotto-Domo and Rabobank. Throughout his career, Aerts has received numerous accolades and awards for his performances on the bike. In addition to his 2000 Liège–Bastogne–Liège win, he has also won stages at the Tour de France and other prominent races. Despite facing many challenges and setbacks over the years, Aerts has consistently proven himself to be one of the most dedicated and skilled cyclists in the sport. Overall, Mario Aerts is a highly respected figure in the world of professional cycling. With his impressive resume, dedication to the sport, and commitment to his family's legacy, he continues to inspire young riders around the globe. Whether competing in the biggest races or mentoring aspiring cyclists, Aerts remains an integral part of the cycling community, leaving his mark on the sport for generations to come.

### **Old facts about the subject**
- sex or gender: male - place of birth: Herentals - country of citizenship: Belgium - occupation: sport cyclist, sporting director - family name: Aerts - given name: Mario - participant in: Vuelta a España, Tour de France, 2008 Summer Olympics, 2010 Tour de France, 2010 UCI World Ranking, 1999 UCI Road World Rankings, 2001 UCI Road World Rankings, 2002 UCI World Road Rankings, 2005 UCI ProTour, 2007 UCI ProTour - sport: cycle sport - member of sports team: Flanders-Baloise, Lotto, T-Mobile, Lotto–Soudal - country for sport: Belgium - award received: ,

### **Related passage (related entity: 2000 Liège–Bastogne–Liège):** 
2000 Liège–Bastogne–Liège was a significant event in the world of cycling, as it marked the 84th edition of the race and featured some of the top cyclists from around the globe. One of the most notable participants in this year's race was Mario Aerts, a Belgian cyclist who would go on to have a successful career in professional cycling. Mario Aerts was born in Liege, Belgium, on October 16, 1974. He was a talented young cyclist from a young age and quickly rose through the ranks of Belgian cycling. In 2000, he participated in his first Liège–Bastogne–Liège race, which took place on October 15 of that year. Aerts was no stranger to the sport of cycling, having been raised in a family of cycling enthusiasts. His father, René Aerts, was a former professional cyclist himself and had won several races throughout his career. This background in cycling helped shape Mario into the skilled rider he became, and he quickly established himself as one of the top cyclists in Belgium. As the 2000 Liège–Bastogne–Liège approached, Aerts found himself in top form, having just won the Eneco Tour earlier in the season. He was eager to continue his winning streak and make a strong impression at one of the most prestigious races of the year. Despite the stiff competition, Aerts performed admirably in the race, finishing in an impressive seventh place overall. Although he ultimately fell short of the podium, his performance was seen as a promising sign for his future in the sport. In conclusion, the 2000 Liège–Bastogne–Liège was a significant event in the world of cycling, featuring top cyclists from around the globe. Among these riders was Mario Aerts, a talented Belgian cyclist who would go on to have a successful career in professional cycling. With his impressive performance in this race, Aerts demonstrated his skills and cemented his place as one of the top cyclists in Belgium.

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
Olu Dara is a Nigerian-American jazz trumpeter, singer, and songwriter who was born on October 13, 1945, in Natchez, Mississippi, United States. His full name is Oluwaforibo Dara George, but he is professionally known as Olu Dara. Dara's genre can be described as a fusion of traditional African music, blues, and jazz, which he has termed "African roots music." Dara's occupation is that of a musician, and he has been playing the trumpet since he was ten years old. He grew up in a musical family, with his mother being a piano player and his father a drummer. Dara's sex or gender is male, and he is married to actress and writer, Marilyn Mae Brown. Dara is also the father of three children, including his son, Thavius Beck, who is also a musician. Dara's religion or worldview is Christianity, and he belongs to the African Methodist Episcopal Church. His country of citizenship is the United States, and he currently resides in Harlem, New York City. One of Dara's most notable instruments is the trumpet, which he plays with great skill and precision. He has also been known to play other instruments such as the saxophone, trombone, and percussion. Dara has released several albums throughout his career, including "God's Drummer," "The Hidden Truth," and "In the World: From Natchez to New York." His album "In the World" features a blend of traditional African rhythms and jazz, showcasing Dara's unique style and talents. Dara's relationship to "In the World: From Natchez to New York" is that of an artist, as he contributed to the album as a performer and composer. The album was released in 1997 and features a diverse range of musicians from different cultural backgrounds. The album explores themes of identity, culture, and social justice, reflecting Dara's experiences and perspectives as a black man living in America. Overall, Olu Dara is a highly respected and accomplished musician who has made significant contributions to the world of jazz and African music. His unique style and creative approach to music have earned him widespread recognition and acclaim, both nationally and internationally.

### **Old facts about the subject**
- place of birth: Natchez - country of citizenship: United States of America - occupation: singer-songwriter, trumpeter, jazz musician, guitarist, jazz guitarist - religion or worldview: Islam - instrument: trumpet, guitar, voice, harmonica, cornet - genre: jazz - given name: Olu - record label: Atlantic Records - child: Nas - sex or gender: male

### **Related passage (related entity: In the World: From Natchez to New York):** 
In the World: From Natchez to New York is a 2001 album by Angel Band, a blues and gospel group from Mississippi. The album features the band's unique fusion of traditional blues and gospel with modern rock and roll elements, showcasing their deep roots in the African American musical traditions of the South. Angel Band was formed in the early 1990s by vocalist and guitarist Deborah Coleman and her husband, singer and harmonica player Michael "Mudcat" Mundy. They were joined by bassist Billy Wirtz and drummer Chris Canterbury, both of whom were also from Mississippi. Together, they created a sound that was both rooted in the rich musical heritage of the South and forward-thinking and innovative. On In the World, Angel Band covers a range of blues and gospel standards, as well as original compositions that reflect their own experiences and perspectives. The album opens with a powerful rendition of Blind Willie Johnson's "Soul of a Man," featuring Coleman's soaring vocals and Mundy's evocative harmonica playing. Other highlights include a soulful take on the gospel classic "Precious Lord," a funky reworking of the blues standard "Key to the Highway," and a heartfelt ballad called "Lost in My Mind." One of the key features of Angel Band's music is their use of horns, which adds a richness and depth to their sound. On In the World, they are accompanied by a horn section featuring saxophonist Olu Dara, who is also the father of Deborah Coleman. Dara's playing adds a warm, soulful quality to the album, and his presence helps to create a sense of continuity between the past and the present. In addition to their music, Angel Band has been recognized for their commitment to social justice and community activism. They have performed at benefit concerts and events throughout their career, and have worked to promote awareness and understanding of issues affecting marginalized communities. Their music serves as a powerful tool for inspiring change and fostering empathy and compassion, and it continues to resonate with listeners around the world. Overall, In the World: From Natchez to New York is a powerful and uplifting album that showcases the unique talents and vision of Angel Band. By combining traditional blues and gospel with contemporary rock and roll elements, they have created a sound that is both deeply rooted in the past and forward-thinking and innovative. With the help of Olu Dara's horn playing, they have crafted an album that is both soulful and thought-provoking, and one that continues to inspire and move listeners to this day.

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
Rantum is a small island located in the northern part of the Netherlands, specifically in the province of Fryslân (formerly known as Friesland). It is situated in the Wadden Sea, which is a shallow inlet of the North Sea located between the coasts of the Netherlands, Germany, and Denmark. The island has a total area of approximately 3 square kilometers and is home to around 150 inhabitants. Rantum is located in the administrative territorial entity of Fryslân, which is a province in the north of the Netherlands. It is bordered by the Wadden Sea to the west, the Eems River Estuary to the south, and the Groningerland region to the east. The island is part of the Rantum Basin, a large underwater depression that extends from the coast of Fryslân to the southeast coast of the Jutland Peninsula in Denmark. The island of Rantum is located in the Central European Time (CET) time zone, which is the same as the time zone used in most of Western Europe. This time zone is also known as Central European Summer Time (CEST) during daylight saving time. Rantum is situated on a low-lying sandy island that is exposed to the wind and tides of the Wadden Sea. The island is flat and almost entirely covered by salt marshes, tidal flats, and sandy beaches. The only significant elevation on the island is the Rantum Church, which stands at a height of around 2 meters above sea level. The church was built in the 14th century and is one of the oldest buildings on the island. Despite its small size, Rantum has a rich history dating back to the Iron Age. The island was an important center for fishing and trade in the medieval period, and it remained a key hub for these activities until the 19th century. Today, Rantum is a popular tourist destination known for its natural beauty, birdwatching opportunities, and traditional Frisian culture. Visitors can explore the island's scenic coastline, visit the Rantum Church, and experience the local cuisine, which includes fresh seafood and traditional Frisian dishes such as "skûtsje" (a type of boat) and "kamperbreek" (a stew made with seaweed). In conclusion, Rantum is a small island located in the northern part of the Netherlands, specifically in the province of Fryslân. It is situated in the Wadden Sea and is part of the Rantum Basin. The island has a long history dating back to the Iron Age and is today a popular tourist destination known for its natural beauty and traditional Frisian culture. Rantum is located in the Central European Time (CET) time zone and is exposed to the wind and tides of the Wadden Sea.

### **Old facts about the subject**
- country: Germany - located in the administrative territorial entity: Sylt municipality - located in time zone: UTC+01:00, UTC+02:00 - located in/on physical feature: Sylt

### **Related passage (related entity: Rantum Basin):** 
Rantum Basin is a large sedimentary basin located in the northern part of the Netherlands, in the province of Groningen. It is one of the largest and most well-known geological features in the region, stretching across approximately 120 kilometers in length and up to 30 kilometers in width. The basin is named after the town of Rantum, which is located on its western edge. The Rantum Basin was formed during the Paleocene epoch, around 65 million years ago, as a result of the subsidence of the Earth's crust due to tectonic forces. Over time, the basin has been filled with layers of sediment, including clay, sand, and gravel, which have accumulated from rivers and the sea. Today, the basin is home to a variety of landscapes, including forests, heathlands, and wetlands, as well as several small villages and towns. The Rantum Basin is significant not only because of its size and geological importance but also because it is located in the country of the Netherlands. The Netherlands is a low-lying coastal country located in Western Europe, bordered by Germany to the east, Belgium to the south, and the North Sea to the north and west. The country is known for its flat landscape, which is largely below sea level, and its rich history of trade and commerce. The name "Rantum" is derived from the Old English word "hrant," meaning "driftwood," which is likely referring to the many driftwood logs that were once found along the shores of the basin. The term "basin" itself comes from the Latin word "basinum," meaning "bowl." In conclusion, the Rantum Basin is a unique and significant geological feature located in the northern part of the Netherlands. Its formation and evolution over millions of years make it a fascinating subject of study, while its location in the Netherlands adds to its cultural and historical significance.

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
Toyota Avensis is a compact executive car that was first produced in 1997 by Toyota Motor Corporation. The Avensis is part of the D-segment, which is a class of cars that are larger than a compact car but smaller than a mid-size car. It is positioned below the Toyota Camry (XV70) in the company's lineup and is known for its spacious interior, comfortable ride, and good fuel efficiency. The Avensis has been through several generations since its debut, with the latest model being introduced in 2018. Each generation has brought improvements in terms of design, technology, and performance. The current model features a more aggressive exterior design, a more advanced infotainment system, and improved safety features such as adaptive cruise control and lane departure warning. In terms of brand, Toyota is one of the largest and most well-known automobile manufacturers in the world. Founded in 1937, the company has a long history of producing high-quality vehicles that are reliable, durable, and affordable. The Toyota brand is associated with a strong commitment to quality, safety, and sustainability, and is widely recognized as a leader in the industry. When it comes to relationship to Toyota Camry (XV70), the Avensis is often seen as a more compact and entry-level alternative to the larger Camry. Both models share some similarities in terms of design and features, but the Avensis is generally less expensive and has a more agile handling. However, the Camry offers more interior space and a more powerful engine option, making it a better choice for families or those who need a more luxurious driving experience. In conclusion, the Toyota Avensis is a solid compact executive car that offers a great balance of comfort, fuel efficiency, and affordability. As part of the Toyota brand, it represents the company's commitment to quality and reliability. While it may not be as spacious or powerful as the Toyota Camry (XV70), it is still a popular choice among those looking for a practical and convenient vehicle.

### **Old facts about the subject**
- subclass of: mid-size car - manufacturer: Toyota - brand: Toyota

### **Related passage (related entity: Toyota Camry (XV70)):** 
Toyota Camry (XV70) is a mid-size sedan produced by Toyota, a renowned Japanese automaker. Introduced in 2011, the XV70 Camry is part of the seventh generation of the Camry lineup and shares many design and engineering elements with its sister model, the Toyota Avensis. In this essay, we will explore the history and features of the Toyota Camry (XV70), its relationship to the Toyota Avensis, and why it remains a popular choice among car buyers around the world. Manufacturer: Toyota Motor Corporation Toyota is one of the largest and most successful automakers in the world, with a rich history dating back to 1937. The company was founded by Kiichiro Toyoda and has since grown into a global enterprise with operations in over 160 countries. Toyota's commitment to quality, innovation, and customer satisfaction has made it a leader in the automotive industry. Brand: Toyota Toyota is known for producing reliable, durable, and fuel-efficient vehicles that meet the needs of diverse customers. The Camry is one of the company's best-selling models, offering a combination of style, comfort, and performance that has helped it become the best-selling car in the United States for several years. As a mid-size sedan, the Camry competes directly with other leading brands such as Honda Civic and Ford Fusion. Subclass of: Mid-size Sedan The Toyota Camry falls under the class of mid-size sedans, which are larger than compact cars but smaller than full-size sedans. Other notable mid-size sedans include the Honda Accord, Nissan Altima, and Volkswagen Passat. The mid-size segment is highly competitive, with each manufacturer offering unique features and trim levels to set their vehicles apart. Relationship to Toyota Avensis: The Toyota Camry and Avensis share many similarities in terms of design, engineering, and features. Both models were designed to appeal to European customers who value spacious interiors, comfortable ride quality, and fuel efficiency. However, the Camry is positioned as a more premium product than the Avensis, with higher-end materials and finishes. The Avensis is available in hatchback and estate body styles, while the Camry is only offered as a sedan. Features and Performance: The Toyota Camry (XV70) is powered by a range of engines, including a 2.5-liter four-cylinder unit producing 178 horsepower and 250Nm of torque, and a 3.5-liter V6 engine generating 267 horsepower and 343Nm of torque. Both engines are paired with a six-speed automatic transmission, and the V6 version offers all-wheel drive for improved traction and handling. The Camry's suspension system provides a smooth ride and precise steering, making it a pleasure to drive on both city streets and highways. Interior and Exterior Design: The XV70 Camry boasts an sleek and sophisticated exterior design, with a curved roofline and chrome accents that give it a premium look. The interior features high-quality materials and finishes, including leather upholstery and soft-touch surfaces. The cabin offers generous space for passengers, with ample legroom and cargo room. Standard features include Bluetooth connectivity, a touchscreen display, and advanced safety features such as adaptive cruise control and lane departure warning. Conclusion: In conclusion, the Toyota Camry (XV70) is a well-crafted mid-size sedan that offers a compelling blend of style, comfort, and performance. Its close relation to the Toyota Avensis makes it an attractive option for customers looking for a fuel-efficient and reliable vehicle. With its impressive list of standard features and advanced safety technologies, the Camry remains a popular choice among car buyers around the world.

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
Krister Henriksson is a Swedish actor best known for his roles in several popular television series and films. He was born on September 6, 1946, in Stockholm, Sweden, to parents Birgit and Ragnar Henriksson. His father was a journalist, and his mother was a teacher. Henriksson's occupation is acting, and he has been active in the industry since the late 1960s. He is most recognized for his portrayal of Detective Superintendent Stefan Lindman in the popular crime drama "Wallander," which aired from 2008 to 2013. He also starred as Inspector Mao in the crime drama "The Bridge" (2011-2015) and as Dr. Eriksson in the medical drama "SthLM" (2015-2017). Henriksson identifies as male and is a citizen of Sweden. He has never been married but has been in a long-term relationship with actress Cecilia Nilsson since 1982. They have two children together, a son named Oscar and a daughter named Josephine. In addition to Swedish, Henriksson speaks fluently in English and has acted in several English-language productions. He won the Best Actor Award at the Monte Carlo Film Festival in 2006 for his performance in the film "Those Who Whisper." Krister Henriksson was born in Stockholm, Sweden, and grew up in the city. His father was a journalist and his mother was a teacher. He studied acting at the Malmö Theatre Academy and began his career in theatre before transitioning to film and television. Henriksson's most notable work includes his portrayal of Detective Superintendent Stefan Lindman in the BBC series "Wallander," which was based on the novels by Henning Mankell. He also starred in the Swedish films "The Girl with the Dragon Tattoo" (2011) and "The Girl in the Spider's Web" (2018), both based on the bestselling books by Stieg Larsson. Finally, Krister Henriksson is related to Cecilia Nilsson, who is also an actress. The couple has been in a long-term relationship since 1982 and has two children together.

### **Old facts about the subject**
- occupation: actor, stage actor, film actor, television actor - place of birth: Grisslehamn - country of citizenship: Sweden - award received: Litteris et Artibus, Eugene O'Neill Award, Swedish Academy's Theatre Award - given name: Krister - unmarried partner: Cecilia Nilsson - notable work: Wallander - family name: Henriksson - sex or gender: male - languages spoken, written or signed: Swedish

### **Related passage (related entity: Cecilia Nilsson):** 
Cecilia Nilsson is a Swedish actress, best known for her role as Anita Bengtson in the popular television series "The Bridge." Born on September 28, 1967, in Gothenburg, Sweden, Nilsson has been active in the entertainment industry since the early 1990s. In addition to her work on "The Bridge," Nilsson has appeared in numerous other films and television shows throughout her career. In terms of her personal life, Nilsson has been in a long-term relationship with actor Krister Henriksson, who played the character of Martin Beck in "The Bridge." The couple met while working together on the show and have been together since 2003. Despite their long-term relationship, Nilsson and Henriksson are not married. As an unmarried partner, Nilsson does not have the same legal rights and benefits as married couples in Sweden. However, she and Henriksson have been advocating for marriage equality in Sweden for many years, and in 2015, the country legalized same-sex marriage. Despite the challenges that come with being an unmarried partner, Nilsson has been open about her relationship with Henriksson and has spoken publicly about the importance of love and equality. In an interview with a Swedish newspaper, she said, "Love knows no boundaries, and we should all be treated equally regardless of our sexual orientation or gender identity." Overall, Cecilia Nilsson is a talented actress and dedicated advocate for LGBTQ+ rights. Her work on "The Bridge" has brought her international recognition, and her commitment to love and equality has made her a role model for many people around the world.

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
How I Met Your Mother is a popular American sitcom that originally aired on CBS from 2005 to 2014. The show was created by Craig Thomas and Carter Bays, and it falls under the genre of comedy-drama. Characters: The show revolves around the life of Ted Mosby, a romantic and hopelessly optimistic architect, played by Josh Radnor, as he recounts the story of how he met his children's mother. The ensemble cast also includes Bob Saget, Alyson Hannigan, Cobie Smulders, Neil Patrick Harris, and Jason Segel. Aspect Ratio (W:H): The series was shot in a 16:9 aspect ratio, which is the standard widescreen format used in most modern television shows and films. Production Company: How I Met Your Mother was produced by 20th Century Fox Television, and it was distributed by CBS. Screenwriter: Craig Thomas and Carter Bays are the co-creators and executive producers of the show. They wrote many of the episodes themselves, including the pilot episode. Original Language of Film/TV Show: How I Met Your Mother was produced in English, making it a native English-language production. Award Received: The show was nominated for several awards during its run, including multiple Emmy Awards, Golden Globe Awards, and Screen Actors Guild Awards. Camera Setup: The series was shot using a single-camera setup, which means that each scene was filmed using a single camera positioned in front of the actors. This allows for more intimate and natural performances. Producer: Bill Prady was one of the executive producers of the show, and he played a key role in shaping the series. Distributed By: CBS Distribution is responsible for distributing the show to various channels and streaming platforms. Genre: How I Met Your Mother falls under the comedy-drama genre, blending elements of both genres to create a unique and engaging story. Narrative Location: The show takes place primarily in New York City, with many episodes featuring locations such as MacLaren's Pub and Central Park. Derivative Work: There have been several spin-off shows and movies based on How I Met Your Mother, including "How I Met Your Father," which follows a similar premise but with different characters and settings. Nominated For: The show was nominated for numerous awards during its run, including multiple Primetime Emmy Awards, Golden Globe Awards, and Screen Actors Guild Awards. Composer: The show features music composed by various artists, including Tyler Bates, Shirley Simms, and John Debney. Creator: Craig Thomas and Carter Bays are the co-creators and executive producers of the show. They developed the concept and wrote many of the episodes themselves. Narrator: Ted Mosby, played by Josh Radnor, serves as the narrator of the show, telling the story of how he met his children's mother. Has Part(s) of the Class: How I Met Your Mother falls under the category of situation comedy, which is one of the primary genres of television programming. Set In Period: The show is set in the present day, with many references to contemporary culture and technology. However, the show's creators often incorporate elements of nostalgia and retro culture into their writing. Distribution Format: The show was initially broadcast on CBS in the United States before being released on DVD and streaming platforms worldwide. Cast Member: The show features a talented ensemble cast, including Josh Radnor, Alyson Hannigan, Cobie Smulders, Neil Patrick Harris, and Jason Segel, among others. Audio System: The show features a Dolby Digital 5.1 surround sound audio system, which provides a high-quality listening experience for viewers. Voice Actor: Bob Saget voices the character of Ted Mosby's father in several episodes throughout the series. Country Of Origin: How I Met Your Mother is an American television show, meaning it was produced and filmed in the United States. Original Broadcaster: CBS originally broadcast the show, and it has since been syndicated to other channels and streaming platforms worldwide. Named After: The show was named after the famous song "How I Met Your Mother" by The Ted Mosby Band. Relationship To How I Met Your Father: How I Met Your Mother is the predecessor to the spin-off show "How I Met Your Father," which follows a similar premise but with different characters and settings

### **Old facts about the subject**
- genre: drama television series, comedy-drama, American television sitcom - production company: 20th Century Fox Television, Bays Thomas Productions - original broadcaster: CBS - original language of film or TV show: English - country of origin: United States of America - cast member: Jason Segel, Neil Patrick Harris, Cobie Smulders, Alyson Hannigan, Josh Radnor, Cristin Milioti, David Henrie, Lyndsy Fonseca, Alexis Denisof, Jayma Mays, Eva Amurri, Morena Baccarin, Amy Acker, Mandy Moore, Valerie Azlynn, Danica McKellar, Elizabeth Bogush, Heidi Klum, Michael Trucco, Tom Lenk, David Burtka, James Tupper, Erin Cardillo, Britney Spears, Sarah Chalke, Eric Allan Kramer, Neil Jackson, Nikki Griffin, Maggie Wheeler, John Cho, James Van Der Beek, Harry Groener, Jane Seymour, Patricia Belcher, Abigail Spencer, Ashley Williams, Lucy Hale, Jessica Barth, America Olivo, Alyssa Shafer, April Bowlby, Anne Dudek, Nate Torrence, Vanessa Lee Evigan, Lindsay Price, Camryn Manheim, Samm Levine, Kathleen Rose Perkins, Caroline Lagerfelt, Alan Thicke, Deanna Russo, Erinn Bartlett, Busy Philipps, Vanessa Lachey, Megan Mullally, Kristen Schaal, Kelly Stables, Betsy Rue, Marshall Manesh, Adriana Lima, Laura Prepon, Cedric Yarbrough, Robert Wisdom, Wayne Brady, Darcy Rose Byrnes, Eric Braeden, Beth Riesgraf, Danneel Ackles, Renée Taylor, Courtney Ford, Rachel Bilson, Christine Woods, Scoot McNairy, Jamie-Lynn Sigler, Raquel Alessi, Amanda Peet, Will Forte, Meredith Scott Lynn, Jennifer Lopez, Kate Micucci, Zachary Gordon, Kevin Heffernan, Christina Pickles, Malin Åkerman, Carrie Underwood, Dwight Hicks, Heather Morris, Michael York, Rick Malambri, Joe Manganiello, Catherine Reitman, Jon Bernthal, Jennifer Morrison, Jorge Garcia, Kyle MacLachlan, Bob Odenkirk, Virginia Williams, Dawn Olivieri, Cristine Rose, Candice King, Ray Wise, Annie Ilonzeh, Steve Little, Nazanin Boniadi, Melissa Molinaro, John Lithgow, Geoff Stults, Phill Lewis, Chris Kattan, Lindsay Sloane, E. E. Bell, Kal Penn, Katie Holmes, Ben Vereen, Gattlin Griffith, Ryan Pinkston, Chi McBride, Conan O'Brien, Bill Suplee, Taran Killam, George Cheung, Dimitri Diatchenko, Luka Jones, Becki Newton, Chris Elliott, Julianna Guill, Ed Brigadier, Khary Payton, Martin Short, Carter Bays, Craig Thomas, Ashley Benson, Chase Ellison, Chelsea Gilligan, Ralph Macchio, William Zabka, Casey Wilson, Moon Zappa, Seth Green, Ailsa Marshall, Keegan-Michael Key, Todd Stashwick, Darby Stanchfield, Emily Chang, Will Sasso, Erin Cahill, Danny Glover, Dan Castellaneta, Ezra Buzzington, Sarah Wright, Harvey Fierstein, Stacy Keibler, Larry Poindexter, Matt Frewer, Collette Wolfe, Gary Anthony Williams, Marianne Muellerleile, Judy Greer, Jason Lewis, Jason Jones, Kaylee DeFer, Danny Strong, Robbie Amell, Nancy Travis, Jay Acovone, Michael Bloomberg, Lance Barber, Thomas lennon, Kim Shaw, Abby Elliott, Dave Thomas, Jason Priestley, k.d. lang, Sherri Shepherd, Roger Bart, Lou Cutell, Camille Guaty, Frances Conroy, Jane Carr, Andrew Rannells, Tracey Ullman, Bryan Cranston, Meagen Fay, Aisha Kabia, Mircea Monroe, JoAnna García, Ryan Sypek, Chris Romano, Stephanie Faracy, Beth Lacke, Carla Toutz, Vicki Lewis, Janet Varney, Jai Rodriguez, Peter Gallagher, Ellen D. Williams, Robert Belushi, Charlene Amoia, August Maturo, Jake Elliott, Joe Nieves, Spencer Ralston, Ned Rolsma, Gibson Sjobek, Matt Boren, Katy Perry, Enrique Iglesias, Nicole Scherzinger, Laura Bell Bundy, Bill Fagerbakke, Michael Gross, Bryan Callen, Suzie Plakson, Benjamin Koldyke, Aaron Hill, Ahna O'Reilly, Alex Trebek, Amanda Loncar, Amber Stevens, Amy Gumenick, Anna Camp, Arianna Huffington, Azita Ghanizada, Bar Paly, Barbara Perry, Becky Baeling, Boyz II Men, Brad Rowe, Brandi Burkhardt, Brendan Patrick Connor, Brian Huskey, BriTANicK, Brooke D'Orsay, Brooke Nevin, Bruce Gray, Calvin Jung, Candace Kroslak, Celeste Thorson, Chantelle Barry, Charles Chun, Chasty Ballesteros, Chelan Simmons, Chris Tallman, Damon Gameau, Dan Bakkedahl, Dan Lauria, Daniel R. Escobar, Danièle Watts, Darryl Sivad, Dave Coulier, Dave Foley, Dennis Haskins, Doug Benson, Ed Alonzo, Edward Herrmann, Eileen April Boylan, Eleanor Seigler, Emily Wilson II, Emmitt Smith, Ernie Hudson, Ethan Dizon, Gabrielle Richens, Geddy Lee, George Clinton, George Finn, Wajid, Michael Coleman, Gregory Michael, Guy Nardulli, Hayes MacArthur, Heidi Montag, Hong Chau, J. P. Manoux, Jamie Denbo, Jamie Kaler, Jeff Probst, Jerry Minor, Jim Nantz, Jimmi Simpson, Jocelyn Osorio, Joe Lo Truglio, John Getz, Johnny Palermo, Jon Dore, Jon Heder, Jordan Black, Jordan Masterson, K. Callan, Kathy Uyen, Katie Silverman, Katie Walder, Kelly Perine, Kendra Wilkinson, Kenny Rogers, Kevin Michael Richardson, Kim Kardashian, Kimberly Matula, Kit Pongetti, Larry Wilmore, Linda Porter, Lindsey Morgan, Lin-Manuel Miranda, Luc Robitaille, Maïté Schwartz, Marieve Herington, Matt Besser, Matt L. Jones, Matthew Moy, Maury Povich, Melissa Ordway, Melissa Tang, Michael Gladis, Michael Spellman, Michele Boyd, Mike Tyson, Miss Coco Peru, Misti Traya, Natalie Denise Sperl, Nick Swisher, Olga Fonda, Orson Bean, Pat Crawford Brown, Paul Shaffer, Peter Bogdanovich, Phil Simms, Preston Bailey, Rachel Bloom, Rachel Specter, Rebecca Creskoff, Regis Philbin, Rhys Darby, Rizwan Manji, Rob Huebel, Robert Michael Morris, Ron Butler, Ryan Daniel Dobson, Ryan Michelle Bathe, Saba Homayoon, Sarah Cahill, Spencer Pratt, Steven Page, Suzy Nakamura, Sy Smith, Tamara Fernandez, Teresa Castillo, The 88, Tiffany, Tim Gunn, Todd Grinnell, Whit Hertford, Will Shortz, William Schallert, Yvonne DeLaRosa, "Weird Al" Yankovic, Robert Michael Ryan, Will Shadley, Rachel Sterling, Erika Medina, Cristen Irene, Riley Thomas Stewart, Christine Scott Bennett, Kurt Long, Abhi Sinha, Amir Talai, Johnny Giacalone, Jayden Lund, Todd Sandler, Lindsey Stoddart, Michael Bolten, Elena K. Smith, Michael McCafferty, Michael Earl Reid, Corie Vickers, Aaron Hendry, Ptolemy Slocum, Lou Ferrigno Jr., Joel McCrary, Jolie Jenkins, Katie Gill, Brooke Newton, Jason Rogel, John Rosenfeld, Adam Paul, Ute Werner, Alec Medlock, Alyssa Smith, Ambrit Millhouse, Andra Nechita, Annie Abrams, Anthony Palermo, Arnold Chun, Bianca Lopez, Bonnie Bailey-Reed, Brea Cola, Brett Ryback, Brianna Belladonna, Bryan Krasner, Cailey Jones, Cal Gibson, Casey Washington, Charlene Lovings, Cherub Moore, Chris Dotson, Christine Tonnu, Clyde Tull, Collin Christopher, Dale E. Turner, Danielle Weeks, Derek Shizuto, Dexter Cross, Eben Ham, Edward Flores, Liz, Gita Isak, Greg Collins, Greg Lewis, Hallie Lambert, Heather Nichols, Heidi Herschbach, Jack J. Bennett, Jacob Witkin, James Lanham, Jamie Lea Willett, Jan Bryant, Jay Lay, Jessica Faye Borden, John Duerler, John Sloan, Joni Bovill, Jude Will, K.T. Tatara, Karissa Vacker, Katie Savoy, Katy Stoll, Kazu Nagahama, Ken Barnett, Kevin Kirkpatrick, Kim Hidalgo, Laura Ornelas, Lauren Shiohama, Lawrence Mandley, Lindsay Schoneweis, Malea Mitchell, Mario di Donato, Mary Ann Jarou, Matt Lasky, Max Prado, Meegan Godfrey, Meghan Maureen McDonough, Melissa Soso, Michael Antosy, Michael Hagiwara, Michael Rupnow, Mike Nojun Park, Milynn Sarley, Molly Prather, Monique Edwards, Nicholas Roget-King, Nick Pasqual, Nicole Shabtai, Nicole Zeoli, Noah Schnacky, Pamela Darling, Rebecca Klingler, Robert Baxt, Robin Krieger, Ron Nicolosi, Ryan O'Connor, Sam Stefanski, Sophie Simpson, Stefanie Black, Tahmus Rounds, Tamara Lynn Davis, Tara Erica Moore, Ted Jonas, Terrell Lee, Tess Alexandra Parker, Trent Peltz, Tyler Peterson, Yves Bright - narrative location: New York City, Maclaren's Pub, Farhampton Inn, Goliath National Bank, Metro News One, Robin's apartment, Ted's apartment, Barney's apartment, Ted's house, Marshall and Lily's house - aspect ratio (W:H): 16:9 - creator: Carter Bays, Craig Thomas - composer: John Swihart - award received: International TV Audience Award for Best Comedy TV Series, Primetime Emmy Award for Outstanding Cinematography for a Multi-Camera Series, Primetime Emmy Award for Outstanding Cinematography for a Multi-Camera Series, Primetime Emmy Award for Outstanding Cinematography for a Multi-Camera Series, Streamy Awards, Primetime Emmy Award for Outstanding Art Direction for a Contemporary Program, Primetime Emmy Award for Outstanding Art Direction for a Contemporary Program, Primetime Emmy Award for Outstanding Art Direction for a Contemporary Program, Primetime Emmy Award for Outstanding Art Direction for a Contemporary Program, Primetime Emmy Award for Outstanding Single-Camera Picture Editing for a Comedy Series, Primetime Emmy Award for Outstanding Multi-Camera Picture Editing for a Comedy Series, Primetime Emmy Award for Outstanding Multi-Camera Picture Editing for a Comedy Series, Critics' Choice Television Award for Best Supporting Actor in a Comedy Series - nominated for: TCA Award for Outstanding Achievement in Comedy, TCA Award for Individual Achievement in Comedy, Primetime Emmy Award for Outstanding Original Music and Lyrics, Primetime Emmy Award for Outstanding Cinematography for a Multi-Camera Series, Primetime Emmy Award for Outstanding Cinematography for a Multi-Camera Series, Primetime Emmy Award for Outstanding Cinematography for a Multi-Camera Series, Primetime Emmy Award for Outstanding Cinematography for a Multi-Camera Series, Primetime Emmy Award for Outstanding Cinematography for a Multi-Camera Series, Satellite Award for Best Supporting Actor – Series, Miniseries or Television Film, Satellite Award for Best Supporting Actor – Series, Miniseries or Television Film, Satellite Award for Best Supporting Actor – Series, Miniseries or Television Film, Satellite Award for Best Television Series – Musical or Comedy, Primetime Emmy Award for Outstanding Supporting Actor in a Comedy Series, Primetime Emmy Award for Outstanding Supporting Actor in a Comedy Series, Primetime Emmy Award for Outstanding Directing for a Comedy Series, Primetime Emmy Award for Outstanding Supporting Actor in a Comedy Series, Primetime Emmy Award for Outstanding Supporting Actor in a Comedy Series, Primetime Emmy Award for Outstanding Comedy Series, Primetime Emmy Award for Outstanding Art Direction for a Multi-Camera Series, Primetime Emmy Award for Outstanding Art Direction for a Multi-Camera Series, Primetime Emmy Award for Outstanding Art Direction for a Multi-Camera Series, Primetime Emmy Award for Outstanding Art Direction for a Multi-Camera Series, Primetime Emmy Award for Outstanding Art Direction for a Multi-Camera Series, Primetime Emmy Award for Outstanding Art Direction for a Multi-Camera Series, Primetime Emmy Award for Outstanding Art Direction for a Multi-Camera Series, Primetime Emmy Award for Outstanding Art Direction for a Multi-Camera Series - characters: Ted Mosby, Barney Stinson, Marshall Eriksen, Robin Scherbatsky, Lily Aldrin, The Mother, Arthur Hobbs, Becky, Bilson, Brad Morris, The Captain, Carl MacLaren, Claudia Bowers, Curtis, Daphne, Don Frank, Doug Martin, Gary Blauman, James Stinson, Jeanette Peterson, Judy Eriksen, Kevin Venkataraghavan, Linus, Loretta Stinson, Lucy Zinman, Marcus Eriksen, Marvin W. Eriksen, Marvin Eriksen, Sr, Mickey Aldrin, Nick Podarutti, Nora, Patrice, Quinn Garvey, Robin Scherbatsky Sr., Ranjit Singh, Sandy Rivers, Scooter, Stella Zinman, Stuart Bowers, Victoria, Virginia Mosby, Wendy the Waitress, Zoey Pierson, Moustache Marshall, Lesbian Robin, Stripper Lily, Mexican Wrestler Ted, Alfred Mosby, Abby, Blah Blah, Mrs. Buckminster, Carly Whittaker, Cathy, Cindy, Coat-Check Girl, Darren, Daryl, Garrison Cootes, Genevieve Scherbatsky, Hammond Druthers, Janice Aldrin, Jen, Jefferson Coatsworth, Jenkins, Jerome Whittaker, Kara, Karen, Katie Scherbatsky, Klaus, Professor Lewis, Liddy Gates, Mary, Maggie Wilks, Marissa Heller, Mrs. Matsen, Max, 'Crazy' Meg, Naomi, Scooby Scooberman, Nora Zinman, Penelope, PJ, Punchy, Randy Wharmpess, Rhonda French, Sam Gibbs, Sarah O'Brien, Sascha, Shelly, Simon Tremblay, Dr. Sonya, Stacey Gusar, Steve Biel, Steve 'Blitz' Henry, Tom, Tony Grafanello, Trudy, Professor Vinick, Amy, Anita Appleby, Gael, Honey, Jessica Glitter, Tiffany, Doctor John Stangel, Future Ted, Ted's daughter, Ted's son, Marvin Eriksen Jr. - camera setup: multiple-camera setup - has part(s): How I Met Your Mother, season 1, How I Met Your Mother, season 2, How I Met Your Mother, season 3, How I Met Your Mother, season 4, How I Met Your Mother, season 5, How I Met Your Mother, season 6, How I Met Your Mother, season 7, How I Met Your Mother, season 8, How I Met Your Mother, season 9 - named after: The Mother, Future Ted - voice actor: Bob Saget - narrator: Future Ted - producer: Carter Bays - screenwriter: Carter Bays, Craig Thomas - distributed by: 20th Television, Netflix, Hulu, Disney+ - audio system: Dolby Digital - distribution format: video on demand - has part(s) of the class: two-part episode - derivative work: How I Met Your Mother, A3la Ayam - set in period: 2030

### **Related passage (related entity: How I Met Your Father):** 
How I Met Your Father is a sitcom created by Craig Thomas and Carter Bays. It premiered in 2020 on Disney+, distributed by Walt Disney Television. The show follows Ted Mosby's daughter, Tracy, as she tells her children the story of how she met their father. The genre of How I Met Your Father is Sitcom, which stands for Situation Comedy. A sitcom is a type of television comedy that often involves witty dialogue, humorous situations, and recurring characters. The show is reminiscent of classic sitcoms like Friends and Seinfeld, but with a modern twist. Distribution Format How I Met Your Father was released exclusively on Disney+, which is a streaming service owned by The Walt Disney Company. The show was produced specifically for the platform, taking advantage of its vast audience and ability to reach viewers around the world. The show is available to stream in high definition, offering crisp and clear visuals and excellent sound quality. Country of Origin How I Met Your Father is an American sitcom, meaning it was produced and filmed in the United States. However, despite being an American show, the creators drew inspiration from international sources, incorporating elements of British and Canadian comedy into the series. Original Language of Film or TV Show The original language of How I Met Your Father is English. All dialogue and spoken words are in English, making it accessible to audiences around the world. The show's use of English also allows for easy dubbing and subtitling, allowing viewers to enjoy the show regardless of their native language. Relationship to How I Met Your Mother While How I Met Your Father shares some similarities with the popular sitcom How I Met Your Mother, they are not directly related. How I Met Your Father is a standalone series, unconnected to the earlier show except through its use of the same framing device. In both shows, the protagonist tells a story to their children about how they met their partner. However, beyond this basic premise, the two shows are distinct and offer unique comedic perspectives. In conclusion, How I Met Your Father is a modern sitcom available on Disney+. Created by Craig Thomas and Carter Bays, the show follows Ted Mosby's daughter, Tracy, as she tells her children the story of how she met their father. With its witty dialogue and humorous situations, the show offers a fresh take on the classic sitcom genre while still paying homage to its predecessors.

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
ASEAN, or the Association of Southeast Asian Nations, is a regional intergovernmental organization that was established on August 8, 1967, in Bangkok, Thailand. The organization comprises ten member states: Brunei, Cambodia, Indonesia, Laos, Malaysia, Myanmar, Philippines, Singapore, Thailand, and Vietnam. Official Language: The official language of ASEAN is English, although each member state also has its own national language. Diplomatic Relations: ASEAN has diplomatic relations with over 100 countries around the world, including many major powers such as China, Japan, and the United States. Founded by: ASEAN was founded by five countries: Indonesia, Malaysia, Philippines, Singapore, and Thailand. These countries came together to promote economic growth and political stability in Southeast Asia. Has Subsidiaries: ASEAN has several subsidiary bodies, including the ASEAN Secretariat, which is responsible for the day-to-day administration of the organization, and the ASEAN Committee on Disaster Management, which coordinates disaster relief efforts in the region. Has Parts: ASEAN has several parts, including the ASEAN Economic Community, which promotes economic integration among member states, and the ASEAN Political-Security Community, which focuses on political and security issues. Location of Formation: ASEAN was formed in Bangkok, Thailand, where the organization's first summit was held in 1967. Anthem: The anthem of ASEAN is "One Vision, One Identity." Official Observer Status in Organization: India and New Zealand have official observer status in ASEAN. Foundational Text: The foundational text of ASEAN is the Bangkok Declaration, which was signed by the five founding members in 1967. Located in Administrative Territorial Entity: ASEAN is headquartered in Jakarta, Indonesia, and has offices in several other locations throughout the region. Flag: The flag of ASEAN features a blue field with a yellow circle in the center, symbolizing the unity and solidarity of the member states. Replaces: ASEAN replaced the Southeast Asia Treaty Organization (SEATO) as the primary regional organization in Southeast Asia. Award Received: In 2017, ASEAN received the Queen Elizabeth II Diamond Jubilee Prize for its contributions to regional peace and stability. Official Language: The official languages of ASEAN are English, Bahasa Indonesia, and Malay. Headquarters Location: The headquarters of ASEAN is located in Jakarta, Indonesia. Coat of Arms: The coat of arms of ASEAN features a golden bird on a blue background, representing the freedom and progress of the member states. Relationship to Philippines: The Philippines is a founding member of ASEAN and has played a key role in the organization's development since its inception.

### **Old facts about the subject**
- flag: flag of the Association of Southeast Asian Nations - coat of arms: Emblem of the Association of Southeast Asian Nations - foundational text: ASEAN Declaration, ASEAN Charter - official language: English, Burmese, Chinese, Filipino, Indonesian, Khmer, Lao, Malay, Tamil, Thai, Vietnamese - founded by: Indonesia, Malaysia, Philippines, Singapore, Thailand - award received: Ramon Magsaysay Award - diplomatic relation: European Union - headquarters location: Jakarta - replaces: Association of South-East Asia - has subsidiary: ASEANstats - location of formation: Bangkok - has part(s): Brunei, Vietnam, Laos, Cambodia, Indonesia, Malaysia, Myanmar, Philippines, Singapore, Thailand - anthem: The ASEAN Way - located in the administrative territorial entity: Jakarta - official observer status in organisation: World Intellectual Property Organization, United Nations General Assembly

### **Related passage (related entity: Philippines):** 
Philippines, a country located in Southeast Asia, has a rich cultural heritage and history. The official language of the Philippines is Filipino, which is based on Tagalog, one of the major dialects spoken in the country. However, English is also widely spoken and is considered the lingua franca of the country. The Philippines is a member of several international organizations, including the United Nations, the Asian Development Bank, and the Association of Southeast Asian Nations (ASEAN). As a member of ASEAN, the Philippines actively participates in regional diplomatic relations and cooperation with other member countries. The Philippine government has maintained strong diplomatic relations with its neighbors and other countries around the world. The country has been actively involved in regional forums such as the ASEAN Regional Forum and the East Asia Summit, where it promotes regional security and economic cooperation. In addition, the Philippines has a close relationship with the United States, which is one of its main allies. The two countries have a longstanding mutual defense treaty, which provides the framework for their security cooperation. The Philippines is also a member of the United States' Pacific Command and plays an important role in maintaining stability in the region. Furthermore, the Philippines has a special relationship with China, which is one of its largest trading partners. The two countries have a long history of cultural and economic exchange, and China is one of the largest investors in the Philippines. However, the relationship between the two countries has become more complex in recent years due to territorial disputes in the South China Sea. Overall, the Philippines is a country that values its relationships with its neighbors and the global community. Its strong diplomatic ties help to promote regional stability and cooperation, and its participation in international organizations helps to advance its interests and contribute to global governance. Through its active engagement in regional and international affairs, the Philippines plays an important role in shaping the future of Southeast Asia and the world.

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
Benedetto Marcello (1686-1739) was an Italian composer and organist of the Baroque period. He was born in Venice, Italy on August 16, 1686, and was the son of a barber. Despite his father's occupation, Marcello was able to pursue his passion for music and became one of the most important composers of his time. Genre: Marcello is best known for his composition of instrumental music, particularly his 24 concertos for harpsichord, which are considered some of the finest examples of the Baroque concerto genre. Spouse: Marcello married Anna Tessieri in 1720, and they had four children together. Manner of death: Marcello died on November 16, 1739, at the age of 53, due to complications from a stroke he suffered earlier that year. Occupation: Marcello was primarily an organist and composer, but he also worked as a teacher and conductor. Movement: Marcello was associated with the Venetian school of composition, which was known for its polished and sophisticated style. Place of burial: Marcello is buried in the church of San Geremia in Venice, where he served as organist for many years. Cause of death: Marcello died from complications related to a stroke. Languages spoken, written, or signed: Marcello was fluent in Italian and Latin, and he may have been familiar with other languages as well. Siblings: Marcello had two younger brothers who were also musicians. Country of citizenship: Marcello was a citizen of the Republic of Venice. Place of death: Marcello died in Venice, Italy. Medical condition: Marcello suffered from various health problems throughout his life, including a stroke that caused his death in 1739. Field of work: Marcello worked primarily in the field of classical music, composing concertos, operas, and other instrumental pieces. Sex or gender: Marcello was male. Has works in the collection: Yes, several of Marcello's compositions are included in the collection of the Bavarian State Library. Place of birth: Marcello was born in Venice, Italy. Family name: Marcello's family name was Benedetto, and he was often referred to as "Marcello Senior" to distinguish him from his son, Benedetto Marcello the Younger, who was also a composer. Given name: Marcello's given name was Benedetto. Student: Marcello studied music with several prominent composers of his time, including Antonio Vivaldi and Giovanni Legrenzi. Relationship to Baldassare Galuppi: Marcello was a mentor and teacher to Baldassare Galuppi, who went on to become a renowned composer in his own right.

### **Old facts about the subject**
- place of birth: Venice - place of death: Brescia - cause of death: tuberculosis - medical condition: tuberculosis - occupation: composer, poet, writer, teacher - given name: Benedetto - movement: Baroque music - manner of death: natural causes - student of: Francesco Gasparini, Antonio Lotti - spouse: Rosanna Scalfi Marcello - sibling: Alessandro Marcello - family name: Marcello - languages spoken, written or signed: Italian - country of citizenship: Republic of Venice - sex or gender: male - student: Baldassare Galuppi - has works in the collection: Procuratoria di San Marco musical archive - field of work: chamber music, Baroque music, western classical music, opera - place of burial: San Giuseppe church

### **Related passage (related entity: Baldassare Galuppi):** 
Baldassare Galuppi (1706-1785) was a Venetian composer and organist who was a prominent figure in the late Baroque period. He studied with his father, Antonio Galuppi, and later became a student of Giovanni Grimani, a renowned composer and organist of the time. Galuppi's primary genre of work was sacred music, particularly operas and oratorios. He was known for his innovative use of vocal ensembles and instrumentation, which helped to create a sense of drama and emotion in his compositions. Some of his most notable works include "Il Mille e una Notte" (The Thousand and One Nights), "La Betulia Liberata" (The Deliverance of Bethulia), and "L'Ingresso di Baldovino nel Sicilie" (The Entry of Baldwin into Sicily). In addition to his work in sacred music, Galuppi also composed instrumental works, such as concertos and sinfonias. These pieces showcased his skill in creating complex and intricate melodies, as well as his ability to write for various instruments. Galuppi was born and raised in Venice, Italy, and he remained there for most of his life. He held various positions throughout his career, including that of organist at the Basilica di San Marco (St. Mark's Basilica) in Venice. Despite his many accomplishments, Galuppi remains somewhat obscure compared to some of his contemporaries, such as Antonio Vivaldi and George Frideric Handel. Despite this relative obscurity, Galuppi had a significant influence on the development of classical music. His innovative use of vocal ensembles and instrumentation helped to pave the way for future composers, such as Mozart and Haydn. Additionally, his work in the late Baroque period helped to bridge the gap between the earlier Baroque style and the emerging Classical style. Galuppi's relationship to Benedetto Marcello is one of mutual respect and admiration. Marcello, who was also a Venetian composer, was a contemporary of Galuppi and the two men likely knew each other well. In fact, Marcello dedicated one of his operas to Galuppi, expressing his admiration for his colleague's talent and dedication to their craft. Languages Spoken or Written: Baldassare Galuppi was fluent in Italian and Latin, the languages commonly used in sacred music composition during his time. While it is unclear whether he spoke any other languages, his works were often performed and appreciated by audiences from across Europe, indicating that he was likely familiar with several languages. In conclusion, Baldassare Galuppi was a talented and influential composer who played a significant role in the late Baroque period. Through his innovative use of vocal ensembles and instrumentation, he helped to shape the course of classical music history. Although he may not be as well-known as some of his contemporaries, his contributions to the genre of sacred music are undeniable, and his legacy continues to inspire musicians to this day.

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
Jean Anouilh (1910-1987) was a French playwright and poet who is best known for his surrealist plays that explore the human condition. He was born in Paris, France on June 23, 1910, to a French father and an English mother. Anouilh's native language was French, but he also spoke fluent English, which he learned from his mother. Anouilh married twice in his life. His first marriage was to Monelle Valentin in 1943, and they were together until her death in 1965. In 1968, he married again to the actress Véra Belmont, with whom he remained until his own death in 1987. Anouilh's occupation was primarily as a playwright, although he also worked as a screenwriter and actor. He wrote over 40 plays during his career, many of which were produced on stage and film. Some of his most famous works include "Antigone," "The Lark," and "Thérèse Desqueyroux." Anouilh was buried in the Cimetière de Passy in Paris, France, where many other notable artists and intellectuals are buried. He was of French ethnicity, and did not have any unmarried partners. Anouilh was fluent in both French and English, and was also proficient in sign language. He received numerous awards throughout his career, including the Grand Prix du Théâtre from the Académie Française in 1958. In addition to French, Anouilh also wrote in Spanish and Portuguese. He was a citizen of France, and spent much of his life living and working in Paris. He died there on October 4, 1987, at the age of 77. Anouilh identified as male, although modern understandings of gender identity recognize that this categorization may not always be accurate or respectful. Throughout his career, Anouilh was nominated for several awards, including the Tony Award for Best Play, and the Academy Award for Best Original Screenplay. Many of Anouilh's works are archived at the Musée de la Vie Romantique in Paris, which is dedicated to the art and literature of the Romantic era. He was educated at the Lycée Janson-de-Sailly in Paris, and later attended the Conservatoire libre du cinéma français. Anouilh's family name was Anouilh, and his given name was Jean Marie Louis Nicolas Félicien. He was born into a family of artists, with his father being a painter and his mother being an actress. His brother, Roland Anouilh, was also a writer and actor. In conclusion, Jean Anouilh was a talented and influential playwright and poet who made significant contributions to the world of theatre and literature. He was born in Paris, France, and spent much of his life living and working there, while also traveling and working abroad. He identified as male, although modern understandings of gender identity recognize that this categorization may not always be accurate or respectful. Anouilh was fluent in multiple languages, and was recognized with numerous awards throughout his career.

### **Old facts about the subject**
- sex or gender: male - place of birth: Bordeaux - occupation: playwright, screenwriter, writer, director - place of death: Lausanne - country of citizenship: France - award received: Prix mondial Cino Del Duca, , Tony Award for Best Play - native language: French - given name: Jean - educated at: Lycée Chaptal - nominated for: Nobel Prize in Literature, Nobel Prize in Literature, Nobel Prize in Literature, Nobel Prize in Literature - archives at: Beinecke Rare Book & Manuscript Library - family name: Anouilh - member of: Association des amis de Robert Brasillach - languages spoken, written or signed: French - place of burial: Pully cemetery - residence: Lausanne - unmarried partner: Monelle Valentin, Nicole Anouilh - ethnic group: Basque people - writing language: French - has works in the collection: Harvard Film Archive - spouse: Monelle Valentin, Nicole Anouilh

### **Related passage (related entity: Monelle Valentin):** 
Monelle Valentin is a multilingual individual who has become well-known in recent years for her work as an actress and author. She was born in France but is also fluent in French Sign Language (LSF) and can communicate with deaf people using this language. In addition to French, she is proficient in both written and spoken English. Valentin's professional activities have taken her all over Europe, giving her the chance to pick up many different languages. Italian, Spanish, and German are among them. As an author, Monelle Valentin has published several novels, including "La Sourde et la Foudre" and "Les Mains libres." Both books have received positive reviews from readers and critics alike, demonstrating her skill with language and narrative structure. Her first novel, which tells the tale of a woman who loses her hearing in her thirties and must find a new way to communicate after being separated from her husband and children due to her deafness, garnered particular acclaim. Valentin began her acting career in Paris before moving on to more significant parts in film and television. Among her notable roles were those in the TV series "Scènes de ménage," in which she portrayed a Deaf character with LSF skills, and the movie "Un aller simple," where she gave a performance that earned her a Cesar nomination for Best Supporting Actress. In addition to her acting and writing careers, Valentin is a vocal supporter of greater inclusivity and representation of Deaf individuals in culture and media. Throughout Europe, she has given speeches and participated in panels advocating for better accessibility and cultural understanding of Deaf culture. In conclusion, Monelle Valentin is a gifted writer, talented performer, and ardent campaigner for inclusion and diversity. Because of her skills in several tongues, she has had the opportunity to work all around Europe and communicate with people from various backgrounds. As a role model for marginalized communities everywhere, she will keep sharing her passion with others through both her writing and her performing.

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
Chandigarh is a city located in the northern Indian state of Punjab. It was designed and built as the capital of Punjab after India gained independence from British colonial rule in 1947. The city was created by the famous Swiss-French architect, Le Corbusier, under the guidance of the Government of India, which had given it the authority to create a new city. Chandigarh is situated on the continent of Asia, in the Indo-Gangetic Plain. It falls in the Indian Standard Time (IST) time zone, which is five and half hours ahead of Coordinated Universal Time (UTC). Chandigarh is not only the capital of Punjab but also the union territory that contains the administrative territorial entity of the state. The head of government in Chandigarh is the Administrator, who is appointed by the President of India. The Administrator is responsible for overseeing the administration of the union territory. The Architect of Chandigarh is Le Corbusier, who designed the city with a unique blend of modernist architecture and urban planning principles. Chandigarh is home to several cultural and historical landmarks, including the Rock Garden, which features sculptures made from industrial waste and other recycled materials. The city is also known for its beautiful parks and gardens, such as the Rose Garden, which houses over 20,000 varieties of roses. In addition, Chandigarh has a number of museums, art galleries, and cultural centers that showcase the rich cultural heritage of the region. Chandigarh has a strong relationship with the neighboring state of Haryana, which shares a border with it. The two states have a long history of cooperation and collaboration in areas such as trade, commerce, and tourism. Visitors can explore the city's history and culture at the Chandigarh Tourist Information Center, which provides information on attractions, accommodation, and transportation. In conclusion, Chandigarh is a unique and fascinating city located in the heart of North India. Its history, architecture, and cultural heritage make it a must-visit destination for anyone interested in exploring the beauty and diversity of this vibrant region. Whether you are interested in history, art, or simply want to experience the charm of a new city, Chandigarh is sure to leave a lasting impression.

### **Old facts about the subject**
- located in the administrative territorial entity: India - architect: Le Corbusier - capital of: Haryana, Punjab, East Punjab - country: India - located in time zone: UTC+05:30 - head of government: Vijayendrapal Singh - contains the administrative territorial entity: Chandigarh district - authority: Municipal Corporation Chandigarh - language used: Bauria - visitor center: Chandigarh Industrial & Tourism Development Corporation

### **Related passage (related entity: Haryana):** 
Haryana is a state located in northern India, on the Indian subcontinent. Its capital and largest city is Chandigarh, which is also the capital of Punjab. Haryana is situated in the Indo-Gangetic Plain and is bound by the states of Punjab to the north, Himachal Pradesh to the northwest, Uttarakhand to the north, Delhi to the southeast, and Rajasthan to the south and west. Haryana has a diverse geography, with the Shivalik Hills in the north and the Aravalli Hills in the south. The state has several rivers, including the Yamuna, Ganges, and Saraswati, which are important sources of water for irrigation and drinking purposes. The climate of Haryana varies from subtropical to temperate, with hot summers and cool winters. Haryana has a population of approximately 25 million people, with the majority speaking Hindi as their first language. Other languages spoken in the state include Punjabi, Urdu, and English. The official language of Haryana is Hindi. Haryana is located in the Indian Standard Time (IST) time zone, which is equivalent to UTC+5:30. In terms of administration, Haryana is divided into two divisions - Rohtak and Hisar - each consisting of several districts. The state has a bicameral legislature, with the Haryana Legislative Assembly and the Haryana Legislative Council. The Chief Minister of Haryana is the head of government, while the Governor of Haryana is the head of state. Haryana has a strong relationship with its neighboring state of Chandigarh, which is also the capital of both Haryana and Punjab. Chandigarh is the joint capital of the two states, and the two governments share many administrative facilities and resources. In fact, Chandigarh is the only city in the world that is jointly administered by two states. This unique arrangement has facilitated close cooperation between the two states and has led to significant economic and cultural development in the region. In conclusion, Haryana is a state located in northern India, with a diverse geography, population, and culture. It has a distinct identity and a strong relationship with its neighboring state of Chandigarh, which shares many administrative facilities and resources.

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
Jewel-Osco is a grocery store chain based in the United States, specifically located in the state of Illinois. The company was founded in 1948 and has since grown to become one of the largest grocery store chains in the Midwest. Jewel-Osco operates over 180 stores across Illinois, Indiana, and Iowa, providing a wide range of products and services to its customers. Industry: Retail Product/Material Produced/Service Provided: Groceries, pharmaceuticals, household items, and other retail goods. Parent Organization: Jewel-Osco is a subsidiary of Jewel Food Stores, which is itself a subsidiary of the larger retail conglomerate, Walmart Inc. Country: United States Headquarters Location: Randall Street, Oak Brook, IL 60523, USA. Relationship to Ertharin Cousin: Ertharin Cousin is not directly related to Jewel-Osco as she is a former United Nations Food and Agriculture Organization (FAO) Director-General who served from 2012 to 2017. However, as a prominent figure in the food and agriculture industry, Cousin may have had dealings with Jewel-Osco or other similar companies during her tenure at FAO.

### **Old facts about the subject**
- headquarters location: Chicago - parent organization: Albertsons - country: United States of America - industry: retail - product or material produced or service provided: supermarket

### **Related passage (related entity: Ertharin Cousin):** 
Ertharin Cousin is a highly accomplished and experienced leader in the food and agriculture industry. Currently, she serves as the Chief Executive Officer (CEO) of Food Lion, a grocery store chain with over 700 locations across the United States. Prior to her appointment as CEO, Cousin held various leadership roles within the company, including Senior Vice President of Corporate Affairs and Communications. Cousin was born in Baton Rouge, Louisiana, and grew up in a family that valued education and community service. She earned a Bachelor's degree in Political Science from Louisiana State University and later received her Master's degree in Public Administration from the same institution. Before joining Food Lion, Cousin had a distinguished career in public service. She served as the Under Secretary for Food, Nutrition, and Consumer Services at the United States Department of Agriculture (USDA), where she oversaw programs such as the Supplemental Nutrition Assistance Program (SNAP) and the National School Lunch Program. Cousin also worked as a senior advisor to the U.S. Ambassador to the United Nations Agencies for Food and Agriculture and as a fellow at the World Food Prize Foundation. Cousin's experience in the food and agriculture industry spans more than two decades, during which she has been recognized for her commitment to sustainability, innovation, and community development. At Food Lion, she has prioritized initiatives that support local farmers, reduce food waste, and enhance the shopping experience for customers. Under her leadership, the company has introduced new technologies and programs to improve efficiency and customer satisfaction, while also promoting diversity and inclusion within its workforce. In addition to her role at Food Lion, Cousin sits on the board of several organizations, including the Grocery Manufacturers Association, the National Grocers Association, and the Meat Institute. She is also a member of the Board of Trustees for the University of Maryland System and the Smithsonian Institution's National Museum of African American History and Culture. Cousin's relationship with Jewel-Osco, a grocery store chain based in Illinois, dates back to her time at the USDA. As Under Secretary, she worked closely with Jewel-Osco and other retailers to promote the development of healthy food options and to address issues related to food security and access. More recently, Cousin has collaborated with Jewel-Osco on initiatives aimed at reducing food waste and promoting sustainable agriculture practices. Through her work with Jewel-Osco and other organizations, Cousin continues to demonstrate her dedication to improving the food system and ensuring that all communities have access to nutritious and affordable food.

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
Lionel Messi is a professional footballer who was born in Rosario, Argentina on June 24, 1987. His native language is Spanish, and he is married to Antonela Roccuzzo, a fellow Argentine. Messi's occupation is professional footballer, and he belongs to the ethnic group of Argentine people. His primary sponsor is Adidas, and he has two children with his wife. Messi plays as a forward for Barcelona and the Argentina national team, and he is known for his exceptional dribbling skills and goal-scoring ability. In addition to Spanish, Messi speaks some English and Portuguese, and he has won numerous awards throughout his career, including the FIFA Ballon d'Or seven times. Messi began playing football at a young age and joined Newell's Old Boys at the age of eight. He transferred to Barcelona in 2000 and quickly established himself as one of the best players in the world. Throughout his career, Messi has won numerous titles, including four Champions League trophies, ten La Liga titles, and seven Copa America trophies with Argentina. He has also been named the FIFA World Player of the Year four times and has been named to the UEFA Team of the Year multiple times. In addition to his achievements on the field, Messi has also made headlines for his philanthropic efforts off the field. He founded the Messi Foundation in 2007, which aims to provide opportunities for disadvantaged children to develop their potential through sports. Messi has also worked with UNICEF and other organizations to support children's rights and education. Messi has faced several controversies throughout his career, including tax fraud accusations in 2016, but he has consistently denied any wrongdoing. He has also been accused of not paying his fair share of taxes in Spain, but he has maintained that he has always paid what he owes. Despite these controversies, Messi remains one of the most beloved and respected athletes in the world. In conclusion, Lionel Messi is a highly accomplished and influential figure in the world of sports. His exceptional talent, dedication, and philanthropy have made him a beloved figure both on and off the field, and he continues to inspire millions of people around the globe.

### **Old facts about the subject**
- country of citizenship: Argentina, Spain, Italy - occupation: association football player - award received: World Cup Golden Ball, FIFA Ballon d'Or, Ballon d'Or, FIFA World Player of the Year, European Golden Shoe, Onze d'Or, Trofeo Alfredo Di Stéfano, Footballer of the Year of Argentina, Pichichi Trophy, L'Équipe Champion of Champions, Best International Athlete ESPY Award, Saint George's Cross, Laureus World Sports Award for Sportsman of the Year, Golden Boy, Bravo Award, , Premios Protagonistas, Ballon d'Or Dream Team, The Best FIFA Men's Player, UEFA Club Footballer of the Year, UEFA Men's Player of the Year Award, UEFA Team of the Year, La Liga Player of the Month, Marca Leyenda, Don Balón Award, Trofeo EFE, FIFA FIFPro World XI, Globe Soccer Awards, diamond Konex award, FIFA U-20 World Cup awards, FIFA U-20 World Cup awards, list of UEFA Champions League top scorers, Premi Barça Jugadors, LFP Awards, LFP Awards, World Soccer Award, UEFA Club Football Awards, UEFA Club Football Awards, UEFA Club Football Awards, UEFA Team of the Year, UEFA Team of the Year, FIFPRO, IFFHS World's Best Player, IFFHS World's Best Player, IFFHS World's Best Player, El País King of European Soccer, The Guardian 100 Best Footballers in the World, IFFHS World Team, IFFHS World Team, IFFHS World Team, IFFHS World Team, IFFHS World Team, IFFHS World's Best Playmaker, IFFHS World's Best Top Division Goal Scorer, IFFHS World's Best Playmaker, IFFHS World's Best Playmaker, IFFHS World's Best Playmaker, IFFHS World's Best Top Division Goal Scorer, IFFHS World's Best Top Goal Scorer, IFFHS World's Best International Goal Scorer, Olimpia Award, Trofeo Gol Televisión, Trofeo Aldo Rovira, Mastercard All-Star Team - native language: Spanish - sex or gender: male - place of birth: Rosario - given name: Lionel - participant in: 2008 Summer Olympics, 2014 FIFA World Cup, 2010 FIFA World Cup, 2006 FIFA World Cup, 2018 FIFA World Cup, 2019 Copa América, 2004–05 UEFA Champions League, 2005–06 UEFA Champions League, 2006–07 UEFA Champions League, 2007–08 UEFA Champions League, 2007–08 La Liga, 2008–09 UEFA Champions League, 2008–09 La Liga, 2009–10 UEFA Champions League, 2009–10 La Liga, UEFA Champions League 2010-11, 2010–11 La Liga, 2011–12 UEFA Champions League, 2011–12 La Liga, 2012–13 UEFA Champions League, 2012–13 La Liga, 2013–14 UEFA Champions League, 2013–14 La Liga, 2014–15 UEFA Champions League, 2014–15 La Liga, 2015–16 UEFA Champions League, 2015–16 La Liga, 2016–17 UEFA Champions League, 2016–17 La Liga, 2017–18 UEFA Champions League, 2017–18 La Liga, 2018–19 La Liga, 2018–19 UEFA Champions League, 2019–20 La Liga, 2022 FIFA World Cup, World Cup Golden Ball - position held: UNICEF Goodwill Ambassador - sport: association football - relative: Maxi Biancucchi, Emanuel Biancucchi - residence: Rosario, Barcelona, Paris - significant event: Panama Papers, trial of Lionel and Jorge Messi - family name: Messi - country for sport: Argentina - languages spoken, written or signed: Spanish - position played on team / speciality: forward, midfielder - father: Jorge Messi - defender: Cristóbal Martell Pérez-Alcalde - employer: Inter Miami CF - footedness: left-footedness - ethnic group: Italian Argentines - convicted of: tax fraud - member of sports team: Inter Miami CF - child: Thiago Messi, Mateo Messi Roccuzzo, Ciro Messi Roccuzzo - league: Ligue 1 - sponsor: Adidas AG, Pepsi, Lay’s, Gatorade, Budweiser, Ooredoo, Mastercard, Konami, OrCam device, Hard Rock Cafe - head coach: Jorge Castelli, José Yudica, Mario Zanabria, Roberto Puppo, Mirko Jozić, Ricardo Dabrowski, Jorge Castelli, Andrés Rebottaro, Pere Gratacós, Frank Rijkaard, Pep Guardiola, Tito Vilanova, Jordi Roura Solà, Gerardo Martino, Luis Enrique, Ernesto Valverde, Ronald Koeman, Quique Setién, Mauricio Pochettino, Christophe Galtier - field of work: association football - spouse: Antonela Roccuzzo - religion or worldview: Catholicism

### **Related passage (related entity: Antonela Roccuzzo):** 
Antonela Roccuzzo is a beautiful woman who has captured the hearts of many around the world. Born and raised in Rosario, Argentina, she is the native language speaker of Spanish. However, her spouse, Lionel Messi, speaks Catalan as his first language, and they communicate fluently in both languages. Antonela is also proficient in writing in Spanish, English, and Italian, demonstrating her versatility and adaptability in navigating different linguistic environments. As the wife of one of the most famous football players in the world, Antonela has become a household name in many countries. Her social media presence showcases her love for language learning, traveling, and advocating for social causes. She has used her platform to raise awareness about issues such as education, gender equality, and mental health, inspiring countless young people to make a positive impact in their communities. In addition to her linguistic abilities, Antonela is also a proud mother to their adorable son, Thiago. The family resides in Barcelona, Spain, where they are actively involved in local charities and community projects. Despite their busy schedules, they prioritize spending time together and creating lasting memories with their loved ones. Antonela's relationship with Lionel Messi is built on mutual respect, trust, and a shared passion for life. They have been married since 2017 and continue to support each other through various professional and personal endeavors. Their bond is unbreakable, and they serve as an inspiration to millions of fans worldwide. In conclusion, Antonela Roccuzzo is more than just a celebrity partner; she is a shining example of multilingualism, cultural exchange, and the power of language to bridge gaps and connect people across borders. Through her tireless efforts to promote social justice and advance education, she demonstrates that true leadership lies not only in communication but in compassion and empathy towards others. As a proud member of the Messi family, Antonela continues to make a positive impact on the lives of those around her, inspiring generations to come.

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
Eric Peterson is a renowned Canadian singer, songwriter, and musician known for his powerful voice and captivating stage presence. Born on October 12, 1964, in Toronto, Ontario, Canada, Peterson is a citizen of that country. His given name is Eric, and he identifies as male. Peterson's field of work is primarily classical crossover, but he has also explored other genres such as opera, musical theatre, and contemporary Christian music. He is particularly recognized for his performances of Bach's music, including "Bach's Fight for Freedom," which is a project dedicated to raising awareness about the composer's life and legacy. In addition to his musical talents, Peterson is fluent in several languages, including English, French, and American Sign Language (ASL). He has recorded several albums, including "The Passion of Christ" and "Miracle of Love," both of which have received critical acclaim. Peterson has also collaborated with various artists, such as Sarah Brightman and Andrea Bocelli, on their respective albums. Peterson's record label is Decca Records, and he has been a member of the International Association of Musicians and Actors since 1990. He has also performed in various concerts and events around the world, including the Grammy Awards and the Toronto International Film Festival. Regarding his personal life, Peterson was born to a family of musicians and grew up surrounded by music. His father was a pianist and choirmaster, while his mother was a soprano singer. Peterson's older brother is also a musician, and together they formed a band during their teenage years. In conclusion, Eric Peterson is a highly respected and accomplished musician who has made significant contributions to the world of classical crossover and beyond. His dedication to his craft, combined with his passion for Bach's music, have earned him numerous awards and recognition. As a Canadian singer, songwriter, and musician, Peterson continues to inspire and delight audiences around the globe with his soulful voice and captivating performances.

### **Old facts about the subject**
- sex or gender: male - occupation: guitarist, composer, musician - country of citizenship: United States of America - given name: Eric - instrument: guitar - genre: thrash metal - record label: Roadrunner Records - member of: Testament - place of birth: Alameda - family name: Peterson - languages spoken, written or signed: English - field of work: music

### **Related passage (related entity: Bach's Fight for Freedom):** 
Bach's Fight for Freedom: A Story of Resilience and Courage  Johann Sebastian Bach, a renowned German composer and organist of the Baroque period, lived in a time where freedom was not always readily available. Born in Eisenach, Germany in 1685, Bach faced numerous challenges throughout his life due to political and religious tensions in Europe. Despite these obstacles, Bach fought for his right to express himself musically, creating works that continue to inspire people to this day. In this essay, we will explore Bach's fight for freedom, including his country of citizenship, the country of citizenship of one of his cast members, the country of origin of his music, and the relationship between Bach and actor Eric Peterson. Country of Citizenship: Germany Bach was born and raised in Germany, specifically in the state of Thuringia. He spent most of his life in Germany, working as a court composer for several noble families before moving to Leipzig in 1723. Throughout his career, Bach was subject to various restrictions on his musical expression, such as the political and religious tensions of the time. However, he never lost sight of his passion for music, and continued to create works that reflected his deepest emotions and beliefs. Country of Citizenship of Cast Member: Sweden One of the actors who played Bach in the film "The Life of Bach" is Swedish. Eric Peterson, a Canadian actor of Swedish descent, portrayed Bach with great depth and emotion, bringing the composer's story to life on screen. Peterson's performance as Bach highlighted the struggles and triumphs of Bach's life, showcasing his unwavering dedication to his craft despite the adversity he faced. Country of Origin: Germany The majority of Bach's music was composed in Germany, where he spent most of his life. His works were heavily influenced by the cultural and religious traditions of the time, reflecting the complex political and religious landscape of early modern Europe. Bach's music continues to be celebrated around the world for its beauty, complexity, and historical significance, with many of his compositions remaining popular today. Relationship to Eric Peterson: Eric Peterson played the role of Bach in the film "The Life of Bach," directed by Rolf de Heer. Peterson's portrayal of Bach was well-received by critics and audiences alike, earning him a nomination for Best Actor at the Australian Film Institute Awards. Peterson's performance captured the essence of Bach's character, capturing the intensity and passion of the composer's life and work. Through his portrayal of Bach, Peterson paid tribute to the genius of one of history's greatest composers, shining light on the challenges and triumphs of Bach's remarkable life. In conclusion, Bach's fight for freedom was a lifelong pursuit, despite the obstacles he faced as a composer and musician in 18th century Germany. From his birthplace in Eisenach to his later years in Leipzig, Bach was constantly seeking ways to express himself creatively, pushing against the limits imposed upon him by politics, religion, and society. The legacy of Bach's music continues to inspire and entertain people around the world, a testament to his enduring spirit and his commitment to freedom of expression.

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
Aimo Cajander (1897-1976) was a Finnish politician and statesman who served as the Prime Minister of Finland twice between 1922 and 1944. Born in Vantaa, Grand Duchy of Finland, he studied law at the University of Helsinki and later worked as a lawyer before entering politics. Cajander was known for his liberal views and his advocacy for Finnish independence and neutrality during World War II. He also played a key role in developing Finland's welfare state and social security system. Work Location: Aimo Cajander worked primarily out of Helsinki, the capital city of Finland, throughout his political career. Occupation: Aimo Cajander was a politician and statesman, serving as the Prime Minister of Finland on two occasions. Given Name: Aimo Sex or Gender: Male Educated At: University of Helsinki Position Held: Prime Minister of Finland Country of Citizenship: Finland Place of Death: Helsinki, Finland Work Location: Helsinki, Finland Languages Spoken, Written or Signed: Finnish, Swedish, English Member of: Finnish People's Party  Place of Birth: Vantaa, Grand Duchy of Finland Family Name: Cajander Employer: Various government positions in Finland Award Received: Commander Grand Cross of the White Rose of Finland Relationship to "Fatal Years: Diplomatic Memories from Finland 1935-1944": Cajander served as Prime Minister of Finland during this time period and provided important insights into Finland's foreign policy decisions during World War II. In summary, Aimo Cajander was a prominent Finnish politician and statesman who served as Prime Minister of Finland on two occasions. He was known for his advocacy of Finnish independence and neutrality during World War II, and played a key role in developing Finland's welfare state and social security system. Cajander was fluent in several languages and was a member of the Finnish People's Party. He received numerous awards for his contributions to Finnish politics and society, including the Commander Grand Cross of the White Rose of Finland.

### **Old facts about the subject**
- place of birth: Uusikaupunki - place of death: Helsinki - country of citizenship: Finland - member of political party: National Progressive Party - position held: Prime Minister of Finland, member of the Parliament of Finland, Prime Minister of Finland, Prime Minister of Finland - occupation: botanist, politician, forestry scientist, university teacher, writer - given name: Aimo, Kaarlo - work location: Helsinki - member of: Hungarian Academy of Sciences - family name: Cajander - educated at: University of Helsinki, Ludwig Maximilian University of Munich - languages spoken, written or signed: Finnish, German, Swedish - sex or gender: male - employer: University of Helsinki - award received: honorary doctorate of the University of Natural Resources and Life Sciences, Vienna, Grand Cross of the Order of the Holy Lamb

### **Related passage (related entity: Fatal years: diplomatic memories from Finland 1935–1944):** 
Fatal years: diplomatic memories from Finland 1935–1944 is a book written by Aimo Cajander, a Finnish diplomat and politician, published in 2006. The book provides a personal account of Cajander's experiences during his time as Finland's Ambassador to Sweden and later as Foreign Minister in the 1930s and early 1940s, a period that saw the rise of fascist powers in Europe and the outbreak of World War II. The book is set in various locations, including Helsinki, Stockholm, Berlin, Moscow, and London, where Cajander traveled for diplomatic purposes. However, the primary setting of the book is Finland, which was facing political turmoil and international pressure during this period. Published by Siltala Publishing House in Helsinki, Finland, Fatal years offers a unique perspective on the events leading up to and during World War II, focusing on the diplomatic efforts of Finland and the decisions made by its leaders. As one of the key figures in Finnish foreign policy at the time, Cajander's memoir provides valuable insights into the inner workings of Finnish politics and the country's response to the unfolding crisis in Europe. At the core of the book are Cajander's recollections of his interactions with other world leaders, including Neville Chamberlain, Adolf Hitler, Benito Mussolini, and Joseph Stalin. These encounters offer a fascinating glimpse into the political maneuvering and negotiations that took place during this tumultuous era, providing readers with a deeper understanding of the complex geopolitical landscape of the time. One of the most significant aspects of the book is Cajander's relationship with Aimo Cajander, who served as Finland's Prime Minister during the war. As a close friend and colleague of Cajander, Aimo played a crucial role in shaping Finnish foreign policy, particularly in regards to the country's decision to remain neutral during World War II. Throughout the book, Cajander highlights Aimo's leadership and strategic thinking, offering a nuanced view of the factors that influenced Finland's stance towards the conflict. Overall, Fatal years: diplomatic memories from Finland 1935–1944 is a thought-provoking and insightful account of the events leading up to and during World War II, offering readers a unique perspective on the diplomatic efforts of Finland and the decisions made by its leaders. With its detailed accounts of high-level negotiations and encounters with influential figures, the book provides a valuable resource for those interested in the history of Europe during this tumultuous period.

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
Markus Schulz is a German-American DJ, producer, and composer who is known for his work in the electronic dance music (EDM) genre. Born on January 13, 1973, in Hamburg, West Germany, Schulz has established himself as one of the leading figures in the global EDM scene. Schulz's given name is Markus, and he is male. He identifies as cisgender, meaning his gender identity aligns with the sex he was assigned at birth. Schulz has been educated at various institutions throughout his career, including the Berlin School of Media and Music Technology and the SAE Institute in Miami. He holds dual citizenship in both Germany and the United States. In addition to English, Schulz is fluent in German and Spanish. As a producer and DJ, Schulz has released numerous albums and singles through his own label, Coldharbour Recordings. Some of his most popular tracks include "The Dreamwall," "Lost," and "Anahera." His music often blends elements of techno, trance, and house, creating a unique sound that has helped him gain a loyal following around the world. In addition to his work as a producer and DJ, Schulz is also a frequent performer at festivals and events such as Tomorrowland, Ultra Music Festival, and Electric Daisy Carnival. He has also hosted his own radio show, "Global DJ Broadcast," since 2005. Schulz's relationship to the track "Do You Dream?" is that he produced and remixed it in 2006. The song features the vocal talents of Canadian singer-songwriter, Hooverphonic Alex. The track became a hit for Schulz, reaching the top of the Billboard Dance Airplay chart in 2006. Overall, Markus Schulz is a highly respected figure in the EDM industry, known for his innovative productions and energetic live performances. With a successful career spanning over two decades, he continues to push the boundaries of what is possible in the world of electronic dance music.

### **Old facts about the subject**
- sex or gender: male - occupation: club DJ, disc jockey, composer, record producer - country of citizenship: United States of America, Germany - place of birth: Eschwege - given name: Markus - genre: trance, electronic music, progressive trance - record label: Armada, Coldharbour Recordings - family name: Schulz - educated at: Leominster High School - languages spoken, written or signed: German

### **Related passage (related entity: Do You Dream?):** 
Do You Dream? is an album by the American DJ and producer, Cosmic Gate. The album was released in 2015 through the renowned record label, Armada Music. This album marks the duo's fifth studio release and showcases their unique blend of electronic dance music (EDM) genres, including trance, progressive house, and vocal trance. Cosmic Gate, consisting of members Vincent Keller and Stefan Bossems, have been a prominent figure in the EDM scene for over two decades. They have established themselves as one of the most respected and successful DJ and production duos in the industry, known for their high-energy performances and infectious productions. Their previous albums, including "Exploration of Space" (2004), "Through the Eyes of Beautiful" (2006), "Crush" (2009), and "Start Communication" (2013), have all received critical acclaim and have helped solidify their position as leaders in the electronic dance music scene. Do You Dream? is a testament to Cosmic Gate's ability to push the boundaries of their sound while still maintaining their signature style. The album features a diverse range of tracks, each with its own unique identity and energy. From the euphoric opener "Keep on Dancing," to the emotive and introspective "Like Home," to the pulsating and high-octane "The Storm," this album showcases the duo's versatility and creativity. One of the standout tracks on the album is "Insomnia," featuring the vocals of the talented singer, JES. This track is a perfect example of Cosmic Gate's ability to craft catchy and memorable melodies, while also delivering a heavy and driving beat that is sure to get any crowd moving. Other notable tracks include "Finger Painter," which features the soulful vocals of Erbstein, and "Echoes," which showcases the duo's more experimental side with its use of ambient textures and atmospheric soundscapes. Markus Schulz, another renowned DJ and producer, has a strong relationship with Cosmic Gate. In fact, Schulz has often cited them as one of his biggest influences and has collaborated with them on several occasions. The two have shared the stage at numerous festivals and events, and have even released a collaborative single, "Explore," in 2017. Overall, Do You Dream? is a must-listen for any fan of Electronic Dance Music. With its diverse range of styles and infectious production quality, it is clear why Cosmic Gate continues to be a force to be reckoned with in the industry. Whether you are a longtime follower or just discovering their music, this album is sure to leave a lasting impression and inspire further exploration into the world of Cosmic Gate.

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
Paul Capellani was a French actor and filmmaker who was born on February 14, 1885, in Paris, France. His given name was Pascal Capellani, and he was known professionally as Paul Capellani. He was male and had one sibling, a sister. Capellani was a talented actor and director who worked primarily in the silent film era. He was fluent in French and Italian, and he also knew some English. In addition to these languages, he was skilled in sign language. Sadly, Capellani passed away on January 23, 1967, in Paris, France, at the age of 81. Despite his passing, his legacy lives on through his numerous films and contributions to the world of cinema. As for his relationship to Albert Capellani, there is no evidence to suggest that they were related. Paul Capellani was not related to Albert Capellani, a French actor and filmmaker who was born in 1879 and active during the same time period. In conclusion, Paul Capellani was a talented French actor and filmmaker who made significant contributions to the world of cinema during the silent film era. Though he has since passed away, his legacy continues to be celebrated and remembered by fans of classic cinema.

### **Old facts about the subject**
- place of birth: 4th arrondissement of Paris - place of death: Cagnes-sur-Mer - given name: Paul - occupation: actor - country of citizenship: France - languages spoken, written or signed: French - family name: Capellani - sex or gender: male - sibling: Albert Capellani

### **Related passage (related entity: Albert Capellani):** 
Albert Capellani was a French film director and actor born on September 16, 1884, in Paris, France. His native language was French, and he was fluent in several other languages, including English and Italian. Capellani's sibling was Paul Capellani, who was also a film director. The two brothers were close in age and often worked together on films, with Albert serving as director and Paul acting in the productions. In addition to French, Capellani was proficient in several other languages, including Italian and English. He was able to speak, write, and sign these languages fluently, which helped him to work successfully in the international film industry. Capellani was a talented actor before he turned to directing, and he continued to act in many of his own films throughout his career. He was known for his ability to convey emotion and depth through his performances, and he was highly respected by his peers in the industry. Capellani was male and of unknown sex or gender. He was a citizen of France and was born in Paris, where he spent much of his life. Capellani's family name is believed to be of Italian origin, and it is thought that his ancestors may have originally come from Italy. However, there is limited information available about his family background, and the exact details are not well documented. In terms of his relationship to Paul Capellani, Albert was the younger brother of Paul. The two brothers were close in age and shared a love of film and acting, which led them to pursue careers in the industry together. While they collaborated frequently on films, they also had distinct styles and approaches to their work, which helped to create a rich and diverse range of films during their careers. Overall, Albert Capellani was a talented and versatile filmmaker who made significant contributions to the early years of cinema. His ability to speak multiple languages and his connections to other figures in the industry helped him to achieve success both in France and internationally. Despite the limited information available about his personal life, his legacy continues to be celebrated by film enthusiasts around the world.

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
Lothar Matthäus is a German former professional footballer and current football coach, born on June 25, 1961, in Erlangen, West Germany (now Germany). He is widely regarded as one of the greatest midfielders of all time, known for his exceptional skill, vision, and leadership on the pitch. Sport: Football (soccer) Participant in: UEFA European Football Championship, FIFA World Cup, and Olympic Games Spouse: Christel Matthäus (married in 1989) Occupation: Football coach and pundit Given Name: Lothar Sport: Football (soccer) League: Bundesliga, UEFA Champions League, and FIFA World Cup Sex or Gender: Male Position played on team/speciality: Central midfielder and captain Country of citizenship: Germany Languages spoken, written, or signed: German (native language), English (fluent), French (basic knowledge) Instrument: Drums Award received: FIFA World Player of the Year (1990, 1999), Ballon d'Or (1990), UEFA European Football Championship Top Scorer (1984) Place of birth: Erlangen, West Germany (now Germany) Family name: Matthäus Native language: German Country for sport: Germany Member of sports team: Bayern Munich, Borussia Dortmund, and the German national team Relationship to 1990 FIFA World Cup Match 47: Matthäus captained West Germany to victory in this match against Argentina. Lothar Matthäus began his playing career with Bayern Munich in 1979, before moving to Borussia Dortmund in 1984. He then returned to Bayern Munich in 1988 and spent two more seasons there before retiring in 1994. Throughout his club career, he won numerous honors, including eight German championships, three UEFA Champions League titles, and the FIFA World Cup. As a member of the German national team, Matthäus was part of the squad that won the 1984 European Championship and the 1990 FIFA World Cup. He also represented West Germany at the Olympic Games in 1988, where they won the bronze medal. After retiring from playing, Matthäus went on to become a successful football coach, managing clubs such as Bayern Munich, Inter Milan, and Sporting CP, among others. He has also worked as a pundit and commentator for various television networks. Throughout his career, Lothar Matthäus has earned a reputation as one of the most skilled and important players in the history of football. His exceptional leadership skills, technical ability, and work ethic have made him a beloved figure both on and off the pitch.

### **Old facts about the subject**
- family name: Matthäus - occupation: association football player, association football manager - place of birth: Erlangen - award received: Footballer of the Year, Bavarian Order of Merit, Ballon d'Or, Hall of Fame des deutschen Sports, Footballer of the Year - country of citizenship: Germany - given name: Lothar - sport: association football - participant in: 1994 FIFA World Cup, 1998 FIFA World Cup, 1990 FIFA World Cup, 1986 FIFA World Cup, 1982 FIFA World Cup, UEFA Euro 1980, UEFA Euro 1984, UEFA Euro 1988, UEFA Euro 2000 - spouse: Anastasia Klimko - position played on team / speciality: midfielder, sweeper - languages spoken, written or signed: German, Italian, English - league: Bundesliga, Major League Soccer - country for sport: Germany - sex or gender: male - native language: German - member of sports team: Borussia Mönchengladbach, FC Bayern Munich, Inter Milan, FC Bayern Munich, New York Red Bulls, Germany national association football team, Germany national under-21 football team, Germany national football B team, Germany national under-18 football team - instrument: voice

### **Related passage (related entity: 1990 FIFA World Cup Match 47):** 
1990 FIFA World Cup Match 47: Germany vs. Cameroon  In this match, which took place on June 20th, 1990 at the Stadio Comunale in Turin, Italy, the German national team faced off against Cameroon in what was a thrilling and closely contested match. The Germans were looking to solidify their position as one of the top teams in the tournament, while the Cameroonians were determined to cause an upset and make a name for themselves on the global stage. Sportsmen Participating: Germany: * Lothar Matthäus (midfielder) Cameroon: * Roger Milla (forward) Points/Goals Scored By: Germany: * Rudi Völler (forward) - 1 goal Cameroon: * Roger Milla (forward) - 1 goal Other Sportsmen: Germany: * Karl-Heinz Rummenigge (forward) Cameroon: * Henri Michel (defender) Relationship to Lothar Matthäus: Lothar Matthäus played a crucial role in the match for Germany, helping his team control possession and create scoring opportunities throughout the game. His midfield prowess and vision allowed him to dictate the pace of play, and he was unfortunate not to score himself, hitting the post on multiple occasions. As a result, Matthäus proved himself to be a key player on the world stage, further cementing his status as one of the best midfielders of his generation. Conclusion: The 1990 FIFA World Cup Match 47 between Germany and Cameroon was an intense and exciting contest that showcased the skills of some of the world's top footballers. With talented players like Lothar Matthäus leading the way, both teams gave it their all and left everything on the field. In the end, Rudi Völler's lone goal was enough to secure victory for the Germans, but the real star of the show was Roger Milla, who made his mark on the tournament with a stunning solo effort. As the two sides continue their journey in the competition, it is clear that this match will be remembered as a defining moment in the history of football.

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
A Latin Dictionary is a comprehensive reference book that provides detailed definitions and translations of Latin words and phrases. Written by Charles du FresneDU Fresne, it was first published in 1687 and has since become a standard tool for scholars studying the ancient language. In this essay, we will explore the history and significance of A Latin Dictionary, including its original language, publisher, language of work, author, country of origin, genre, and relationship to Charlton Thomas Lewis. Original Language of Film or TV Show: A Latin Dictionary is primarily used as a reference for the study of Latin, which was the language spoken in ancient Rome and is still studied today for various reasons such as historical interest, literary appreciation, and linguistic curiosity. Therefore, it does not have an original language of film or TV show, as it is a reference book rather than a script or screenplay. Publisher: The first edition of A Latin Dictionary was published by Samuel Keeton in 1687, in London, England. Since then, there have been numerous editions and reprints of the book, with different publishers over the years. Language of Work or Name: A Latin Dictionary is written in Latin, as it is intended to provide definitions and translations of Latin words and phrases. The book contains over 20,000 entries, covering a wide range of topics including grammar, mythology, history, literature, and everyday life in ancient Rome. Author: Charles du FresneDU Fresne (1645-1730) was a French scholar and lexicographer who compiled and wrote the first edition of A Latin Dictionary. He was born in Paris, France, and studied law at the University of Orleans. Du Fresne was also a professor of rhetoric and belles-lettres at the University of Poitiers and later became a member of the French Academy. Country of Origin: A Latin Dictionary was originally written and published in France, specifically in Paris. However, due to its widespread use and significance, the book has become a standard reference for scholars studying Latin from all over the world. Genre: A Latin Dictionary is a reference book, belonging to the non-fiction genre. It provides definitions and translations of Latin words and phrases, making it an essential tool for anyone studying the ancient language. Relationship to Charlton Thomas Lewis: Charlton Thomas Lewis (1851-1942) was a British scholar and lexicographer who contributed significantly to the field of classical studies. He was particularly known for his work on Latin dictionaries, including A Latin Dictionary, which he edited and revised several times throughout his career. Lewis's contributions to the field of Latin lexicography have been widely recognized and appreciated, and his works remain highly regarded among scholars today. In conclusion, A Latin Dictionary is a comprehensive reference book that provides detailed definitions and translations of Latin words and phrases. Compiled and written by Charles du Fresne, it was first published in 1687 and has since become a standard tool for scholars studying the ancient language. Although it does not have an original language of film or TV show, A Latin Dictionary remains an important resource for anyone interested in classical studies, Latin language, and the history of Western civilization.

### **Old facts about the subject**
- author: Charlton Thomas Lewis, Charles Short - country of origin: United States of America - genre: bilingual dictionary - publisher: Harper - language of work or name: English, Latin

### **Related passage (related entity: Charlton Thomas Lewis):** 
Charlton Thomas Lewis was a British actor and television personality who was born on May 20, 1935, in Bournemouth, England. He is best known for his role as the voice of Wallace in the popular animated films "Wallace and Gromit" and their accompanying television series. Lewis's original language of film and TV shows was English. However, he was also fluent in several other languages, including Welsh, French, German, Italian, Spanish, and Sign Language. This multilingual ability served him well in his career, allowing him to easily take on roles that required different languages. One of Lewis's most notable works is his portrayal of the titular character in the "Wallace and Gromit" franchise. The series of short films and television episodes follows the adventures of Wallace, a cheese-loving inventor, and his intelligent dog Gromit, as they solve various problems and go on quirky adventures. The franchise has become a cult classic and has won numerous awards, including several Academy Awards. In addition to his work on "Wallace and Gromit," Lewis also had a successful career in radio broadcasting. He hosted several radio shows, including "The Charlton Lewis Show" and "The Saturday Club." These programs allowed him to showcase his multilingual abilities and his love of language, as he interviewed guests from around the world and discussed various linguistic topics. Lewis's relationship to A Latin Dictionary is somewhat indirect. Although he was not directly involved in the creation or publication of the dictionary, his passion for language and his multilingual abilities are reminiscent of the Latin scholars who created and expanded upon the dictionary over the centuries. The dictionary, which contains over 16,000 entries covering Latin grammar, syntax, and vocabulary, is a testament to the enduring legacy of Latin and its influence on modern languages. In conclusion, Charlton Thomas Lewis was a talented actor and television personality who was fluently bilingual in multiple languages. His ability to speak, write, and sign various languages made him a versatile performer, and his passion for language was evident in his work on "Wallace and Gromit" and his radio broadcasts. Although he did not directly contribute to A Latin Dictionary, his dedication to language and his multilingual abilities are similar to those of the scholars who created and expanded upon the dictionary over the centuries.

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
Michelangelo Buonarroti (1475-1564) was a renowned Italian artist, sculptor, painter, architect, and poet of the High Renaissance. He is widely regarded as one of the greatest artists of all time, known for his incredible mastery of form, proportion, and beauty. Michelangelo was born in Caprese, Italy, and spent most of his life in Florence, Rome, and Venice. He was occupationally a sculptor, painter, architect, and poet, and his works are characterized by their grandeur, emotional intensity, and technical innovation. Movement: Michelangelo was a key figure in the High Renaissance movement, which emphasized humanism, revival of classical forms, and naturalism. He was influenced by the ancient Greeks and Romans, and his works reflect this influence through their attention to proportion, anatomy, and beauty. Place of Burial: Michelangelo died in Rome on February 18, 1564, and was buried in the Basilica of Santa Croce in Florence, where many other famous artists and intellectuals are buried. Sponsor: Michelangelo was sponsored by the Medici family, who were powerful bankers and politicians in Florence. They commissioned many of Michelangelo's works, including his famous statue of David, which stands over 17 feet tall and is considered one of the greatest works of art in history. Ethnic Group: Michelangelo was born into a Florentine family, but his ancestry is not well documented. Some sources suggest that he had distant Tuscan and Roman ancestry, while others indicate that he may have been of mixed Italian and Greek heritage. Cause of Death: Michelangelo died at the age of 89 due to complications from a long illness. He had suffered from poor health throughout his life, particularly respiratory problems, and had several close calls with death. Despite his poor health, Michelangelo continued to work until the end of his life, leaving behind an extraordinary body of work. Unmarried Partner: Michelangelo was known to have had several romantic relationships throughout his life, but he never married. His most famous relationship was with a man named Tommaso de Cavalieri, who was a young nobleman and a fellow artist. The two men lived together for many years and were believed to be in a loving relationship, although their exact nature remains a subject of debate among historians. Languages Spoken, Written, or Signed: Michelangelo was fluent in Italian and Latin, and he also had some knowledge of Greek. He wrote poetry and letters in these languages, and his correspondence provides valuable insights into his thoughts and feelings about his work and his contemporaries. Critical Catalogue: Michelangelo's works are numerous and diverse, spanning sculpture, painting, architecture, and poetry. Some of his most famous works include the statue of David, the frescoes on the ceiling of the Sistine Chapel, and the tomb of Pope Julius II. His works are celebrated for their beauty, grandeur, and technical innovation, and they continue to inspire artists and art lovers around the world. Depicted by: Michelangelo was depicted by many artists, including his contemporary Raphael. One of the most famous portraits of Michelangelo is the painting "The Entombment" by Caravaggio, which shows Michelangelo lying in a pose reminiscent of Christ's crucifixion. Country of Citizenship: Michelangelo was a citizen of Italy, specifically the city-state of Florence. Place of Death: Michelangelo died in Rome, Italy, on February 18, 1564. Genre: Michelangelo worked in a variety of genres, including sculpture, painting, architecture, and poetry. However, his most famous works are in the genre of figurative sculpture and fresco painting. Family: Michelangelo came from a modestly wealthy family in Florence. His father was a builder, and his mother was a midwife. He had several brothers and sisters, including a younger brother named Leonardo, who also became an artist. Notable Work: Michelangelo's most famous work is arguably the statue of David, which he sculpted between 1501 and 1504. The statue stands over 17 feet tall and is carved from a single block of white Carrara marble. It is considered one of the greatest works of art in history and is celebrated

### **Old facts about the subject**
- student of: Domenico Ghirlandaio, Bertoldo di Giovanni, Poliziano - occupation: sculptor, draftsperson, painter, architect, poet, engineer, general contractor, writer - movement: High Renaissance, Renaissance painting - place of birth: Caprese Michelangelo - place of death: Rome - place of burial: Basilica of Santa Croce - country of citizenship: Republic of Florence - given name: Michelangelo - notable work: David, davo, Dying Slave, The Last Judgment, Doni Tondo, Madonna of the Stair, Battle of the Centaurs, The Genius of Victory, The Deposition, Rondanini Pietà, Sistine Chapel ceiling, Rebellious Slave, St. Matthew, Medici Chapels, Bacchus, Brutus, St. Peter's Basilica, Slaves, Biblioteca Medicea Laurenziana - unmarried partner: Tommaso dei Cavalieri - family name: Buonarroti - religion or worldview: Catholicism - languages spoken, written or signed: Italian - genre: Christian art, homoeroticism - student: Guglielmo della Porta - different from: Michelangelo Anselmi, Michelangelo Buonarroti - depicted by: Michelangelo Buonarroti, Michelangelo & Sebastiano, Portrait of Michelangelo Buonarroti, Life of Michelangelo - work location: Florence, Bologna, Rome, Florence, Rome, Florence, Rome, Florence, Venice, Florence, Rome, Florence, Rome, Florence, Rome - sponsor: Lorenzo de' Medici - sex or gender: male - ethnic group: Italians - cause of death: infection, asphyxia - has works in the collection: Städel Museum, Minneapolis Institute of Art, Museo del Prado, The Nelson-Atkins Museum of Art, National Gallery of Victoria, National Gallery of Art, Nationalmuseum, Ashmolean Museum, Gallerie degli Uffizi, Metropolitan Museum of Art, M Leuven, Galleria dell'Accademia, Museo dell'Opera del Duomo, Palazzo Vecchio, Bargello National Museum, Victoria and Albert Museum, Medici Chapels, Casa Buonarroti, Uffizi, British Museum, Isabella Stewart Gardner Museum, Palais des Beaux-Arts de Lille, Vatican Museums, National Gallery, Holkham Hall, Royal Academy of Arts, Kimbell Art Museum, Hermitage Museum, Staatliche Graphische Sammlung München, Kupferstichkabinett Berlin, Albertina, National Museum in Warsaw, Museum of Fine Arts, Budapest, Smithsonian American Art Museum, Cleveland Museum of Art, Condé Museum, Maison de Victor Hugo, Museum Boijmans Van Beuningen, Auckland Art Gallery, Teylers Museum, Church of Our Lady, Musea Brugge - religious order: Franciscans - relative: Michelangelo Buonarroti - educated at: University of Florence - family: Buonarroti family - critical catalogue: Michelangelo: The Complete Paintings, Sculptures and Architecture - artist files at: Frick Art Reference Library - father: Lodovico di Leonardo Buonarroti Simoni - mother: Francesca di Neri del Miniato Siena

### **Related passage (related entity: Michelangelo Buonarroti):** 
Michelangelo Buonarroti (1475 - 1564) was a renowned Italian artist, sculptor, painter, architect, and poet. He is widely regarded as one of the most influential artists of all time, known for his iconic works such as the ceiling of the Sistine Chapel and David. Here are some key facts about Michelangelo's life and career: Occupation: Michelangelo was primarily an artist, but he also worked in other fields, including architecture and poetry. He was appointed as the architect of the Medici family in Florence and designed several buildings, including the Laurentian Library. Occupation of Relative: Michelangelo's father, Leonardo Buonarroti, was an amateur artist who provided financial support for Michelangelo's artistic education. His mother, Francesca di Neri del Migliore, was a member of a prominent family in Florence. Given Name: Michelangelo was born with the given name Ludovico, which was later changed to Michelangelo by his father. Sex or Gender: Michelangelo was male. Place of Burial: Michelangelo was buried in the Basilica of Santa Croce in Florence, Italy. Languages Spoken, Written, or Signed: Michelangelo was fluent in Latin, Greek, and Italian. He was also skilled in writing poetry and letters. Family: Michelangelo's father, Leonardo Buonarroti, and his mother, Francesca di Neri del Migliore, were both members of the rising middle class in Florence. Michelangelo had three brothers and a sister. Family Name: Buonarroti is Michelangelo's family name. Relationship to Michelangelo: Leonardo Buonarroti, Michelangelo's father, supported his son's artistic education and encouraged his talent. In conclusion, Michelangelo Buonarroti was a multifaceted artist who excelled in various fields, including painting, sculpture, architecture, and poetry. His upbringing and family background played an essential role in shaping his talents and interests. As one of the greatest artists of the Renaissance, Michelangelo left an indelible mark on Western art history.

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
Kazys Lozoraitis was a Lithuanian poet, writer and philosopher. He was born on October 25th, 1934, in Druskininkai, Lithuania, to parents Valentinas and Marija Lozoraitis. His father worked as a forest ranger, and his mother was a homemaker. Kazys had one younger sister, Auksė. Lozoraitis studied at the University of Vilnius, where he earned a degree in Lithuanian language and literature. After completing his studies, he worked as a teacher and later became a professor of philosophy at Vytautas Magnus University in Kaunas. Tragically, Kazys Lozoraitis passed away on December 20th, 2007, due to complications from a stroke. He was 73 years old at the time of his death. He was buried in the Petrašiūnai Cemetery in Vilnius, Lithuania, according to the Greek Orthodox Church's traditions. Lozoraitis was known for his deep religious beliefs and his strong commitment to his Lithuanian heritage. Throughout his life, he wrote numerous poems, plays, and essays that explored themes of love, spirituality, and the struggle for independence in Lithuania. Some of his most notable works include "The Gates of the Sun," "The Birth of the Eagle," and "The Song of the Earth." In addition to his literary achievements, Lozoraitis received several awards for his work. In 1996, he was awarded the National Prize of Lithuania for Literature, and in 2003, he received the Lithuanian President's Prize for Culture. Despite his passing, Kazys Lozoraitis' legacy lives on through his powerful and thought-provoking writing. His poetry and prose continue to inspire and influence writers and thinkers around the world, and his contributions to Lithuanian culture are widely recognized and respected.

### **Old facts about the subject**
- sex or gender: male - place of burial: Petrašiūnai Cemetery - father: Stasys Lozoraitis - place of birth: Berlin - place of death: Rome - award received: Knight of St. Sylvester - occupation: diplomat, politician - given name: Kazys - manner of death: natural causes - sibling: Stasys Lozoraitis - religion or worldview: Catholicism - educated at: Sapienza University of Rome - family name: Lozoraitis - cause of death: cancer - mother: Vincenta Matulaitytė-Lozoraitienė

### **Related passage (related entity: Stasys Lozoraitis):** 
Stasys Lozoraitis was a Lithuanian poet, writer and public figure who lived from 1937 to 2008. He is best known for his work in the field of literature and his contributions to the Lithuanian language and culture. Here is some information about Stasys Lozoraitis' life and career: Occupation: Stasys Lozoraitis was a poet, writer, and public figure. He worked as a teacher and journalist throughout his life, and also served as a member of the Lithuanian parliament. Occupation of Sibling: Stasys Lozoraitis' younger brother, Vytautas Lozoraitis, was also a well-known figure in Lithuania. Vytautas was a composer and musicologist, and he composed many works for theater and film. Sibling: Stasys Lozoraitis had two siblings, Vytautas and Lyda Lozoraitiene. Father: Stasys Lozoraitis' father was Pranas Lozoraitis, a lawyer and politician. Manner of Death: Stasys Lozoraitis passed away on February 4, 2008, at the age of 70, due to complications from cancer. Sex or Gender: Stasys Lozoraitis was male. Educated At: Stasys Lozoraitis studied at the University of Vilnius, where he earned a degree in Lithuanian Language and Literature. Place of Burial: Stasys Lozoraitis is buried in the Petrašiūnai Cemetery in Vilnius, Lithuania. Religion or Worldview: Stasys Lozoraitis was a Catholic. Mother: Stasys Lozoraitis' mother was Elena Lozoraitienė. Place of Birth: Stasys Lozoraitis was born in Klaipėda, Lithuania, which was then part of Germany. Family Name: Stasys Lozoraitis was born into a family with a long history of literary and political achievement. His father, Pranas Lozoraitis, was a prominent lawyer and politician, and his uncle, Kazys Lozoraitis, was a notable poet and writer. Relationship to Kazys Lozoraitis: Stasys Lozoraitis was the nephew of Kazys Lozoraitis. The two men were close friends and collaborators, and they shared many similarities in their writing style and themes. Stasys Lozoraitis was a highly respected and influential figure in Lithuanian literature and culture. Throughout his life and career, he worked tirelessly to promote the Lithuanian language and culture, and his contributions to these fields will be remembered for generations to come.

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
Windows 7 is a operating system developed by Microsoft Corporation, the copyright holder is Microsoft Corporation. The manufacturer of Windows 7 is Microsoft Corporation. Windows 7 is a read only file format, meaning that once it is installed on a computer, its files cannot be modified or deleted without proper authorization. Windows 7 was developed based on the Windows NT kernel, which is a part of the Windows family of operating systems. It also includes features from Windows Vista, such as Aero and SuperBar. The language of work or name for Windows 7 is English, but it can be translated into other languages as well. Windows 7 is designed to run on x86, IA-64 and ARM architectures, making it compatible with most modern computers. The graphical user interface (GUI) toolkit or framework used in Windows 7 is Windows Presentation Foundation (WPF), which provides a high level of flexibility and customization options for developers. The developer of WPF is Microsoft Corporation. Windows 7 is part of the Windows NT series of operating systems, which is a subclass of the Windows lineage. It is the successor to Windows Vista and the predecessor to Windows 8. Windows 7 has a similar relationship to Windows 8 as Windows 8 has to Windows 10, as they are both successive versions of the same operating system family. In conclusion, Windows 7 is a powerful and widely used operating system that offers a wide range of features and capabilities for users. Its development and design have been influenced by previous versions of the Windows operating system, and it has evolved over time to become one of the most popular and widely used operating systems in the world.

### **Old facts about the subject**
- GUI toolkit or framework: Windows API, .NET Framework, Windows Forms, Windows Presentation Foundation, DirectX, Media Foundation - platform: IA-32, x86_64, x86 - developer: Microsoft - copyright holder: Microsoft - subclass of: Windows NT - manufacturer: Microsoft - part of the series: Windows NT - readable file format: Windows Portable Executable file format, 32-bit, Windows Portable Executable file format, 64-bit, New Executable - based on: Windows Vista - language of work or name: multiple languages

### **Related passage (related entity: Windows 8):** 
Windows 8 is a series of operating systems developed by Microsoft, a well-known computer software company. The latest version of Windows 8 was released in 2012 and has gained popularity due to its unique features and improved performance. In this essay, we will explore the key aspects of Windows 8, including its developer, manufacturer, copyright holder, and more. Developer: Microsoft Corporation is the developer of Windows 8. Founded in 1975, Microsoft is a leading technology company that specializes in designing, manufacturing, licensing, and supporting a wide range of software products. With a long history of innovation and excellence, Microsoft is known for creating some of the most popular and widely used operating systems, including Windows, Office, and Azure. Developer of Based On: Windows 8 is built on top of the Windows NT kernel, which provides a robust and secure foundation for the operating system. Developed by Microsoft, the Windows NT kernel is a microkernel architecture that allows for faster and more efficient processing of system requests. This architecture also provides better compatibility with hardware devices and applications, making it easier for developers to create new programs and software. Manufacturer: Microsoft is the manufacturer of Windows 8. As a leading technology company, Microsoft designs, develops, markets, and distributes a wide range of software products, including operating systems, productivity software, gaming consoles, and cloud computing services. With a global presence and a strong reputation for quality and reliability, Microsoft is one of the largest and most successful technology companies in the world. Copyright Holder: The copyright holder of Windows 8 is Microsoft Corporation. As the creator and owner of the operating system, Microsoft holds the exclusive rights to Windows 8, including its intellectual property and patents. This gives Microsoft the power to license and distribute Windows 8 to other companies and individuals, as well as to control how the operating system is used and distributed. Based On: Windows 8 is based on the Windows NT kernel, which is a result of the work done by many developers at Microsoft over several years. The Windows NT kernel is designed to provide a solid foundation for the operating system, allowing for faster and more efficient processing of system requests. It also enables better compatibility with hardware devices and applications, making it easier for developers to create new programs and software. Readable File Format: Windows 8 uses the Portable Executable (PE) file format for executable files. PE is a compact and portable file format that can be easily read and executed by any Windows operating system, regardless of its version. This makes it ideal for distributing software applications and utilities, as well as for using them on different computers. Platform: Windows 8 is designed to run on both desktop and mobile devices, making it a versatile operating system that can cater to different user needs and preferences. Whether you are working on a powerful desktop computer or a lightweight laptop, Windows 8 provides a consistent and intuitive user experience that is easy to navigate and use. GUI Toolkit or Framework: Windows 8 uses the Windows Presentation Foundation (WPF) as its GUI toolkit or framework. WPF is a set of APIs that enable developers to build visually appealing and responsive user interfaces for their applications. With its support for vector graphics, animations, and multimedia content, WPF allows developers to create high-quality and engaging user experiences that enhance the overall user experience. Part of the Series: Windows 8 is part of the Windows NT series of operating systems, which includes earlier versions such as Windows 7, Vista, XP, and others. Each version of Windows NT builds upon the previous one, introducing new features, improvements, and optimizations that make the operating system more efficient, reliable, and user-friendly. Subclass of: Windows 8 is a subclass of Windows 7, which means that it shares many similarities with its predecessor but also offers new features and improvements. For example, Windows 8 includes the Metro interface, which provides a touch-friendly and intuitive user interface for tablets and other mobile devices. Additionally, Windows 8 supports multitasking, file sharing, and other features that are not available in Windows 7. Relationship to Windows 7: Windows 8 is closely related to Windows 7, sharing many common features and improvements. However, Windows 8 also introduces new capabilities and functionality that are not available in Windows 7. For example, Windows 8 includes the Metro interface, which is designed specifically for touch-based devices and provides a more intuitive and interactive user experience. Additionally, Windows 8 offers improved security and privacy features compared to Windows 7, making it a more secure and reliable choice for users.

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
Province of Venice: An Overview The Province of Venice is a administrative territorial entity located in the Veneto region, northeastern Italy. It is situated on the Venetian Lagoon, along the Adriatic Sea, and is composed of numerous islands and mainland territories. The capital city of the province is Venice, which is also the largest city in the region and one of the most famous tourist destinations in Italy. Capital: Venice Head of Government: President of the Province of Venice The President of the Province of Venice is the highest authority in the administrative entity. The current president is Francesco Gasparin, who was elected in 2018. The president is responsible for overseeing the administration of the province and represents the province in regional and national affairs. Shares Border With: The Province of Venice shares borders with the following administrative territories: * Metropolitan City of Venice to the northwest * Province of Padua to the west * Province of Rovigo to the southwest * Region of Friuli-Venezia Giulia to the east  Located In: Administrative Territorial Entity The Province of Venice is located within the Veneto region, which is an administrative territorial entity in northeastern Italy. The province covers an area of approximately 560 square kilometers and is home to over 900,000 inhabitants. Contains the Administrative Territorial Entity: The Province of Venice contains several smaller administrative territorial entities, including 34 municipalities, 27 comunes, and 4 island communities. These entities are governed by elected representatives and are responsible for providing various local services, such as education, healthcare, and infrastructure maintenance. Located In Time Zone: Central European Time (CET) Replaced By: Metropolitan City of Venice In 2015, the Province of Venice was replaced by the Metropolitan City of Venice, which is a larger administrative entity that includes not only the province but also several other nearby territories. The Metropolitan City of Venice is responsible for coordinating regional policies and providing additional services to its inhabitants. Country: Italy Has Part(s): None  Relationship to Metropolitan City of Venice: The Province of Venice is a part of the Metropolitan City of Venice, and the two entities work together to provide services and coordinate policies to their inhabitants. While the province has limited autonomy compared to other Italian provinces, it plays an important role in regional governance and is responsible for many local services.

### **Old facts about the subject**
- has part(s): list of coat of arms in the province of Venice - located in the administrative territorial entity: Veneto - shares border with: Province of Rovigo, Province of Padua, Province of Treviso, Province of Pordenone, Province of Udine - contains the administrative territorial entity: Annone Veneto, Campagna Lupia, Campolongo Maggiore, Camponogara, Caorle, Cavallino-Treporti, Cavarzere, Ceggia, Chioggia, Cinto Caomaggiore, Cona, Veneto, Concordia Sagittaria, Dolo, Eraclea, Fiesso d'Artico, Fossalta di Piave, Fossalta di Portogruaro, Fossò, Gruaro, Jesolo, Marcon, Martellago, Meolo, Mira, Mirano, Musile di Piave, Noale, Noventa di Piave, Pianiga, Portogruaro, Pramaggiore, Quarto d'Altino, Salzano, San Donà di Piave, San Michele al Tagliamento, Santa Maria di Sala, San Stino di Livenza, Scorzè, Spinea, Stra, Teglio Veneto, Torre di Mosto, Venice, Vigonovo - capital: Venice - head of government: Francesca Zaccariotto, Davide Zoggia - located in time zone: UTC+01:00, UTC+02:00 - country: Italy - replaced by: Metropolitan City of Venice - office held by head of government: president of the Province of Venice

### **Related passage (related entity: Metropolitan City of Venice):** 
Metropolitan City of Venice, officially known as Comune di Venezia, is a city and metropolitan area located in northeastern Italy. It is the capital of the Veneto region and serves as a major cultural, economic, and touristic hub within the region. The city is situated on the picturesque Venetian Lagoon, along the Adriatic Sea, and is renowned for its historic architecture, canals, and rich artistic heritage. Capital of Replaces: Metropolitan City of Venice replaced the former Province of Venice in 2015, when Italy adopted a new local government structure. Under this new system, the province-level administrations were abolished, and their functions were transferred to the metropolitan cities. As a result, Metropolitan City of Venice became the highest level of local government in the Veneto region, responsible for overseeing various aspects of governance, including urban planning, transportation, education, healthcare, and economic development. Has Parts: Metropolitan City of Venice comprises several territories, including the historical city center, the islands of Murano, Burano, and Torcello, as well as numerous smaller islands and mainland areas. These territories are home to a diverse range of communities, each with their unique culture, history, and traditions. Replaces: The former Province of Venice was dissolved and replaced by Metropolitan City of Venice in order to streamline local governance and improve the efficiency of public services. By consolidating powers and responsibilities at the metropolitan level, the Italian government aimed to enhance the quality of life for residents and promote sustainable development throughout the region. Shares Border With: Metropolitan City of Venice shares a border with the provinces of Padua, Rovigo, Treviso, and Veneto, as well as the Adriatic Sea to the north. This strategic location facilitates trade and commerce between Venice and neighboring regions, while also providing easy access to the sea for maritime transportation. Located In Administrative Territorial Entity: Metropolitan City of Venice is located within the Veneto region, which is one of Italy's five autonomous macroregions. The Veneto region covers an area of approximately 14,000 square kilometers and is home to over 5 million people, making it the fifth most populous region in Italy. Contains The Administrative Territorial Entity: Metropolitan City of Venice contains several administrative territorial entities, including 37 municipalities, 65 comunes, and 11 provinces. Each of these entities has its own governing body and is responsible for managing local affairs, such as infrastructure maintenance, education, and social services. Located In Time Zone: Metropolitan City of Venice is located in the Central European Time (CET) time zone, which is the same as Coordinated Universal Time (UTC) plus one hour. This time zone allows for convenient coordination with other European countries and facilitates international communication and trade. Country: Metropolitan City of Venice is located in Italy, a country that is a member of the European Union and has a population of around 60 million people. Italy is known for its rich cultural heritage, including art, literature, music, and culinary traditions. The country is also famous for its beautiful landscapes, ranging from the snow-capped Alps in the north to the sun-kissed Mediterranean beaches in the south. Relationship To Province Of Venice: Metropolitan City of Venice replaces the former Province of Venice, which was a subnational administrative division within the Veneto region. The Province of Venice was abolished in 2015 as part of a broader reform aimed at simplifying local governance and improving efficiency. The transition from province to metropolitan city was intended to provide more autonomy and decision-making power to the local community, while also enhancing the delivery of public services. Today, Metropolitan City of Venice continues to serve as the primary administrative entity for the Veneto region, while also maintaining close ties with the Province of Venice through shared cultural, historical, and economic connections.

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
Dmitry Malikov is a Russian singer, songwriter, and producer who was born on May 7, 1980, in Moscow, Russia. His native language is Russian, and he is the son of a Russian lawyer. Malikov's father played a significant role in his early musical development, teaching him how to play the guitar and encouraging him to write songs from a young age. Malikov's career in music began in the late 1990s, when he started performing in various bands and writing his own songs. He eventually released his debut album in 2001, which became a huge success in Russia and led to him being recognized as one of the country's most promising young singers. In addition to his work as a solo artist, Malikov has also collaborated with other musicians and producers, including his sister Inna Malikova, with whom he has co-written several songs. He is known for his soulful voice, catchy melodies, and introspective lyrics, which often touch on themes of love, life, and social issues. Malikov's education includes a degree in music production from the Moscow State Institute of Culture and Art, where he graduated in 2003. He has since become one of the most successful and respected figures in the Russian music industry, with numerous awards and accolades to his name. Malikov is married and has two children, a boy and a girl, and he is known to be a private person who keeps his personal life out of the spotlight. However, he is active on his official website and Instagram account, where he shares updates about his music, tours, and personal life with his fans. Some of Malikov's notable works include his hit singles "Sosedi" (Neighbors), "Mama," and "Razom k Niche" (Together to the Sky), as well as his albums "Prizyv" (Wake-Up Call) and "Zima" (Winter). He has also performed at various music festivals and concerts around the world, including the annual MTV Europe Music Awards. In terms of his field of work, Malikov is primarily a pop and rock singer-songwriter, but he has also experimented with other genres such as electronic and hip-hop. His music is known for its catchiness and emotional depth, and he is widely regarded as one of the most talented and innovative musicians in Russia today. As for his relationship with his sister Inna Malikova, she is also a singer and songwriter who has worked with Dmitry on several occasions. The two have a close creative partnership and have collaborated on many songs together. Overall, Dmitry Malikov is a highly talented and influential figure in the Russian music scene, with a long list of achievements and a dedicated fan base both in Russia and around the world.

### **Old facts about the subject**
- educated at: Moscow Conservatory - place of birth: Moscow - father: Yuriy Malikov - occupation: singer, composer, pianist, record producer, actor, television presenter, songwriter, manufacturer, presenter, film score composer, musician - website account on: My World@Mail.Ru - award received: People's Artist of the Russian Federation, Merited Artist of the Russian Federation, Order of Friendship, Golden Gramophone Award, ZD Awards, Ovation, World Music Awards - country of citizenship: Soviet Union, Russia - given name: Dmitry - native language: Russian - sibling: Inna Malikova - instrument: voice, keyboard instrument - languages spoken, written or signed: Russian - voice type: tenor, baritone - sex or gender: male - family name: Malikov - field of work: Europop, pop music, instrumental music, western classical music - member of: Samotsvety - record label: Russian Disc, Rec Records, , Universal Music Russia, CD Land Group, Artur Music, Kvadro-Disk,

### **Related passage (related entity: Inna Malikova):** 
Inna Malikova is a talented Russian singer, songwriter, and actress who was born on July 24, 1986, in Moscow, Russia. Her native language is Russian, which she speaks fluently with her siblings. Her younger brother, Dmitry Malikov, is also a singer and composer, and the two often collaborate on music projects. In addition to Russian, Inna Malikova is skilled in several other languages, including English, French, and Spanish. She has also learned sign language and has been involved in various charity work for the deaf community. Malikova's father, Alexander Malikov, is a renowned Russian actor and singer, who has inspired her love for music from a young age. Her mother, Natalia Chistyakova, is a poet and writer, and has supported her daughter's creative pursuits throughout her career. Inna Malikova's occupation is singer, songwriter, and actress. She has released several successful albums and singles, and has appeared in numerous films and TV shows. Her versatility and talent have earned her a large following both in Russia and internationally. Malikova is a citizen of Russia and has won numerous awards for her contributions to music and the arts. In 2013, she received the Russian Music Award for Best Female Singer, and in 2015, she was awarded the Golden Mask Award for Best Actress. Born in Moscow, Inna Malikova grew up surrounded by music and creativity. Her relationship with her older brother, Dmitry Malikov, is close and supportive, and the two often work together on music projects. Despite their busy schedules, they make time for regular family gatherings and maintain a strong bond. In conclusion, Inna Malikova is a talented and multilingual singer, songwriter, and actress who has made significant contributions to the world of music and entertainment. With her native language of Russian, proficiency in multiple languages, and dedication to her craft, she continues to inspire audiences around the globe.

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
Ariane Labed is a French actress and filmmaker who has gained recognition for her unique style and perspective in the film industry. Born on April 14, 1985, in Paris, France, Labed's native language is French. She is married to the actor and director, Yves Piat. Labed's given name is Ariane, which is a feminine given name derived from the Greek word for "Venus," the goddess of love and beauty. Her occupation is actress and filmmaker, and she identifies as a woman. She was educated at the Paris University of Sorbonne, where she studied philosophy and literature. Labed holds dual citizenship in France and Greece, and speaks fluent French and Greek, as well as some English. In addition to her work in film, Labed is also a member of the collective known as "The Actors' Gang," a group of actors and directors who collaborate on innovative and experimental productions. In 2018, Labed won the Best Actress award at the Cannes Film Festival for her role in the film "The Killing of a Sacred Deer." Despite her success and acclaim, Labed remains humble and dedicated to her craft. In an interview with The Guardian, she stated, "I'm not interested in being famous; I just want to keep making films that move people." (Source: The Guardian). Labed's relationship to the actor and director, Olga Kurylenko, is simply a coincidence as they are not related. However, both Labed and Kurylenko have had successful careers in the film industry and have worked together on various projects. In conclusion, Ariane Labed is a talented and innovative actress and filmmaker who has made a significant impact in the film industry. Her dedication to her craft and commitment to creating meaningful and moving films has earned her widespread recognition and acclaim. Despite her success, Labed remains humble and focused on her art, continually pushing the boundaries of what is possible in film.

### **Old facts about the subject**
- sex or gender: female - occupation: actor, stage actor, film actor, film director, screenwriter - place of birth: Athens - country of citizenship: France, Greece - given name: Ariane - languages spoken, written or signed: French, Modern Greek - native language: French - spouse: Yorgos Lanthimos - educated at: Aix-Marseille University, University of Provence - Aix-Marseille I - member of: Collectif 50/50 - award received: Volpi Cup for Best Actress

### **Related passage (related entity: Olla):** 
Olla is a 2016 Greek drama film directed by Christina Economou and written by Anastasia Pappas. The film stars Ariane Labed, Aggeliki Papoulou, and Vangelis Mourikis. In this essay, we will explore the linguistic features of Olla and its creative team, including their native languages, original language, and relationships with the film's star, Ariane Labed. Native Language of Director and Screenwriter: Christina Economou is a Greek film director born in Athens, Greece. Her native language is Greek, which she uses as the primary language for directing and writing films. Anastasia Pappas, on the other hand, is a Greek screenwriter who was born in Athens, Greece. Her native language is also Greek. Original Language of Film or TV Show: Olla is a Greek film written and directed by a Greek crew. Therefore, the original language of the film is Greek. The dialogue and any other spoken elements in the film are primarily in Greek, reflecting the cultural context and setting of the story. Screenwriter: Anastasia Pappas is the screenwriter of Olla. She is a Greek screenwriter known for her work in both film and television. Pappas has written several screenplays, including Olla, which premiered at the Locarno International Film Festival in 2016. Director: Christina Economou is the director of Olla. She is a Greek film director and producer known for her work in both feature films and documentaries. Economou has directed several films, including Olla, which was her debut feature film. She is known for her distinct visual style and attention to detail in her films. Relationship to Ariane Labed: Ariane Labed is a Greek actress who stars in Olla alongside Vangelis Mourikis and Aggeliki Papoulou. Labed's role in the film is that of a young woman living in Athens who becomes embroiled in a series of strange events after befriending a mysterious woman. Labed has worked with both Economou and Pappas before, having appeared in several short films directed by Economou and written by Pappas. Their collaboration on Olla marks their first feature-length film together. In conclusion, Olla is a Greek drama film directed by Christina Economou and written by Anastasia Pappas. The film stars Ariane Labed and explores themes of identity, loneliness, and the blurred lines between reality and fantasy. The native languages of the director and screenwriter are Greek, reflecting the cultural context and setting of the story. The film's original language is also Greek, and it has received critical acclaim for its unique visual style and thought-provoking narrative. Through their collaboration on Olla, Economou and Pappas have established themselves as talented and innovative filmmakers in the Greek film industry.

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
Rufus Isaacs, 1st Marquess of Reading (1860-1935) was a British lawyer and politician who served as the Viceroy of India from 1921 to 1926. Here is some information about his life: Work Location: Rufus Isaacs worked primarily in London, England, but also traveled extensively throughout India during his time as Viceroy. Spouse: Rufus Isaacs married Stella Bowman in 1891; they had one child together, a daughter named Violet. Occupation: Rufus Isaacs was a lawyer by profession and practiced law in London before entering politics. Candidacy in Election: Rufus Isaacs was elected to Parliament in 1906 as the Member of Parliament (MP) for the constituency of South Shields. Child: Rufus Isaacs' only child is his daughter Violet, born in 1901. Languages Spoken, Written, or Signed: Rufus Isaacs spoke English fluently, as well as some Hindi and Urdu, which he learned during his time as Viceroy of India. Award Received: Rufus Isaacs was awarded the Knight Grand Cross of the Order of the Bath (GBE) in 1921 for his service to the British Empire. Sibling: Rufus Isaacs had two siblings, a brother and a sister. Country of Citizenship: Rufus Isaacs was a citizen of the United Kingdom. Place of Death: Rufus Isaacs died on December 7, 1935, at his home in London, England. Sex or Gender: Rufus Isaacs was male. Mother: Rufus Isaacs' mother was Elizabeth Isaacs. Work Location: Rufus Isaacs worked primarily in London, but also traveled extensively throughout India during his time as Viceroy. Place of Birth: Rufus Isaacs was born on July 25, 1860, in London, England. Family Name: Rufus Isaacs' family name is Isaacs. Father: Rufus Isaacs' father was Benjamin Isaacs. Given Name: Rufus Isaacs' given name is Rufus. Different From: Rufus Isaacs was known as Lord Reading during his time in politics, as he was appointed Lord Reading in 1911. Educated At: Rufus Isaacs was educated at Trinity College, Cambridge, where he earned a degree in law. Position Held: Rufus Isaacs held several positions in government, including Viceroy of India, Secretary of State for India, and President of the Board of Trade. Noble Title: Rufus Isaacs held the noble title of Marquess of Reading, which was granted to him in 1921. Member of: Rufus Isaacs was a member of the Conservative Party. Relationship to Stella Isaacs, Marchioness of Reading: Rufus Isaacs was married to Stella Isaacs, who became the Marchioness of Reading after Rufus' death in 1935.

### **Old facts about the subject**
- sex or gender: male - place of birth: London - country of citizenship: United Kingdom, United Kingdom of Great Britain and Ireland - member of political party: Liberal Party - place of death: London - occupation: politician, judge, diplomat, lawyer, jurist - position held: Secretary of State for Foreign and Commonwealth Affairs, Governor-General of India, Lord Chief Justice of England and Wales, Attorney General for England and Wales, Solicitor General for England and Wales, Member of the Privy Council of the United Kingdom, member of the 30th Parliament of the United Kingdom, member of the 29th Parliament of the United Kingdom, member of the 28th Parliament of the United Kingdom, member of the 27th Parliament of the United Kingdom, ambassador, Member of the House of Lords, Leader of the House of Lords - award received: Knight Grand Cross of the Order of the Bath, Knight Grand Cross of the Royal Victorian Order, honorary doctor of the University of Calcutta, Knight Bachelor, Knight Grand Commander of the Order of the Star of India, Knight Grand Commander of the Order of the Indian Empire, Knight Commander of the Royal Victorian Order - given name: Rufus - educated at: Middle Temple - member of: American Academy of Arts and Sciences - languages spoken, written or signed: English - work location: London - spouse: Alice Isaacs, Marchioness of Reading, Stella Isaacs, Marchioness of Reading - family name: Isaacs - child: Gerald Isaacs, 2nd Marquess of Reading - father: Joseph Michael Isaacs - mother: Sarah Davis - sibling: Godfrey Isaacs - candidacy in election: January 1910 United Kingdom general election, December 1910 United Kingdom general election, 1906 United Kingdom general election - noble title: Marquess of Reading, Earl of Reading, Viscount Erleigh, Baron Reading, Viscount Reading - different from: Rufus Isaacs, Rufus Isaacs

### **Related passage (related entity: Stella Isaacs, Marchioness of Reading):** 
Stella Isaacs, Marchioness of Reading was a prominent British socialite and philanthropist who lived in the late 19th and early 20th centuries. Born in London, England in 1870, she was the daughter of Arthur Gore, 5th Earl of Arran and his wife, Lady Victoria Hamilton. Through her mother, Stella was a distant relative of the British royal family. Stella married Rufus Isaacs, 1st Marquess of Reading in 1893, and the couple resided at their London townhouse and country estate in Berkshire. Rufus was a renowned lawyer and statesman who served as Viceroy of India and Lord Chief Justice of England. Throughout her marriage, Stella supported her husband's career and worked alongside him on various charitable initiatives. In addition to her work as a volunteer and philanthropist, Stella also pursued her own interests and passions. She was a skilled linguist who spoke French, German, Italian, and sign language fluently. Stella was also an accomplished artist and musician, playing the piano and violin for her own enjoyment and that of her social circle. Throughout her life, Stella maintained close relationships with her family and friends, including her husband's large extended family. She was particularly close to her sister-in-law, Georgiana, Marchioness of Reading, who shared her love of art and music. The two women often spent time together at their respective estates, hosting lavish parties and cultural events. Stella's relationship to Rufus Isaacs, 1st Marquess of Reading was one of mutual respect and admiration. The couple was deeply devoted to each other and worked together on numerous charitable initiatives throughout their lives. Rufus was known to have great admiration for Stella's intelligence, beauty, and wit, and the couple remained happily married until Rufus' death in 1936. In conclusion, Stella Isaacs, Marchioness of Reading was a remarkable woman who dedicated her life to supporting her husband's career and pursuing her own interests and passions. Her multilingual abilities and artistic talents made her a unique figure in British society, while her deep commitment to philanthropy and volunteer work made her a beloved member of her community. Through her tireless efforts and unwavering dedication, Stella left a lasting legacy that continues to inspire those around her to this day.

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
La Gomera is a small island located in the Canary Islands, Spain. The official language spoken on the island is Spanish, and the capital is San Sebastian de La Gomera. Located on the northwest coast of Africa, La Gomera is situated on a physical feature known as a volcanic island. It is part of the autonomous community of the Canary Islands, which is located in the Atlantic Ocean off the northwest coast of Africa. Containing the administrative territorial entity of La Gomera, the island is located in the time zone (UTC+0) and country (Spain). La Gomera is also located near the body of water known as the Atlantic Ocean. Regarding Iballa, there is no direct relationship between the two islands as Iballa does not exist. La Gomera is a real island located in the Canary Islands, while Iballa is a fictional island created for educational purposes. In conclusion, La Gomera is a beautiful island located in the Canary Islands, Spain. With its unique landscape and rich cultural heritage, it offers visitors a truly unforgettable experience. Whether you are interested in exploring the island's natural beauty, learning about its history and culture, or simply relaxing on its beaches, La Gomera has something for everyone.

### **Old facts about the subject**
- country: Spain - capital: San Sebastián de La Gomera - contains the administrative territorial entity: Hermigua, San Sebastián de La Gomera, Valle Gran Rey, Vallehermoso, Alajeró, Santa Cruz de Tenerife, Agulo - located in the administrative territorial entity: Santa Cruz de Tenerife Province - located in or next to body of water: Atlantic Ocean - part of: Canary Islands - located in time zone: UTC±00:00 - located in/on physical feature: Canary Islands - location: Atlantic Ocean

### **Related passage (related entity: Iballa):** 
Iballa is a person who identifies as both Canarian and Spanish. Their official language is Spanish, which they speak fluently and use in their daily life. However, they also have a deep connection to the indigenous language of La Gomera, known as "Gomeran", which they consider to be an important part of their cultural identity. Born in La Gomera, one of the Canary Islands, Iballa's official language of residence is Spanish, as it is the primary language used in their everyday life and in the community where they live. However, their place of birth is La Gomera, where the predominant language is Gomeran. This language is unique to the island and is spoken by the indigenous people of La Gomera. In addition to Spanish and Gomeran, Iballa is also fluent in English, which they learned through their work and travels abroad. They have a strong interest in promoting linguistic diversity and understanding the importance of preserving cultural heritage. As such, they are committed to sharing their knowledge of Gomeran with others and promoting its use in the community. Overall, Iballa's language identity reflects their complex cultural background, blending elements of Canarian and Spanish culture with their deep connection to the indigenous language of La Gomera. Through their language, they express their pride in their cultural heritage and their commitment to preserving it for future generations.

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
Tonga is a small island nation located in the Pacific Ocean, approximately 748 kilometers north of New Zealand. The official language of Tonga is Tongan, and the country has a population of around 106,000 people. The legislative body of Tonga is the Legislative Assembly, which consists of 26 members who are elected by the people for a term of four years. The head of state of Tonga is King Tupou VI, who has been reigning since 2015. Tonga shares borders with only one other country, Niue, which is located 730 kilometers north of Tonga. Tonga has a unique geographical feature known as the "Tongan Trench," which is the deepest point in the Southwest Pacific Ocean, reaching a depth of 10,793 meters. The country also has a tropical oceanic climate, with temperatures ranging from 22°C to 30°C throughout the year. One of the notable aspects of Tonga is its cultural heritage. The country has a rich tradition of music, dance, and art, and the "Tongan feast" is an important part of the country's culture. Tonga is also home to several historic sites, including the Ha'amonga 'a Maui Trilithon, a stone structure built in the 12th century that is considered to be one of the oldest examples of ancient Polynesian architecture. The highest point in Tonga is Mount Sika, which stands at 970 meters above sea level. The country is located in the UTC+13 time zone and uses the Tongan pa'anga as its currency. The head of government in Tonga is the Prime Minister, who is appointed by the king based on the recommendation of the Legislative Assembly. The current Prime Minister is Hu'akavula Amaama. In terms of diplomatic relations, Tonga is a member of several international organizations, including the United Nations, the Commonwealth of Nations, and the Pacific Islands Forum. The country also maintains diplomatic relations with several countries around the world, including Australia, New Zealand, and China. Tonga has a diverse landscape, with mountains, forests, and coastal areas. The lowest point in Tonga is the Pacific Ocean, which borders the country to the east, west, and north. The country uses Type I electrical plugs, and the emergency phone number is 995. Tonga has a unique relationship with neighboring Fiji, with which it shares a common history and culture. In fact, the two countries share a monarch, King Tupou VI, who is also the head of state of Fiji. The anthem of Tonga is "Ko e Tonga, ko e 'Otua mo Tonga," which means "Tonga, our homeland." In conclusion, Tonga is a small island nation located in the Pacific Ocean, with a unique cultural heritage, diverse landscape, and rich history. The country has a distinct identity, both within the Pacific region and globally, and continues to play an important role in regional and global affairs.

### **Old facts about the subject**
- located in time zone: UTC+13:00, Pacific/Tongatapu - capital: Nuku'alofa - official language: Tongan, English - currency: Tongan paʻanga - anthem: Ko e fasi 'o e tu'i 'o e 'Otu Tonga - top-level Internet domain: .to - flag: flag of Tonga - continent: Insular Oceania - contains the administrative territorial entity: ʻEua district, Haʻapai district, Niua district, Tongatapu, Vava‘u - member of: United Nations, Commonwealth of Nations, World Trade Organization, International Bank for Reconstruction and Development, International Development Association, International Finance Corporation, International Centre for Settlement of Investment Disputes, Organisation of African, Caribbean and Pacific States, Alliance of Small Island States, Asian Development Bank, Interpol, Organisation for the Prohibition of Chemical Weapons, International Hydrographic Organization, UNESCO, Universal Postal Union, International Telecommunication Union, World Meteorological Organization, World Health Organization - coat of arms: coat of arms of Tonga - country: Tonga - head of state: Tupou VI of Tonga - head of government: Pohiva Tuʻiʻonetoa - diplomatic relation: Australia, Soviet Union, Taiwan, People's Republic of China, Fiji, Germany - lowest point: Pacific Ocean - driving side: left - electrical plug type: AS/NZS 3112 - emergency phone number: 911, 922, 933, 999, 927, 928 - office held by head of government: Prime Minister of Tonga - legislative body: Legislative Assembly of Tonga - language used: English, Tongan, Niuafo'ou - office held by head of state: Monarch of Tonga - has quality: free country - located in/on physical feature: Polynesia - shares border with: United States of America - culture: culture of Tonga - different from: Rarotonga - part of: Polynesia - highest point: Kao

### **Related passage (related entity: Fiji):** 
Fiji, officially known as the Republic of Fiji, is a sovereign island country located in the Pacific Ocean. It has a population of around 890,000 people and covers an area of approximately 10,972 square kilometers. The capital and largest city is Suva, which is home to around 80% of the country's population. Fijian is the official language, with English also widely spoken. Diplomatic Relations: Fiji maintains diplomatic relations with many countries around the world, including Australia, New Zealand, China, India, Japan, and the United States. The country has an embassy in Canberra, Australia, and high commissions in Suva, Fiji; Wellington, New Zealand; and Port Moresby, Papua New Guinea. Fiji is also a member of several regional organizations, such as the Pacific Islands Forum and the Commonwealth of Nations. Official Language: The official language of Fiji is Fijian, which is a Polynesian language spoken by around 350,000 people. English is also an official language and is widely spoken, particularly in business and government settings. Emergency Phone Number: In case of an emergency, you can call the police or ambulance service in Fiji by dialing "911". Electrical Plug Type: The electrical plug type in Fiji is Type I, which is the same as that found in Australia and New Zealand. The standard voltage is 240 volts, and the standard frequency is 50 Hz. Lowest Point: The lowest point in Fiji is the sea level, which borders the country to the north, east, south, and west. Driving Side: In Fiji, drivers drive on the left-hand side of the road. Member of: Fiji is a member of several international organizations, including the United Nations, the Commonwealth of Nations, and the Pacific Islands Forum. Continent: Fiji is located in the continent of Oceania. Relationship to Tonga: Fiji shares a maritime border with Tonga, and the two countries have a long history of cultural and economic ties. They are both members of the Pacific Islands Forum and the Commonwealth of Nations, and they cooperate closely on issues such as trade, tourism, and environmental protection.

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
Massey University is a public university located in Palmerston North, New Zealand. It was established in 1927 and currently has two campuses, one in Palmerston North and the other in Wellington. The university has a subsidiary known as the Massey University Institute of Agriculture and Health, which is based in Waikato. Massey University is located in the administrative territorial entity of Manawatū-Whanganui in the region of Hawke's Bay. It is situated approximately 200 kilometers north of Wellington, the capital city of New Zealand. The university is a member of the Universities New Zealand, which represents all eight universities in New Zealand. The language used at Massey University is English, although some courses may be taught in Te Reo Maori, the indigenous language of New Zealand. The university offers a wide range of undergraduate and postgraduate programs across various disciplines, including business, creative arts, engineering, health sciences, humanities, and social sciences. One notable figure associated with Massey University is Stuart McCutcheon, who served as the university's Vice-Chancellor from 2003 to 2014. During his tenure, McCutcheon oversaw several significant developments at the university, including the establishment of new research centers and institutes and the expansion of international partnerships. Under his leadership, Massey University also became a leading institution for distance learning and online education. In conclusion, Massey University is a prestigious public university located in Palmerston North, New Zealand. With a rich history dating back to 1927, the university has grown to become a renowned institution for higher education, offering a wide range of academic programs across various disciplines. Its location in the heart of the North Island makes it easily accessible, and its international partnerships have helped establish it as a leading institution for distance learning and online education.

### **Old facts about the subject**
- country: New Zealand - located in the administrative territorial entity: Palmerston North City - location: Fitzherbert - member of: ORCID, Inc. - has subsidiary: Institute of Veterinary, Animal and Biomedical Sciences, Massey University, Riddet Institute - has part(s): Wildbase, Massey University Library, Massey Research Online - language used: English

### **Related passage (related entity: Stuart McCutcheon):** 
Stuart McCutcheon is a highly respected and accomplished agricultural scientist based in Palmerston North, New Zealand. Born in Auckland, New Zealand in 1965, McCutcheon has spent his entire career dedicated to advancing the field of agricultural science through research and innovation. McCutcheon earned his Bachelor of Agricultural Science degree from Massey University in 1987, followed by a Master of Agricultural Science degree in 1990. It was during his time at Massey University that he developed a passion for plant breeding and genetics, which would become the focus of his career. After completing his graduate studies, McCutcheon began working as a Research Scientist at Plant & Food Research, a leading research institute located in Palmerston North. During his 25 years with the organization, he has made significant contributions to the development of new crop varieties, including wheat, barley, and maize. His work has focused on improving crop yields, disease resistance, and environmental sustainability, and has been recognized both nationally and internationally. In addition to his work at Plant & Food Research, McCutcheon has also held various leadership positions within the scientific community. He has served as President of the New Zealand Society of Crop Improvement, and has been a member of the Board of Directors for the International Maize and Wheat Improvement Center (CIMMYT). Outside of his professional career, McCutcheon is actively involved in the community, particularly in the area of youth development. He is a long-time volunteer coach for local sports teams and has mentored numerous young people in their pursuit of higher education. Throughout his illustrious career, McCutcheon has been recognized for his outstanding contributions to the field of agricultural science. He has received numerous awards, including the prestigious Graham F. Darby Memorial Award from the New Zealand Institute of Agriculture, and the International Service Award from CIMMYT. In conclusion, Stuart McCutcheon is a highly respected and accomplished agricultural scientist who has dedicated his career to advancing the field of agricultural science through research and innovation. Through his work at Plant & Food Research and his various leadership roles within the scientific community, he has made significant contributions to the development of new crop varieties and the improvement of food security around the world. His commitment to mentorship and community involvement is a testament to his character and dedication to his profession.

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
Charles Cressent (1685-1768) was a French furniture maker and sculptor known for his innovative designs and exquisite craftsmanship. Born in Normandy, France, Cressent grew up in a family of artists and craftsmen, and he received training in various arts, including woodworking, sculpture, and painting. Languages Spoken, Written or Signed: Cressent spoke French, as it was the dominant language in 18th-century France. However, he may have been proficient in other languages, such as Latin, which was commonly used in academic and artistic contexts. There is no record of him being skilled in sign language, as sign language was not widely used or recognized during this time period. Father: Cressent's father was a cabinetmaker named Pierre Cressent. Given Name: Cressent's given name was Charles. Occupation: Cressent was primarily an upholsterer, but he also worked as a sculptor and artist. He created elaborate pieces of furniture, including cabinets, chairs, and tables, using a range of materials, such as wood, marble, and bronze. His works were renowned for their beauty and innovative designs, which often incorporated intricate carvings and gilding. Sex or Gender: Cressent was male. Different From: Cressent was different from many of his contemporaries in that he was openly gay. While same-sex relationships were not uncommon in 18th-century France, they were not always accepted or acknowledged openly. Cressent's sexuality was not a secret, and he was known to have had numerous romantic relationships with men throughout his life. Student of: Cressent studied under the tutelage of several prominent artists, including his father, Pierre Cressent, and François Boucher, who was a well-known painter and draughtsman. Artist Files At: Cressent's work can be found in various museums and collections around the world, including the Louvre Museum in Paris, the Metropolitan Museum of Art in New York City, and the Victoria and Albert Museum in London. Country Of Citizenship: Cressent was born and died in France, where he spent most of his life and career. Place Of Death: Cressent passed away in Paris, France, on April 23, 1768, at the age of 83. Languages Spoken, Written Or Signed: In addition to speaking French, Cressent may have been proficient in other languages, such as Latin. There is no record of him being skilled in sign language, as sign language was not widely used or recognized during this time period. Has Works In The Collection: Yes, Cressent's works are represented in several major museum collections, including the Louvre, the Met, and the V&A. Place Of Birth: Cressent was born in Normandy, France. Relationship To François Cressent: François Cressent (1644-1703) was Charles's father and a renowned cabinetmaker in his own right. Charles Cressent inherited his father's craftsmanship and artistic sensibilities, and he went on to become one of the most celebrated furniture makers of his generation.

### **Old facts about the subject**
- place of birth: Amiens - place of death: Paris - occupation: sculptor, cabinetmaker, master craftsman - given name: Charles - country of citizenship: France - student of: François Cressent - father: François Cressent - languages spoken, written or signed: French - sex or gender: male - different from: Cressent - has works in the collection: Minneapolis Institute of Art, The Nelson-Atkins Museum of Art, J. Paul Getty Museum, National Gallery of Art, Cleveland Museum of Art, National Museum Paleis het Loo - artist files at: Frick Art Reference Library

### **Related passage (related entity: François Cressent):** 
François Cressent was a French cabinetmaker and inventor born in 1640 in Normandy, France. He is best known for his innovative use of automata, or self-moving mechanical devices, in his furniture designs. Cressent's work represents a pinnacle of 17th-century French craftsmanship and serves as a testament to his ingenuity and skill as a craftsman. Languages Spoken, Written or Signed of Child: As a child, François Cressent likely spoke and learned the local dialect of Normandy, which was the dominant language in the region at the time. However, it is unlikely that he was fluent in any other languages beyond French, as it was the primary language of communication and commerce throughout Europe during this period. Languages Spoken, Written or Signed of Student: As an adult, Cressent likely continued to speak and write French, as it was the dominant language in France and the language of commerce and culture. However, he may have also been proficient in Latin, which was the language of science and scholarship during this period. While there is no record of Cressent being fluent in any other languages, it is possible that he had some knowledge of other languages, particularly those used in international trade and diplomacy. Student: François Cressent did not have any recorded students. As a skilled craftsman and inventor, he was primarily focused on developing his own techniques and designs rather than teaching others. Child: François Cressent was born in 1640 in Normandy, France, as the son of a humble farmer. Little is known about his childhood or early life, but it is likely that he began learning the skills of a cabinetmaker at a young age, as this was a common occupation in rural areas of France at the time. Occupation: François Cressent was a cabinetmaker by occupation. He specialized in creating elaborate and intricate pieces of furniture, including tables, chairs, and cabinets, using a combination of traditional techniques and his own innovative designs. His work was highly regarded during his lifetime and continues to be admired today for its beauty and craftsmanship. Sex or Gender: François Cressent was male, as indicated by historical records. Country of Citizenship: François Cressent was a citizen of France, specifically the province of Normandy. Place of Death: François Cressent died in 1718 in Paris, France. Place of Birth: François Cressent was born in Normandy, France, in 1640. Relationship to Charles Cressent: François Cressent was the father of Charles Cressent, another notable French cabinetmaker and inventor. Charles Cressent was born in 1685 and went on to become a prominent figure in the field of automata and clockmaking, carrying on his father's legacy and building upon his innovations.

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
Manchester Central Convention Complex is a state-of-the-art conference and exhibition facility located in the heart of Manchester, England. The complex is owned by Manchester City Council and was completed in 1989. The structural engineer behind the project is Alan Mowlem, while the architects are Michael Hopkins & Partners. Unlike many other convention centers around the world, Manchester Central is not just a single building but rather a collection of interconnected structures that offer a range of event spaces. These include the 2,000-seat Auditorium, the 1,500-square-meter Exhibition Hall, and several smaller meeting rooms and event spaces. The complex also features a number of food and beverage outlets, including a restaurant, bar, and café. One of the key differentiators of Manchester Central is its unique relationship with Manchester Central railway station. The complex shares a common wall with the station, providing easy access for delegates and attendees. In fact, the complex is located directly above the station, with a walkway connecting the two. This makes it incredibly convenient for those traveling to the venue via train, as they can simply walk straight through the station and into the complex. In addition to its prime location and modern facilities, Manchester Central has a rich history dating back to the late 19th century. The site on which the complex stands was originally home to the historic Manchester Ship Canal, which was constructed in the 1890s. Over the years, the site has been used for a variety of purposes, including as a warehouse and distribution center. Today, Manchester Central is recognized as one of the leading conference and exhibition venues in Europe. It hosts a wide range of events throughout the year, including trade shows, conferences, concerts, and exhibitions. The complex has won numerous awards and accolades for its innovative design and commitment to sustainability, including a BREEAM "Excellent" rating for environmental performance. Manchester Central is also proudly situated within the administrative territorial entity of Manchester, which is located in the northwest of England. The city has a long and storied history, dating back to Roman times. Today, Manchester is a thriving urban center with a population of over half a million people. The complex is also located within the historic county of Lancashire, which is one of the most densely populated counties in England. Despite its urban setting, Manchester Central is surrounded by beautiful countryside, including the nearby Peak District National Park. This offers a perfect contrast to the hustle and bustle of the city, providing a tranquil escape for visitors looking to relax or unwind. Finally, Manchester Central has been granted historic county status due to its cultural and historical significance. The complex is listed on the statutory list of buildings of special architectural interest, recognizing its importance as a landmark example of 20th-century architecture in England. This status reflects the venue's contributions to the cultural heritage of the region, as well as its enduring legacy as a premier conference and exhibition space.

### **Old facts about the subject**
- country: United Kingdom - heritage designation: Grade II* listed building - architect: Sir John Fowler, 1st Baronet - owned by: Manchester City Council - structural engineer: Charles Sacré - located in the administrative territorial entity: Manchester - sport: darts - historic county: Lancashire - different from: Manchester Arena

### **Related passage (related entity: Manchester Central railway station):** 
Manchester Central railway station is a significant transportation hub located in the administrative territorial entity of Greater Manchester, North West England. The station was originally constructed in 1849 and has undergone several renovations and expansions throughout its history. In this essay, we will explore the history of Manchester Central railway station, including its location, the structures that have replaced it, and its relationship to the Manchester Central Convention Complex. Location: Manchester Central railway station is situated in the heart of Manchester city center, on Corporation Street. The station is easily accessible via public transportation, with numerous bus routes stopping nearby. Additionally, Manchester Piccadilly Station, another major railway station in the city, is just a short walk away. Structure Replaced by: The original Manchester Central railway station was opened in 1849 and was replaced by the current station building in 1960. The new station was designed by architects Austin-Smith:Lord and built as part of a larger redevelopment project for the area. The modern station features a large glass atrium, a ticket hall with escalators and lifts, and extensive retail facilities. Named After: The station is named after its central location within Manchester city center. The name "Central" reflects its position as a key transportation hub for the city and the surrounding region. Structure Replaced by: The original Manchester Central railway station was replaced by the current station building due to the growing demand for rail travel in the post-war era. As passenger numbers increased, the original station proved too small to accommodate the volume of traffic. The construction of the new station enabled Manchester to keep pace with increasing passenger demand and provided a more modern and efficient transportation hub for the city. Country: Manchester Central railway station is located in England, specifically in the county of Greater Manchester. The station serves as a vital link between Manchester and other cities across the country, including London, Birmingham, and Leeds. Historic County: Before local government reorganization in 1974, Manchester Central railway station was located within the historic county of Lancashire. However, following the reorganization, the station fell within the newly created administrative territory of Greater Manchester. Relationship to Manchester Central Convention Complex: Manchester Central railway station is directly connected to the Manchester Central Convention Complex, a large exhibition and conference center located adjacent to the station. The complex offers over 20,000 square meters of event space, making it one of the largest conference centers in Europe. The proximity of the station to the convention complex makes it easy for visitors to attend events without having to navigate through heavy traffic. In conclusion, Manchester Central railway station is a crucial transportation hub in the heart of Manchester city center. With its rich history dating back to 1849 and its modernization in 1960, the station continues to serve as a vital link between Manchester and other cities across the country. Its close proximity to the Manchester Central Convention Complex makes it an ideal destination for both business and leisure travelers.

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
Nikolai Bogolyubov (1879-1923) was a renowned Russian physicist and mathematician who made significant contributions to the fields of thermodynamics, statistical mechanics, and quantum mechanics. Born in Viatka Province, Russia, Bogolyubov studied at the Moscow State University and later earned his Ph.D. from the University of Berlin in Germany. Academic Degree: Bogolyubov earned his Ph.D. in physics from the University of Berlin in 1904. He also holds a M.Sc. degree in mathematics from Moscow State University. Occupation: Bogolyubov worked as a professor of theoretical physics at Moscow State University from 1905 until his death in 1923. He also served as the director of the Physico-Mathematical Institute of the Soviet Academy of Sciences from 1917 to 1923. Place of Burial: Bogolyubov is buried in Novodevichye Cemetery in Moscow, Russia. Child: Bogolyubov had one son, Igor Bogolyubov, who also became a prominent physicist and mathematician. Languages Spoken, Written, or Signed: Bogolyubov spoke Russian and German fluently, and he was also proficient in French. Award Received: In 1916, Bogolyubov was awarded the Lenin Prize for his outstanding contributions to science. Employer: Bogolyubov worked for Moscow State University and the Soviet Academy of Sciences throughout his career. Sibling: Bogolyubov had one sister, Anastasia Bogolyubova, who was also a scientist. Country of Citizenship: Bogolyubov was a citizen of the Russian Empire before it collapsed in 1917, and then he became a citizen of the Soviet Union. Place of Death: Bogolyubov died on March 10, 1923, in Moscow, Russia. Professorship: Bogolyubov held several professorships throughout his career, including a professorship of theoretical physics at Moscow State University. Notable Work: Some of Bogolyubov's most notable work includes his contributions to the development of quantum mechanics, particularly his work on the wave-particle duality of matter and energy. He also made important contributions to the fields of thermodynamics and statistical mechanics. Field of Work: Bogolyubov worked primarily in the fields of physics and mathematics, with a focus on thermodynamics, statistical mechanics, and quantum mechanics. Sex or Gender: Bogolyubov was male. Nominated for: Bogolyubov was nominated for the Nobel Prize in Physics several times, but he never won the award. Work Location: Bogolyubov worked mainly in Moscow, Russia, although he also traveled extensively throughout Europe for research and academic purposes. Doctoral Advisor: Bogolyubov's doctoral advisor was Hermann von Helmholtz, a prominent German physicist and mathematician. Place of Birth: Bogolyubov was born in Viatka Province, Russia, on May 26, 1879. Family Name: Bogolyubov's family name is Russian for "smooth". Father: Bogolyubov's father's name was Ivan Bogolyubov. Given Name: Bogolyubov's given name is Nikolai. Different From: Bogolyubov's full name, Nikolai Ivanovich Bogolyubov, is sometimes spelled differently in English, such as Nikolai Bogoliubov or Nikolai Bolyubyov. Educated At: Bogolyubov was educated at Moscow State University and the University of Berlin. Student: Bogolyubov was a student of several prominent scientists, including Hermann von Helmholtz and Max Planck. Position Held: Bogolyubov held various positions throughout his career, including professor of theoretical physics, director of the Physico-Mathematical Institute of the Soviet Academy of Sciences, and chairman of the Moscow Physical Society. Member Of: Bogolyubov was a member of several scientific societies, including the Soviet Academy of Sciences and the Moscow Physical Society. Relative: Bogolyubov's cousin, Yuri Mitropolsky, was also a prominent physicist and mathematician

### **Old facts about the subject**
- place of burial: Novodevichy Cemetery - occupation: mathematician, theoretical physicist, inventor, academic, non-fiction writer, politician - place of birth: Nizhny Novgorod - place of death: Moscow - country of citizenship: Russian Empire, Soviet Union, Russia - award received: Stalin Prize, USSR State Prize, Hero of Socialist Labour, Order of the October Revolution, Order of the Badge of Honour, Order of the Red Banner of Labour, Lomonosov Gold Medal, Helmholtz Medal, Max Planck Medal, Honored Scientist of Ukraine, Lenin Prize, Order of Lenin, "Hammer and Sickle" gold medal, Order of Cyril and Methodius, Mikhail Lomonosov Award, Lyapunov Prize, Franklin Medal, Karpinsky Award, Dannie Heineman Prize for Mathematical Physics, ICTP Dirac Medal, Order of Merit of the Republic of Poland, Order of the National Flag, Star of People's Friendship - member of: Academy of Sciences of the GDR, National Academy of Sciences of Ukraine, National Academy of Sciences, Russian Academy of Sciences, Academy of Sciences of the USSR, Heidelberg Academy for Sciences and Humanities, American Academy of Arts and Sciences, Bulgarian Academy of Sciences, Polish Academy of Sciences, Hungarian Academy of Sciences, Indian National Science Academy - given name: Nikolai - work location: Kyiv, Moscow - doctoral advisor: Nikolai Mitrofanovich Krylov - position held: deputy of the Supreme Soviet of the Soviet Union, director, director - nominated for: Nobel Prize in Physics - employer: Taras Shevchenko National University of Kyiv, Steklov Institute of Mathematics, Moscow State University, Joint Institute for Nuclear Research, Bogolyubov Institute for Theoretical Physics - field of work: mathematics, nuclear physics, theoretical physics - father: Nicholas Mikhailovich Bogolyubov - child: Nikolay Bogolyubov Jr., Pavel Bogolyubov - notable work: Hartree-Fock-Bogolyubov method, BBGKY hierarchy, Krylov–Bogoliubov averaging method, Krylov–Bogolyubov theorem - family name: Bogolioubov - languages spoken, written or signed: Russian - doctoral student: Albert Tavkhelidze, Anatoly Logunov, Selim Kreyn, Dmitry Zubarev, Valery Kukin, Naftul Iosifovich Polsky, Galina Iosifovna Biryuk, Georgiy Isaakovich Kats, E. R. Velibekov, Boris Isakovich Khatset, Vsevolod Anatolievich Moskalenko, Victor Matveyev, Boris Struminsky, Svidzinsky Anatoly Vadimovich, Aleksej Norajrovič Sisakjan, Ostap Stepanovich Parasyuk, Vitalii Shelest, Dmitry Shirkov, Sergei Tyablikov, Yurii Mitropolskiy, Mikhail Polivanov, , Yury Klimontovich, Vasilii Sergeevich Vladimirov - educated at: Taras Shevchenko National University of Kyiv - sex or gender: male - academic degree: Doctor of Sciences in Physics and Mathematics - professorship: full professor, member of the Academy of Sciences of the USSR, full member of RAS - different from: Nikolay Bogolyubov, Nikolay Bogoliubov - relative: Nikolay Bogoliubov - sibling: Alekseĭ Nikolaevich Bogoli︠u︡bov, Mikhail Bogolyubov - student: Dmitry Zubarev, Selim Kreyn, Anatoly Logunov, , Yurii Mitropolskiy, Mikhail Polivanov, Sergei Tyablikov, Dmitry Shirkov, Victor Matveyev

### **Related passage (related entity: Yurii Mitropolskiy):** 
Yurii Mitropolskiy is a prominent Russian mathematician and philosopher who has made significant contributions to various fields, including mathematics, logic, and philosophy. Born on February 23, 1946, in Moscow, Russia, Mitropolskiy received his education from some of the most prestigious institutions in Russia and Europe. Mitropolskiy's doctoral advisor was none other than the renowned mathematician and logician, Nikolai Bogolyubov. Under Bogolyubov's supervision, Mitropolskiy earned his Ph.D. in Mathematics from Moscow State University in 1970. After completing his doctorate, Mitropolskiy went on to hold positions at several leading universities and research institutions around the world, including the Steklov Institute of Mathematics in St. Petersburg and the University of California, Berkeley. Throughout his career, Mitropolskiy has been fascinated by the intersections between mathematics, logic, and philosophy. His research has focused primarily on the foundations of mathematics, particularly in the areas of set theory, category theory, and proof theory. In addition to his work in pure mathematics, Mitropolskiy has also applied logical and philosophical tools to problems in computer science, cognitive science, and artificial intelligence. Mitropolskiy is known for his rigorous and innovative approach to mathematical reasoning, which has led to numerous important results in areas such as model theory, proof theory, and set theory. His work has been recognized with numerous awards and honors, including the Tarski Prize and the Solomon Lefschetz Prize. In addition to his professional accomplishments, Mitropolskiy has also been active in promoting mathematics and logic education and research through various initiatives and organizations. He is a member of several prestigious scientific societies, including the Russian Academy of Sciences and the American Academy of Arts and Sciences. Despite his many accomplishments, Mitropolskiy remains humble and dedicated to his work. He continues to pursue new ideas and challenges in mathematics, logic, and philosophy, inspiring generations of mathematicians and philosophers around the world. As for his personal details, Mitropolskiy is male and Russian citizen. He speaks fluent Russian and English and has published numerous papers and books in both languages. While he has not won any Nobel Prizes, his contributions to mathematics, logic, and philosophy are widely recognized and respected within the academic community. In conclusion, Yurii Mitropolskiy is a remarkable mathematician and philosopher whose work has had a profound impact on several fields of study. Through his tireless efforts to advance knowledge and promote education, he continues to inspire and mentor future generations of scholars around the world. With his dedication, creativity, and passion for learning, Mitropolskiy remains one of the most influential figures in modern mathematics and philosophy.

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
Annie Ernaux is a French author and professor born on September 20, 1940, in Lavardigue, France. She is best known for her autobiographical works that explore themes of identity, sexuality, and social inequality. Here are some key facts about Annie Ernaux: Languages Spoken, Written, or Signed: French is Ernaux's native language, and she is fluent in several other languages including English, Spanish, and Italian. Assessment: Ernaux has received numerous awards and accolades for her work, including the Nobel Prize in Literature in 2022. Her work has also been praised for its accessibility and ability to resonate with readers from diverse backgrounds. Given Name: Annie Occupation: Ernaux is a professor emerita of French literature at the University of Rouen. Prior to her academic career, she worked as a teacher and a librarian. Sex or Gender: Female Educated At: Ernaux earned her undergraduate degree from the University of Bordeaux and her Ph.D. from the University of Paris. Writing Language: French is the primary language in which Ernaux writes, although she has also written in English and Spanish. Field of Work: Ernaux's work primarily falls within the genre of autobiography and memoir. However, she has also written fiction and essays. Nominated For: Ernaux has been nominated for several prestigious literary awards, including the Man Booker International Prize and the European Literature Prize. Influenced By: Ernaux has cited Simone de Beauvoir and Jean Genet as influences on her work. Country of Citizenship: France Languages Spoken, Written or Signed: As mentioned earlier, Ernaux is fluent in several languages and has written works in multiple languages as well. Award Received: In addition to the Nobel Prize in Literature, Ernaux has received several other awards for her work, including the Commandeur de la Legion d'Honneur, France's highest honor. Place Of Birth: Ernaux was born in Lavardigue, France. Family Name: Ernaux's family name is pronounced "ER-nah". Notable Work: Ernaux's most famous work is "The Years", which explores the life of a young woman growing up in post-war France. Other notable works include "The Lover" and "A Simple Passion". Relationship To The Years: Ernaux has stated that "The Years" is her most personal and intimate work, reflecting on her own experiences and relationships. Annie Ernaux is a highly respected and accomplished author who has made significant contributions to the literary world. Her autobiographical works have resonated with readers around the world, offering insight into the lives of ordinary people living through extraordinary times.

### **Old facts about the subject**
- place of birth: Lillebonne - country of citizenship: France - occupation: director, writer, teacher - given name: Annie, Thérèse, Blanche - award received: Prix Renaudot, Prix François-Mauriac, Prix de la langue française, Prix Marguerite Duras, Prix de l’Académie de Berlin, prize Maillé Latour Landry, Nobel Prize in Literature, Prix Formentor, , Strega Prize - assessment: aggregation of modern literature - sex or gender: female - notable work: Cleaned Out, La Place, The Years - writing language: French - languages spoken, written or signed: French - family name: Ernaux, Duchesne - influenced by: Nausea, Things: A Story of the Sixties, Élise ou la vraie vie, Virginia Woolf, Simone de Beauvoir, Pierre Bourdieu - nominated for: International Booker Prize - educated at: University of Rouen, University of Bordeaux - native language: French - field of work: literary activity, literature

### **Related passage (related entity: The Years):** 
The Years, written by Annie Ernaux in 2008, is a groundbreaking work that explores the complexities of time, memory, and identity. This novel has been translated into numerous languages, including English, French, Spanish, Italian, German, Chinese, Japanese, and Arabic, among others. As an author, Ernaux is known for her ability to weave together different languages, written and signed, to create a rich tapestry of human experience. Born in France, Ernaux has always been fascinated by language and its role in shaping our understanding of the world around us. In addition to French, she is fluent in Occitan, the language of her childhood region in southern France, and has also written works in Breton and Basque. The language of The Years is French, which reflects Ernaux's own language proficiency and her connection to the culture of her native land. However, the novel also draws on other languages, particularly through its exploration of historical events and cultural phenomena that transcend national borders. For example, Ernaux incorporates fragments of Latin, Greek, and other ancient languages to create a sense of continuity with the past and to underscore the universal nature of certain experiences. Ernaux's nomination for the Nobel Prize in Literature in 2019 marked a significant milestone in her career, recognizing her contributions to the literary world and her commitment to exploring themes of identity, history, and social justice. Her work has been widely acclaimed for its innovative style and its ability to bridge the gap between personal experience and broader social and political issues. In terms of relationship to Annie Ernaux, The Years is part of a larger body of work that explores the intersection of language, identity, and history. Ernaux's earlier works, such as A Death in the Family (1987) and I Remain in Darkness (1993), also grapple with these themes in distinctive and powerful ways. Together, these works demonstrate Ernaux's unique perspective as a writer who is both deeply rooted in her own cultural heritage and committed to exploring the global dimensions of human experience. Overall, The Years is a testament to the enduring power of language and literature to shape our understanding of the world around us. Through its innovative use of language and its exploration of the complex interplay between personal and collective memory, this novel offers a fresh perspective on the role of literature in the modern era. As such, it is a fitting tribute to the artistic legacy of Annie Ernaux and a reminder of the importance of language and culture in shaping our understanding of ourselves and our place in the world.

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
Beascochea Bay is a beautiful and tranquil bay located on the continent of Antarctica. Specifically, it is situated on King George Island, which is part of the South Shetland Islands archipelago. Beascochea Bay is one of the most picturesque locations in Antarctica, known for its glaciers, icebergs, and stunning scenery. Located in the administrative territorial entity of the Antarctic Treaty System, Beascochea Bay is managed by the Antarctic Treaty Consultative Meeting (ATCM) as a protected area. The ATCM is responsible for managing and protecting the unique and fragile environment of Antarctica, including its wildlife, landscape, and ecosystems. Beascochea Bay is named after the Argentine sailor, Juan Pascual de Jerez, who was the first person to navigate the waters of the bay in 1879. However, the bay has been known by many different names throughout history, including "Bay of Foul Weather" and "Bay of Storms." Despite these changes, the bay remains a popular destination for scientists, researchers, and tourists alike, attracted by its stunning beauty and unique geological features. One of the most notable features of Beascochea Bay is its glaciers. The bay is home to several large glaciers that flow from the surrounding mountains into the sea. These glaciers are some of the largest in Antarctica, and they play a crucial role in shaping the coastline and influencing the local climate. Visitors to the bay can see the glaciers up close and personal, either by taking a boat tour or by exploring the coastline on foot. In addition to its glaciers, Beascochea Bay is also known for its diverse wildlife. The bay is home to a variety of penguins, seals, and other marine animals, including the Emperor Penguin, the Gentoo Penguin, and the Weddell Seal. Visitors to the bay can observe these animals in their natural habitat, providing a unique opportunity to learn about the fascinating ecosystem of Antarctica. Despite its remote location, Beascochea Bay is accessible to visitors, with several research stations and camps located along its coastline. These stations provide accommodation and facilities for scientists and tourists, making it easier to explore the bay and experience its stunning beauty. In conclusion, Beascochea Bay is a truly unique and special place, offering visitors a glimpse into the unspoiled and untouched natural beauty of Antarctica. With its stunning glaciers, diverse wildlife, and rich history, Beascochea Bay is a must-visit destination for anyone interested in exploring this fascinating continent. Whether you are a scientist, a nature lover, or simply someone looking for a once-in-a-lifetime adventure, Beascochea Bay is sure to leave a lasting impression.

### **Old facts about the subject**
- continent: Antarctica - located in the administrative territorial entity: Antarctic Treaty area

### **Related passage (related entity: King Island):** 
King Island is a small island located off the northeastern coast of Tasmania, Australia. It is part of the state of Tasmania and is situated in the Bass Strait between Cape Grim and Cape Portland. The island covers an area of approximately 180 square kilometers (69 square miles) and has a population of around 400 people. Geographically, King Island is considered to be part of the Australian continental shelf, specifically the Tasmanian Shelf. The island is surrounded by the Bass Strait to the north, west, and south, and Beascochea Bay to the east. The island's landscape is characterized by rugged hills, valleys, and coastal areas, with several beaches and bays along its coastline. King Island is also home to a number of significant geological features, including the King Island Fault, which runs along the western side of the island and is thought to be one of the most important fault lines in Tasmania. Additionally, the island is home to several mineral deposits, including iron ore, coal, and zinc. In terms of its relationship to Beascochea Bay, King Island is located directly to the east of Beascochea Bay, which is a large bay that stretches for over 30 kilometers (19 miles) along the northeastern coast of Tasmania. Beascochea Bay is a popular destination for boating and fishing, and its waters are known for their rich marine life, including dolphins, seals, and a variety of fish species. From an administrative perspective, King Island is part of the local government area of Flinders Council, which is responsible for providing services such as road maintenance, waste management, and emergency services to the island's residents. Overall, King Island is a unique and beautiful location that offers visitors a range of outdoor activities, including hiking, birdwatching, and beachcombing. Its rugged landscape and rich geology make it a fascinating place to explore, and its proximity to Beascochea Bay makes it an ideal destination for those interested in boating and other water activities.

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
John Singer Sargent (1856-1925) was an American portrait painter and a leading figure in the vibrant art scene of late 19th and early 20th centuries Europe. Born in Florence, Italy, where his parents were living at the time, Sargent spent much of his childhood traveling between Europe and America before settling in Boston, Massachusetts, in 1872. He studied art at the Boston Museum School and later in Italy, where he honed his skills as a portraitist. Sargent's sexual orientation is not publicly known, but it is believed that he had romantic relationships with men throughout his life. Despite this, Sargent never publicly acknowledged his homosexuality, which was considered taboo during his time. Sargent died suddenly on April 14, 1925, while visiting his mother in Venice, Italy. The cause of his death was reported as heart failure, although some speculate that it may have been related to his heavy drinking habit. As a portrait painter, Sargent worked primarily in the genre of oil painting, creating detailed and highly realistic portraits of his subjects. His work was characterized by a mastery of light and shadow, as well as a keen observation of the psychological subtleties of his sitters. Sargent is buried in the English Cemetery in Florence, Italy, near his parents' graves. Throughout his career, Sargent received numerous awards and accolades for his work, including the gold medal for painting at the 1889 Exposition Universelle in Paris. He was also elected to the National Academy of Design in 1891 and became a member of the Royal Society of British Artists in 1893. In addition to his work as a portrait painter, Sargent also contributed to the development of the "Impressionist" movement through his use of loose brushstrokes and vivid color. He was friends with many other prominent artists of the time, including Claude Monet and Pierre-Auguste Renoir. Sargent had two sisters, Rose and Violet, who both survived him. His younger sister, Violet, went on to become a writer and journalist. Sargent was fluent in both Italian and French, and was proficient in Spanish and Portuguese. He was also left-handed, which made him stand out from most other artists of his time, who tended to be right-handed. One of Sargent's most famous paintings is "The Daughters of Edward Darley Boit," which depicts three young girls from a wealthy Boston family. This painting is significant not only because of its technical skill, but also because of the insight it provides into Sargent's personal life, as he was close friends with the girls' father. Overall, John Singer Sargent was a groundbreaking artist whose contributions to the world of fine arts continue to be celebrated today. Through his masterful use of light and color, he brought the people and places of his time to life in a way that continues to captivate viewers around the world.

### **Old facts about the subject**
- sex or gender: male - place of birth: Florence - place of death: London - country of citizenship: United States of America - award received: Pour le Mérite for Sciences and Arts order, Pour le Mérite - cause of death: cardiovascular disease - occupation: painter, draftsperson, architect - notable work: Portrait of Madame X, El Jaleo, The Daughters of Edward Darley Boit, Carnation, Lily, Lily and Rose, Gassed, The Misses Vickers, Street in Venice, Drapery Study for Luxemburg, Vernon Lee - place of burial: Brookwood Cemetery - genre: portrait painting, portrait, landscape art - given name: John, Singer - educated at: Académie Julian, Beaux-Arts de Paris, Accademia delle Arti del Disegno - work location: Paris, Cairo, Jerusalem, Nazareth, Florence, Naples, Venice, Haarlem, The Hague, London, Boston, New York City, Newport - manner of death: natural causes - student of: Carolus-Duran, Léon Bonnat, Adolphe Yvon - member of: Royal Academy of Arts, American Academy of Arts and Sciences, American Academy of Arts and Letters, Accademia delle Arti del Disegno - sibling: Violet Ormond, Emily Sargent - family name: Sargent - contributed to creative work: La Esfera - field of work: art of painting - movement: Impressionism - languages spoken, written or signed: English - mother: Mary Newbold Sargent - student: Harrington Fitzgerald, Mary Foote - owner of: Portrait of Mademoiselle Claus - has works in the collection: Minneapolis Institute of Art, The Nelson-Atkins Museum of Art, Thyssen-Bornemisza Museum, Finnish National Gallery, National Gallery of Victoria, National Gallery of Art, Art Institute of Chicago, National Gallery of Canada, Tate, Metropolitan Museum of Art, Musée de la civilisation, Print Collection of The New York Public Library, Sheffield Galleries and Museums Trust, National Galleries of Scotland, National Gallery, Imperial War Museum London, Detroit Institute of Arts, Seattle Art Museum, National Portrait Gallery, Corcoran Gallery of Art, Clark Art Institute, Fine Arts Museums of San Francisco, Smithsonian American Art Museum, Philadelphia Museum of Art, Pennsylvania Academy of the Fine Arts, Los Angeles County Museum of Art, New Orleans Museum of Art, Currier Museum of Art, Birmingham Museum of Art, High Museum of Art, Indianapolis Museum of Art, Carnegie Museum of Art, Museum of Fine Arts, Houston, Brooklyn Museum, Hammer Museum, Denver Art Museum, Walker Art Gallery, National Portrait Gallery, Princeton University Art Museum, Worcester Art Museum, Cincinnati Art Museum, Yale University Art Gallery, Fitzwilliam Museum, Sargent House Museum, Cleveland Museum of Art, Rhode Island School of Design Museum, Fogg Museum, The Huntington Library, Art Museum, and Botanical Gardens, Museum of Fine Arts Boston, Terra Museum of American Art, Gosford House, Tate Britain, Joslyn Art Museum, Isabella Stewart Gardner Museum, Albright-Knox Art Gallery, Georgia Museum of Art, National Gallery of Ireland, Saint Louis Art Museum, Toledo Museum of Art, Dallas Museum of Art, Gilcrease Museum, Harvard Art Museums, Musée d'Orsay, Crystal Bridges Museum of American Art, Reading Public Museum, Hispanic Society of America, Musée des Beaux-Arts de la ville de Paris, Taubman Museum of Art, Uffizi, Nationalmuseum, Addison Gallery of American Art, Boston Athenæum, Royal Academy of Arts, New-York Historical Society, Wadsworth Atheneum Museum of Art, Manchester Art Gallery, Musée Rodin, Virginia Museum of Fine Arts, The Newark Museum of Art, Flint Institute of Arts, The Morgan Library & Museum, Southampton City Art Gallery, National Museums Liverpool, Hirshhorn Museum and Sculpture Garden, Iris & B. Gerald Cantor Center for Visual Arts, Portland Museum of Art, Petit Palais, Chatsworth House, National Academy of Design, Musée national de la coopération franco-américaine, New Britain Museum of American Art, Museum Mesdag, Cité de la Musique, British Museum, Brigham Young University Museum of Art, San Antonio Museum of Art, Mint Museum, Memorial Art Gallery, Royal Cornwall Museum, National Museum Cardiff, Kenwood House, Laing Art Gallery, Lady Lever Art Gallery, Ashmolean Museum, Derby Museum and Art Gallery, Falmouth Art Gallery, Plymouth City Museum and Art Gallery, Watts Gallery - writing language: English - father: FitzWilliam Sargent - sexual orientation: non-heterosexuality - artist files at: Philadelphia Museum of Art Library and Archives, Smithsonian American Art and Portrait Gallery Library, Frick Art Reference Library - depicted by: Self-portrait

### **Related passage (related entity: The Daughters of Edward Darley Boit):** 
The Daughters of Edward Darley Boit is a painting created by American artist John Singer Sargent in 1882. The work is located at the Museum of Fine Arts in Boston, Massachusetts, where it has been on display since 1970. The painting depicts two young girls, Mary and Dorothy Boit, daughters of a wealthy Boston family, sitting on a bench in a beautiful garden. John Singer Sargent was born in Florence, Italy, in 1856 and studied art in Europe before moving to the United States in the late 1870s. He became one of the most prominent portrait painters of his time, known for his innovative techniques and skillful use of color. The Daughters of Edward Darley Boit is one of Sargent's most famous works and is considered a masterpiece of late 19th-century Impressionism. In the painting, the two girls are dressed in their Sunday best, with Mary wearing a blue dress and Dorothy in a yellow one. They sit side by side on a wooden bench, surrounded by lush greenery and vibrant flowers. The girls look directly at the viewer with bright, curious expressions, as if they are eager to engage with the observer. The painting is characterized by its loose brushwork and bold use of color, which creates a sense of light and atmosphere that seems almost palpable. Sargent had a close relationship with the Boit family, who were his patrons and friends. The painter often visited the family's home in Boston and painted portraits of several members of the household, including the two daughters depicted in this work. The Daughters of Edward Darley Boit is not only a beautiful representation of two young girls, but also a testament to the deep affection and respect that Sargent had for his subjects and his artistic process. Overall, The Daughters of Edward Darley Boit is a stunning example of John Singer Sargent's talent and genius as a portrait painter. Its beautiful colors, loose brushwork, and captivating subject matter make it a beloved piece of art that continues to inspire viewers to this day.

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
Windows XP Media Center Edition is a version of the Windows XP operating system that was specifically designed for home entertainment and media usage. Developed by Microsoft, it was released in 2004 as a part of the Windows XP family of operating systems. As the name suggests, Media Center Edition is focused on providing users with an easy-to-use interface for accessing and enjoying various forms of digital media, including music, videos, photos, and television programs. To achieve this, it includes a number of features such as: 1. Media Player: A comprehensive media player that can play various audio and video formats, including DVDs and CDs. 2. TV Tuner: An integrated TV tuner that allows users to watch live television programming directly from within the Media Center interface. 3. Picture and Video Viewing: A built-in photo and video viewer that makes it easy to browse and view digital images and videos. 4. Music Playback: A fully-functional music player that supports popular audio file formats and can be controlled using the remote control. 5. DVD Playback: The ability to play DVDs directly from within the Media Center interface. 6. Customizable Menu: Users can customize their Media Center menu to include only the applications they use most frequently, making it easier to access their favorite media content. In addition to these media-specific features, Media Center Edition also includes many of the standard features found in other versions of Windows XP, such as the Windows Taskbar, Windows Explorer, and Windows Security Center. The relationship between Windows XP Media Center Edition and Microsoft Windows is that it is a variant of the Windows XP operating system that has been optimized for home entertainment and media usage. While it shares many similarities with other versions of Windows XP, such as the user interface and underlying architecture, it includes a number of unique features and functionality that make it particularly well-suited for media consumption. Overall, Windows XP Media Center Edition provides users with a powerful and easy-to-use platform for enjoying digital media within their home environment. Its focus on media functionality and ease of use make it an attractive option for anyone looking to enhance their home entertainment experience.

### **Old facts about the subject**
- developer: Microsoft

### **Related passage (related entity: Microsoft Windows):** 
Microsoft Windows is a family of operating systems developed by Microsoft Corporation, a multinational technology company based in Washington. The first version of Windows was released in 1985 and since then, Microsoft has continued to develop and improve the platform with each new release. The most recent version of Windows is Windows 10, which was launched in 2015. Windows 10 offers a range of features and improvements over previous versions, including improved security, faster performance, and enhanced gaming capabilities. One of the key features of Windows 10 is its ability to integrate with other Microsoft products and services, such as Office and Azure. Windows has had a significant impact on the computer industry, as it has become the dominant operating system used in personal computers around the world. According to market research, Windows accounted for over 80% of the global desktop operating system market share in 2020. This dominance has allowed Microsoft to maintain a strong position in the software industry and expand into other areas, such as cloud computing and artificial intelligence. Windows has also had a significant impact on popular culture, particularly through its use in media and entertainment. For example, Windows Media Center Edition, which was introduced in 2004, provided a central location for users to access and manage their digital media, such as music, videos, and photos. This feature helped to popularize the concept of multimedia centers and paved the way for later innovations in home entertainment. In terms of the relationship between Windows and Windows XP Media Center Edition, Windows XP Media Center Edition was a variant of Windows XP that was specifically designed for home entertainment purposes. It included additional features such as a program guide, recording capabilities, and support for DVD playback. While Windows XP Media Center Edition was popular among consumers, it did not replace the traditional desktop interface of Windows XP, but rather provided an alternative user experience for those who wanted to use their PCs for media consumption. Overall, Microsoft Windows has played a crucial role in shaping the computer industry and popular culture. Its continuous evolution and innovation have allowed it to maintain a strong position in the market, and its influence can be seen in many areas of technology and society today. As Microsoft continues to develop new versions of Windows, it will be interesting to see how the platform evolves and adapts to changing user needs and technological advancements.

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
Tanvir Mokammel is a talented Bangladeshi filmmaker, producer, and screenwriter who has made a significant impact in the Bangladeshi cinema industry. Born on May 15, 1973, in Dhaka, Bangladesh, Tanvir is known for his unique storytelling style and his ability to tackle complex social issues through his films. Tanvir holds Bangladeshi citizenship and is currently residing in Dhaka. He works as a freelance filmmaker and producer, and his primary occupation is making films that address social and political issues affecting Bangladesh and other parts of South Asia. Tanvir identifies as male and is educated at the University of Dhaka, where he earned a degree in Film Studies. After completing his education, he began his career in the film industry by working as a scriptwriter and assistant director for various production houses in Bangladesh. In 2017, Tanvir received the Best Director Award at the International Film Festival of India for his film "Chitra Nodir Parjanya," which he produced and directed himself. This was a significant achievement for Tanvir, as it recognized his talent and dedication to his craft. Tanvir's mother tongue is Bengali, and he is fluent in English, which he uses to communicate with international audiences and collaborators. His employer is typically a production house or a film studio, although he has also worked independently on some projects. Tanvir's relationship to Chitra Nodir Pare, a renowned actress in Bangladesh, is that he directed her in several films, including "Chitra Nodir Parjanya." Chitra has been a prominent figure in Bangladeshi cinema for decades, and her collaboration with Tanvir has resulted in some of their most critically acclaimed films. Overall, Tanvir Mokammel is a talented and dedicated filmmaker who has made a significant contribution to the Bangladeshi cinema industry. Through his films, he addresses important social and political issues, and his work continues to inspire and influence new generations of filmmakers and artists in Bangladesh and beyond.

### **Old facts about the subject**
- occupation: film director, screenwriter, writer, film producer - place of birth: Khulna - country of citizenship: Bangladesh, Pakistan - award received: Ekushey Padak, Bangladesh National Film Award for Best Story, Bangladesh National Film Award for Best Dialogue, Bangladesh National Film Award for Best Director - educated at: University of Dhaka - native language: Bengali - sex or gender: male - employer: Bangladesh Short Film Forum, Bangladesh Short Film Forum, Kino-Eye Films

### **Related passage (related entity: Chitra Nodir Pare):** 
Chitra Nodir Pare is a renowned filmmaker from Bangladesh who has made significant contributions to the country's cinematic industry. Born in 1980 in Dhaka, Bangladesh, Pare is a multi-talented individual who has worked as a screenwriter, director, and producer in various films. In this essay, we will explore Pare's background, career, and notable works, including their relationship with acclaimed filmmaker Tanvir Mokammel. Country of Citizenship and Career Chitra Nodir Pare was born and raised in Bangladesh, where he developed a passion for storytelling at a young age. He pursued his studies in filmmaking at the University of Dhaka and later went on to work as a screenwriter and director in several Bangladeshi films. Pare's career spans over two decades, during which he has written and directed numerous feature films, documentaries, and television serials. Notable Works Pare's most notable work includes the screenplay and direction of the 2016 film "Bishorjon" (The Traitor). Set against the backdrop of the Liberation War of Bangladesh in 1971, the film tells the story of a young man who betrays his fellow freedom fighters and joins the Pakistani military. The film received critical acclaim and won several awards, including the National Film Award for Best Screenplay. Another notable work by Pare is the 2013 film "Ghore Bairey Gorosthan" (In the Darkness), based on the novel of the same name by noted Bengali writer Syed Wahid Hossain. The film follows the story of a blind musician who becomes embroiled in a murder mystery while searching for his missing daughter. "Ghore Bairey Gorosthan" was well-received by audiences and critics alike, and it won several awards, including the Best Film award at the 2014 International Film Festival of India. Relationship to Tanvir Mokammel Tanvir Mokammel is another prominent Bangladeshi filmmaker known for his critically acclaimed works such as "Jagoroni" (The Strong Ones, 2015) and "Kaler Kaler Pore" (The Wall, 2013). While Pare and Mokammel have not collaborated directly on any projects, they share a strong bond as colleagues and peers in the Bangladeshi film industry. Both Pare and Mokammel are known for their unique storytelling styles and their ability to tackle complex social issues through their films. Conclusion In conclusion, Chitra Nodir Pare is a highly skilled filmmaker from Bangladesh who has made a significant impact on the country's cinematic industry. Through his work as a screenwriter, director, and producer, Pare has proven himself to be a versatile talent with a keen eye for detail and a deep understanding of human emotions. His notable works, including "Bishorjon" and "Ghore Bairey Gorosthan," demonstrate his ability to craft compelling stories that resonate with audiences. As a colleague and peer of acclaimed filmmaker Tanvir Mokammel, Pare shares a common bond with him in terms of their commitment to creating meaningful cinema that reflects the social and cultural realities of Bangladesh.

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
Archie Gemmill is a Scottish former professional footballer who was born on February 27, 1954, in Bellshill, Scotland. He played as an attacking midfielder for several clubs during his playing career, including Dundee United, Derby County, and Glasgow Rangers. Gemmill was known for his exceptional technique, speed, and goal-scoring ability, which earned him the nickname "The Flying Gemmill." He was also a skilled free-kick taker and was known for his ability to score important goals from set pieces. In addition to his club career, Gemmill represented Scotland at the international level, scoring three goals in 23 appearances between 1976 and 1980. He was a key player in the Scottish national team that reached the quarterfinals of the 1978 World Cup. After retiring from football, Gemmill went on to become a successful coach and manager. He managed several clubs in Scotland, including Livingston and St. Mirren, before joining the Scottish Football Association as a youth coach. Gemmill's son, Scot Gemmill, is also a former professional footballer and currently serves as the manager of the Scotland national team. Personal Information: * Given name: Archibald Gemmell * Sex or Gender: Male * Occupation: Former professional footballer, coach, and manager * Family Name: Gemmell * Date of Birth: February 27, 1954 * Place of Birth: Bellshill, Scotland * Languages Spoken, Written, or Signed: English (written and spoken), Scottish Gaelic (written) * Country of Citizenship: Scotland * Coach of Sports Team: Yes, managed several clubs in Scotland as a coach and manager * Child: Yes, has a son named Scot Gemmill who is also a former professional footballer and current manager of the Scotland national team * Position Played on Team / Speciality: Attacking midfielder, skilled free-kick taker, and goal-scorer * Relationship to Scot Gemmill: Father

### **Old facts about the subject**
- sex or gender: male - member of sports team: Birmingham City F.C., Jacksonville Tea Men, Preston North End F.C., St. Mirren F.C., Derby County F.C., Nottingham Forest F.C., Wigan Athletic F.C., Derby County F.C., Scotland national football team - occupation: association football player - place of birth: Paisley - country of citizenship: United Kingdom - sport: association football - participant in: 1978 FIFA World Cup - given name: Archie - position played on team / speciality: midfielder - country for sport: Scotland - family name: Gemmill - coach of sports team: Nottingham Forest F.C. - languages spoken, written or signed: English - child: Scot Gemmill

### **Related passage (related entity: Scot Gemmill):** 
Scot Gemmill is a Scottish former professional footballer and current manager. He was born on September 30, 1956, in Bellshill, Scotland, and grew up in a footballing family. His father, Archie Gemmill, was also a professional footballer who played as a winger for clubs such as Celtic and Leeds United. Gemmill himself began his career as a midfielder for Livingston, Dundee United, and Celtic before moving into management. He managed various clubs in Scotland and England, including Dundee United, Kilmarnock, and Preston North End. In 2017, he was appointed as the assistant manager of the Scotland national team, working under manager Alex McLeish. In addition to his footballing accomplishments, Gemmill is known for his skills on the pitch and his dedication to the sport. He has been recognized for his contributions to Scottish football with numerous awards and accolades. Gemmill's occupation is football manager, and he is male. His country of citizenship is Scotland, and he speaks English. He was born in Bellshill, Scotland, and his family name is Gemmill. He is a member of the Scotland national football team and has a close relationship with his fellow player, Archie Gemmill, who is his father. Here are some key points about Scot Gemmill: * Position played on team: Midfielder / Speciality: Versatility, work rate * Father: Archie Gemmill / Occupation: Professional footballer / Sex or Gender: Male * Country of citizenship: Scotland / Languages spoken, written, or signed: English / Place of birth: Bellshill, Scotland / Family name: Gemmill / Country for sport: Scotland / Member of sports team: Scotland national football team / Relationship to Archie Gemmill: Son and fellow player By including these details in your essay, you will have a comprehensive understanding of Scot Gemmill's background, skills, and achievements in the world of football.

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
1992 Summer Paralympics, also known as the Games of the X Paralympic Winter Olympics, was held in Barcelona, Spain from September 4th to September 11th, 1992. The event was organized by the International Paralympic Committee (IPC) and featured athletes from over 60 countries competing in various sports. The official mascot for the 1992 Summer Paralympics was a cartoon character named "Blancafort," who represented the spirit of Barcelona and the Paralympic movement. One of the key highlights of the 1992 Summer Paralympics was the introduction of new sports, such as quad rugby and sitting volleyball, which were specifically designed for athletes with spinal cord injuries or other mobility impairments. These sports helped to expand the scope of the Paralympic movement and increase participation from athletes with a wider range of disabilities. In terms of wheelchair fencing, the 1992 Summer Paralympics marked a significant milestone for the sport. For the first time, athletes with different types of disabilities were allowed to compete together in the same events, creating a more inclusive and diverse environment. This move helped to promote greater understanding and respect between athletes with different abilities and challenges, and it paved the way for further growth and development of the sport in future Paralympic Games. Overall, the 1992 Summer Paralympics was a groundbreaking event that helped to promote greater awareness and inclusion of people with disabilities in society. Through the introduction of new sports, the expansion of existing ones, and the promotion of diversity and inclusivity, the event helped to create a more inclusive and accessible environment for athletes and spectators alike. As such, it remains an important moment in the history of the Paralympic movement and a testament to the power of sports to bring people together and break down barriers.

### **Old facts about the subject**
- location: Barcelona - country: Spain - sport: disabled sport - mascot: Petra

### **Related passage (related entity: wheelchair fencing at the 1992 Summer Paralympics):** 
wheelchair fencing at the 1992 Summer Paralympics was held in Barcelona, Spain. Specifically, the fencing competition took place at the Palau Sant Jordi, which is located within the Barcelona Olympic Stadium Complex. This venue provided a world-class facility for athletes with disabilities to compete in the sport of fencing. Fencing has been a part of the Paralympic Games since the inaugural event in Rome in 1960. At the 1992 Summer Paralympics, there were three categories of competition in wheelchair fencing: men's epee, women's foil, and men's sabre. A total of 87 athletes from 24 countries participated in these events. The United States was one of the countries that fielded a team in wheelchair fencing at the 1992 Summer Paralympics. The US team consisted of four athletes: David Cogen, Michael Kates, Jeff Strickland, and Deborah Scott. Cogen and Strickland competing in the men's epee category, while Kates and Scott competed in the women's foil category. Unfortunately, none of the US athletes medaled in these events. Overall, the inclusion of wheelchair fencing at the 1992 Summer Paralympics marked another important milestone in the development of adaptive sports for individuals with disabilities. As more countries begin to recognize the benefits of participating in sports for people with disabilities, it is likely that wheelchair fencing will continue to grow and become an even bigger part of future Paralympic Games.

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


