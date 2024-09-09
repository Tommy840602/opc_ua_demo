#先導入opcua套件
from opcua import ua,Client 
import socket 

#找出OPC UA Server的連接字串並初始化客戶端對象，將{}替換為OPC UA Server主機名稱
url ="opc.tcp://huangyaweideAir.lan:53530/OPCUA/SimulationServer"
client = Client(url) 

#連線到OPC UA伺服器 
client.connect()
print("OPC UA Server已連接")

# 呼叫 get_root_node 方法定位層次結構頂部的節點
root_node = client.get_root_node() 
print(root_node)

# 使用 get_children 向下鑽取層次結構
print([x.get_browse_name() for x in root_node.get_children()])

# 定位我們的變數儲存的物件節點
objects = root_node.get_children()[0] 
print(objects)
# 或你可以使用get_objects_node直接定位物件節點
objects = client.get_objects_node() 
print(objects)

#瀏覽該物件的子節點物件節點
print([ x. get_browse_name() for x in objects.get_children ()])

# 使用 get_children 方法探索物件節點的子節點
# 使用索引選擇所需的子節點
sim_data_node =objects.get_children()[2] 
print(sim_data_node)

#套用 get_browse_name取得節點名稱而不是節點 id
print([{ "NodeID" :x , "Node Name" : x.get_browse_name()} for x in sim_data_node.get_children()])

# 您可以使用 NodeId 物件或字串指定 NodeId: 
# 以下兩個方法到達同一個節點
# 透過指定節點索引來取得特定節點 using get_node 方法
from opcua.ua import NodeId 
print(client.get_node(NodeId( 1004 , 3 )).get_browse_name())
print(client.get_node('ns=3;i=1004').get_browse_name())

# 索引所需變數並套用 get_value 方法讀取值
sim_data_node_sin = client.get_node('ns=3;i=1004') 
print(sim_data_node_sin.get_value())

# 索引所需變數並套用 set_value 方法寫入值數
sim_data_node_test =  client.get_node('ns=3;i=1001')
print("The original value of {} is {}".format(sim_data_node_test.get_browse_name(), sim_data_node_test.get_value()))
sim_data_node_test.set_value(4.0)
print("The modified value of {} becomes {}".format(sim_data_node_test.get_browse_name(), sim_data_node_test.get_value()))

