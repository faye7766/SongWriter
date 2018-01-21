library(ggplot2)
library(readr)
library(dplyr)
library(tidyr)
library(tidytext)
library(RColorBrewer)
library(reshape2)
library(wordcloud)
library(igraph)
library(widyr)
library(ggraph)
library(ngram)
library(wordcloud2)
library("ggthemes")

song_data<-read.csv("songdata.csv")
song_data$text<-as.character(song_data$text)
tidy_lyrics<-tidy_lyrics <- song_data%>% 
  unnest_tokens(word,text)
song_wrd_count<-tidy_lyrics %>%count(song)

top10 =  song_wrd_count[order(- song_wrd_count$n),][1:10,]
btm10 =  song_wrd_count[order(song_wrd_count$n),][1:10,]

p1 = ggplot(top10, aes(x=reorder(song, -n),y = n)) +geom_bar(stat = "identity" ,alpha = 0.8, fill = 'lightblue') + scale_color_gdocs() + ggtitle("Words per song-Top 10") +
  labs(x = "Song", y = "# Words") 
p1

p2 = ggplot(btm10, aes(x=reorder(song, n),y = n)) +geom_bar(stat = "identity" ,alpha = 0.8, fill = 'orange') + scale_color_gdocs() + ggtitle("Words per song-Lowest 10") +
  labs(x = "Song", y = "# Words") 
p2

lyric_counts <- tidy_lyrics %>%
  left_join(song_wrd_count, by = "song")%>%rename(total_words=n)
head(lyric_counts)

lyric_sentiment<-lyric_counts %>% inner_join(get_sentiments("nrc"),by="word")
lyric_sentiment %>%count(word,sentiment,sort=TRUE)%>%group_by(sentiment)%>%top_n(n=10)%>%ungroup() %>%
  mutate(word=reorder(word,n))%>%ggplot(aes(x=word,y=n,fill=sentiment))+geom_col(show.legend = FALSE)+
  scale_fill_hue(c=45, l=80) + facet_wrap(~sentiment,scales="free")+coord_flip()


pos_percent<-lyric_sentiment %>%
  count(song,sentiment,total_words)%>%
  ungroup() %>%
  mutate(percent=round(n/total_words,2)) %>%
  filter(sentiment %in% c('positive','negative')) %>%
  arrange(desc(percent))

pos_percent %>% arrange(desc(percent))%>%group_by(sentiment)%>% top_n(n=20)%>%ggplot(aes(x=substr(song,1,20),y=percent,group=sentiment,fill=sentiment))+geom_area(alpha=0.3)+theme(axis.text.x=element_text(angle=90),legend.position = "none")+geom_point()+labs(x="song",title="Proportion of words against Total words")+facet_wrap(~sentiment)


artist<-as.data.frame(table(lyric_sentiment$artist))%>%arrange(desc(Freq))
colnames(artist)<-c("artist","Songs")
nrow(artist) #643

artist_t20<-artist %>%top_n(20)
artist_t20 %>%ggplot(aes(x=factor(artist,levels=artist),y=Songs,fill=artist))+geom_bar(stat="identity")+theme(axis.text.x = element_text(angle=90),legend.position = "none")+labs(x="Artist",title="Which artist has more songs - top")
artist_percent<-lyric_sentiment%>%filter(sentiment=='positive')%>%count(artist,song,total_words)%>%ungroup()%>%mutate(percent=n/total_words)%>%right_join(artist_t20)

# top 20 artist
artist_percent %>% ggplot(aes(x=artist,y=percent,fill=artist))+geom_boxplot()+
  theme(axis.text.x = element_text(angle=60),legend.position = "none")+scale_fill_hue(c=45, l=80)+labs(x="Artist",title="Percentage of positive words - Top20 Artists")

# top positive artist
artist_pos = lyric_sentiment%>%filter(sentiment=='positive')%>%count(artist,song,total_words)%>%ungroup()%>%mutate(percent=n/total_words)%>%right_join(artist)
# average the percent and find the top 10 artist
pos10 = aggregate(artist_pos$percent, list(artist_pos$artist), mean)
colnames(pos10)[2] <- "Percent"
colnames(pos10)[1] <- "Artist"

pos10 <- pos10[order(- pos10$Percent),][1:10,]
p5 = ggplot(pos10, aes(x=reorder(Artist, -Percent),y = Percent)) +geom_bar(stat = "identity", fill = 'purple', alpha = 0.5) + scale_fill_hue(c=45, l=80) + ggtitle("Top 10 Positive Artist") +
  labs(x = "Artist", y = "Percent") + theme(axis.text.x = element_text(angle=60),legend.position = "none")
p5

png("comparison_cloud_top_500_words.png", width = 480, height = 480)
tidy_lyrics %>%
  inner_join(get_sentiments("nrc")) %>%
  count(word, sentiment, sort = TRUE) %>%
  acast(word ~ sentiment, value.var = "n", fill = 0) %>%
  comparison.cloud(colors = c("#F8766D", "#00BFC4", "#00B2FF", "red", "#FF0099", "#6600CC", "brown", "pink", "green"),
                   max.words = 400, title.size=1.5)
dev.off()

png("comparison_cloud_top_500_words.png", width = 480, height = 480)
tidy_lyrics %>%
  inner_join(get_sentiments("bing")) %>%
  count(word, sentiment, sort = TRUE) %>%
  acast(word ~ sentiment, value.var = "n", fill = 0) %>%
  comparison.cloud(colors = c( "#00B2FF", "red"),
                   max.words = 300, title.size=1.5)
dev.off()