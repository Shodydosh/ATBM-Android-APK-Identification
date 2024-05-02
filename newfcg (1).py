import os
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
def tryy(apk_directory, output_directory):
    # Lặp qua tất cả các tệp APK trong thư mục apk_directory
    for filename in os.listdir(apk_directory):
        if filename.endswith(".apk"):
            try:
                apk_path = os.path.join(apk_directory, filename)         
                try:
                    fcg = apk_to_fcg(apk_path)
                    nx.write_gexf(fcg, os.path.join(output_directory, '' + os.path.splitext(filename)[0] + '.gexf')) 
                except:
                    continue   
            except Exception as e:
                print(f"Error processing {filename}: {e}")
apk_directory = r'C:\Users\Minnef\Desktop\minh\mal'
# Đường dẫn tới thư mục để chứa các tệp txt đầu ra
output_directory = r'C:\Users\Minnef\Desktop\minh\fcg'
# Gọi hàm để chuyển đổi tất cả các tệp APK trong thư mục và lưu kết quả vào thư mục đầu ra
tryy(apk_directory, output_directory)
