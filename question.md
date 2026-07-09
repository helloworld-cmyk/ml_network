----- Page 1 -----
```md
Câu 1: Giá trị BER (Bit Error Rate = Tỷ lệ bít lỗi/Tỷ lệ bít truyền) phản ánh đặc trưng nào sau đây của đường truyền?
A. Tốc độ truyền tin tối đa
B. Thông lượng
C. Độ tin cậy
D. Độ suy hao tín hiệu
E. Độ trễ
ans: C

Câu 2: Thông số RTT(Round Trip Time) trong quá trình truyền tin cho biết điều gì?
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
ans: A

Câu 5: Tại sao đường truyền phải có giá trị MTU(Maximum Transmission Unit) để giới hạn kích thước của gói tin được truyền?
A. Giảm xác suất đụng độ
B. Giảm tỉ lệ lỗi bit (BER – Bit Error Rate)
C. Giảm xác suất phải truyền lại dữ liệu
D. Tăng tốc độ truyền tin
ans: A
```

----- Page 2 -----
```md
Câu 6: Tại sao phải đặt giá trị MTU (Maximum Transmission Unit) cho đường truyền?
A. Giảm tỉ lệ phải truyền lại do lỗi bit trên gói tin
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
ans: D,E

Câu 8: Phát biểu nào sau đây là SAI về giao thức truyền thông?
A. Quy định khuôn dạng dữ liệu khi truyền
B. Quy định cách thức xử lý dữ liệu ở mỗi bên
C. Quy định thứ tự các thông điệp khi truyền
D. Độc lập với các giao thức khác
ans: D

Câu 9: Mô tả nào sau đây là đúng về kiến trúc phân tầng trong hệ thống truyền thông? (chọn 2 đáp án)
A. Thứ tự các tầng có thể thay đổi linh hoạt khi triển khai
B. Tầng trên quyết định cách thức cung cấp dịch vụ của tầng dưới
C. Tầng dưới cung cấp dịch vụ cho tầng trên qua điểm truy cập dịch vụ (SAP)
D. Một số tầng không cần triển khai trên tất cả các nút mạng
E. Giao thức của mỗi tầng độc lập với nhau
ans: C,D

Câu 10: Trong kiến trúc phân tầng của hệ thống truyền thông, phát biểu nào sau đây là đúng? (Chọn 2 đáp án)
A. Tại mỗi tầng, hai bên tham gia quá trình truyền tin phải sử dụng giao thức giống nhau
B. Quá trình đóng gói dữ liệu tại bên gửi được thực hiện từ tầng trên xuống tầng dưới
C. Mỗi mô hình phân tầng chọn một giao thức mạng để điều khiển hoạt động tất cả các tầng
D. Hoạt động của mỗi tầng không phụ thuộc vào các tầng khác
ans: A,B

Câu 11: Khái niệm PDU trong kiến trúc phân tầng là gì?
A. Một giao thức truyền thông
B. Một tầng trong mô hình OSI
C. Đơn vị dữ liệu được đóng gói theo giao thức của mỗi tầng trong kiến trúc phân tầng
D. Điểm truy cập dịch vụ của mỗi tầng cung cấp cho tầng trên
ans: C
```

----- Page 3 -----
```md
Câu 1: Trong kiến trúc phân tầng, khi nhận được dữ liệu từ tầng cao hơn chuyển xuống, tầng dưới xử lý như thế nào?
A. Sửa thông tin phần tiêu đề
B. Loại bỏ phần tiêu đề của gói tin
C. Thêm tiêu đề cho gói tin
D. Thay thế tiêu đề của gói tin bằng tiêu đề mới
ans: C [suy luận]

Câu 2: Đóng gói dữ liệu (encapsuation) trong kiến trúc phân tầng được thực hiện như thế nào?
A. Thêm phần tiêu đề mới vào gói tin nhận được ở tầng trên
B. Thay thế tiêu đề của gói tin tầng trên bằng tiêu đề mới
C. Nén phần dữ liệu trong gói tin nhận được từ tầng trên
D. Chỉ thực hiện thêm phần tiêu đề ở tầng dưới cùng
ans: A [suy luận]

Câu 3: Tính trong suốt trong kiến trúc phân tầng thể hiện như thế nào?
A. Tầng trên sử dụng dịch vụ của tầng dưới qua điểm truy cập dịch vụ (SAP) mà không cần quan tâm cách thức tầng dưới thực hiện
B. Mỗi tầng cung cấp nhiều dịch vụ khác nhau
C. Dữ liệu được đóng gói theo giao thức điều khiển
D. Chức năng trên mỗi tầng là khác nhau
E. Hai tầng trên liên kết phải sử dụng giao thức giống nhau
ans: A [suy luận]

Câu 4: Trong mô hình TCP/IP, tầng nào thực hiện chức năng điều khiển truyền dữ liệu trên liên kết vật lý?
A. Tầng vật lý
B. Tầng liên kết dữ liệu
C. Tầng mạng
D. Tầng giao vận
ans: B [suy luận]

Câu 5: Trong quá trình truyền dữ liệu, chức năng của tầng nào trong mô hình TCP/IP chỉ thực hiện trên các hệ thống đầu cuối? (chọn 2 đáp án)
A. Tầng ứng dụng
B. Tầng giao vận
C. Tầng mạng
D. Tầng liên kết dữ liệu
E. Tầng vật lý
ans: A,B [suy luận]

Câu 6: Tầng ứng dụng của mô hình TCP/IP đảm nhận chức năng những tầng nào khi tham chiếu tới mô hình OSI?
A. Tầng ứng dụng, tầng phiên
B. Tầng ứng dụng, tầng trình diễn
ans: [không chắc] [câu bị cắt - thiếu phần cuối]
```
