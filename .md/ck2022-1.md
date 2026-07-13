----- Page 1 -----
```md
Câu 1: Ưu điểm của giao thức UDP so với TCP là gì? (Chọn 2 đáp án)
A. Tốc độ truyền nhanh hơn
B. Đơn giản hơn
C. Tin cậy hơn
D. Không gây tắc nghẽn (congestion) đường truyền
ans: A,B

Câu 2: Làm thế nào để kiểm tra xem địa chỉ IP của gói tin có nằm trong một mạng cục bộ không?
A. Gửi bản tin RARP với địa chỉ IP của gói tin
B. Không có cách nào đúng
C. Kiểm tra địa chỉ IP và mặt nạ mạng
D. Gửi gói tin đến Default Gateway
ans: C

Câu 3: Quá trình định tuyến được thực hiện để làm gì?
A. Tìm đường đi giữa 2 router
B. Tìm đường đi tới router mặc định
C. Tìm đường đi giữa 2 máy tính trong cùng mạng
D. Tìm đường đi giữa 2 switch
ans: A
```

----- Page 2 -----
```md
Câu 4: Cơ chế tự học của switch được dùng để làm gì
A. Giúp chuyển tiếp dữ liệu trong một mạng LAN có topo dạng trục
B. Giúp chuyển tiếp dữ liệu trong một mạng LAN không dây.
C. Giúp chuyển tiếp dữ liệu trong một mạng LAN có topo dạng điểm-điểm
D. Giúp chuyển tiếp dữ liệu giữa các mạng
ans: C

Câu 5: Ánh xạ các mô tả vào các kỹ thuật tương ứng

1. Phía gửi được phép gửi nhiều gói tin mà không cần chờ báo nhận
2. Phía gửi chỉ được phép gửi một gói tin và phải chờ báo nhận
3. Phía gửi phải gửi lại đúng gói tin bị lỗi
4. Phía gửi phải gửi lại một số gói tin gồm cả gói tin không bị lỗi

A. Cửa sổ trượt - Sliding windows
B. Loại bỏ chọn lọc - Selective Reject
C. Dừng và chờ - Stop-and-wait
D. Go back N

ans: A,C,B,D
```


----- Page 3 -----
```md
Câu 6: Hãy lựa chọn thứ tự của từng tầng trong mô hình OSI khi liệt kê theo thứ tự từ dưới lên (Đáp án lựa chọn là 1-7 cho mỗi tầng, các tầng sẽ được sắp xếp không theo thứ tự)

- Tầng ứng dụng (Application Layer): 7
- Tầng trình diễn (Presentation Layer): 6
- Tầng liên kết dữ liệu (Data-link Layer): 2
- Tầng vật lý (Physical Layer): 1
- Tầng phiên (Session Layer): 5
- Tầng giao vận (Transport Layer): 4
- Tầng liên mạng (Internetwork Layer): 3

A. 
B. 
C. 
D. 
ans: Physical=1, Data-link=2, Network=3, Transport=4, Session=5, Presentation=6, Application=7 [suy luận - câu matching/fill-in]

Câu 7: Khi truyển dữ liệu từ máy A đến máy B, giả thiết gói tin đi qua 13 router trong mạng, số các mạng gói tin đi qua là bao nhiêu?
A. 1
B. 24
C. 13
D. 28
ans: D [suy luận]

Câu 8: Điểm khác biệt khi triển khai dịch vụ theo mô hình P2P so với mô hình Client-Server là gì? (Chọn 3 đáp án)
A. Không cần tất cả các nút mạng thành phần phải duy trì kết nối liên tục
B. Không cần quản lý tài nguyên tập trung
C. Các nút mạng có thể vừa gửi yêu cầu dịch vụ, vừa cung cấp dịch vụ cho các nút khác
D. Có điểm thất nút cổ chai
ans: A,B,C

Câu 9: Phát biểu nào sau đây là đúng về máy chủ tên miền gốc (root server) trong hệ thống DNS? (Chọn 2 đáp án)
A. Quản lý thông tin các máy chủ tên miền cấp 1 (TLD Server)
B. Lưu trữ thông tin của toàn bộ tên miền trên Internet
C. Không trả lời các thông điệp DNS Query truy vấn tên miền
D. Có thể được đặt ở nhiều vị trí khác nhau trên Internet
ans: A,D [suy luận - phần cuối đáp án D bị cắt bởi tooltip "Generating Speech Output"]
```


----- Page 4 -----
```md
Câu 10: Bảng MAC/CAM của một switch có nội dung như sau. Switch thực hiện các xử lý nào khi trên cổng e2 nhận được một khung tin có địa chỉ nguồn là 55-55-55-ee-ee-ee và địa chỉ đích là 11-11-11-aa-aa-aa.(Chọn 2 đáp án)

| Host | Interface |
|:-:|:-:|
| 11-11-11-aa-aa-aa | e1 |
| 22-22-22-bb-bb-bb | e2 |
| 33-33-33-cc-cc-cc | e3 |
| 44-44-44-dd-dd-dd | e1 |

A. Hủy khung tin
B. Gửi khung tin ra cổng e1
C. Gửi khung tin ra cổng e2
D. Gửi báo lỗi cho nút nguồn
E. Gửi khung tin ra tất cả các cổng trừ cổng e2
F. Thêm địa chỉ 55-55-55-ee-ee-ee vào bảng MAC/CAM với cổng chuyển tiếp là e2
ans: E,F

Câu 11: Đặc điểm của phương pháp CSMA là gì? (Chọn 2 đáp án)
A. Các nút sử dụng đường truyền một cách ngẫu nhiên
B. Lắng nghe tín hiệu sóng mang (carrier) trên đường truyền trước khi gửi
C. Các nút sử dụng đường truyền đồng thời, mỗi nút mạng sử dụng một mã để truyền tin
D. Không có đáp án đúng
ans: A,B

Câu 12: Mã Checksum được sử dụng để làm gì?
A. Sửa lỗi phát sinh do quá trình truyền dữ liệu.
B. Phát hiện lỗi phát sinh do quá trình truyền dữ liệu.
ans: B
```


----- Page 5 -----
```md
Câu 12: Mã Checksum được sử dụng để làm gì?
A. Sửa lỗi phát sinh do quá trình truyền dữ liệu.
B. Phát hiện lỗi phát sinh do quá trình truyền dữ liệu.
C. Báo hiệu cho bên gửi dữ liệu rằng dữ liệu có lỗi.
D. Bảo mật cho dữ liệu.
ans: B

Câu 13: Cho một đường truyền có thể phát được 2²⁰ xung (pulse/s), khi áp dụng phương pháp mã hoá NRZ-L, tốc độ dữ liệu sinh ra là bao nhiêu.
A. 100 Mbps
B. 0.5 Mbps
C. 1 Mbps
D. 10 Mbps
ans: C

Câu 14: Các yếu tố nào sau đây ảnh hưởng đến trễ khứ hồi (Round Trip Time) trong mạng?
A. Tốc độ xử lý của các thiết bị mạng
B. Tất cả các yếu tố đã được đề cập
C. Tải trên đường truyền
D. Tốc độ xử lý của nút nhận
E. Băng thông đường truyền
ans: B

Câu 15: Trường nào trong tiêu đề của gói tin IP được dùng để xác định loại dữ liệu (payload) mà gói tin IP đang vận chuyển?
A. Type of service
B. Checksum
C. Identification
D. Protocol
ans: D
```


----- Page 6 -----
```md
Câu 16: Dữ liệu của một gói tin gửi đi là 1010 0011 0111 (dạng nhị phân). Hệ thống sử dụng mã checksum 4-bit để kiểm tra lỗi. Hãy cho biết mã checksum cần được đính kèm với dữ liệu (Chỉ ghi mã checksum dưới dạng nhị phân, không thêm bất cứ kí tự nào)
A. 1010
B. 1110
C. 0101
D. 1011
ans: A [suy luận]

Câu 17: Các gói tin TCP nào sau đây được sử dụng để đóng liên kết? (Chọn 2 đáp án)
A. SYN
B. ACK
C. FIN
D. SYN/ACK
ans: B,C [suy luận]

Câu 18: Để có thể yêu cầu phía gửi phát lại dữ liệu khi có lỗi, kỹ thuật nào sau đây có thể được áp dụng? (Chọn 2 đáp án)
A. Dừng và chờ (Stop-and-wait)
B. Go back N
C. Checksum
D. Slowstart
ans: A,B [suy luận]

Câu 19: Thông điệp DHCP nào được client gửi đi khi vừa kết nối vào mạng và xin cấp phát địa chỉ IP mới?
A. DHCP Request
B. DHCP Offer
C. DHCP Discover
D. DHCP ACK
ans: C [suy luận]
```


----- Page 7 -----
```md
Câu 20: Phát biểu nào sau đây là đúng về các chương trình trên tầng ứng dụng? (Chọn 2 đáp án)
A. Sử dụng socket để truyền dữ liệu
B. Chỉ cần triển khai trên hệ thống đầu cuối
C. Phải cài đặt các cơ chế để đảm bảo truyền thông tin cậy
D. Chọn đường đi tốt nhất để truyền dữ liệu
ans: A,B

Câu 21: Các phương pháp mã hóa như Manchester, NRZ-L, AMI Bipolar được sử dụng để làm gì?
A. Biểu diễn dữ liệu thành tín hiệu
B. Kiểm soát luồng
C. Kiểm soát lỗi của khi truyền dữ liệu trên đường truyền
D. Bảo mật cho dữ liệu
ans: A

Câu 22: Đâu là hình trạng mạng sử dụng một đường truyền dùng chung cho mọi nút?
A. Hình sao (Star)
B. Hình trục (Bus)
C. Hình lưới (Mesh)
D. Hình vòng (Ring)
ans: B

Câu 23: Trong hoạt động của giao thức TCP, bên gửi thực hiện hoạt động nào? (Chọn 3 đáp án)
A. Yêu cầu thiết lập liên kết trước khi gửi
B. Chờ báo nhận
C. Phát lại dữ liệu khi có lỗi
D. Gửi dữ liệu với tốc độ nhanh nhất
ans: A,B,C
```


----- Page 8 -----
```md
Câu 24: Hai tiến trình thực hiện truyền tin theo giao thức TCP. Tiến trình gửi đang sử dụng cửa sổ kiểm soát tắc nghẽn (congestion window) là 14.000 byte và ngưỡng kiểm soát tắc nghẽn (ssthreshold) là 11.200 byte. Tiến trình gửi nhận được gói tin ACK báo thành công cho các gói tin đã gửi, trong đó giá trị Receive Window là 65.535. Giả sử các bên đã thỏa thuận 1 MSS = 1.400 byte. Trong lượt tiếp theo, tiến trình gửi có thể gửi tối đa bao nhiêu byte? (Chỉ ghi đáp án số, không kèm đơn vị).
A. 7000
B. 14000
C. 15400
D. 28000
ans: A [không chắc - câu dạng điền số, hệ thống ghi đáp án 7000 nhưng cwnd giải thích = 15400]

Câu 25: Giao thức nào sau đây nằm ở tầng giao vận? (Chọn 2 đáp án)
A. IP
B. TCP
C. UDP
D. HTTP
ans: B,C

Câu 26: Đâu là ưu điểm của phương pháp chuyển mạch kênh khi so sánh với chuyển mạch gói? (Chọn 2 đáp án)
A. Cung cấp chất lượng dịch vụ tốt hơn
B. Hầu như không có trễ trung gian sau khi kênh truyền được thiết lập
C. Hiệu quả sử dụng kênh truyền tốt hơn
D. Giảm chi phí vận hành một hệ thống mạng
ans: B,C

Câu 27: Vấn đề mà kiểm soát đa truy nhập đường truyền (media access control) giải quyết là gì?
A. Điều khiển truyền dữ liệu giữa các nút mạng nối với nhau bằng switch
B. Điều khiển việc sử dụng đường truyền chung khi có nhiều nút cùng muốn truyền tin
C. Điều khiển [phần đầu bị che bởi overlay "Generating Speech Output"]...uyện theo thứ tự của giao thức mạng [không chắc]
D. [không rõ - có thể bị che bởi overlay]
ans: B
```


----- Page 9 -----
```md
Câu 28: Trong kỹ thuật Cửa sổ trượt (Sliding windows), phía gửi được phép truyền lượng dữ liệu tối đa là bao nhiêu?
A. Bằng kích thước vùng đệm của bên nhận
B. Một gói tin
C. Bằng kích thước cửa sổ phát của bên gửi
D. Bằng kích thước vùng đệm còn trống của bên nhận
ans: D

Câu 29: Mạng cần cung cấp địa chỉ cho 109 máy cần dùng mặt nạ mạng nào để hạn chế dư thừa địa chỉ ip? (Nhập mặt nạ mạng dạng thập phân, ví dụ: 255.255.255.0)
A. 255.255.255.0
B. 255.255.255.128
C. 255.255.255.192
D. 255.255.255.224
ans: B

Câu 30: Cho 4 phương pháp TDMA, FDMA, CSMA, Token Ring. Loại phương pháp truy nhập đường truyền tương ứng với mỗi phương pháp là gì?
A. TDMA - Chia kênh; FDMA - Chia kênh; CSMA - Truy nhập ngẫu nhiên; Token Ring - Truy nhập tuần tự
B. TDMA - Truy nhập ngẫu nhiên; FDMA - Chia kênh; CSMA - Chia kênh; Token Ring - Truy nhập tuần tự
C. TDMA - Chia kênh; FDMA - Truy nhập tuần tự; CSMA - Truy nhập ngẫu nhiên; Token Ring - Chia kênh
D. Tất cả đều cùng thuộc một loại
ans: A
```


----- Page 10 -----
```md
Câu 31: Dịch vụ phân giải tên miền đăng ký sử dụng số hiệu cổng dịch vụ là bao nhiêu?
A. 53
B. 25
C. 80
D. 110
ans: A

Câu 32: Có 6 mạng đang kết nối với nhau sử dụng 5 router, hỏi có bao nhiêu bảng định tuyến được sử dụng?
A. 5
B. 6
C. 1
D. 11
ans: A

Câu 33: Trong hoạt động của giao thức UDP, bên nhận thực hiện những hoạt động nào? (Chọn 2 đáp án)
A. Kiểm tra lỗi trên gói tin
B. Chuyển dữ liệu tới đúng ứng dụng
C. Đưa các gói tin không đúng thứ tự vào bộ đệm
D. Gửi báo nhận
ans: A,B

Câu 34: Trong kiến trúc phân tầng, tại bên nhận, hoạt động nào sau đây có thể được thực hiện trong xử lý ở mỗi tầng?
A. Thay thế tiêu đề của gói tin bằng tiêu đề mới và chuyển lên tầng trên
B. Bóc tách tiêu đề và chuyển phần thân của gói tin lên tầng trên
C. Thêm tiêu đề mới và chuyển xuống tầng dưới
D. Phân nhỏ gói tin
ans: B
```


----- Page 11 -----
```md
Câu 35: Phát biểu nào sau đây là SAI về số hiệu cổng ứng dụng?
A. Được sử dụng để xác định đường đi khi chuyển tiếp gói tin
B. Các chương trình ứng dụng trên một nút mạng phải đăng ký số hiệu cổng ứng dụng khác nhau
C. Được sử dụng trong quá trình truyền tin giữa các ứng dụng tại tầng giao vận
D. Là một số nguyên 16 bit
ans: A

Câu 36: Cho mạng có địa chỉ 208.139.245.0/26, hỏi địa chỉ quảng bá của mạng đó là địa chỉ nào?
A. 208.139.245.63
B. 208.139.245.64
C. 208.139.245.65
D. 208.139.245.127
ans: A

Câu 37: Phát biểu nào sau đây là đúng về giao thức định tuyến (routing protocol) dạng link-state? (Chọn 2 đáp án)
A. Các router trao đổi với nhau thông tin khoảng cách đường đi
B. Các router trao đổi với nhau thông tin về các liên kết (links)
C. Mỗi router có thể nhận thông tin từ tất cả các router khác
D. Các router hợp tác với nhau để tính toán đường đi
ans: B,D

Câu 38: Đâu là đặc điểm của mạng sử dụng kỹ thuật chuyển mạch kênh (Chọn 3 đáp án)
A. Thiết lập kênh trước khi truyền
B. Gói tin được truyền đi ngay
C. Các gói tin có thể tới đích không đúng thứ tự
D. Các gói tin trong mỗi kênh truyền giữa 2 nút luôn đi theo tuyến đường giống nhau
E. Tài nguyên được cấp phát để dùng riêng trên mỗi kênh truyền giữa 2 nút
ans: A,D,E
```


----- Page 12 -----
```md
Câu 39: Khi nhận được một gói tin có TTL = 0, nút mạng báo lỗi bằng thông điệp nào?
A. ICMP Time exceeded
B. ICMP Destination Network Unknown
C. ICMP Echo Request
D. ICMP Echo Reply
ans: A

Câu 40: Tầng vật lý thực hiện các chức năng nào sau đây?
A. Đánh số các gói dữ liệu gửi đi
B. Biểu diễn các bit thành tín hiệu và ngược lại
C. Đóng gói dữ liệu thành các gói tin
D. Kiểm tra dữ liệu nhận được có bị lỗi không
ans: B

Câu 41: Những thay đổi của giao thức HTTP 1.1 so với HTTP 1.0 là gì? (Chọn 3 đáp án)
A. Chỉ thiết lập 1 liên kết TCP để truyền nhiều thông điệp khác nhau
B. Có cơ chế pipeline để tăng tốc độ truyền tin
C. Bổ sung thêm các phương thức yêu cầu mới cho thông điệp HTTP Request
D. Sử dụng các cơ chế truyền thông tin cậy để luôn đảm bảo truyền thành công
ans: A,B,C

Câu 42: Mạng đang sử dụng địa chỉ 172.29.0.0/16 có thể có bao nhiêu mạng con nếu dùng mặt nạ mạng 255.255.255.192? (Nhập số mạng con)
A. 62
B. 1022
C. 1024
D. 4094
ans: B
```


----- Page 13 -----
```md
Câu 43: Khi không tìm thấy tài nguyên được yêu cầu, máy chủ Web gửi thông điệp HTTP Response với mã trả lời là bao nhiêu?
A. 200
B. 301
C. 404
D. 500
ans: C

Câu 44: Cho một đường truyền từ A đến B đi qua 3 đoạn kết nối khác nhau có băng thông lần lượt là 5 Mbps, 10 Mbps và 15 Mbps. Giả sử các đường kết nối này chỉ phục vụ cho việc truyền dữ liệu từ A đến B, trễ trên thiết bị không đáng kể, và tỷ lệ lỗi và mất gói tin bằng 0. Hỏi thông lượng trung bình từ A đến B là bao nhiêu?
A. 5 Mbps
B. 10 Mbps
C. Không thể xác định được
D. 15 Mbps
ans: A

Câu 45: Một gói tin IP với kích thước payload là 4723 byte đi vào mạng có MTU = 968 byte, biết tiêu đề IP có kích thước 20 byte, hỏi lượng dữ liệu ở mảnh IP cuối là bao nhiêu? (Nhập số nguyên, không nhập đơn vị, ví dụ: 52)
A. 474
B. 931
C. 948
D. 1024
ans: B
```
