import os
# from gensim.models import Word2Vec
from androguard.misc import AnalyzeAPK
import networkx as nx
def apk_to_fcg(apk_path):
    a, d, dx = AnalyzeAPK(apk_path)

    # Tạo đồ thị rỗng
    fcg = nx.DiGraph()

    # Duyệt qua tất cả các phương thức
    for method in dx.get_methods():
        # Thêm nút cho mỗi phương thức
        method_name = method.get_method().get_name()
        if method_name is not None:
            method_name = method_name.replace(':', '') 
            fcg.add_node(method_name)

        # Thêm cạnh cho mỗi lời gọi phương thức
        for _, call, _ in method.get_xref_to():
            call_name = call.get_method().get_name()
            if call_name is not None:
                call_name = call_name.replace(':', '')  
                if method_name is not None:
                    fcg.add_edge(method_name, call_name)

    return fcg
# Tạo 2 biến chứa đường dẫn tới 1 thư mục chứa sẵn file apk và 1 thư mục để chứa file fcg
# Nhớ đổi thành đường dẫn của bọn mày nhé
apk_directory = r'C:\Users\Minnef\Desktop\test\begin'
fcg_directory = r'C:\Users\Minnef\Desktop\test\output_fcg'


#duyệt qua tất cả các file apk trong thư mục apk_directory và chuyển thành file fcg, lưu vào thư mục fcg_directory
for i in range(1,1000):
    try:
        fcg = apk_to_fcg(r"C:\Users\Minnef\Desktop\test\begin\apk (" + str(i+1) + ").apk")
        nx.write_gexf(fcg, os.path.join(fcg_directory, 'fcg' + str(i+1) + '.gexf')) 
    except:
        continue   
        