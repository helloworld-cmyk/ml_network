----- Page 1 -----
```md
Câu 1: Giá trị BER (Bit Error Rate = Tỷ lệ bít lỗi/Tỷ lệ bít truyền) phản ánh đặc trưng nào sau đây của đường truyền?
A. Tốc độ truyền tin tối đa
B. Thông lượng
C. Độ tin cậy
D. Độ suy hao tín hiệu
E. Độ trễ
ans: C

Câu 2: Thông số RTT (Round Trip Time) trong quá trình truyền tin cho biết điều gì?
A. Trễ hàng đợi trên các thiết bị chuyển tiếp
B. Thời gian chọn đường trên bộ định tuyến (router)
C. Trễ lan truyền tín hiệu trên đường truyền
D. Trễ 2 chiều giữa nút nguồn và nút đích
ans: D

Câu 3: Giả sử đường đi từ nút A đến nút B qua 3 liên kết với băng thông lần lượt là 4Mbps, 1Mbps và 2 Mbps. Thời gian để A truyền đến B một file có kích thước 10 MB là bao nhiêu. Giả sử các kết nối không truyền dữ liệu nào khác, trễ lan truyền và trễ tại các nút trung gian là không đáng kể?
A. 80 s
B. 20 s
C. 40 s
D. 140 s
E. Xấp xỉ 11.4 s
ans: A

Câu 4: Đặc điểm của cơ chế truyền "best-effort" là gì?
A. Chỉ gửi dữ liệu 1 lần, không phát lại
B. Thiết lập liên kết trước khi truyền
C. Sử dụng báo nhận
ans: A [suy luận]

Câu 5: Tại sao đường truyền phải có giá trị MTU (Maximum Transmission Unit) để giới hạn kích thước của gói tin được truyền?
A. Giảm xác suất đụng độ
B. Giảm tỉ lệ lỗi bít (BER – Bit Error Rate)
C. Giảm xác suất phải truyền lại dữ liệu
D. Tăng tốc độ truyền tin
ans: B
```

----- Page 2 -----
```md
Câu 6: Tại sao phải đặt giá trị MTU (Maximum Transmission Unit) cho đường truyền?
A. Giảm tỉ lệ phải truyền lại do lỗi bít trên gói tin
B. Giảm trễ hàng đợi
C. Tăng hiệu suất sử dụng đường truyền
D. Tránh tắc nghẽn
ans: C [suy luận]

Câu 7: Thông số nào sau đây được sử dụng để đánh giá độ tin cậy của đường truyền? (Chọn 2 đáp án)
A. Băng thông
B. Độ trễ
C. Độ suy hao
D. Tỉ lệ lỗi bit (BER)
E. Tỉ lệ mất gói tin
ans: D,E [suy luận]

Câu 8: Phát biểu nào sau đây là SAI về giao thức truyền thông?
A. Quy định khuôn dạng dữ liệu khi truyền
B. Quy định cách thức xử lý dữ liệu ở mỗi bên
C. Quy định thứ tự các thông điệp khi truyền
D. Độc lập với các giao thức khác
ans: D [suy luận]

Câu 9: Mô tả nào sau đây là đúng về kiến trúc phân tầng trong hệ thống truyền thông? (chọn 2 đáp án)
A. Thứ tự các tầng có thể thay đổi linh hoạt khi triển khai
B. Tầng trên quyết định cách thức cung cấp dịch vụ của tầng dưới
C. Tầng dưới cung cấp dịch vụ cho tầng trên qua điểm truy cập dịch vụ (SAP)
D. Một số tầng không cần triển khai trên tất cả các nút mạng
E. Giao thức của mỗi tầng độc lập với nhau
ans: C,D [suy luận]

Câu 10: Trong kiến trúc phân tầng của hệ thống truyền thông, phát biểu nào sau đây là đúng? (Chọn 2 đáp án)
A. Tại mỗi tầng, hai bên tham gia quá trình truyền tin phải sử dụng giao thức giống nhau
B. Quá trình đóng gói dữ liệu tại bên gửi được thực hiện từ tầng trên xuống tầng dưới
C. Mỗi mô hình phân tầng chọn một giao thức mạng để điều khiển hoạt động tất cả các tầng
D. Hoạt động của mỗi tầng không phụ thuộc vào các tầng khác
ans: A,B [suy luận]

Câu 11: Khái niệm PDU trong kiến trúc phân tầng là gì?
A. Một giao thức truyền thông
B. Một tầng trong mô hình OSI
C. Đơn vị dữ liệu được đóng gói theo giao thức của mỗi tầng trong kiến trúc phân tầng
D. Điểm truy cập dịch vụ của mỗi tầng cung cấp cho tầng trên
ans: C [suy luận]
```

----- Page 3 -----
```md
Câu 12: Trong kiến trúc phân tầng, khi nhận được dữ liệu từ tầng cao hơn chuyển xuống, tầng dưới xử lý như thế nào?
A. Sửa thông tin phần tiêu đề
B. Loại bỏ phần tiêu đề của gói tin
C. Thêm tiêu đề cho gói tin
D. Thay thế tiêu đề của gói tin bằng tiêu đề mới
ans: C [suy luận]

Câu 13: Đóng gói dữ liệu(encapsuation) trong kiến trúc phân tầng được thực hiện như thế nào?
A. Thêm phần tiêu đề mới vào gói tin nhận được ở tầng trên
B. Thay thế tiêu đề của gói tin tầng trên bằng tiêu đề mới
C. Nén phần dữ liệu trong gói tin nhận được từ tầng trên
D. Chỉ thực hiện thêm phần tiêu đề ở tầng dưới cùng
ans: A [suy luận]

Câu 14: Tính trong suốt trong kiến trúc phân tầng thể hiện như thế nào?
A. Tầng trên sử dụng dịch vụ của tầng dưới qua điểm truy cập dịch vụ (SAP) mà không cần quan tâm cách thức tầng dưới thực hiện
B. Mỗi tầng cung cấp nhiều dịch vụ khác nhau
C. Dữ liệu được đóng gói theo giao thức điều khiển
D. Chức năng trên mỗi tầng là khác nhau
E. Hai tầng trên liên kết phải sử dụng giao thức giống nhau
ans: A [suy luận]

Câu 15: Trong mô hình TCP/IP, tầng nào thực hiện chức năng điều khiển truyền dữ liệu trên liên kết vật lý?
A. Tầng vật lý
B. Tầng liên kết dữ liệu
C. Tầng mạng
D. Tầng giao vận
ans: B [suy luận]

Câu 16: Trong quá trình truyền dữ liệu, chức năng của tầng nào trong mô hình TCP/IP chỉ thực hiện trên các hệ thống đầu cuối? (chọn 2 đáp án)
A. Tầng ứng dụng
B. Tầng giao vận
C. Tầng mạng
D. Tầng liên kết dữ liệu
E. Tầng vật lý
ans: A,B [suy luận]
```

----- Page 4 -----
```md
Câu 17: Tầng ứng dụng của mô hình TCP/IP đảm nhận chức năng những tầng nào khi tham chiếu tới mô hình OSI?
A. Tầng dụng, tầng phiên
B. Tầng ứng dụng, tầng trình diễn
C. Tầng ứng dụng, tầng phiên, tầng trình diễn
D. Tầng ứng dụng, tầng giao vận, tầng mạng
E. Tầng ứng dụng, tầng giao vận, tầng mạng
ans: C [suy luận]

Câu 18: Chức năng của tầng nào dưới đây chỉ thực hiện trên các nút mạng đầu cuối?
A. Tầng giao vận
B. Tầng mạng
C. Tầng liên kết dữ liệu
D. Tầng vật lý
ans: A [suy luận]

Câu 19: Phát biểu nào sau đây là SAI?
A. Mạng chuyển mạch kênh cung cấp dịch vụ theo mô hình hướng kết nối (connection-oriented)
B. Trong mạng chuyển mạch gói, dữ liệu của các liên kết khác nhau được truyền trên cùng một đường truyền vật lý
C. Chuyển tiếp dữ liệu trên mạng chuyển mạch kênh chậm hơn trên mạng chuyển mạch gói
D. Khi chuyển tiếp dữ liệu trong mạng chuyển mạch gói, có thể thiết lập độ ưu tiên cho các gói tin khi xử lý hàng đợi
E. Trong chuyển mạch kênh, tài nguyên của mỗi cuộc hội thoại được xác định trong giai đoạn thiết lập kênh và không đổi trong suốt quá trình truyền dữ liệu
ans: C [suy luận]

Câu 20: Phát biểu nào sau đây là đúng về chuyển mạch kênh?
A. Tài nguyên của mỗi kênh là như nhau với mọi liên kết, không phụ thuộc vào yêu cầu chất lượng dịch vụ.
B. Trong mạng chuyển mạch kênh, do trước khi truyền dữ liệu, kênh truyền đã được thiết lập nên các giao thức tầng trên luôn là giao thức hướng không kết nối (connectionless).
C. Tài nguyên của mỗi kênh được xác định trong giai đoạn thiết lập kênh và không đổi trong suốt quá trình truyền dữ liệu.
D. Để tăng độ tin cậy khi truyền tải dữ liệu, một kênh làm việc và một kênh dự phòng sẽ được thiết lập cho mỗi liên kết.
E. Kênh sẽ được giải phóng khi một trong hai bên bất kỳ ngắt liên kết.
ans: C [suy luận]

Câu 21: Ưu điểm của kỹ thuật chuyển mạch gói so với chuyển mạch kênh là gì?
A. Thời gian chuyển tiếp dữ liệu ngắn hơn
B. Hiệu suất sử dụng đường truyền cao hơn
C. Không xảy ra tắc nghẽn
D. Đảm bảo chất lượng dịch vụ
E. Không mất thời gian thiết lập kênh truyền
ans: B [suy luận]
```

----- Page 5 -----
```md
Câu 22: Những phát biểu nào là SAI về hoạt động của kỹ thuật chuyển mạch gói? (Chọn 2 đáp án)
A. Gói tin của các liên kết khác nhau được truyền trên cùng một đường truyền vật lý
B. Độ trễ trong mạng không phụ thuộc vào tải
C. Trên cùng một liên kết vật lý, tất cả các gói tin đều được truyền với tốc độ như nhau.
D. Các gói tin tới cùng một đích luôn được truyền theo cùng tuyến đường đi
E. Cho phép thiết lập độ ưu tiên cho các gói tin khi xử lý hàng đợi
ans: B,D

Câu 23: Đồ thị nào sau đây mô tả tình trạng tắc nghẽn của mạng? (Chọn 2 đáp án)
img: assets/cau-12-do-thi-tac-nghen.png
A. [Đồ thị a: Thông lượng - Tải, đường cong giảm dần]
B. [Đồ thị b: Độ trễ - Tải, đường cong tăng theo hàm mũ]
C. [Đồ thị c: Thông lượng - Tải, đường cong tăng rồi giảm đột ngột]
D. [Đồ thị d: Băng thông - Tải, đường cong giảm dần]
ans: B,C

Câu 24: Giao thức nào sau đây không nằm cùng nhóm với các giao thức còn lại?
A. HTTP
B. FTP
C. SMTP
D. TCP
E. ICMP
ans: E [suy luận]

Câu 25: Các giao thức nào sau đây sử dụng giao thức TCP của tầng giao vận? (Chọn 2 đáp án)
A. DNS
B. DHCP
C. FTP
D. POP
E. IP
F. OSPF
ans: C,D

Câu 26: Một người dùng trong mạng LAN sử dụng dịch vụ Web để tải một file lên máy chủ. Theo mô hình TCP/IP, dữ liệu của người dùng có thể được đóng gói lần lượt bằng các giao thức nào?
A. FTP, UDP, IP, Ethernet
B. HTTP, UDP, IP, Ethernet
```

----- Page 6 -----
```md
Câu 27: [tiếp từ trang trước]
C. HTTP, TCP, IP, Ethernet
D. Ethernet, IP, TCP, HTTP
E. Ethernet, IP, TCP, FTP
ans: [không chắc] [tiếp từ trang trước]

Câu 28: Đâu là một thứ tự sử dụng các giao thức đóng gói dữ liệu trong mạng TCP/IP?
A. HTTP, TCP, Ethernet, IP
B. Ethernet, IP, TCP, FTP
C. SMTP, UDP, IP, Ethernet
D. DNS, UDP, IP, Ethernet
ans: D [suy luận]

Câu 29: Những giao thức tầng ứng dụng nào sau đây là cần thiết khi một người dùng sử dụng web mail để gửi email từ địa chỉ user@gmail.com tới user@yahoo.com? (Chọn 3 đáp án)
A. SMTP
B. POP
C. IMAP
D. DNS
E. HTTP
F. TCP
ans: A,D,E [suy luận]

Câu 30: Những giao thức tầng ứng dụng nào sau đây là cần thiết khi một người dùng sử dụng web mail để gửi email từ địa chỉ user@gmail.com tới user@yahoo.com? (Chọn 2 đáp án)
A. SMTP
B. POP
C. IMAP
D. DNS
E. HTTP
F. TCP
ans: A,E [suy luận]

Câu 31: Phát biểu nào sau đây là SAI về hệ thống tên miền DNS?
A. Không gian tên miền có kiến trúc phân cấp
B. Tìm kiếm thông tin tên miền được bắt đầu từ tên miền cấp 1
C. Trong cơ chế phân giải đệ quy, máy chủ tên miền luôn chuyển truy vấn cho máy chủ gốc
D. Trong cơ chế phân giải tương tác, máy chủ tên miền luôn trả lại thông tin tên miền được truy vấn
ans: D [suy luận]

Câu 32: Phát biểu nào sau đây là đúng về hệ thống DNS? (Chọn 2 đáp án)
A. Mỗi tên miền chỉ ánh xạ tới một địa chỉ IP
B. Mỗi địa chỉ IP có thể ánh xạ tới nhiều tên miền
C. Hệ thống máy chủ tên miền gốc lưu trữ thông tin của toàn bộ tên miền trên Internet
D. Quá trình tìm kiếm thông tin tên miền được thực hiện từ gốc tới các nút nhánh
ans: B,D [suy luận]
```

----- Page 7 -----
```md
Câu 33: Giao thức nào cho phép client lấy đồng thời tiêu đề và thân email từ server?
A. HTTP
B. SMTP
C. POP
D. IMAP
ans: D

Câu 34: Giả sử một máy chủ Web được chuyển đổi kết nối sang một mạng khác, những thao tác nào sau đây cần thực hiện để người dùng vẫn truy cập được qua tên miền cũ?
A. Gán địa chỉ IP cho máy chủ theo địa chỉ mạng mới
B. Cấu hình lại giao thức định tuyến trên bộ định tuyến
C. Thay đổi ánh xạ tên miền sang địa chỉ IP mới
D. Cấu hình lại máy chủ DHCP
ans: C

Câu 35: Phương thức nào được sử dụng trong thông điệp HTTP Request để yêu cầu một tài nguyên? (Chọn 2 đáp án)
A. GET
B. POST
C. PUT
D. HEAD
ans: A,D

Câu 36: Có tối thiểu bao nhiêu thông điệp HTTP Request được phát đi khi người dùng truy cập vào một trang web chứa 20 bức ảnh?
A. 1
B. 2
C. 20
D. 21
ans: D

Câu 37: Một trang web có một đoạn văn văn và 10 ảnh minh họa. File mã nguồn HTML và các file ảnh nằm trên 2 máy chủ Web khác nhau. Khi người dùng truy cập vào trang web này, có bao nhiêu kết nối TCP được thiết lập nếu giao thức được sử dụng là HTTP 1.1?
A. 10
B. 11
C. 1
D. 2
E. Không xác định
ans: D
```

----- Page 8 -----
```md
Câu 38: Có bao nhiêu thông điệp được trao đổi giữa trình duyệt và máy chủ Web nếu người dùng truy cập vào một trang Web có vài đoạn văn bản và 4 bức ảnh?
A. 1 HTTP Request, 1 HTTP Response
B. 1 HTTP Request, 5 HTTP Response
C. 5 HTTP Request, 5 HTTP Response
D. 5 HTTP Request, 1 HTTP Response
E. Không xác định
ans: C [suy luận]

Câu 39: Giao thức FTP sử dụng số hiệu cổng ứng dụng nào? (Chọn 2 đáp án)
A. 20
B. 21
C. 22
D. 25
E. 53
ans: A,B [suy luận]

Câu 40: Hai kết nối giữa client và server trong dịch vụ FTP được sử dụng như thế nào?
A. Một kết nối hoạt động, một kết nối để dự phòng
B. Cả 2 kết nối cùng tải tệp tin lên (upload), hoặc cùng tải xuống (download)
C. Một kết nối tải tệp tin lên (upload), kết nối còn lại để tải xuống (download)
D. Một kết nối để truyền dữ liệu của tệp tin, một kết nối để truyền thông điệp điều khiển
ans: D [suy luận]

Câu 41: Tại bên nhận, dựa vào thông tin nào dữ liệu được chuyển tới đúng tiến trình trên tầng ứng dụng để xử lý?
A. Số hiệu cổng ứng dụng nguồn
B. Số hiệu cổng ứng dụng đích
C. Địa chỉ IP đích
D. Giao thức tại tầng giao vận
ans: B [suy luận]

Câu 42: Giả sử từ trên nút mạng A có hai tiến trình trao đổi dữ liệu với một tiến trình trên nút mạng B, điều khiển bởi giao thức UDP. Phát biểu nào sau đây là đúng? (Chọn 2 đáp án)
A. Hai tiến trình trên nút mạng A sử dụng chung một socket để trao đổi dữ liệu với tiến trình trên nút B
B. Nút B sử dụng hai socket khác nhau để trao đổi dữ liệu với hai tiến trình của nút A
C. Các gói tin gửi từ nút A tới tiến trình trên nút B có cùng số hiệu cổng đích
D. Các gói tin gửi từ nút B tới hai tiến trình trên nút A có cùng số hiệu cổng đích
E. Hai tiến trình trên nút A đều có thể gửi dữ liệu liên tục với tốc độ cao nhất có thể
ans: C,E [không chắc]

Câu 43: Giao thức UDP nên được sử dụng khi xây dựng các ứng dụng mạng nào dưới đây?
A. Truyền dữ liệu từ các trạm quan trắc môi trường về trung tâm dữ liệu
B. Điều khiển máy tính từ xa
C. Kiểm tra trạng thái hoạt động giữa các nút mạng
D. Truyền dữ liệu video trong hội nghị trực tuyến
ans: D [suy luận]
```

----- Page 9 -----
```md
Câu 44: Phát biểu nào sau đây là đúng về giao thức UDP? (Chọn 3 đáp án)
A. Là một giao thức thuộc tầng giao vận
B. Truyền dữ liệu theo datagram
C. Cung cấp các cơ chế truyền thông tin cậy
D. Sử dụng time-out riêng cho mỗi datagram gửi đi
E. Gửi liên tục các datagram mà không cần chờ báo nhận
ans: A,B,E [suy luận]

Câu 45: Điều gì chứng tỏ UDP là một giao thức không tin cậy?
A. Không thiết lập liên kết trước khi truyền
B. Không sử dụng báo nhận
C. Không kiểm tra lỗi trên gói tin
D. Không kiểm soát lượng dữ liệu gửi đi làm quá tải bên nhận
ans: B [suy luận]

Câu 46: Tại phía gửi, giao thức UDP thực hiện những thao tác xử lý nào?
A. Chia dữ liệu nhận được từ tầng ứng dụng vào các gói tin
B. Thiết lập liên kết với phía nhận
C. Gửi lại nếu không nhận được báo nhận
D. Chuyển gói tin xuống tầng mạng
E. Đặt bộ đếm time-out cho mỗi gói tin gửi đi
ans: D [suy luận]

Câu 47: Trong hoạt động của giao thức UDP, phía nhận không thực hiện thao nào dưới đây khi nhận được dữ liệu? (Chọn 2 đáp án)
A. Kiểm tra lỗi trên gói tin
B. Báo nhận thành công
C. Loại bỏ các gói tin nhận được không theo đúng thứ tự
D. Chuyển dữ liệu cho tiến trình tầng ứng dụng dựa vào số hiệu cổng đích
ans: B,C [suy luận]

Câu 48: Những mô tả nào là đúng về hoạt động của giao thức UDP tại nút nhận? (Chọn 2 đáp án)
A. Nhận dữ liệu từ tầng ứng dụng, xử lý dữ liệu và chuyển xuống cho tầng mạng
B. Kiểm tra lỗi bit trên phần tiêu đề gói tin dựa vào mã checksum
C. Chuyển dữ liệu cho tiến trình trên tầng ứng dụng dựa vào số hiệu cổng ứng dụng đích
D. Gửi gói tin ACK cho nút nguồn để báo nhận thành công
E. Loại bỏ các gói tin nhận được không theo đúng thứ tự
F. Huỷ liên kết sau khi đã nhận đủ dữ liệu
ans: B,C [suy luận]
```

----- Page 10 -----
```md
Câu 49: Trong hoạt động của giao thức UDP, phía nhận xử lý như thế nào khi gói tin nhận được bị lỗi?
A. Nếu giao thức tầng trên có chức năng sửa lỗi thì chuyển lên cho giao thức đó
B. Huỷ gói tin
C. Gửi lại cho phía gửi sửa lỗi
D. Báo nhận không thành công để phía gửi phát lại
ans: A,B [suy luận]

Câu 50: Lợi thế của giao thức UDP so với TCP là gì? (Chọn 3 đáp án)
A. Kích thước phần tiêu đề nhỏ hơn
B. Hoạt động đơn giản hơn
C. Nhanh hơn
D. Không phải phát lại dữ liệu
ans: A,B,C [suy luận]

Câu 51: Ưu thế của giao thức TCP so với UDP là gì? (Chọn 3 đáp án)
A. Nhanh hơn do truyền dữ liệu theo dòng byte
B. Tin cậy hơn
C. Không làm quá tải nút nhận
D. Có cơ chế kiểm soát tắc nghẽn
ans: B,C,D [suy luận]

Câu 52: Những hoạt động nào sau đây cho thấy TCP là một giao thức truyền thông tin cậy? (Chọn 3 đáp án)
A. Sử dụng ACK báo nhận dữ liệu thành công
B. Sử dụng checksum để kiểm soát lỗi
C. Phát lại dữ liệu khi xảy ra time-out
D. Kiểm soát luồng, không làm quá tải phía nhận
E. Kiểm soát tắc nghẽn
ans: A,B,C [suy luận]

Câu 53: Trong hoạt động của giao thức TCP, khi nào cần phát lại gói tin đã gửi đi? (Chọn 2 đáp án)
A. Nhận được 3 gói tin báo nhận có ACK Number giống nhau
B. Xảy ra timeout
C. Phát hiện lỗi trên gói tin báo nhận
D. Giá trị ACK Number trên gói tin báo nhận không nằm trong cửa sổ trượt
ans: A,B [suy luận]

Câu 54: Giao thức TCP thực hiện báo nhận thành công như thế nào? (Chọn 2 đáp án)
A. Thiết lập cờ ACK trên gói tin phản hồi
B. Thiết lập cờ SYN trên gói tin phản hồi
C. Tính toán ACK Number trên gói tin phản hồi để yêu cầu dữ liệu tiếp theo
D. Phản hồi lại gói tin đã nhận
ans: A,C [suy luận]

Câu 55: Giá trị Windows size trong phần tiêu đề của gói tin TCP được sử dụng như thế nào?
A. Phát hiện lỗi trên gói tin
B. Xác định lượng dữ liệu tối đa bên gửi có thể gửi đi
C. Xác định lượng dữ liệu tối đa bên nhận có thể nhận
D. Thiết lập liên kết
ans: C [suy luận]
```

----- Page 11 -----
```md
Câu 56: Nút mạng nhận được gói tin TCP có 32 bit đầu tiên là 1000 1000 0001 0001 0000 0000 0001 1001. Nếu dịch vụ trên nút mạng này đang sử dụng số hiệu cổng ứng dụng chuẩn, hãy cho biết giao thức điều khiển dịch vụ là gì?
A. HTTP
B. HTTPS
C. SMTP
D. POP
E. FTP
ans: C

Câu 57: Giá trị checksum trong phần tiêu đề của gói tin TCP được sử dụng như thế nào?
A. Phát hiện lỗi trên gói tin
B. Xác định lượng dữ liệu tối đa bên nhận có thể nhận
C. Thiết lập liên kết
D. Sửa lỗi trên gói tin
ans: A

Câu 58: Mã phát hiện lỗi nào sau đây được sử dụng để kiểm tra lỗi trên phần tiêu đề của gói tin TCP?
A. Mã parity
B. Mã checksum 16 bit
C. Mã checksum 32 bit
D. Mã CRC 16 bit
E. Mã CRC 32 bit
ans: B

Câu 59: Khi nào một bên trong quá trình truyền tin điều khiển bằng TCP gửi gói tin có cờ FIN được thiết lập?
A. Yêu cầu thiết lập liên kết
B. Đồng ý thiết lập liên kết
C. Báo kết thúc gửi dữ liệu
D. Báo kết thúc nhận dữ liệu
ans: C

Câu 60: Giả sử từ mỗi host A và B có một tiến trình trao đổi dữ liệu với một tiến trình host C, điều khiển bởi giao thức TCP. Phát biểu nào sau đây là đúng?
A. Host A và B không thể kết nối tới cùng một cổng trên host C
B. Socket trên host A và B phải sử dụng số hiệu cổng khác nhau
C. Nếu phát hiện tắc nghẽn xảy ra trên liên kết với host A thì host C khởi động giai đoạn Slow Start trên cả 2 liên kết
D. Host C sử dụng các socket khác nhau để tạo liên kết với host A và B
E. Host C sử dụng giá trị cửa sổ nhận giống nhau cho cả hai liên kết với A và B
ans: D
```

----- Page 12 -----
```md
Câu 61: Giả sử trên một nút mạng, P1 và P2 là hai tiến trình sử dụng giao thức TCP để trao đổi dữ liệu với tiến trình P3 trên nút mạng khác. Phát biểu nào sau đây là đúng?
A. P1 và P2 phải sử dụng số hiệu cổng ứng dụng giống nhau
B. P1 và P2 không thể đồng thời gửi dữ liệu cho P3
C. Khi P1 ngắt liên kết, P2 vẫn trao đổi dữ liệu một cách bình thường với P3
D. P1 và P2 sử dụng cửa sổ kiểm soát tắc nghẽn giống nhau
ans: C [suy luận]

Câu 62: Trong hoạt động của giao thức TCP, phía nhận thực hiện thao tác xử lý nào nếu nhận được một gói tin khi bộ đệm đã đầy? (Chọn 2 đáp án)
A. Xóa bộ đệm
B. Loại bỏ gói tin
C. Gửi lại ACK xác nhận các gói tin trước đó với giá trị Receive Window = 0
D. Gửi ACK xác nhận gói tin vừa nhận được với giá trị Receive Window = 0
E. Gửi gói tin ACK bất kỳ với giá trị Receive Window bằng kích thước dữ liệu trong bộ đệm
ans: C,D [suy luận]

Câu 63: Giả sử giao thức TCP sử dụng thuật toán Go-back-N để phát lại các gói tin bị lỗi. Phía gửi cần truyền các gói tin được đánh số thứ tự là 0, 1, 2, 3, 4; kích thước cửa sổ gửi là 3. Nếu gói tin số 2 bị mất thì tổng số gói tin phía gửi đã gửi đi là bao nhiêu sau khi kết thúc quá trình truyền tin?
A. 4
B. 5
C. 6
D. 7
E. 8
ans: E [suy luận]

Câu 64: Tại sao sử dụng cơ chế "hồi phục nhanh" trong quá trình kiểm soát tắc nghẽn làm tăng hiệu năng của giao thức TCP?
A. Phía gửi phát hiện sớm tắc nghẽn
B. Phía nhận sẽ nhận được các gói tin còn thiếu một cách sớm nhất
C. Cho phép lượng dữ liệu gửi đi lớn hơn giá trị của sổ nhận của phía nhận
D. Cho phép gửi dữ liệu ngay mà không cần chờ báo nhận
E. Phía gửi không cần chuyển sang giai đoạn tránh tắc nghẽn
ans: A [suy luận]

Câu 65: Quá trình điều khiển tắc nghẽn trong giao thức TCP không thực hiện thao tác nào?
A. Giảm kích thước của sổ kiểm soát tắc nghẽn khi có timeout
B. Khởi tạo cửa sổ kiểm soát tắc nghẽn là 1 MSS (Maximum Segment Size)
C. Giữ nguyên kích thước của sổ kiểm soát tắc nghẽn khi vượt qua giá trị ngưỡng của giai đoạn Slow Start
D. Giảm giá trị ngưỡng của giai đoạn Slow Start khi có timeout
ans: C [suy luận]
```

----- Page 13 -----
```md
Câu 66: Phát biểu nào sau đây là sai trong quá trình điều khiển tắc nghẽn của giao thức TCP?(Chọn 2 đáp án)
A. Tăng gấp đôi kích thước cửa sổ kiểm soát tắc nghẽn khi gửi thành công trong giai đoạn Slow Start?
B. Không tăng kích thước cửa sổ kiểm soát tắc nghẽn trong giai đoạn tránh tắc nghẽn
C. Bắt đầu lại giai đoạn tránh tắc nghẽn khi có time-out
D. Khi bắt đầu giai đoạn Slow Start, kích thước của sổ kiểm soát tắc nghẽn là 1MSS (Maximum Segment Size)
ans: B,C [suy luận]

Câu 67: Giả sử trong một khoảng thời gian nào đó quan sát quá trình truyền dữ liệu giữa hai ứng dụng được điều khiển bởi giao thức TCP, ta thu được đồ thị điều khiển tắc nghẽn như sau:
img: assets/tcp-congestion-graph.png
Giai đoạn Slow Start bắt đầu tại những lượt gửi nào?
A. 10 và 14
B. 14 và 19
C. 10 và 23
D. 19 và 23
ans: C [suy luận]

Câu 68: Giả sử trong một khoảng thời gian nào đó quan sát quá trình truyền dữ liệu giữa hai ứng dụng được điều khiển bởi giao thức TCP, ta thu được đồ thị điều khiển tắc nghẽn như sau:
img: assets/tcp-congestion-graph.png
Đoạn nào biểu diễn giai đoạn tránh tắc nghẽn?
A. 6-14
B. 6-10 và 14-18
C. 6-10, 14-18 và 19-22
D. 19-22
ans: C [suy luận]
```

----- Page 14 -----
```md
Câu 69: Giả sử trong một khoảng thời gian nào đó quan sát quá trình truyền dữ liệu giữa hai ứng dụng được điều khiển bởi giao thức TCP, ta thu được đồ thị điều khiển tắc nghẽn như sau:
img: assets/tcp-congestion-graph.png
Tại lượt gửi nào, phía gửi xảy ra time-out?(Chọn 2 đáp án)
A. 9
B. 14
C. 18
D. 22
ans: [không chắc]

Câu 70: Trong quá trình truyền tin được điều khiển bởi giao thức TCP, tiến trình đích nhận được gói tin có trường Sequence Number = 5600 trong phần tiêu đề, dữ liệu có kích thước 1400 byte. Nếu phát hiện có lỗi trên phần tiêu đề qua việc kiểm tra trường checksum, tiến trình đích sẽ thực hiện các bước xử lý như thế nào? (Chọn 2 đáp án)
A. Sửa lỗi bit tìm thấy trên phần tiêu đề
B. Hủy gói tin bị lỗi
C. Gửi báo nhận với ACK Number = 5600 cho bên nhận
D. Hủy tất cả các gói tin đã nhận trước đó
E. Tách phần dữ liệu và chuyển cho tầng ứng dụng
ans: B,C [suy luận]

Câu 71: Trong quá trình truyền tin được điều khiển bởi giao thức TCP, tiến trình nguồn không nhận được báo nhận khi đã hết thời gian time-out. Giả sử giá trị của sổ kiểm soát tắc nghẽn là 5600 byte, và 1 MSS = 1400 byte, tiến trình này gửi đi liên tiếp tối đa bao nhiêu byte?
A. 0
B. 1400
C. 4200
D. 5600
E. 7000
ans: B

Câu 72: Trong hoạt động của giao thức TCP, tiến trình nguồn đang sử dụng cửa sổ kiểm soát tắc nghẽn là 8400 byte thì nhận được 3 gói tin báo nhận có ACK giống nhau (có trường Receive windows trong tiêu đề là 65000). Giả sử giá trị MSS = 1400 byte. Hãy cho biết tiến trình nguồn có thể gửi liên tiếp tối đa bao nhiêu byte?
A. 1400 byte
B. 65000 byte
C. 4200 byte
D. 2800 byte
E. 7000 byte
ans: C
```

----- Page 15 -----
```md
Câu 73: Trong hoạt động của giao thức TCP, khi xảy ra time-out, phía gửi thực hiện những thao tác xử lý nào?(Chọn 2 đáp án)
A. Tính toán lại giá trị của sổ kiểm soát tắc nghẽn
B. Tính toán lại giá trị của sổ kiểm soát luồng
C. Phát lại dữ liệu đã gửi mà chưa nhận được ACK
D. Chờ thêm một khoảng thời gian tối thiểu 2 lần RTT trung bình trước khi phát lại dữ liệu
E. Đóng liên kết hiện tại và thiết lập liên kết mới
ans: A,C

Câu 74: Trong hoạt động của giao thức TCP, phía nhận thực hiện thao tác xử lý nào nếu nhận được một gói tin khi bộ đệm đã đầy?(Chọn 2 đáp án)
A. Xóa bộ đệm
B. Loại bỏ gói tin
C. Gửi lại ACK trước đó với giá trị Receive Window = 0
D. Gửi ACK cho gói tin vừa nhận được với giá trị Receive Window = 0
E. Gửi gói tin ACK bất kỳ với giá trị Receive Window bằng kích thước dữ liệu trong bộ đệm
ans: B,C

Câu 75: Phát biểu nào sau đây là đúng về địa chỉ IP 116.12.34.113 /28?(Chọn 2 đáp án)
A. Là một địa chỉ phân lớp A
B. Phần địa chỉ máy trạm (Host ID) có 28 bit
C. Có thể gán cho một nút mạng
D. Chỉ dùng trong mạng LAN
E. Nằm trong mạng có địa chỉ 116.12.34.128 /28
ans: A,C

Câu 76: Sử dụng mặt nạ 255.255.252.0 để chia mạng 160.12.64.0 /19 thành các mạng con. Số mạng con thành lập được là bao nhiêu?
A. 22
B. 19
C. 3
D. 8
E. 6
ans: D

Câu 77: Sử dụng mặt nạ 255.255.252.0 để chia mạng 160.12.64.0 /19 thành các mạng con. Mỗi mạng con có thể cấp phát được tối đa bao nhiêu địa chỉ máy trạm?
A. 3
B. 8
C. 22
D. 1022
E. 1024
ans: D

Câu 78: Sử dụng mặt nạ 255.255.252.0 để chia mạng 160.12.64.0 /19 thành các mạng con. Địa chỉ nào sau đây không phải là một địa chỉ mạng con có được từ cách chia trên?(Chọn 2 đáp án)
A. 160.12.68.0 /22
B. 160.12.70.0 /22
C. 160.12.72.0 /22
D. 160.12.74.0 /22
ans: B,D
```

----- Page 16 -----
```md
Câu 79: Các địa chỉ IP nào sau đây có cùng NetworkID (chọn 2 đáp án)?
A. 172.16.100.1 /20
B. 172.16.110.1 /20
C. 172.16.120.1 /20
D. 172.16.130.1 /21
E. 172.16.140.1 /21
F. 172.16.150.1 /21
ans: A,B [suy luận]

Câu 80: Những địa chỉ IP nào sau đây KHÔNG dùng trên mạng Internet?(Chọn 3 đáp án)
A. 127.0.0.1 /8
B. 169.254.1.1 /16
C. 192.168.1.1 /24
D. 12.34.56.78 /8
E. 203.147.12.156 /24
F. 172.12.101.57 /16
ans: A,B,C [suy luận]

Câu 81: Địa chỉ 148.37.21.104 thuộc phân lớp nào?
A. A
B. B
C. C
D. D
E. E
ans: B [suy luận]

Câu 82: Địa chỉ IP nào sau đây gán được cho một nút mạng?
A. 230.146.21.45 /28
B. 192.168.1.0 /24
C. 10.64.0.0 /12
D. 10.64.0.0 /10
E. 172.16.3.255 /21
F. 172.16.3.255 /22
ans: E [suy luận]
```

----- Page 17 -----
```md
Câu 83: Một mạng có địa chỉ phân mạng dài 23 bit. Nếu chia thành 4 mạng con thì số địa chỉ IP tối đa mỗi mạng con có thể gán cho máy trạm là bao nhiêu?
A. 512
B. 256
C. 128
D. 254
E. 126
F. 30
ans: E [suy luận]

Câu 84: Có bao nhiêu địa chỉ có thể sử dụng để gán cho các nút mạng trong mạng 204.16.156.32/27?
A. 32
B. 30
C. 27
D. 5
ans: B [suy luận]

Câu 85: Địa chỉ IP nào sau đây là một địa chỉ multicast?
A. 127.0.0.1
B. 192.168.1.1
C. 8.8.8.8
D. 224.0.0.25
ans: D [suy luận]

Câu 86: Gói tin IP có địa chỉ đích 67.125.90.13 sẽ được router chuyển tiếp tới mạng nào?
A. 67.125.64.0 /19
B. 67.125.0.0 /17
C. 67.125.96.0 /19
D. 67.125.128.0 /17
ans: A [suy luận]

Câu 87: Mặt nạ mạng nào sau đây có thể chia mạng 172.16.64.0 /18 thành 16 mạng con?
A. 255.255.0.0
B. 255.255.192.0
C. 255.255.252.0
D. 255.255.255.0
ans: C [suy luận]

Câu 88: Ý nghĩa của trường TTL(Time-to-live) trong tiêu đề gói tin IP là gì?
A. Góc thời gian để đồng bộ giữa hai bên
B. Thời điểm gói tin được gửi đi
C. Số chặng tối đa gói tin có thể được chuyển tiếp qua
D. Số chặng mà gói tin đã đi qua trước khi tới đích
E. Thời gian tối đa gói tin có thể nằm trong hàng đợi
ans: C [suy luận]
```

----- Page 18 -----
```md
Câu 89: Trong hoạt động của giao thức IP, phía gửi không thực hiện thao tác nào dưới đây? (Chọn 2 đáp án)
A. Đặt dữ liệu nhận được từ tầng giao vận vào gói tin và thêm thông tin điều khiển
B. Thiết lập liên kết với phía nhận trước khi truyền đi
C. Chuyển gói tin cho tầng liên kết dữ liệu xử lý
D. Chờ báo nhận trước khi gửi gói tin tiếp theo
ans: B,D [suy luận]

Câu 90: Giao thức IP thực hiện những quá trình nào sau đây tại phía nhận? (Chọn 3 đáp án)
A. Phát ACK báo nhận thành công
B. Kiểm tra checksum để phát hiện lỗi
C. Hợp mảnh các gói tin nếu cần
D. Thêm thông tin phân tiêu đề trước khi chuyển cho giao thức tầng trên
E. Xác định giao thức tầng trên nào sẽ xử lý tiếp dữ liệu
ans: B,C,E [suy luận]

Câu 91: Giao thức IP không thực hiện thao tác nào tại phía nhận? (Chọn 2 đáp án)
A. Kiểm tra lỗi trên gói tin
B. Sửa lỗi nếu có lỗi
C. Phát báo nhận cho nút gửi
D. Hủy gói tin nếu TTL = 0
ans: B,C [suy luận]

Câu 92: Nếu không tìm được cổng để chuyển tiếp gói tin IP đi, router xử lý như thế nào?
A. Gửi gói tin ra tất cả các cổng
B. Thực hiện quá trình định tuyến để tìm đường đi cho gói tin này
C. Hủy gói tin và báo lỗi cho nút nguồn
D. Gửi lại gói tin cho nút nguồn
ans: C [suy luận]

Câu 93: Router không thực hiện bước xử lý nào sau đây khi chuyển tiếp một gói tin IP? (Chọn 2 đáp án)
A. Kiểm tra giá trị TTL của gói tin
B. Kiểm tra lỗi bit cho phần tiêu đề
C. Phân mảnh gói tin nếu kích thước lớn hơn giá trị MTU của đường truyền
D. Tìm kiếm lối ra dựa trên địa chỉ đích
E. Bổ sung địa chỉ đích vào bảng chuyển tiếp nếu chưa biết
F. Giảm giá trị TTL của gói tin
ans: E [không chắc] [chỉ xác định rõ 1 đáp án không phù hợp - đề gốc yêu cầu 2]
```

----- Page 19 -----
```md
Câu 94: Bộ định tuyến không thực hiện thao tác nào khi chuyển tiếp (forwarding) gói tin IP? (Chọn 3 đáp án)
A. Thiết lập liên kết với nút kế tiếp
B. Quảng bá gói tin nếu không tìm thấy lối ra
C. Giảm giá trị TTL (time-to-live) của gói tin
D. Phân mảnh gói tin nếu cần
E. Bổ sung địa chỉ đích vào bảng chuyển tiếp nếu chưa biết
ans: A,B,E [suy luận]

Câu 95: Trong hoạt động chuyển tiếp gói tin IP trên router, lý do nào sau đây khiến gói tin bị loại bỏ? (Chọn 4 đáp án)
A. Phát hiện lỗi thông qua trường checksum
B. Gói tin bị phân mảnh
C. Không tìm thấy cổng ra trên bảng chuyển tiếp
D. Hàng đợi trên router bị đầy
E. Giá trị TTL = 1
ans: A,C,D,E [suy luận]

Câu 96: Cơ chế nào được sử dụng để chuyển đổi địa chỉ IP khi chuyển tiếp gói tin IP giữa mạng cục bộ và mạng công cộng?
A. DNS
B. DHCP
C. ARP
D. NAT
ans: D

Câu 97: Khi nào cần phân mảnh gói tin IP trong quá trình truyền?
A. Có tắc nghẽn xảy ra trên đường truyền
B. Kích thước gói tin lớn hơn MTU của đường truyền
C. Kích thước gói tin lớn hơn kích thước còn trống trên bộ đệm của nút nhận
D. Phát hiện lỗi trên gói tin
ans: B

Câu 98: Khi chuyển tiếp, gói tin IP bị phân mảnh trong trường hợp nào?
A. Mạng có tắc nghẽn
B. Mạng có đụng độ
C. Kích thước gói tin lớn hơn MTU của đường truyền
D. Có nhiều lối ra phù hợp để đưa dữ liệu tới mạng đích
E. Kích thước vùng trống trong bộ đệm của nút kế tiếp không đủ để nhận gói tin
ans: C

Câu 99: Một gói tin IP có kích thước phần dữ liệu (payload) là 1200 byte bị phân thành 3 mảnh có giá trị Fragment Offset lần lượt là 0, 69, 138. Phần dữ liệu trong các mảnh này có kích thước lần lượt là bao nhiêu byte?
A. 0, 69, 138
B. 400, 400, 400
C. 50, 50, 50
D. 552, 552, 96
E. 96, 552, 552
ans: D [suy luận]
```

----- Page 20 -----
```md
Câu 100: Phát biểu nào sau đây là đúng đối với gói tin IP có địa chỉ đích là 255.255.255.255?
A. Được sử dụng để thiết lập liên kết
B. Được ưu tiên đưa vào hàng đợi của router khi chờ chuyển tiếp
C. Được chuyển tới mọi nút trong miền quảng bá
D. Được sử dụng để thông báo có đụng độ xảy ra trong mạng điểm-đa điểm
E. Được chuyển ngay ra ngoài mạng Internet mà không cần chuyển đổi địa chỉ
ans: C [suy luận]

Câu 101: Phát biểu nào sau đây là đúng về định tuyến theo vec-tơ khoảng cách?
A. Mỗi nút thu thập thông tin định tuyến từ tất cả các nút trong mạng
B. Cho phép tìm đường đi ngắn nhất giữa mọi cặp nút
C. Để tránh lỗi lặp vô hạn, các nút trao đổi toàn bộ vec-tơ khoảng cách với nhau
D. Chuyển tiếp các vec-tơ khoảng cách nhận được từ hàng xóm ra các cổng khác
E. Tốc độ hội tụ không phụ thuộc vào số liên kết giữa các nút
ans: D [suy luận]

Câu 102: Định tuyến theo vec-tơ khoảng cách hoạt động như thế nào? (Chọn 2 đáp án)
A. Trao đổi thông tin vec-tơ khoảng cách với các bộ định tuyến hàng xóm
B. Lan truyền thông tin vec-tơ khoảng cách nhận được tới các bộ định tuyến khác
C. Tính toán và cập nhật đường đi mỗi khi nhận được vec-tơ khoảng cách
D. Xây dựng sơ đồ mạng từ các vec-tơ khoảng cách nhận được
ans: A,C [suy luận]

Câu 103: Tốc độ hội tụ của định tuyến theo vector khoảng cách phụ thuộc vào các yếu tố nào? (Chọn 2 đáp án)
A. Số lượng nút định tuyến
B. Số kết nối giữa các nút định tuyến
C. Băng thông đường truyền
D. Độ trễ
E. Độ mất mát gói tin
ans: A,B [suy luận]

Câu 104: Phát biểu nào sau đây là SAI về định tuyến theo trạng thái liên kết?
A. Thông tin trạng thái liên kết được lan truyền cho tất cả các nút trong mạng
B. Sử dụng thuật toán Bellman-Ford để tìm đường đi ngắn nhất
C. Mỗi nút tự xây dựng hình trạng (topology) của mạng
D. Số lượng bản tin trao đổi tăng nhanh theo số liên kết trong mạng
ans: B [suy luận]

Câu 105: Giao thức định tuyến theo trạng thái liên kết không thực hiện hoạt động nào sau đây?
A. Quảng bá thông tin trạng thái liên kết trên mạng
B. Thu thập thông tin đường đi từ hàng xóm
C. Xây dựng topology của mạng
ans: B [suy luận]
```

----- Page 21 -----
```md
Câu 106: Trong một mạng sử dụng định tuyến theo trạng thái liên kết, router A thu thập được các thông tin liên kết dạng (link, cost) sau: (BA, 8), (CA, 1), (BC, 1), (CB, 1), (BD, 15), (DB, 15). Những đường đi nào dưới đây là đường đi ngắn nhất? (Chọn 2 đáp án)
A. A→B
B. A→C→B
C. A→B→D
D. A→C→B→D
ans: B,D

Câu 107: Trong một mạng sử dụng định tuyến theo vec-tơ khoảng cách, router A có các hàng xóm là B, C, D với khoảng cách lần lượt là 3, 5, 3. Giả sử A nhận được thông tin đường đi dạng (đích đến, chi phí) từ B là (C, 1) và (E, 5), từ C là (D, 8) và (E, 4), từ D là (E, 4) và (C, 8). Đường đi nào sau đây KHÔNG phải là đường đi mà A lựa chọn?
A. (B, 3)
B. (C, 4)
C. (D, 3)
D. (E, 8)
ans: D

Câu 108: Giao thức định tuyến nào được sử dụng để tìm đường đi giữa các vùng tự trị (AS – Autonomous System)?
A. RIP
B. OSPF
C. IGRP
D. EIGRP
E. BGP
ans: E

Câu 109: Giao thức nào sau đây không nằm cùng nhóm với các giao thức còn lại?
A. OSPF
B. RIP
C. IGRP
D. EIGRP
E. BGP
ans: E

Câu 110: Phát biểu nào sau đây là SAI về giao thức định tuyến OSPF?
A. Thông tin trạng thái liên kết của một nút được lan truyền tới tất cả các nút trong miền
B. Có cơ chế định tuyến phân cấp
C. Sử dụng thuật toán Bellman-Ford để tìm đường đi ngắn nhất
D. Mỗi nút tự xây dựng hình trạng (topology) của toàn mạng
E. Tìm đường đi ngắn nhất từ một nút tới các nút khác
ans: C
```

----- Page 22 -----
```md
Câu 111: Phát biểu nào sau đây là SAI về giao thức OSPF?
A. Là giao thức định tuyến theo vec-tơ khoảng cách
B. Được thực hiện trên các bộ định tuyến (router)
C. Là giao thức định tuyến nội vùng
D. Hỗ trợ định tuyến phân cấp
ans: A [suy luận]

Câu 112: Giao thức định tuyến RIPv2 tính chi phí đường đi dựa trên thông số nào?
A. Băng thông
B. Số chặng (hop)
C. Độ trễ
D. Tải
ans: B [suy luận]

Câu 113: Giao thức định tuyến nào phù hợp để cài đặt cho các router trong vùng tự trị (AS) có 40 router?
A. RIPv1
B. RIPv2
C. OSPF
D. BGP
E. Tất cả các giao thức trên
ans: C [suy luận]

Câu 114: Ưu thế của giao thức định tuyến RIP so với OSPF là gì?
A. Đơn giản hơn khi thực hiện cập nhật bảng định tuyến
B. Tốc độ hội tụ nhanh hơn
C. Tiết kiệm băng thông
D. Triển khai trên mạng có số lượng nút định tuyến lớn
ans: A [suy luận]
```

----- Page 23 -----
```md
Câu 115: Cho đồ thị mô hình hóa một hệ thống mạng, trong đó mỗi đỉnh là một router và mỗi liên kết có chi phí như hình vẽ dưới đây. Hãy trả lời các câu hỏi sau:
img: assets/cau61-graph.png
Nếu các router cài đặt giao thức định tuyến OSPF thì tuyến đường ngắn nhất từ A tới E là gì?
A. (A, B, D, E)
B. (A, C, D, E)
C. (A, C, E)
D. (A, B, C, D, E)
ans: [không chắc]

Câu 116: Nếu các router cài đặt giao thức định tuyến RIP thì tuyến đường ngắn nhất từ A tới E là gì?
img: assets/cau61-graph.png
A. (A, B, D, E)
B. (A, C, D, E)
C. (A, C, E)
D. (A, B, C, D, E)
ans: C

Câu 117: Giao thức BGP thực hiện chức năng nào?
A. Điều khiển truyền dữ liệu giữa các tiến trình trên hệ thống cuối
B. Thiết lập kênh trong mạng chuyển mạch kênh
C. Định tuyến giữa các vùng tự trị (Autonomous System) trên Internet
D. Điều khiển truy nhập đường truyền trong mạng đa truy nhập
ans: C

Câu 118: Có thể cài đặt giao thức định tuyến nào sau đây trên router để tìm đường đi tới mạng 108.21.16.0 /20 nằm trong vùng tự trị (AS) của router đó?
A. RIPv1
B. RIPv2
C. OSPF
D. BGP
ans: B,C [suy luận]

Câu 119: Phát biểu nào sau đây là SAI về giao thức định tuyến BGP?
A. Là giao thức định tuyến giữa các AS (Autonomous System)
B. Phiên eBGP thực hiện giữa các router cùng một AS
C. Các thông điệp của phiên iBGP được định tuyến bởi các giao thức định tuyến nội vùng
D. Hai phiên iBGP và eBGP sử dụng giao thức giống nhau
ans: B

Câu 120: Phát biểu nào sau đây là SAI về giao thức BGP?
A. Được cài đặt trên tất cả các bộ định tuyến trong AS
B. Tìm đường đi tới các AS
C. Truyền thông tin định tuyến giữa các bộ định tuyến qua liên kết TCP
D. Sử dụng thuật toán định tuyến vec-tơ đường đi (path-vector)
ans: A

Câu 121: Tầng liên kết dữ liệu không thực hiện chức năng nào?
A. Đồng bộ tốc độ truyền dữ liệu giữa 2 nút mạng trên liên kết
B. Biểu diễn các bit thành tín hiệu
C. Kiểm soát lỗi
D. Điều khiển truy nhập đường truyền
ans: B
```

----- Page 24 -----
```md
Câu 122: Trong hình trạng (topology) mạng nào sau đây, sự cố xảy ra trên đường truyền vật lý có thể cản trở đến quá trình truyền dữ liệu toàn bộ mạng?
A. Hình trục
B. Hình sao
C. Hình vòng
D. Hình lưới
ans: A,C [suy luận]

Câu 123: Mạng nào sau đây là mạng điểm-điểm (point-to-point)?
A. Mạng hình trục (bus)
B. Mạng hình sao (star) sử dụng bộ chia mạng (hub)
C. Mạng hình sao sử dụng bộ định tuyến (router)
D. Cả 3 mạng trên
ans: C [suy luận]

Câu 124: Mạng nào sau đây thực hiện lan truyền tín hiệu theo phương thức điểm-đa điểm?
A. Mạng hình trục (bus)
B. Mạng hình sao (star) sử dụng hub
C. Mạng hình sao (star) sử dụng switch
D. Mạng LAN không dây sử dụng chuẩn IEEE802.11
E. Mạng hình sao (star) sử dụng router
ans: A,B,D [suy luận]

Câu 125: Mạng nào sau đây thực hiện lan truyền tín hiệu theo phương thức điểm-đa điểm?
A. Mạng hình trục (bus)
B. Mạng hình sao (star) sử dụng hub
C. Mạng hình sao (star) sử dụng switch
D. Mạng LAN không dây sử dụng chuẩn IEEE802.11
E. Mạng hình vòng (ring)
ans: A,B,D [suy luận]

Câu 126: Các phương pháp điều khiển truy nhập đường truyền nào sau đây thuộc nhóm phương pháp điều khiển ngẫu nhiên? (Chọn 3 đáp án)
A. CSMA
B. TDMA
C. FDMA
D. CDMA
E. Slotted Aloha
F. Token Passing
ans: A,E [suy luận] [không chắc]

Câu 127: Xác suất xảy ra đụng độ trong phương pháp điều khiển truy nhập đường truyền nào sau đây là cao nhất?
A. Pure Aloha
B. Slotted Aloha
C. CSMA/CA
D. CSMA/CD
E. Token passing
ans: A
```

----- Page 25 -----
```md
Câu 128: Phương pháp điều khiển truy nhập đường truyền nào dưới đây không nằm cùng nhóm với các phương pháp khác?
A. Pure Aloha
B. Slotted Aloha
C. CSMA/CD
D. Token Passing
ans: D [suy luận]

Câu 129: Phương pháp điều khiển truy nhập đường truyền nào dưới đây không nằm cùng nhóm với các phương pháp khác?
A. FDMA
B. CDMA
C. CSMA
D. TDMA
ans: C [suy luận]

Câu 130: Phát biểu nào sau đây là đúng về phương pháp điều khiển truy nhập đường truyền Pure Aloha?
A. Thuộc nhóm phương pháp điều khiển truy nhập ngẫu nhiên
B. Kiểm tra trạng thái đường truyền trước khi gửi dữ liệu
C. Đồng bộ thời gian giữa các nút
D. Truyền nhiều khung tin nhất có thể trong một khung thời gian (frame time)
ans: A

Câu 131: Phát biểu nào sau đây là sai trong hoạt động của phương pháp điều khiển truy nhập đường truyền Slotted Aloha? (Chọn 2 đáp án)
A. Đồng bộ thời gian giữa các nút mạng
B. Mỗi nút mạng được phép truyền trong khe thời gian dành riêng cho nút mạng đó
C. Truyền dữ liệu ngay khi cần
D. Phát hiện đụng độ và thông báo cho các nút trong mạng
ans: B,D [suy luận]

Câu 132: Điều gì làm cho phương pháp điều khiển truy nhập Slotted Aloha có hiệu quả cao hơn Pure Aloha?
A. Kiểm tra trạng thái đường truyền trước khi đưa dữ liệu lên
B. Thiết lập mức ưu tiên truyền của các nút
C. Đồng bộ thời gian giữa các nút
D. Truyền nhiều hơn một khung tin trong một khe thời gian (frame time)
ans: C [suy luận]
```

----- Page 26 -----
```md
Câu 133: Đặc điểm nào trong hoạt động của các giao thức điều khiển truy cập đường truyền Pure Aloha làm cho nó có hiệu quả thấp hơn hơn so với SlottedAloha?
A. Truyền dữ liệu ngay khi có thể mà không kiểm tra trạng thái đường truyền
B. Chỉ gửi 1 gói tin trong mỗi frame-time
C. Không đồng bộ thời gian giữa các nút
D. Không kiểm tra trạng thái đường truyền trước khi truyền
E. Không thiết lập thứ tự truy cập đường truyền giữa các nút
ans: C [suy luận]

Câu 134: Phương pháp điều khiển truy nhập đường truyền CSMA/CD thực hiện như thế nào? (Chọn 3 đáp án)
A. Cảm nhận năng lượng sóng mang trên đường truyền trước khi truyền
B. Cảm nhận năng lượng sóng mang khi truyền khung tin đầu tiên để phát hiện đụng độ
C. Duy trì việc phát tín hiệu báo đụng độ trên đường truyền trong một khoảng thời gian để tất cả nút mạng khác cảm nhận được
D. Thiết lập độ ưu tiên truy nhập đường truyền cho các nút mạng
ans: A,B,C [suy luận]

Câu 135: Trong hoạt động của phương pháp điều khiển truy nhập đường truyền CSMA/CD, nút mạng không thực hiện những thao tác nào?
A. Kiểm tra sự có mặt của tín hiệu sóng mang trên đường truyền
B. Kiểm tra đụng độ trong quá trình truyền
C. Phát tin hiệu JAM để duy trì đụng độ
D. Chờ đụng độ được vãn hồi trong khoảng thời gian nào đó
E. Sau khi đụng độ được vãn hồi, truyền lại ngay mà không cần kiểm tra trạng thái đường truyền
ans: E [suy luận]

Câu 136: Phát biểu nào sau đây là đúng về thẻ bài trong phương pháp truy nhập đường truyền Token Passing? (Chọn 2 đáp án)
A. Thẻ bài được luân chuyển tuần tự qua các nút mạng
B. Mỗi nút mạng được phép sử dụng thẻ bài trong một khe thời gian xác định
C. Thẻ bài được sử dụng để phát hiện đụng độ trong mạng
D. Cho phép thiết lập mức độ ưu tiên truyền dữ liệu
E. Là một gói tin có khuôn dạng và kích thước xác định
ans: A,E [suy luận]

Câu 137: Trong các mô tả sau về hoạt động của giao thức điều khiển truy nhập đường truyền Token Passing, câu nào là SAI? (Chọn 2 đáp án)
A. Chỉ tồn tại duy nhất một thẻ bài trong mạng để xác định quyền đưa dữ liệu lên đường truyền.
B. Một nút mạng muốn truyền dữ liệu nó phải đợi cho tới khi nhận được thẻ bài có trạng thái rỗi.
C. Khi kết thúc truyền dữ liệu, nút nguồn sẽ gửi thông báo để nút đích xác lập trạng thái cho thẻ bài là rỗi.
D. Sau khi truyền xong dữ liệu, nút mạng sẽ trả thẻ bài về cho trung tâm phân phối thẻ bài
ans: C,D [suy luận]
```

----- Page 27 -----
```md
Câu 138: Khi điều khiển truy nhập đường truyền, ưu thế của phương pháp sử dụng thẻ bài (Token Passing) so với điều khiển ngẫu nhiên là gì?
A. Xác suất đụng độ thấp hơn
B. Đơn giản hơn
C. Hiệu suất sử dụng đường truyền cao hơn
D. Cả 3 đáp án trên
ans: A [suy luận]

Câu 139: Ưu điểm của phương pháp CSMA/CD so với Token Passing là gì?
A. Đơn giản hơn
B. Xác suất đụng độ thấp hơn
C. Có cơ chế thiết lập thứ tự ưu tiên truyền
D. Có cơ chế phát hiện và vãn hồi đụng độ
E. Tất cả các đáp án trên
ans: A,D [suy luận]

Câu 140: Điểm khác biệt của chuyển tiếp dữ liệu ở tầng 2 trên switch so với chuyển tiếp ở tầng 3 trên router là gì?(Chọn 2 đáp án)
A. Không cần giao thức xác định trước đường đi
B. Không cần bảng chuyển tiếp
C. Nút đích phải cùng một mạng với nút nguồn
D. Các gói tin được xử lý độc lập
E. Không quảng bá dữ liệu có địa chỉ đích là địa chỉ quảng bá
ans: A,C [suy luận]

Câu 141: Khi nhận được một khung tin, switch có thể thực hiện những thao tác xử lý nào ? (Chọn 3 đáp án)
A. Tìm kiếm cổng ra trên bảng chuyển tiếp theo địa chỉ đích
B. Phân mảnh khung tin
C. Bổ sung địa chỉ nguồn vào bảng chuyển tiếp nếu chưa biết
D. Quảng bá khung tin nếu chưa biết địa chỉ đích
ans: A,C,D [suy luận]

Câu 142: Switch xây dựng bảng MAC Table như thế nào?
A. Nếu chưa biết địa chỉ nguồn trên khung tin, thêm vào bảng MAC Table
B. Nếu chưa biết địa chỉ đích trên khung tin, thêm vào bảng MAC Table
C. Quảng bá một thông điệp tìm kiếm địa chỉ các nút mạng, bổ sung thông tin từ thông điệp trả lời vào bảng MAC Table
D. Sử dụng bảng MAC Table từ các switch khác gửi tới
ans: A [suy luận]
```

----- Page 28 -----
```md
Câu 143: Switch thực hiện những thao tác xử lý nào khi nhận được một khung tin có địa chỉ đích là A1-B2-C3-D4-E5-F6?(Chọn 2 đáp án)
A. Tìm cổng tương ứng trong bảng MAC Table và chuyển khung tin ra cổng đó nếu tìm thấy
B. Bổ sung địa chỉ này vào bảng MAC Table nếu trong bảng chưa có
C. Kiểm tra lỗi trên khung tin
D. Chuyển ngay khung tin ra tất cả các cổng trừ cổng nhận khung tin
E. Hủy khung tin và báo lỗi vì địa chỉ này không hợp lệ.
ans: A,D [suy luận]

Câu 144: Switch hoạt động ở chế độ chuyển tiếp "store and forward" thực hiện những thao tác xử lý nào khi nhận được khung tin có địa chỉ MAC đích là FF-FF-FF-FF-FF?(Chọn 2 đáp án)
A. Tìm cổng tương ứng trong bảng Switching Table và chuyển khung tin ra cổng đó nếu tìm thấy.
B. Bổ sung địa chỉ này vào bảng Switching Table nếu trong bảng chưa có
C. Kiểm tra lỗi trên khung tin
D. Chuyển khung tin ra tất cả các cổng trừ cổng nhận khung tin
E. Hủy khung tin và báo lỗi vì địa chỉ này không hợp lệ.
ans: C,D [suy luận]

Câu 145: Khi một nút mạng nhận được yêu cầu gửi gói tin tới một nút khác cùng mạng, nếu chưa biết địa chỉ MAC của nút đích, nó sẽ thực hiện như thế nào?
A. Gửi gói tin tới gateway mặc định
B. Gửi gói tin với địa chỉ quảng bá
C. Gửi thông điệp ARP Request tìm kiếm địa chỉ MAC của nút đích
D. Từ chối yêu cầu gửi dữ liệu và báo lỗi
ans: C [suy luận]

Câu 146: Giao thức ARP(Address Resolution Protocol) thực hiện chức năng nào?
A. Chuyển đổi giữa địa chỉ IP cục bộ và địa chỉ IP công cộng
B. Tìm kiếm địa chỉ MAC khi biết địa chỉ IP
C. Tìm kiếm địa chỉ IP khi biết địa chỉ MAC
D. Tìm kiếm địa chỉ mạng của một mạng
ans: B [suy luận]

Câu 147: Mô tả nào sau đây là đúng về địa chỉ MAC?(Chọn 2 đáp án)
A. Có 32 bit giá trị
B. Sử dụng giá trị duy nhất làm địa chỉ quảng bá là FF-FF-FF-FF-FF-FF
C. Địa chỉ MAC của nút mạng thay đổi một cách định kỳ
D. Địa chỉ MAC của các nút mạng được cấp phát tự động bởi dịch vụ DHCP
E. Được sử dụng để định danh tại tầng liên kết dữ liệu
ans: B,E [suy luận]

Câu 148: Phát biểu nào sau đây là đúng về địa chỉ MAC?(Chọn 2 đáp án)
A. Là giá trị định danh cho nút mạng tại tầng liên kết dữ liệu
B. Thay đổi tùy thuộc theo địa chỉ của mạng mà nút mạng đang kết nối
C. Có kích thước 32 bit
D. Có thể cấp phát bởi dịch vụ DHCP
ans: A [suy luận]
```

----- Page 29 -----
```md
Câu 149: Phát biểu nào sau đây là sai về chuẩn Ethernet 1000-BASE-T?
A. Sử dụng cáp xoắn đôi
B. Điều khiển truy nhập đường truyền bằng phương pháp CSMA/CD
C. Khoảng cách kết nối tối đa là 1000 mét
D. Tốc độ truyền tối đa là 1 Gbps
ans: C [suy luận]

Câu 150: Loại mã phát hiện lỗi nào sau đây cho phép phát hiện nhiều vị trí lỗi nhất trên gói dữ liệu?
A. Parity
B. Checksum
C. CRC-16
D. CRC-32
ans: D [suy luận]

Câu 151: Chuẩn nào sau đây dùng cho mạng LAN không dây (WLAN)?
A. IEEE 802.3
B. IEEE 802.5
C. IEEE 802.11
D. IEEE 802.13
ans: C [suy luận]

Câu 152: Các chuẩn Fast Ethernet có tốc độ truyền tin tối đa là bao nhiêu?
A. 10 Mbps
B. 100 Mbps
C. 10 Gbps
D. 1 Gbps
E. 54 Mbps
ans: B [suy luận]

Câu 153: Những mô tả nào sau đây là đúng với chuẩn Ethernet 1000BASE-T? (Chọn 3 đáp án)
A. Mạng dùng cáp xoắn đôi
B. Khoảng cách truyền dẫn tối đa là 1000m
C. Phù hợp với mọi hình trạng mạng
D. Điều khiển truy nhập đường truyền bằng CSMA/CD
E. Sử dụng đầu nối RJ-45
ans: A,D,E [suy luận]

Câu 154: Chuẩn nào sau đây là chuẩn Fast Ethernet? (Chọn 2 đáp án)
A. 10BASE-2
B. 10BASE-5
C. 100BASE-T
D. 100BASE-F
E. 1000BASE-T
F. 1000BASE-CX
ans: C,D [suy luận]
```


----- Page 30 -----
```md
Câu 155: Cáp xoắn đôi được sử dụng trong các chuẩn mạng nào dưới đây?
A. 10BASE2
B. 10BASE5
C. 100BASE-T
D. 100BASE-FX
E. IEEE 802.11n
ans: C [suy luận]

Câu 156: Phương pháp mã hóa nào sau đây sử dụng để điều chế dữ liệu số-tín hiệu số? (Chọn 2 đáp án)
A. Mã parity
B. Mã checksum
C. Mã vòng CRC
D. Mã NRZ
E. Mã Manchester
ans: D,E [suy luận]

Câu 157: Phát biểu nào sau đây là đúng về mã Manchester?
A. Được sử dụng tại tầng vật lý
B. Bit 1 được biểu diễn luân phiên bởi các xung âm và xung dương
C. Chuyển về mức điện áp 0 ở giữa xung
D. Thay thế chuỗi các bit 0 liên tiếp bằng mẫu bit đặc biệt để tránh mất đồng bộ
ans: A [suy luận]

Câu 158: Mã chống nhiễu nào sau đây có thể phát hiện được nhiều lỗi nhất?
A. Mã parity chẵn
B. Mã parity lẻ
C. Mã checksum
D. Mã CRC-16
E. Mã CRC-32
ans: E [suy luận]

Câu 159: Phương pháp mã hóa Manchester có thể được sử dụng tại tầng nào trong mô hình OSI?
A. Tầng ứng dụng
B. Tầng giao vận
C. Tầng liên kết dữ liệu
D. Tầng vật lý
ans: D [suy luận]
```
