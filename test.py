import py2neo
from py2neo import Node, Relationship,Graph

graph=Graph("localhost")
user=graph.find_one("User","username","yenyen")

category="其他小吃"
division="Jiaoxi Township"

query="""
match(reco:Restaurant)-[:IN_DIVISION]-(d:Division),
(reco)-[:IN_CATEGORY]->(c:Category)
where c.SDCategory="其他小吃" and
	d.e_name="Luodong Township"
with  reco order by reco.SDRate limit 5
return reco.shopId
"""
res=graph.find_one("Restaurant","shopId",37965)
a=graph.match_one(start_node=user,rel_type='INTEREST',end_node=res,bidirectional=False)
a["level"]=a["level"]+1
graph.push(a)
print(a.properties["level"])
#graph.push(a)
#a=graph.match_one(start_node=user,rel_type='INTEREST',end_node=res,bidirectional=False)
print(a)

query='''
match(reco:Restaurant)-[:IN_DIVISION]-(d:Division),
(reco)-[:IN_CATEGORY]->(c:Category)
where c.SDCategory={category} and
	d.e_name={division}
return reco order by reco.SDRate desc limit 20
'''
print graph.run(query,category=category,division=location)

# if(a==None):
	# print (a) #create the interest relationship
# else:
	# #update the relationship


