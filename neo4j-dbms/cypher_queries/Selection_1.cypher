//Selection 1
MATCH (p:Professionals)-[]->(t:Tags)
WHERE t.tags_tag_name='college'
RETURN p,t