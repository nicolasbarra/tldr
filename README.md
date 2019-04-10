# TL;DR 
TL;DR: Repository for NETS 213 Final Project

## docs

### Collect news articles.  (Amount of Work: 2)
The first step of our project will be to collect articles from a variety of news sources. This section will require the use of a parser to convert the articles into sentences and paragraphs that can then be segmented off for the purpose of creating a HIT. 

### Create HITs on Mechanical Turk. (Amount of work: 3)
The second step of our project will be to post HITs on mechanical turk.  Each HIT will ask a Turker to select the three most important sentences out of a section of text.  The section of text will contain 3-6 paragraphs, depending on paragraph length.  If there are any pronouns in the selected sentences, the Turker will replace them with proper nouns to help make the finally summary more clear.  Each HIT will be completed by 10 Turkers.  We will only post our HITs to Turkers who are in the United States, have completed at least 500 HITs, and have an acceptance rate of at least 90% to help ensure we are obtaining high quality results. 

### Process HIT data. (Amount of work: 4)
Each segment of text data will be read by 10 workers and then be assigned a binary label as to whether that sentence is essential to the understanding of the text. We will process this data using the Python libraries we’ve been learning about throughout the semester in order to aggregate the votes for every sentence in a particular piece of text. Additionally for every sentence that has pronouns but not proper pronouns we will use majority vote to replace the pronouns with the proper pronouns. Once that is done we will output lists of the edited sentences belonging to a specific article in the order they were originally read as well as their corresponding relevancy score that was created by aggregating the votes from all of the turkers. 

### Create User Interface. (Amount of work: 3)
Java will be used to implement the user interface. There will be a drop down menu that gives options of articles to summarize. Once an article is selected, the slider bar will be enables such that when adjusted, the length of the outputed summary changes. That is when the slider bar is moved higher the threshold for how many turkers agreed that was a relevant sentence increases and when it is moved lower this requirement is lowered. 

### Integrate HIT data with UI. (Amount of work: 4)
When an article option is clicked in the drop down menu, we extract the corresponding summary from the list of summaries we generated from out hits. When the slider bar is increased, we increase the number of sentences included in the summary in order of importance (ranked by Turkers) and when the slider bar is decreased, we decrease the number of sentences included in the summary.

## data

### Data Format
We are starting with 5 New Yorker articles.  We are then pasting the text of each article into a .txt file and using the Python Natural Language Toolkit (NLTK) library to split the article into individual sentences.  We will manually go through each article and determine appropriate sections of sentences, comprised of some number of paragraphs.  This will ensure Turkers see sections of appropriate length, roughly 15 sentences, comprised of complete paragraphs, so they have appropriate context to select the most important sentences.  
We now have sections of text which contain about 15 sentences, but might have more or less.  For every unique section length, we will create a new CSV file where each row corresponds to 1 section, and column i  in that row will contain the ith sentence in that section.  (For example, if we end up with sections of length 12,13,14,15,16, and 17, we will make 6 different CSV files). We will also include in each row the name of the article which that section came from, and article ID which we assign to each article at the beginning.  Because we are making a unique CSV for every section length, within each CSV, every row will have the same number of columns. We will then upload these CSVs to Mechanical Turk where each CSV is a batch of HITs, and each row of a CSV will correspond to 1 HIT. 
For each batch of HITs we upload, we will receive an output CSV.  Each row in the CSV will correspond to 1 HIT, and each piece of information from the HIT will be in a different column.  Our column headers will be:

- Article_ID
- Article_Name
- HIT_ID
- Worker_ID
- For each sentence in the section: 
    - Sentence_i_input: Sentence text
    - Sentence_i_output: Yes or No (important or not important)

Note that we don’t need to keep track of the global position of the sentence in the article, because we had to create a dictionary of (sentence text → sentence position) when parsing the article into sentences, so we can just access this dictionary when sorting sentences for the final summary we are outputting.  

### Input/Output CSV Format For Quality Control
The input for quality control is each output CSV from Mechanical Turk.  The output CSV will have the following format, where each row corresponds to 1 sentence.
Header categories:
  - Article_ID: ID of article where sentence originated.
  - Article_Name: Name of article where sentence originated
  - Sentence_Order_Number: Initial position of sentence within article. 
  - Sentence: Sentence Text
  - Number_of_Votes: Number of Turkers who marked this sentence as important
  - Max_Article_Votes: The greatest number of votes received by any sentence in that article.
  - Agreement: Number_of_Votes / Max_Article_Votes

### Which Parts of Code Deal with Quality Control Module
The code for quality control is located in src/qualitycontrol.py and works as follows: convert the input CSV to a Pandas Dataframe.  For each sentence from each article, we will get the rows of the Dataframe which contain that sentence.  There will be 10 of these rows.  We will then sum the sentence_i_output cell for each row as the value will be 1 if the worker in that HIT marked the sentence as important, and 0 if the worker in that HIT did not mark the sentence as important and store this sum as a variable Votes.  We will then create a tuple of the sentence, Votes, Article_Name, Article_ID, and Sentence_Order_Number.  For each article ID, we store a max value which corresponds to the greatest number of votes received by any sentence in that article.  If votes is greater than the current max, we replace votes with max. After we create a tuple for each sentence, we iterate through each tuple and add Max_Article_Votes and Agreement.  

Note: We originally constructed a quality control algorithm based on what we thought the format of the Mechanical Turk output data would be.  We have since realized that the actual format will be slightly different since each HIT contains multiple sentences.  Thus, we also created a sample Mechanical Turk output/ input to the quality control module with the correct format, however we have not yet changed the algorithm to account for this different format.  Going forward, we will update the algorithm to interface with the data in this format, but we do not anticipate this to be at all challenging.  

### Input/Output CSV Format For Aggregation
The input for aggregation consists of the location of the output from quality control, an article ID, and a scale value. The scale value is indicative of how summarized the requester wants the output to be, with 0 being the least summarized (longest outputted summary) and 100 being the most summarized (shortest outputted summary). The output for aggregation will be a paragraph summary of the article. If n is the article ID and s is the scale value chosen by the requester for this summary, we select the sentences in article with ID n that have an agreement value greater than or equal to the scale value and include these in the summary paragraph outputted in the order they appear in the original article.

### Which Parts of Code Deal with Aggregation Module
The code for aggregation is located in src/aggregation.py and works as follows: data from the quality control as well as an article ID and a scale value are taken as input. The scale value is indicative of how summarized the requester wants the output to be, with 0 being the least summarized (including the most sentences) and 100 being the most summarized (including the least sentences). We use the article ID to find the sentences from the quality control that are from the desired article. For each sentence, if it has a greater agreement value than the scale value, it is included in the paragraph outputted in the order it appears in the original article.

### Where to find:
- Raw data (txt and pdf of articles)
    - Found in /data/raw_data_input
- Sample input/output for QC (old and new formats)
    - Found in src/qc/data
- Sample input/output for aggregation
    - Found in src/ag/data
- Code for QC
    - Found in src/qc
- Code for aggregation
    - Found in src/ag
