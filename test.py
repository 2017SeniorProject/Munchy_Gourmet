import py2neo
from py2neo import Node, Relationship,Graph
import random

graph=Graph("localhost")
#find user
user=graph.find_one("User","username","yenyen")
#input user, division
category="其他小吃"
#division="Jiaoxi Township"
division="Luodong Township"

query="""
match(reco:Restaurant)-[:IN_DIVISION]-(d:Division),
	(reco)-[:IN_CATEGORY]->(c:Category)
	where c.SDCategory={category} and
		d.e_name={division}
return reco order by reco.SDRate desc limit 20
"""
reco=graph.run(query,category=category,division=division)
result=list(reco)
#list_res1=reco.data()
#print(list_res1)
print (result)

# length=len(list_res1)

# if length>=1 and length<=3:
	# list_res=list_res1.copy()
# if length>3:
	# list_res=[0]*3
	# for i in range(3):
		# no=random.randint(0,length-1)
		# list_res[i]=list_res1[no]

# for i in range(len(list_res)):
	# res=graph.find_one("Restaurant","shopId",list_res[i]['reco']['shopId'])
	# relation=graph.match_one(start_node=user,rel_type='INTEREST',end_node=res,bidirectional=False)
	# if(relation==None):
		# rel = Relationship(user, 'INTEREST',res,level=1)
		# graph.create(rel)
	# else:
		# relation["level"]=relation["level"]+1
		# graph.push(relation)

# print ("ok")
# res=graph.find_one("Restaurant","shopId",37965)
# a=graph.match_one(start_node=user,rel_type='INTEREST',end_node=res,bidirectional=False)
# print(a)

Recommendation General:

query="""
Match (reco:Restaurant)-[:IN_DIVISION]->(d:Division),
	(reco)-[rel:GOOD_IN]->(m:Month),
    (reco)-[:IN_CATEGORY]->(c:Category)
    where 
    d.e_name="Jiaoxi Township"
    and rel.month_tendency=1 and
    m.month=6 
   and  c.SDCategory="其他小吃"
return (reco) order by reco.SDRate limit 40
"""


