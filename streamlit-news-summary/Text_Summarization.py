import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest
import pandas as pd

def summarizer(rawdocs):
    stopwords = list(STOP_WORDS)
    nlp = spacy.load('en_core_web_sm')
    doc = nlp(rawdocs)
    tokens = [token.text for token in doc]
    word_freq = {}
    for word in doc:
        if word.text.lower() not in  stopwords and word.text.lower() not in punctuation:
            if word.text not in word_freq.keys():
                word_freq[word.text] = 1
            else:
                word_freq[word.text] += 1
    max_freq = max(word_freq.values())
    for word in word_freq.keys():
        word_freq[word] = word_freq[word] / max_freq  # Normalizing the word frequency
        sent_scores = {}
    sent_tokens = [sent for sent in doc.sents]
    for sent in sent_tokens:
        for word in sent:
            if word.text in word_freq.keys():
                if sent not in sent_scores.keys():
                    sent_scores[sent] = word_freq[word.text]
                else:
                    sent_scores[sent] += word_freq[word.text]

    scores_df = dictToDf(sent_scores) # create a dataframe for scores

    select_len = int(len(sent_tokens) * 0.3)
    summary = nlargest(select_len, sent_scores, key = sent_scores.get)
    final_summary = [word.text for word in summary]
    summary = ' '.join(final_summary)
    return summary, doc, scores_df, len(rawdocs.split(' ')), len(summary.split(' '))

def dictToDf(dictionary):
    my_series = pd.Series(dictionary, name='Scores')

    # Reset the index to get a DataFrame
    df_from_series = my_series.reset_index()
    df_from_series.columns = ['Sentence', 'Scores']

    # Return Dataframe
    return df_from_series
            

text = "Delhi News Live Updates: The Supreme Court Tuesday deferred its order in Delhi Chief Minister Arvind Kejriwal’s interim bail plea. The court is likely to hear the matter day after tomorrow. Earlier in the day, it said that if it grants interim bail to Arvind Kejriwal, he cannot function as the chief minister as it will have “cascading effect” on other issues. “We are on the issue of propriety today, not on legality. We do not want anything to affect the functioning of the government,” the court noted.Kejriwal’s counsel submitted, “I cannot be fettered that I will not perform my constitutional role as Chief Minister,” adding that he “will not sign on anything related to excise policy.” The Enforcement Directorate (ED), meanwhile, has opposed Kejriwal’s interim bail plea, saying that it will “demoralise common man” and that “campaigning was a luxury”. The ED also flagged that Kejriwal had evaded the its summons in the excise policy case on nine occasions. It added that allegations show his “involvement”, and that the bail application must be before a trial court and not the Supreme Court.The top court, on its part, noted that it has given “interim bail even in heinous crimes”. It expressed concerns over the delay in the probe into the case, and has demanded that the agency present the case files that led to the arrest of the AAP leader. Kejriwal was arrested on March 21 and is currently lodged in Tihar Jail under judicial custody."
    
#print(summarizer(text))