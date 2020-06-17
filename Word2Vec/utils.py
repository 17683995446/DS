from pprint import pprint

with open('small_corpus.txt', encoding='utf8') as f:
    small_corpus = [line.strip() for line in f.readlines()]

with open('stop_words.txt', encoding='utf8') as f:
    stop_words = [line.strip('\n') for line in f.readlines()]  # 保留空格

if __name__ == '__main__':
    pprint(small_corpus)
    pprint(stop_words[:10])
