verwendete SQL Befehle:

Aufgabe 2.2:

SELECT 
  hashtags.name, 
  pairs.h_id2, 
  pairs.h_id1, 
  hashtags.id2
FROM 
  public.hashtags, 
  public.pairs, 
  public.tweets
WHERE 
  hashtags.id2 = pairs.h_id1 AND
  hashtags.id2 = pairs.h_id2;

Aufgabe 2.4, 2.5:

SELECT 
  tweets."time", 
  hashtags.name, 
  hashtags.anzahl
FROM 
  public.contains, 
  public.hashtags, 
  public.tweets
WHERE 
  contains.t_id = tweets.id1 AND
  hashtags.id2 = contains.h_id;
GROUP BY 
  tweets."time",
  hashtags.name
ORDER BY
  tweets."time" ASC;




