//Recursion 1
MATCH (q:Questions)<-[:IS_REPLY_TO*1..]-(a:Answers)
RETURN q,a