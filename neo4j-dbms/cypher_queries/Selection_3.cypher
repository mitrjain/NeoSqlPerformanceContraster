//Selection 3
MATCH (p:Professionals{professionals_id:
'0079e89bf1544926b98310e81315b9f1'})-
[:GOT_EMAIL]->(e:Emails)
RETURN e