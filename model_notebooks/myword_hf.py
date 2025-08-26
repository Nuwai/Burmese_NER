import re
from huggingface_hub import hf_hub_download
import word_segment as wseg

# Download the required dict files from your HF repo
UNIGRAM_WORD_BIN = hf_hub_download(repo_id="nuwaithetsophia/myword_tokenizer", filename="unigram-word.bin")
BIGRAM_WORD_BIN = hf_hub_download(repo_id="nuwaithetsophia/myword_tokenizer", filename="bigram-word.bin")

# Load models once (global, to avoid reloading every call)
wseg.P_unigram = wseg.ProbDist(UNIGRAM_WORD_BIN, True)
wseg.P_bigram = wseg.ProbDist(BIGRAM_WORD_BIN, False)

def tokenize_burmese_text(text: str, delimiter: str = " "):
    """
    Tokenize Burmese text using Viterbi word segmentation.
    - Splits sentences by '။'
    - Segments each sentence
    - Returns list of tokenized sentences
    """
    # Split into sentences (keep "။")
    sentences = re.split(r"(။)", text)
    merged_sentences = []
    for i in range(0, len(sentences), 2):  # sentence + delimiter
        if i < len(sentences) - 1:
            merged_sentences.append(sentences[i] + sentences[i+1])
        else:
            if sentences[i].strip():
                merged_sentences.append(sentences[i])

    tokenized_sentences = []
    for sentence in merged_sentences:
        clean_sentence = sentence.replace(" ", "").strip()
        if not clean_sentence:
            continue
        listString = wseg.viterbi(clean_sentence)
        wordStr = delimiter.join(listString[1]).strip(delimiter)
        tokenized_sentences.append(wordStr)

    return tokenized_sentences


# Example usage
if __name__ == "__main__":
    sample = "ရန်ကုန်မှာနေထိုင်ပါတယ်။ ကျွန်တော် စာသင်ယူနေသည်။"
    tokens = tokenize_burmese_text(sample)
    print(tokens)
    # for t in tokens:
    #     print(t)