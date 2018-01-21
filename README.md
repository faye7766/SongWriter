# SongWriter
We all love songs. Not only music, good lyrics are also an essential part that build up good songs. However, writing lyrics is not very easy and may take a long time for songwriters to come up with new ideas for songs.

In this project, I investigated the song datasets to get ideas of how typical song lyrics are like and also built up a lyrics generator which generates new original lyrics from different music genre or artist.

The lyrics generator can provide inspirations for songwriters and also get a new song lyrics done with a simple phrase.

### Methods:
- Multi-layer Recurrent Neural Networks (LSTM, RNN) for character-level language models
- Extract data in genres: pop, rap, country, rock, folk and chinese rap

### Tools:
- Python (pandas, nltk)
- R (tidytext, tidyr, ggplot, wordcloud, wordcloud2)
- NVIDIA GPU/ Cuda/ Ubuntu/ Torch/ g2.x2large instance 
- Max_epoch: 50/ batch_size:50/ num_layers:2/ learning_rate: 0.002/ Rnn_size: 200-512


