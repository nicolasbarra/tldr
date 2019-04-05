# TL;DR 
TL;DR: Repository for NETS 213 Final Project

## Collect news articles.  (Amount of Work: 2)
The first step of our project will be to collect articles from a variety of news sources. This section will require the use of a parser to convert the articles into sentences and paragraphs that can then be segmented off for the purpose of creating a HIT. 

## Create HITs on Mechanical Turk. (Amount of work: 3)
The second step of our project will be to post HITs on mechanical turk.  Each HIT will ask a Turker to select the three most important sentences out of a section of text.  The section of text will contain 3-6 paragraphs, depending on paragraph length.  If there are any pronouns in the selected sentences, the Turker will replace them with proper nouns to help make the finally summary more clear.  Each HIT will be completed by 10 Turkers.  We will only post our HITs to Turkers who are in the United States, have completed at least 500 HITs, and have an acceptance rate of at least 90% to help ensure we are obtaining high quality results. 

## Process HIT data. (Amount of work: 4)
Each segment of text data will be read by 10 workers and then be assigned a binary label as to whether that sentence is essential to the understanding of the text. We will process this data using the Python libraries we’ve been learning about throughout the semester in order to aggregate the votes for every sentence in a particular piece of text. Additionally for every sentence that has pronouns but not proper pronouns we will use majority vote to replace the pronouns with the proper pronouns. Once that is done we will output lists of the edited sentences belonging to a specific article in the order they were originally read as well as their corresponding relevancy score that was created by aggregating the votes from all of the turkers. 

## Create User Interface. (Amount of work: 3)
Java will be used to implement the user interface. There will be a drop down menu that gives options of articles to summarize. Once an article is selected, the slider bar will be enables such that when adjusted, the length of the outputed summary changes. That is when the slider bar is moved higher the threshold for how many turkers agreed that was a relevant sentence increases and when it is moved lower this requirement is lowered. 

## Integrate HIT data with UI. (Amount of work: 4)
When an article option is clicked in the drop down menu, we extract the corresponding summary from the list of summaries we generated from out hits. When the slider bar is increased, we increase the number of sentences included in the summary in order of importance (ranked by Turkers) and when the slider bar is decreased, we decrease the number of sentences included in the summary.

