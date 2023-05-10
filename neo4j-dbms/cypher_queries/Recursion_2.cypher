//Recursion 2
MATCH (q:Questions)<-[:IS_REPLY_TO*1..2]-
(a:Answers)
RETURN q, a