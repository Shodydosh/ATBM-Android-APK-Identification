import os
from androguard.misc import AnalyzeAPK

def apk_to_java(apk_directory, output_directory):
    # Lặp qua tất cả các tệp APK trong thư mục apk_directory
    for filename in os.listdir(apk_directory):
        if filename.endswith(".apk"):
            apk_path = os.path.join(apk_directory, filename)
            try:
                # Phân tích tập tin APK
                apk, _, dx = AnalyzeAPK(apk_path)
                sequence = ''
                for method in dx.get_methods():
                    try:
                        method_name = method.get_method().get_source()
                        if method_name is not None:
                            sequence += method_name + "\n"
                    except Exception as e:
                        print("Error:", e)

                # Lưu chuỗi vào tập tin output trong thư mục output_directory
                output_path = os.path.join(output_directory, "" + os.path.splitext(filename)[0] + ".txt")
                with open(output_path, 'w', encoding='utf-8') as f:
                    f.write(sequence)
            except Exception as e:
                print(f"Error processing {filename}: {e}")
# Đường dẫn tới thư mục chứa các tệp APK
apk_directory = r'C:\Users\Minnef\Desktop\minh\mal'

# Đường dẫn tới thư mục để chứa các tệp txt đầu ra
output_directory = r'C:\Users\Minnef\Desktop\minh\java'

# Gọi hàm để chuyển đổi tất cả các tệp APK trong thư mục và lưu kết quả vào thư mục đầu ra
apk_to_java(apk_directory, output_directory)
