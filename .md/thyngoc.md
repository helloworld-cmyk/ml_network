----- Page 1 -----
```md
Câu 1: Khẳng định nào sau đây là sai về Hệ tự trị (AS) trong định tuyến?
A. Chính sách định tuyến chung được áp dụng ở cùng một AS
B. Các giao thức định tuyến cục bộ được dùng bên trong các AS
C. Các giao thức định tuyến liên vùng được dùng để kết nối các AS với nhau
D. Số lượng các AS là cố định
ans: D

Câu 2: Mục đích của DHCP là gì (Dynamic Host Configuration Protocol)?
A. Cho phép gán địa chỉ IP động từ server mạng khi một máy tính gia nhập một mạng
B. Chuyển giao địa chỉ IP giữa các máy tính
C. Cấu hình bảng định tuyến của các máy tính
D. Cấu hình máy tính qua đường kết nối từ xa
ans: A

Câu 3: Trong các khẳng định sau về VLAN (Virtual LAN), khẳng định nào là sai?
A. VLAN cho phép gom nhóm, quản lý các máy tính về mặt logic thay vì vị trí địa lý từng máy
B. VLAN cho phép giảm bớt lưu lượng trong mạng LAN nhờ giảm số khung tin quảng bá trong mạng
C. VLAN giúp giảm độ phức tạp và giá thành vận hành mạng
D. VLAN cho phép tăng tính bảo mật mạng nhờ có thể phân quyền người dùng theo nhóm, phân vùng
ans: C [suy luận]

Câu 4: Trong các khẳng định sau về cơ chế cập nhật bảng chuyển tiếp và chuyển tiếp gói tin của Switch sau, khẳng định nào là SAI? **(2 đáp án)**
A. Việc cập nhật bảng chuyển tiếp dựa vào thuật toán tìm đường đi với chi phí nhỏ nhất
B. Khi một khung tin đến Switch mà địa chỉ MAC đích chưa có trong bảng chuyển tiếp, khung tin đó LUÔN LUÔN được quảng bá ra tất cả các cổng còn lại (trừ cổng đến)
C. Khi một khung tin đến Switch mà bảng chuyển tiếp địa chỉ MAC nguồn có cổng khác với cổng mà khung tin đến thì Switch cập nhật lại cổng ứng với địa chỉ đích
D. Khi một khung tin đến Switch mà địa chỉ MAC nguồn chưa có trong bảng chuyển tiếp mà khung tin đến thì Switch cập nhật lại cổng ứng với địa chỉ đích
E. Khi một khung tin đến Switch mà địa chỉ MAC máy đích khớp với nhiều dòng trong bảng chuyển tiếp của Switch, Switch chọn dòng ứng với đường truyền có băng thông lớn hơn.
ans: A,E [suy luận]

Câu 5: Hai vai trò chính của chức năng điều khiển truy nhập của tầng liên kết dữ liệu là gì? **(2 đáp án đúng)**
A. Cho phép máy tính gia nhập vào mạng
B. Xác định cách các nút mạng chia sẻ đường truyền
C. Giao tiếp để chia sẻ đường truyền
D. Cho phép máy tính kết nối với mạng Internet
ans: B,C

Câu 6: Trong các khẳng định sau về định tuyến dạng distance-vector, khẳng định nào là ĐÚNG?
A. Mỗi router có đầy đủ thông tin về các kết nối trong mạng để dựng nên đồ thị mạng.
B. Tốc độ hội tụ khi có sự thay đổi trong mạng nhanh
C. Giao thức định tuyến dạng distance-vector thường phù hợp với các mạng cỡ nhỏ
D. Các khẳng định khác đều sai.
ans: C [suy luận]

Câu 7: Một mạng sử dụng mã parity chẵn để phát hiện lỗi gây ra bởi quá trình truyền dữ liệu. Dữ liệu cần gửi đi là 1001 1100, mã parity được dùng là gì?
A. 0
B. 01
C. 1
D. 11
ans: A

Câu 8: Một gói dữ liệu (1011 1000 0011 1100) được gửi sử dụng mã CRC. Biết rằng G = 10011, tính mã CRC được đính kèm vào gói tin ban đầu.
A. 1100
B. 1001
C. 0110
D. 1011
E. 0011
F. None of the mentioned
ans: A

Câu 9: Trong các khẳng định sau về giao thức định tuyến RIP (Routing Information Protocol), khẳng định nào là SAI?
A. Sử dụng giải thuật Link-state
B. Đơn vị chi phí được tính mặc định dựa vào số máy đã đi qua (hop count).
C. RIP phù hợp với các mạng cỡ nhỏ
D. Định kỳ kiểm tra trạng thái các router hàng xóm thông qua chính các gói tin cập nhật bảng vector khoảng cách
ans: A

Câu 10: Trong các khẳng định sau đây về trường TTL trong gói tin IP, khẳng định nào là SAI?
A. Khi trường TTL giảm về 0, router sẽ hủy bỏ thay vì chuyển tiếp gói tin.
B. Mục đích của trường TTL là ngăn chặn việc gói tin IP có thể bị lặp vòng trong mạng
C. Trường TTL giảm 1 đơn vị khi đi qua 1 router
D. Trường TTL được trả về từ lệnh ping là số giây từ khi gửi gói tin đến khi nhận được gói tin phản hồi
ans: D

Câu 11: Cho một đường liên kết mạng có băng thông R = 25 Mbps. Nếu việc định tuyến qua đoạn mạng này sử dụng giao thức định tuyến OSPF thì chi phí giá mặc định trên đoạn mạng này là bao nhiêu?
A. 1
B. 4
C. 25
D. 10
ans: B

Câu 12: Trong các khẳng định sau về việc định tuyến liên vùng giữa các mạng khác nhau, khẳng định nào là ĐÚNG?
A. Giao thức định tuyến BGP dựa trên thuật toán dạng link-state.
B. Định tuyến BGP giữa các miền tự trị (AS) ưu tiên hiệu năng hơn chính sách
C. Tại các router biên kết nối giữa các miền tự trị (AS) với nhau có 2 bảng định tuyến, một cho định tuyến nội vùng, một cho định tuyến liên vùng
D. Việc quảng bá thông tin định tuyến liên vùng hay không chủ yếu dựa vào chính sách của từng vùng tự trị
ans: D [suy luận]

Câu 13: Khi mạng xảy ra tình trạng tắc nghẽn (congestion) trên mạng sẽ khiến độ trễ nào tăng lên?
A. Trễ lan truyền (Propagation delay)
B. Trễ truyền tin (Transmission delay)
C. Trễ xử lý (Processing delay)
D. Trễ hàng đợi (Queuing delay)
ans: D

Câu 14: Với một đường truyền mạng có tỷ lệ lỗi bit (BER) không đổi, khi kích thước gói tin tăng lên thì ....
A. Tỷ lệ lỗi gói tin tăng lên (Packet error rate increases)
B. Tỷ lệ lỗi gói tin không đổi
C. Tỷ lệ lỗi gói tin giảm đi
D. Chưa thể khẳng định được tỷ lệ lỗi gói tin tăng, giảm hay không đổi.
ans: A

Câu 15: Trong mô hình OSI, chức năng định tuyến được thực hiện ở tầng nào?
A. Network Layer
B. Transport layer
C. Datalink Layer
D. Application Layer
ans: A

Câu 16: Địa chỉ Ethernet gồm bao nhiêu bit?
A. 64 bits
B. 48 bits
C. 16 bits
D. 32 bits
ans: B

Câu 17: Mô hình TCP/IP có bao nhiêu tầng?
A. 4
B. 6
C. 5
D. 7
ans: A

Câu 18: (Những) cơ chế nào giúp cho giao thức các tầng khác nhau giữa máy gửi và máy nhận trong mô hình kiến trúc phân tầng của TCP/IP có thể hoạt động với nhau nhưng không ảnh hưởng đến dữ liệu các tầng khác? **(2 đáp án đúng)**
A. Đóng gói (Encapsulation)
B. Tháo gói (Decapsulation)
C. [không rõ trong ảnh — bị cắt ở cuối trang]
D. [không rõ trong ảnh — bị cắt ở cuối trang]
ans: A,B [không chắc] [câu bị cắt - thiếu phần cuối]
```

----- Page 2 -----
```md
Câu 19: Thiết bị nào sau đây không sử dụng cho mạng LAN?
A. Cổng kết nối mạng (NIC)
B. Máy tính
C. Cáp nối
D. Modem
ans: D

Câu 20: Cho một đường truyền sử dụng mã hóa Manchester vi sai có tốc độ truyền dữ liệu là 100.000 bit/s. Hỏi tốc độ baud của đường truyền này là:
A. 50.000 baud
B. 200.000 baud
C. 100.000 baud
D. Không xác định được
ans: B

Câu 21: Trong các mạng được mô tả dưới đây, mạng nào kết nối dưới dạng điểm - đa điểm? **(3 đáp án đúng)**
A. Một điện thoại thông minh kết nối với nhiều thiết bị ngoại vi qua Bluetooth
B. Các máy tính để bàn kết nối với nhau qua một switch trung gian
C. Các máy tính để bàn kết nối với nhau qua một hub trung gian
D. Các máy tính kết nối với nhau qua mạng WLAN
E. Các máy tính kết nối với nhau dưới dạng Token Ring
ans: A,C,D [suy luận]

Câu 22: Nhược điểm của cáp quang khi so sánh với cáp xoắn đôi và cáp đồng trục là gì? **(2 đáp án đúng)**
A. Giá thành đắt đỏ khi sử dụng cho mạng LAN
B. Dễ hư hỏng hơn
C. Băng thông truyền tải thấp hơn
D. Có kích thước và trọng lượng lớn hơn
E. Dễ bị ảnh hưởng bởi sóng điện từ
ans: A,B [suy luận]

Câu 23: Cho một mạng với địa chỉ IP như sau: 200.23.0.0/22. Địa chỉ nào sau đây không thuộc về mạng đã cho?
A. 200.23.2.1
B. 200.23.1.1
C. 200.23.3.1
D. 200.23.4.1
ans: D

Câu 24: Trong truyền tin sử dụng CSMA/CA để truy cập đường truyền chia sẻ, vì sao đụng độ vẫn xảy ra dù các máy đã lắng nghe (đảm bảo không có máy đang truyền dữ liệu) trước khi truyền?
A. Do độ trễ lan truyền nên 2 máy phát tín hiệu đồng thời không nhận ra tín hiệu của nhau
B. Do các máy có thể phát tín hiệu trên các tần số khác nhau
C. Khi mạng tắc nghẽn có thể ảnh hưởng đến việc nhận diện tín hiệu truyền dữ liệu
D. Tất cả các đáp án khác đều đúng.
ans: A

Câu 25: Cho một mạng có đường truyền chia sẻ gồm 10 máy. Khả năng mỗi máy có nhu cầu truyền dữ liệu tại 1 thời điểm là 80%. Hãy lựa chọn kỹ thuật truy cập đường truyền phù hợp nhất trong các đáp án sau
A. Aloha
B. CSMA/CD
C. Slotted Aloha
D. TDMA
ans: D [suy luận]

Câu 26: Trong mạng không dây ad-hoc,
A. Cần có AP
B. Mọi nút đều là AP
C. Các máy tính không cần thiết
D. AP không cần thiết
ans: D

Câu 27: Kỹ thuật truy cập đường truyền nào được dùng trong chuẩn mạng LAN không dây 802.11?
A. CDMA
B. CSMA/CA
C. CSMA/CD
D. ALOHA
ans: B

Câu 28: Trường nào trong gói tin IP được dùng để sắp xếp lại các phân mảnh khi truyền tin?
A. Flag
B. TTL
C. Identifier
D. Offset
ans: D

Câu 29: Những thiết bị nào dưới đây hoạt động chủ yếu ở tầng liên kết dữ liệu? **(Có thể có nhiều phương án đúng)**
A. Repeater
B. Hub
C. Router
D. Switch
E. Bridge
F. Máy tính cá nhân
ans: D,E

Câu 30: Giả sử đường truyền từ A đến B đi qua 3 đường liên kết với băng thông lần lượt là 4Mbps, 1Mbps, và 2 Mbps. Nếu các đường kết nối này chỉ phục vụ đường truyền từ A đến B, coi trễ lan truyền bằng 0, thì mất bao nhiêu giây để A truyền một file 20 MB đến B?
A. 140
B. 320
C. 40
D. 160
E. 80
F. 200
ans: D

Câu 31: Chuyện gì xảy ra nếu MTU của một kết nối mạng quá nhỏ?
A. Làm tăng tỷ lệ lỗi
B. Làm giảm hiệu suất truyền dữ liệu do phần đầu gói tin có kích thước cố định
C. Tăng tắc nghẽn mạng bởi vì số lượng gói tin
D. Giảm băng thông của kết nối mạng
ans: B

Câu 32: Mạng máy tính đầu tiên có tên gọi là
A. CNNET
B. NSFNET
C. ASAPNET
D. ARPANET
ans: D

Câu 33: Mạng nào sau đây sử dụng đường dây điện thoại?
A. WAN
B. LAN
C. Wireless
D. WWAN
ans: A

Câu 34: Switch là thiết bị mạng gắn với dạng mạng là ...
A. Bus
B. Ring
C. Star
D. Mesh
ans: C

Câu 35: Đơn vị đo thông lượng nào dưới đây cho tốc độ nhanh nhất?
A. bps
B. Mbps
C. Kbps
D. Gbps
ans: D

Câu 36: Nhược điểm của chuyển mạch kênh là gì? **(3 đáp án đúng)**
A. Đảm bảo chất lượng dịch vụ kém hơn chuyển mạch gói
B. Hiệu suất truyền thấp khi tỷ lệ truyền dữ liệu thấp sau khi thiết lập liên kết
C. Hiệu suất truyền thấp khi lượng dữ liệu truyền nhỏ do phải thiết lập và hủy liên kết khi truyền dữ liệu
D. Khi một thiết bị chuyển mạch bị lỗi phải bắt đầu lại quá trình thiết lập kênh truyền
E. Trễ khi chuyển mạch cao
ans: B,C,D [suy luận]

Cho bảng chuyển tiếp MAC của một switch như sau:

| Host | Interface |
|:-----|:---------:|
| 12-12-12-ab-ab-ab | e1 |
| 11-11-11-dd-dd-dd | e2 |
| 33-33-33-ee-ee-ee | e3 |
| 55-55-55-cc-cc-cc | e4 |

Câu 37: Khi switch nhận được khung tin với địa chỉ đích là 12-12-12-ab-ab-ab và địa chỉ nguồn là 11-11-11-dd-dd-dd đến từ cổng e3.
A. Hủy khung tin
B. Chuyển tiếp khung tin ra cổng e1
C. Chuyển tiếp khung tin ra cổng e2
D. Quảng bá khung tin ra tất cả các cổng (trừ cổng khung tin đến)
E. Thêm/Cập nhật địa chỉ 12-12-12-ab-ab-ab vào bảng chuyển tiếp
F. Thêm/Cập nhật địa chỉ 11-11-11-dd-dd-dd vào bảng chuyển tiếp
ans: B,F

Câu 38: Khi switch nhận được khung tin với địa chỉ đích là 12-12-12-ab-aa-aa và địa chỉ nguồn là 33-33-33-ee-ee-ee đến từ cổng e3.
A. Hủy khung tin
B. Chuyển tiếp khung tin ra cổng e1
C. Chuyển tiếp khung tin ra cổng e2
D. Quảng bá khung tin ra tất cả các cổng (trừ cổng khung tin đến)
E. Thêm/Cập nhật địa chỉ 12-12-12-ab-ab-ab vào bảng chuyển tiếp
F. Thêm/Cập nhật địa chỉ 33-33-33-ee-ee-ee vào bảng chuyển tiếp
ans: D,F

Nếu một gói tin IP với kích thước phần dữ liệu (payload) là 4926 bytes được gửi qua một kết nối mạng có MTU là 880 bytes (giả sử kích thước phần header là 20 bytes) thì:

Câu 39: Gói tin IP tách thành bao nhiêu phân mảnh để thỏa mãn yêu cầu của kết nối đó?
A. 4
B. 6
C. 440
D. 5
E. 7
ans: B

Câu 40: Kích thước phần payload của mảnh tin cuối cùng là bao nhiêu byte?
A. 626
B. 426
C. 440
D. 526
E. 640
F. 520
ans: A
```
