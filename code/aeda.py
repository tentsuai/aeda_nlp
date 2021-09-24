# AEDA: An Easier Data Augmentation Technique for Text classification
# Akbar Karimi, Leonardo Rossi, Andrea Prati

import random
import json
import jieba

random.seed(0)

PUNCTUATIONS = ['。', '，', '！', '？', '；', '：']
PUNC_RATIO = 0.3

# Insert punction words into a given sentence with the given ratio "punc_ratio"
def insert_punctuation_marks(sentence, punc_ratio=PUNC_RATIO):
	words= list(jieba.cut(sentence,cut_all=False))
	new_line = []
	q = random.randint(1, int(punc_ratio * len(words) + 1))
	qs = random.sample(range(0, len(words)), q)

	for j, word in enumerate(words):
		if j in qs:
			new_line.append(PUNCTUATIONS[random.randint(0, len(PUNCTUATIONS)-1)])
			new_line.append(word)
		else:
			new_line.append(word)
	new_line = ''.join(new_line)
	return new_line


def main():
    
    json_data = []
    new_data = []
    with open('../data/train.json', 'r') as train_orig:
        for line in train_orig:
            json_data.append(json.loads(line))
        dic = {}
        for now_dic in json_data:
            dic = now_dic
            sentence = now_dic['sentence']
            for i in range(4):
                sentence_aug = insert_punctuation_marks(sentence)
                dic['sentence'] = sentence_aug
                new_data.append(str(dic))

 
        
    with open('../data/train_new.json', 'w') as f:
        for i in new_data:
            dic = eval(i)
            str_sen = json.dumps(dic, ensure_ascii=False)
            f.write(str_sen+'\n')

if __name__ == "__main__":	
		main()
