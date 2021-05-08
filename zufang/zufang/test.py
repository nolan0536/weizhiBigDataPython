import chardet
import base64
str_url = base64.b64encode(str(123).encode())  # 被编码的参数必须是二进制数据
print(str_url)
str_url2 = base64.b64decode(str_url).decode("utf-8")
print(str_url2)

