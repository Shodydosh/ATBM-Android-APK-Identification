from androguard.misc import AnalyzeAPK

def apk_to_java(apk_path, i):
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

        # Lưu chuỗi vào tập tin 'sequence.txt'
        fcg_directory = r'C:\Users\Minnef\Desktop\test\output_java\java'+str(i)+'.txt'
        with open(fcg_directory, 'w', encoding='utf-8') as f:
            f.write(sequence)
    except Exception as e:
        print("Error:", e)

# Tạo 2 biến chứa đường dẫn tới 1 thư mục chứa sẵn file apk và 1 thư mục để chứa file fcg
# Nhớ đổi thành đường dẫn của bọn mày nhé
# apk_directory = r'C:\Users\Minnef\Desktop\test\begin'

# duyệt qua tất cả các file apk trong thư mục apk_directory và chuyển thành file fcg, lưu vào thư mục fcg_directory
for i in range(1, 10):
    try:
        apk_to_java(r"C:\Users\Minnef\Desktop\test\begin\apk (" + str(i+1) + ").apk", i)
    except Exception as e:
        print("Error:", e)
        continue
