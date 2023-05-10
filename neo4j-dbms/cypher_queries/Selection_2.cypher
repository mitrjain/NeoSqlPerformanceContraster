//Selection 2
MATCH (t:Tags)<-[:HAS_TAG]-(s:Students)-
[:MEMBER_IN]->(b)
WHERE t.tags_tag_name='college'
AND b.groups_group_type='youth program'
RETURN s,t,b