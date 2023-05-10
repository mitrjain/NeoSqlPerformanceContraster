//Recursion 3
MATCH (q:Questions)<-[:IS_REPLY_TO*1..3]-
(a:Answers)
RETURN q,a