----- Page 1 -----
```md
Câu 1: Choose the correct statement(s) about application traceroute
A. traceroute is used to measure the propagation latency from the source to the destination through IP networks.
B. traceroute is used to display the list of intermediate nodes between the source and the destination in IP networks
C. traceroute uses TCP for communication
D. traceroute command stops after 3 seconds without reply (error "Time exceeded")
E. traceroute command works only with domain name
ans: A,B

Câu 2: What is the correct statement about Top level domain (TLD) server in the DNS system?
A. Do not answer DNS Query asking for domain name resolution but only response to Root server
B. Independent, TLD server is not in the DNS hierarchy
C. Store all information about the domain belongs to it (example: .vn)
D. Manage the information about Authoritative servers
ans: D
```

----- Page 2 -----
```md
Câu 3: Which statement(s) is/are correct?
A. In point-to-point topology, all network nodes must connect to a common node
B. In point-to-point topology, a link connects only two nodes
C. In point-to-multipoint topology, all nodes must connect to a common bus
D. In point-to-multipoint topology, all nodes must share a common transmission medium
ans: B,D

Câu 4: Sliding windows control flows between a transmitter and a receiver by
A. Do not allow the transmitter to send more data than the receiver's buffer size
B. Do not allow the transmitter to send more data than its buffer size
C. Do not allow the transmitter to send more data than the free space of the receiver buffer
D. Do not allow the transmitter to send data in the same time with the receiver
ans: C

Câu 5: According to OSI model, which information may be contained in the header of a packet?
A. The packet of the upper layer
B. Header of the packet of the upper layer
C. Sequence number
D. Size of the packet
ans: B,C,D

Câu 6: Which Automatic repeat request (ARQ) techniques require that packets should be numbered?
A. Stop-and-wait
B. Selective Reject
C. Go back N
D. None
ans: B,C
```

----- Page 3 -----
```md
Câu 7: Classify following characteristics to those of switches and those of routers?
1. Forward data to the destination node in the same network
2. Forward data to the destination node in another network
3. Forward data according IP addresses
4. Build the forwarding guideline table itself by learning
5. Forward data according to MAC addresses
6. Build the forwarding guideline by interaction with other nodes

A. 1-Switch, 2-Router, 3-Router, 4-Switch, 5-Switch, 6-Router
B. 1-Router, 2-Switch, 3-Router, 4-Switch, 5-Switch, 6-Router
C. 1-Switch, 2-Router, 3-Router, 4-Router, 5-Switch, 6-Switch
D. 1-Switch, 2-Router, 3-Switch, 4-Switch, 5-Router, 6-Router
ans: A

Câu 8: What is (are) the characteristic(s) of application using P2P model?
A. All participant nodes must be online all the time.
B. Do not need to centrally manage resources
C. Scale up easily because the participant nodes contribute to provide application services
D. Having bottleneck point
ans: B,C

Câu 9: Two processes communicate by a reliable protocol using stop-and-wait mechanism. The size of file to be sent is 10000 bytes, the size of each packet is 1000 bytes, assuming that the header size is zero. RTT between the 2 hosts is 100ms. The bandwidth of the transmission line is 1Mbps (Megabits per second). How much of time it takes to complete the transmission?
A. 1010
B. 1080
C. 1100
D. 1000
ans: B
```

----- Page 4 -----
```md
Câu 10: Given a fixed pulse generation speed, how NRZ-L, Manchester, Bipolar AMI encodings provide data speed (bit/s)?
A. NRZ-L and Bipolar AMI result in higher data speeds than Manchester
B. The 3 methods result in identical data speeds
C. Manchester and Bipolar AMI result in higher data speeds than NRZ-L
D. NRZ-L and Manchester result in higher data speeds than Bipolar AMI
ans: B

Câu 11: Which protocol(s) belong(s) to transport layer?
A. IP
B. ICMP
C. TCP
D. UDP
E. HTTP
ans: C,D

Câu 12: When a DHCP server sends DHCP ACK message(s) to a client?
A. When the client asks to be assigned an IP address
B. When the client registers an IP address after receiving an offer from the server
C. When the client needs to extend the validation of and IP address it has been assigned
D. When the server confirms that there is no error in data received from the client
E. All statements are incorrect
ans: B

Câu 13: Assume that the window size in the Sliding window mechanism is equivalent N packets. Choose the correct statement about the efficiency of Sliding window in comparison with Stop-and-wait:
A. Data transmission efficiency of Sliding windows is N times higher
B. Data transmission efficiency of Sliding windows is 2N times higher
ans: A
```

----- Page 5 -----
```md
Câu 14: Assume that the window size in the Sliding window mechanism is equivalent N packets. Choose the correct statement about the efficiency of Sliding window in comparison with Stop-and-wait:
A. Data transmission efficiency of Sliding windows is N times higher
B. Data transmission efficiency of Sliding windows is 2N times higher
C. Data transmission efficiency of Sliding windows is N<sup>2</sup> times higher
D. Data transmission efficiency of the 2 methods are identical.
ans: A

Câu 15: In the layering model, when a packet arrives to an intermediate node, how it is processed?
A. Forward from application layer to lower layers then physical layer.
B. Forward from physical layer to application later
C. Forward from upper layers to physical layer then from physical layer to upper layers
D. Forward from the physical layer to upper layers and then from the upper layers to the physical layer.
ans: D

Câu 16: Choose the correct statement(s) about interdomain routing protocol BGP.
A. BGP routing prioritizes management policies over performance
B. BGP does not have a mechanism to avoid loops in routing paths
C. BGP uses path-vector routing instead of link-state or distance-vector routing
D. BGP selects best paths based on bandwidth metric to achieve the best performance
ans: A,C

Câu 17: Identify the multiple access methods that have the following characteristics:

1. Network nodes sequentially send data
   - Token bus

2. Network nodes can send data simultaneously without collision
   - FDMA, CDMA

3. Network nodes only send data when the transmission line is free
   - CSMA

4. Network nodes send data even if the transmission line is busy
   - Aloha

A. 1-Token bus, 2-FDMA, CDMA, 3-CSMA, 4-Aloha
B. 1-Token bus, 2-FDMA, 3-CSMA, 4-Aloha
C. 1-Aloha, 2-FDMA, CDMA, 3-CSMA, 4-Token bus
D. 1-Token bus, 2-CDMA, 3-CSMA, 4-Aloha
ans: A
```

----- Page 6 -----
```md
Câu 18: What is the purpose of the field TTL in IP packet?
A. To avoid the packet looping in an IP network forever
B. To limit the execution time of ping command
C. To help finding path from the source to the destination by using command traceroute
D. To help administrator limit the routing scope of the packet
ans: A

Câu 19: When a router receives a packet whose destination address matches several rows in the routing table, what the router does?
A. Router forwards the packet to the interface (port) with the smallest index
B. Router reports error because the destination address matches with more than one rows in routing table
C. No answer is correct
D. Router forwards the packet to the interface (port) corresponding to the destination network that has the largest mask
ans: D

Câu 20: Forwarding table (MAC table) of a switch is as belows. What the switch will do when it receives a frame with source address 12-12-12-ab-ab-ab and destination address 11-11-11-dd-dd-dd.

| Host | Interface |
|:----:|:---------:|
| 11-11-11-aa-aa-aa | e1 |
| 22-22-22-bb-bb-bb | e2 |
| 33-33-33-cc-cc-cc | e3 |
| 44-44-44-dd-dd-dd | e4 |

A. Destroy the frame
B. Forward the frame to port e1
C. Broadcast the frame
D. Send error message to the source
E. Add the address 11-11-dd-dd-dd to the forwarding table (MAC table)
ans: C
```

----- Page 7 -----
```md
Câu 21: Which statement(s) are FALSE about congestion control mechanism of TCP?
A. Ssthreshold (Slow-start threshold) changes depending on the network bandwidth and it is updated periodically
B. Ssthreshold is updated when congestion happens
C. cwnd window reduces to 1 MSS when receiver receives 3 ACKs segment of the same index
D. cwnd window reduces to 1 MSS when a timeout occurs for one segment
E. slow-start period stop when the number of segments to be sent in the circle meets the slow start threshold
F. After receiving 3 ACKs with the same index, sender move to slow-start state
ans: C,F

Câu 22: Why video streaming applications tend to use UDP instead of TCP?
A. TCP is more complicated so more error-prone
B. UDP has smaller header than TCP so the transmission efficiency is better
C. UDP can transmit data with larger bandwidth at the same transmission line
D. Video streaming application does not need the transmission accuracy 100%
ans: B,D

Câu 23: Sort the error detection codes Parity, Checksum, CRC in decreasing order of their error detection capacity
A. CRC-12, Parity, Checksum 8 bit
B. Checksum 8 bit, CRC-12, Parity
C. CRC-12, Checksum 8 bit, Parity
D. Parity, Checksum 8 bit, CRC-12
ans: C
```

----- Page 8 -----
```md
Câu 24: Sending host A and receiving host B uses ARQ Go-back-N with window size is 5. A sends packets numbered pk0, pk1, pk2, pk3, pk4 but pk2 gets errors on the transmission line. What is (are) the FALSE statement(s) about ARQ Go-back-N protocol?
A. Receiver sends acknowledgements ack0, ack1, ack3 and ack4 corresponding to the packets it received successfully
B. Receiver sends ack0 and (several times) ack1
C. Sender sends again pk2
D. Sender sends again packets pk2, pk3, pk4
ans: A

Câu 25: Choose the correct statement(s) about HTTP Cookie?
A. HTTP Cookie deals with the problem that HTTP does not keep track of the state of the session
B. HTTP Cookie helps to access to data faster when using HTTP protocol
C. HTTP Cookie is used for applications that require authentication like email and e-commerce
D. HTTP Cookie is used uniquely on web server browser, not server
ans: A,C

Câu 26: Below signal could be generated with which encoding method(s)?
A. NRZ-L
B. Manchester
C. Bipolar AMI
D. No correct answer
ans: C

Câu 27: Choose the correct statement(s) about the applications on application layer?
A. Use socket to send data
B. Run only on end-systems
C. Multiple applications use a common port on transport layer
D. Need to implement mechanisms to achieve reliable transmission
E. Choose the best path to send data
ans: A,B
```

----- Page 9 -----
```md
Câu 28: Mapping the following characteristics to Packet switching mechanism and Circuit switching mechanism
1. Data is store in switches before being analysed and forwarded
2. Data must be divided into packets
3. Data always follow the same set of links in one transmission process
4. Data can follow different sets of links in one transmission process
A. 1-Packet switching mechanism, 2-Packet switching mechanism, 3-Circuit switching mechanism, 4-Packet switching mechanism
B. 1-Circuit switching mechanism, 2-Packet switching mechanism, 3-Circuit switching mechanism, 4-Packet switching mechanism
C. 1-Packet switching mechanism, 2-Circuit switching mechanism, 3-Packet switching mechanism, 4-Circuit switching mechanism
D. 1-Circuit switching mechanism, 2-Packet switching mechanism, 3-Packet switching mechanism, 4-Circuit switching mechanism
ans: A

Câu 29: Choose the correct answer(s) about NAT Overloading (PAT), a mechanism to convert from internal to public addresses
A. Each private address is converted STATICALLY to a separate public address
B. Each private address is converted DYNAMICALLY (change over time) to a separate public address
C. All local addresses are converted to an UNIQUE public address
D. Each application in a local network is refered to by a separate port of the public address
E. All of the above statements are false
ans: B,D

Câu 30: Choose the address(es) that IS (ARE) NOT ALLOWED to be assigned as public IP addresses?
A. 10.20.10.1
B. 11.22.10.1
C. 172.20.10.1
D. 192.168.10.1
E. 202.191.10.1
F. 225.34.6.8
ans: A,C,D,F
```

----- Page 10 -----
```md
Câu 31: In which scope MAC address is used to forward data?
A. To forward data between network nodes that connect directly to each other
B. To forward data between network nodes of two LANs
C. To forward data between network nodes connected to each other through switches
D. To forward data between network nodes on the Internet
ans: A,C

Câu 32: Why the connection-oriented transmission is more reliable than connectionless transmission?
A. Data cannot be lost
B. Data follows the same path
C. Connection-oriented transmission makes sure that the receiver is ready to receive data
D. Connection-oriented transmission makes sure that the receiver is not overloaded.
ans: C

Câu 33: In the header of a transport layer packet, which field is used to determine the application that sent the packet.
A. checksum code
B. Port of the destination application
C. Source IP address
D. Destination IP address
E. Port of the source application
ans: E

Câu 34: When an Web server found a requested resource, it sends HTTP Response with an answer code. What is the value of the answer code?
A. 200
B. 200
ans: A
```

----- Page 11 -----
```md
Câu 35: The WiFi network that laptops, mobile phones connect to in a coffee shop belongs to what kind of network?
A. Local area network (LAN)
B. Wide area network (WAN)
C. Metro area network (MAN)
D. PAN
ans: A

Câu 36: Compare two communication lines whose BERs are 5.10⁻⁶ and 10⁻⁶ respectively, which one is better in terms of quality?
A. The line with BER 5.10⁻⁶ is better
B. The line with BER 10⁻⁶ is better
C. Two lines have similar quality
D. Impossible to compare
ans: B

Câu 37: What is the port that FTP service uses to transmit data?
A. 20
B. 21
C. 22
D. 23
ans: A

Câu 38: Which statement(s) is/are correct about link-state routing protocol?
A. Routers exchange information about links
B. Routers exchange the information about distance of paths
C. Each router may have the information about all links of the network
D. Routers collaborate to calculate paths
E. The calculation converges slower than distance-vector protocol in large networks
ans: A,C,D
```

----- Page 12 -----
```md
Câu 39: In a TCP segment sent from host A to host B, the value of sequence number field is 100, the value of ACK field is 200, data payload is 1000 bytes length. The data is sent successfully to the destination. When B send back an acknowledgement, the fields in its TCP segment are:

Value of field Sequence
A. 200
B. 100
C. 1100
D. 1000

Value of field ACK
A. 1100
B. 200
C. 100
D. 1000

Attention: Write only number, no space or unit
ans: A,C

Câu 40: What information is not defined in a network protocol
A. Packet format to be used during the transmission
B. How data packet should be processed by participants
C. No correct answer
D. Procedure to send and receive data
ans: B

Câu 41: Given a network with bus topology, the data transmission between two nodes can be performed by which methods?
A. CSMA
B. Using MAC table (forwarding table) and self-learning mechanism of switch
C. FDMA
D. Token bus
ans: A,D
```

----- Page 13 -----
```md
Câu 42: What network mask should be used to minimize IP address waste for 122 machine that needs to be assigned an address? (Enter the network mask in decimal format, for example, 255.255.255.0)
A. 255.255.255.128
B. 255.255.255.0
C. 255.255.255.192
D. 255.255.255.224
ans: A

Câu 43: If an IP packet with a payload size of 5246 bytes is sent into a network with an MTU of 1192 bytes, and assuming the IP header size is 20 bytes, what will be the size of data (payload) in the last IP fragment? (Enter an integer without any unit, for example: 52)
A. 1172
B. 558
C. 1152
D. 1192
ans: B

Câu 44: Given a network with subnet address 219.131.107.0/26, what is the broadcast address of that network? (Enter the IP address in decimal format, for example: 192.168.1.0)
A. 219.131.107.63
B. 219.131.107.0
C. 219.131.107.1
D. 219.131.107.64
ans: A
```

----- Page 14 -----
```md
Câu 45: How many subnets are possible for a network with address 172.19.0.0/16 if the network mask used is 255.255.192.0? (Enter the number of subnets, for example: 2)
A. 2
B. 4
C. 8
D. 16
ans: B

Câu 46: Đâu là các phát biểu ĐÚNG về giao thức định tuyến bên trong vùng (nội vùng)
A. Giao thức định tuyến bên trong (IGP) bao gồm tên định danh (performance) hơn là cảnh sách (policy)
B. Giao thức định tuyến nội vùng thường định tính 2 hay 3 hoạt động link-state với distance vector
C. Giao thức định tuyến bên trong (BGP) đặc trưng link-state
D. Giao thức định tuyến nội vùng của các mạng từ tỉ (AS) khác nhau có thể khác nhau
ans: B,D

Câu 47: Việc phân chia mạng theo CIDR thực hiện phân chia dựa trên lớp gì?
A. Có thể chia nhỏ thành nhiều mạng con (subnet)
B. Tận dụng được không gian địa chỉ tốt hơn
C. Cho phép chia thành nhiều phân lớp hơn so với trước
D. Không có đặc điểm gì
ans: B

Câu 48: Chuyển gì xảy ra nếu MTU của một đường truyền kết nối quá nhỏ?
A. Giảm bớt từng gói dữ liệu truyền
B. Tăng khả năng lỗi trên đường truyền
C. Tăng khả năng tốc nghiệp do sẽ gửi từ từng gói
D. Giảm hiệu suất truyền dữ liệu do phải header có kích thước cố định
ans: D
```

----- Page 15 -----
```md
Câu 49: Cho các địa chỉ mạng dưới đây, hãy lựa chọn loại địa chỉ hợp lệ 192.168.1.128/25
A. Địa chỉ mạng
B. Địa chỉ máy
C. Địa chỉ quảng bá
D. Không hợp lệ
ans: A

Câu 50: Cho các địa chỉ mạng dưới đây, hãy lựa chọn loại địa chỉ hợp lệ 192.168.1.255/23
A. Địa chỉ quảng bá
B. Địa chỉ máy
C. Địa chỉ mạng
D. Không hợp lệ
ans: B
```

----- Page 16 -----
```md
Câu 51: **Phân mảnh gói tin** (đạt 1/1 điểm, không tích lũy vào tiến trình học)

Một gói tin IP có kích thước là 2420 bytes, bao gồm 20 bytes là phần header. Gói tin này phải đi qua một đường kết nối có MTU=940 bytes. Hỏi gói tin phải phân chia thành mấy mảnh (fragment)?
A. 2
B. 3
C. 4
D. 5
ans: B

Câu 52: Một gói tin IP có kích thước là 2420 bytes, bao gồm 20 bytes là phần header. Gói tin này phải đi qua một đường kết nối có MTU=940 bytes. Trường offset của phân mảnh thứ 2 có giá trị là bao nhiêu?
A. 100
B. 115
C. 120
D. 130
ans: B

Câu 53: Chuyện gì xảy ra nếu MTU của một đường truyền kết nối quá nhỏ
A. Tăng khả năng lỗi bit trên đường truyền
B. Tăng khả năng tắc nghẽn do số gói tin tăng lên
C. Giảm hiệu suất truyền dữ liệu do phần header có kích thước cố định
D. Giảm băng thông của đường truyền
ans: C

Câu 54: **MC_05_02** (đạt 1.0/1.0 điểm, không tích lũy vào tiến trình học)

Ưu điểm của giao thức UDP so với giao thức TCP là gì?
A. Tốc độ gửi nhanh hơn
B. Có điều khiển luồng
C. Tin cậy hơn
D. Quá trình bắt tay giữa máy nguồn và đích tốt hơn
ans: A
```

----- Page 17 -----
```md
Câu 55: **MC_05_07** (đạt 1.0/1.0 điểm, không tích lũy vào tiến trình học)

Câu 13 thiết bị mạng nào dưới đây hoạt động ở tầng 1-2-3 trong mô hình TCP/IP?
A. Repeater
B. Hub
C. Bridge
D. Switch
E. Router
F. Computer
ans: F

Câu 56: **MC_05_08** (đạt 1.0/1.0 điểm, không tích lũy vào tiến trình học)

Phân mảnh gói tin
(Bài 13/52) điểm, không tích lũy vào tiến trình học)

Hệ gói tin IP có kích thước là 2420 bytes, bao gồm 20 bytes là phần header. Giải sử máy phát đi qua mạng đến kết nối với MTU=1080 bytes. Hỏi:

Giải bài phân phải chia thành mấy phần (fragment)?
A. 2
B. 3
C. 4
D. 5
ans: B

Câu 57: **MC_05_09** (đạt 1.0/1.0 điểm, không tích lũy vào tiến trình học)

Trường offset của phân mảnh thứ 2 có giá trị bao nhiêu?
A. 0
B. 135
C. 270
D. 540
ans: B

Câu 58: **MC_05_10** (đạt 1.0/1.0 điểm, không tích lũy vào tiến trình học)

Truyền tin qua môi đường truyền
(Bài 13/52) điểm, không tích lũy vào tiến trình học)

Một đường truyền vật lý tốc độ 3.440 vị trí (bit vị trí) như với băng thông (tốc độ tín hiệu) là 20 Mbps, 1 Mbps, 50 Mbps. Giả sử các đường truyền số nhị phân với tốc độ 8 tín hiệu/giây và tốc độ 8 tín hiệu/giây và tốc độ 8 tín hiệu/giây. Hỏi mỗi giây cần (bit vị trí) truyền số lượng bit tối đa là bao nhiêu (MB)?
A. 8
B. 16
C. 32
D. 64
ans: B
```

----- Page 18 -----
```md
Câu 59: Đâu là những nhược điểm của cặp quang so với cáp loại cáp khác?
A. Giá thành đắt đỏ
B. Lắp đặt phức tạp do cần thiết bị chuyên dụng
C. Dễ suy hao tín hiệu lớn
D. Dễ bị ảnh hưởng bởi nhiễu từ sóng điện từ
E. Dễ hư hỏng
F. Kích thước lớn
ans: A,B,E

Câu 60: Chuyển gói xảy ra nếu MTU của một đường truyền kết nối qua nhỏ thì:
A. Góm hiệu suất truyền dữ liệu do phần header có kích thước cố định
B. Tăng khả năng tối bit trên đường truyền
C. Tăng khả năng tốc nghiên do số gói tin tăng lên
D. Giảm băng thông của đường truyền
ans: C

Câu 61: Vì sao khi sử dụng mã hóa Manchester và Manchester vi sai không xảy ra tình trạng mất đồng bộ giữa máy gửi và máy nhận?
A. Các đáp án khác đều sai
B. Chỉ sử dụng 2 mức điện áp
C. Luôn có sự chuyển mức 0 giữa các chu kỳ bit tín hiệu
D. Có tốc độ tín hiệu lớn hơn với cùng tốc độ dữ liệu
ans: C

Câu 62: **MC_05_01**
(dạy từ 1 điểm, không tích lũy vào tiến trình học)
Vì sao cổng giao vào có thêm định danh CỔNG (PORT) khi đã có địa chỉ IP và địa chỉ MAC để gửi dữ liệu tới máy nguồn đến máy đích?
A. Máy gửi không thông tin công cho máy đích bằng một đường tản công
B. Router cần thông tin công cho việc định tuyến
C. Máy đích cần thông tin công cho việc xử lý dữ liệu trên tầng ứng dụng
D. Máy đích và nguồn cần thông tin công để phân biệt các ứng dụng giao tiếp trong cùng một máy
ans: D
```

----- Page 19 -----
```md
Câu 63: Cho các địa chỉ mạng dưới đây thuộc các phân lớp nào khi sử dụng cơ chế phân lớp?
A. 150.55.1.128
B. 192.168.1.128
C. 10.168.255.240
D. 200.168.1.128
ans: B,C,A,D
```

----- Page 20 -----
```md
Câu 64: Việc phân chia mạng theo CIDR thay vì theo phân lớp đem lại lợi ích gì?
A. Có thể chia nhỏ thành nhiều mạng con (subnet)
B. Cho phép chia thành nhiều phân lớp hơn so với trước
C. Tận dụng được không gian địa chỉ tốt hơn
D. Không có đáp án đúng
ans: C

Câu 65: Trong các phát biểu sau, phát biểu nào là ĐÚNG về địa chỉ MAC
A. Có độ dài 48 bit
B. Một nhà sản xuất CHỈ CÓ MỘT số OUI
C. Địa chỉ MAC có thể thay đổi khi một máy kết nối với các mạng khác nhau
D. Router dùng địa chỉ MAC để xác định đường đi
E. Có 24 bit đầu là số OUI để phân biệt các nhà sản xuất
F. Một thiết bị đầu cuối (máy tính, điện thoại thông minh) chỉ có thể có một địa chỉ MAC
ans: A,E
```

----- Page 21 -----
```md
Câu 66: Khi sử dụng DHCP, client sẽ nhận ra mình đã được cấp phát địa chỉ IP khi nào?
A. Client lựa chọn offer đầu tiên
B. Client từ chối cả 2 offer do xung đột
C. Client nhận thêm cả 2 offer
D. Không có đáp án đúng
E. Client lựa chọn offer theo chính sách nguồn quản trị địa ra
ans: A

Câu 67: Vì sao chuẩn Ethernet không sử dụng kỹ thuật truy cập đường truyền CSMA/CA thay vì CSMA/CD với cổng kết nối dây đồng thời chỉ có tối độ 40G?
A. Vì CSMA/CA cho tốc độ truyền tốt hơn
B. Vì CSMA/CD yêu cầu thiết bị phức tạp hơn
C. Vì CSMA/CD yêu cầu đường truyền dây tối thiểu đủ dài
D. Vì tính tương tuyến không dây có đặc thù riêng nên không thể dùng hợp thức truyền không dây các máy trong mạng
ans: D

Câu 68: Cho một mạng có địa chỉ 172.16.0.0/16. Ngành to sử dụng 5 bit phần HostID để chia mạng thành các mạng con (subnet). Hỏi số mạng con tối đa có thể chia là? (Chỉ ghi số)
A. 32
B. 2^n (n = số bit phân HostID) => 2^5
ans: A

Câu 69: Số máy tối đa trong mỗi mạng con là? (Chỉ ghi số)
A. 2046
B. 2^11 - 2
ans: A
```

----- Page 22 -----
```md
Câu 70: Cho các địa chỉ mạng dưới đây, hãy lựa chọn loại địa chỉ hợp lệ
A. 192.168.1.128/25
B. 192.168.1.128/24
C. 192.168.1.255/25
D. 192.168.1.256/23
E. 192.168.1.255/23
F. 192.168.2.255/23
G. 192.168.2.0/23
ans: A [suy luận]
```

----- Page 23 -----
```md
Câu 71: Sắp xếp các giao thức định tuyến sau vào đúng loại của mình
A. Routing Information Protocol - RIP
B. Open Shortest Path First - OSPF
C. Enhanced Interior Gateway Routing Protocol - EIGRP
D. Border Gateway Protocol - BGP
ans: A,B,C,D

Câu 72: Cho các địa chỉ mạng dưới đây thuộc các phân lớp nào khi sử dụng cơ chế phân lớp?
A. 150.55.1.128
B. 192.168.1.128
C. 10.168.255.240
D. 200.168.1.128
ans: A,B,C,D

Câu 73: Một đường truyền từ A tới B qua 3 kết nối vật lý nối tiếp nhau với băng thông lần lượt là 5 Mbps, 2 Mbps, 1 Mbps. Giả sử các đường kết nối này chỉ phục vụ liên kết giữa A và B và thời gian xử lý và lan truyền dữ liệu là không đáng kể (bằng 0). Hỏi thời gian cần thiết để truyền một gói tin có kích thước 43 MB từ A tới B là bao nhiêu giây?
A. Chỉ ghi số giây, không ghi đơn vị hay bất cứ kí tự nào khác. Trường hợp số giấy lẻ, làm tròn đến 2 chữ số sau phần thập phân
ans: A
```

----- Page 24 -----
```md
Câu 74: Ưu điểm của giao thức UDP so với giao thức TCP là gì?
A. Có điều khiển luồng
B. Tốc độ gửi nhanh hơn
C. Quá trình bắt tay giữa máy nguồn và đích tốt hơn
D. Tin cậy hơn
ans: B
```

----- Page 25 -----
```md
Câu 75: Việc phân chia mạng theo CIDR thay vì theo phân lớp đem lại lợi ích gì?
A. Tận dụng được không gian địa chỉ tốt hơn
B. Không có đáp án đúng
C. Có thể chia nhỏ thành nhiều mạng con (subnet)
D. Cho phép chia thành nhiều phân lớp hơn so với trước
ans: A

Câu 76: Cho switch với bảng địa chỉ MAC và kết nối các máy như hình trên. Khi A gửi gói tin với địa chỉ đích là D đến switch thì switch sẽ ...
A. Cập nhật bảng địa chỉ MAC của A vào bảng địa chỉ MAC
B. Cập nhật địa chỉ MAC của D vào bảng địa chỉ MAC
C. Gửi gói tin theo cổng số 4 kết nối đến D
D. Gửi gói tin quảng bá đến các cổng từ 2 – 6
E. Gửi gói tin quảng bá đến các cổng từ 1 – 6
ans: A,D
```

----- Page 26 -----
```md
Câu 77: Cho một mạng có địa chỉ 172.16.0.0/16. Nếu yêu cầu đưa ra 5 bit phân HostID để chia mạng thành các mạng con (subnet). Hỏi số mạng con tối đa có thể chia là? (Chỉ ghi số)
A. 32
B. 32
ans: B

Câu 78: Số máy tối đa trong mỗi mạng con là? (Chỉ ghi số)
A. 2046
B. 2046
ans: A

Câu 79: Vì sao khi sử dụng mã hóa Manchester và Manchester vì sự không xảy ra tình trạng một đồng bộ giữa máy gửi và máy nhận?
A. Các độp ởn khác đều sai
B. Chỉ sử dụng 2 mức điện áp
C. Có tốc độ tín hiệu lớn hơn với cùng tốc độ dữ liệu
D. Luôn có sự chuyển mức ở giữa của chu kỳ bit tín hiệu
ans: D

Câu 80: Vì sao chuẩn Ethernet không dây (IEEE 802.11) sử dụng kỹ thuật truy cập đường truyền CSMA/CA thay vì CSMA/CD vẫn có khả năng giảm giảm thời gian phát lại khi có xung đột?
A. Vì CSMA/CD yêu cầu đường truyền dây trị tốc độ cố định
B. Vì CSMA/CA cho tốc độ truyền tốt hơn
C. Vì môi trường truyền không dây có đặc thù nhiều nhiễu hơn nên truyền không truyền đến hết các máy trong mạng
D. Vì CSMA/CD yêu cầu thiết bị phức tạp hơn
ans: C
```

----- Page 27 -----
```md
Câu 81: Vì sao tầng giao vận có thêm định danh CỔNG (PORT) khi đã có địa chỉ IP và địa chỉ MAC để giải đề từ máy nguồn đến máy đích?
A. Máy dịch còn thông tin công cho việc xử lý dữ liệu trên tầng ứng dụng
B. Máy gửi dùng thông tin công cho mục đích bảo mật chống tấn công
C. Máy dịch và nguồn cần thông tin công để phân biệt các ứng dụng giao tiếp mạng trên cùng một máy
D. Router cần thông tin công cho việc định tuyến
ans: C

Câu 82: Cho sơ đồ với bảng địa chỉ MAC và kết nối các máy như hình trên. Khi A gửi gói tin với địa chỉ đích là D đến switch thì sẽ .....
img: assets/mc_03_06.png
A. Cập nhật bảng địa chỉ MAC của A vào bảng địa chỉ MAC
B. Cập nhật địa chỉ MAC của D vào bảng địa chỉ MAC
C. Gửi gói tin theo cổng số 4 kết nối đến D
D. Gửi gói tin qua bốn đến các cổng từ 2 – 6
E. Gửi gói tin qua bốn đến các cổng từ 1 – 6
ans: A,E
```

----- Page 28 -----
```md
Câu 83: Nguyên tắc "longest matching" được áp dụng khi một địa chỉ đích khớp với trong nhiều dòng của một bảng định tuyến vì ...
A. Vì mạng có số bit cho phần NetworkID càng lớn thì mạng càng nhỏ và gói tin nhiều khả năng đến đích nhanh hơn
B. Vì sẽ giúp giảm tải cho bộ định tuyến
C. Vì đó là giao tiếp mạng có băng thông lớn nhất
D. Vì mạng với số bit phần NetworkID càng lớn thì mạng càng lớn và tăng khả năng gói tin đến được đích
ans: A

Câu 84: Mô tả bài tập
Dữ liệu của một gói tin gồi địa là 1010011010001 (đang nhị phân). Mã CRC cần gán vào cho dữ liệu là bao nhiêu khi biết rằng G = 10011 (đang nhị phân). Lưu ý chỉ ghi mã CRC dưới dạng nhị phân, không ghi thêm bất cứ kí tự nào
A. 0100
B. 0101
C. 0110
D. 0111
ans: A

Câu 85: Sắp xếp các giao thức định tuyến sau vào đúng loại của mình
Routing Information Protocol – RIP
A. Nội vùng - trạng thái liên kết (link-state)
B. Nội vùng - khoảng cách vector (distance vector)
C. Liên vùng
Open Shortest Path First – OSPF
A. Nội vùng - trạng thái liên kết (link-state)
B. Nội vùng - khoảng cách vector (distance vector)
C. Liên vùng
Enhanced Interior Gateway Routing Protocol – EIGRP
A. Nội vùng - trạng thái liên kết (link-state)
B. Nội vùng - khoảng cách vector (distance vector)
C. Liên vùng
Border Gateway Protocol – BGP
A. Nội vùng - trạng thái liên kết (link-state)
B. Nội vùng - khoảng cách vector (distance vector)
C. Liên vùng
ans: B,A,B,C
```

----- Page 29 -----
```md
```

----- Page 30 -----
```md
Câu 86: Đâu là các phát biểu ĐÚNG về giao thức định tuyến liên vùng và nội vùng
A. Giao thức định tuyến liên vùng (BGP) quan tâm đến hiệu năng (performance) hơn là chính sách (policy)
B. Giao thức định tuyến nội vùng thường dựa trên 2 thuật toán đơng link-state và distance vector
C. Giao thức định tuyến liên vùng (BGP) dựa trên link-state
D. Giao thức định tuyến nội vùng của các miền tự trị (AS) khác nhau có thể khác nhau
ans: B,D

Câu 87: (Các) thiết bị mạng nào dưới đây hoạt động ở tầng 1-2-3 trong mô hình TCP/IP
A. Repeater
B. Hub
C. Bridge
D. Switch
E. Router
F. Computer
ans: E,F
```

----- Page 31 -----
```md
Câu 88: Sắp xếp các giao thức định tuyến sau vào đúng loại của mình
Routing Information Protocol - RIP
Chọn một tùy chọn
Open Shortest Path First - OSPF
Chọn một tùy chọn
Border Gateway Protocol - BGP
Chọn một tùy chọn
ans: [không chắc]

Câu 89: (tối đa 1 điểm, không tính lũy vào tiến trình học)
Khi nhận được một gói tin, router chuyển tiếp gói tin ra cổng tương ứng dựa trên
A. Chính sách do người quản trị mạng đề ra
B. Giao thức định tuyến được thiết lập
C. Các dòng thông tin trong bảng định tuyến
D. Theo cấu hình do máy gửi yêu cầu
ans: C
```

----- Page 32 -----
```md
Câu 90: (đạt 0.0/1.5 điểm, không tính lũy vào tiến trình học)
Cho các địa chỉ mạng dưới đây thuộc các phân lớp nào khi sử dụng cơ chế phân lớp?
150.55.1.128
Chọn một tùy chọn
192.168.1.128
Chọn một tùy chọn
10.168.255.240
Chọn một tùy chọn
200.168.1.128
Chọn một tùy chọn
ans: [không chắc]

Câu 91: (đạt 1/1 điểm, không tích lũy vào tiến trình học)
Các gói tin có độ dài là 1500 bytes được truyền qua đường dây cáp quang với tốc độ 2.5 Mbps. Độ dài của đường dây là 290 km. Biết tốc độ lan truyền thông tin là 200000 km/s. Hỏi thời gian để truyền một gói tin là bao nhiêu micro giây? (chỉ ghi số, không ghi đơn vị)
A. 1930
B. 193
C. 19300
D. 193000
ans: A

Câu 92: (đạt 1/1 điểm, không tích lũy vào tiến trình học)
Đâu là các phát biểu ĐÚNG về giao thức định tuyến liên vùng và nội vùng
A. Giao thức định tuyến liên vùng (BGP) quan tâm đến hiệu năng (performance) hơn là chính sách (policy)
B. Giao thức định tuyến nội vùng thường dựa trên 2 thuật toán dạng link-state và distance vector
C. Giao thức định tuyến liên vùng (BGP) dựa trên link-state
D. Giao thức định tuyến nội vùng của các miền tự trị (AS) khác nhau có thể khác nhau
ans: B,D

Câu 93: (đạt 1/1 điểm, không tích lũy vào tiến trình học)
(Các) ưu điểm của các thuật toán định tuyến dựa trên vector khoảng cách (distance vector) so với các thuật toán định tuyến trạng thái liên kết (link - state) là
A. Có tốc độ hội tụ nhanh hơn
B. Yêu cầu khả năng tính toán của router thấp hơn
C. Áp dụng được cho các mạng cỡ trung bình và lớn
ans: B
```

----- Page 33 -----
```md
Câu 94: Trong phương pháp điều khiển truy cập đường truyền CSMA, vì sao dung độ vẫn xảy ra dù các máy đó lắng nghe trước khi truyền?
A. Do có độ trễ lan truyền thông tin trong đường truyền
B. Có những máy truyền trên các tần số mây khác không lắng nghe được
C. Các máy mất đồng bộ nên không thể lắng nghe tin hiệu trên đường truyền
D. Các phương án khác đều sai
ans: A

Câu 95: Trong các phát biểu sau, phát biểu nào là ĐÚNG về địa chỉ MAC
A. Có độ dài 48 bit
B. Mỗi nhà sản xuất CHỈ CÓ MỘT số OUI
C. Địa chỉ MAC có thể thay đổi khi một máy kết nối với các mạng khác nhau
D. Router dùng địa chỉ MAC để xác định đường đi
E. Có 24 bit đầu là số OUI để phân biệt các nhà sản xuất
F. Một thiết bị đầu cuối (máy tính, điện thoại thông minh) chỉ có thể có một địa chỉ MAC
ans: A,E
```

----- Page 34 -----
```md
Câu 96: Lượng dữ liệu tối đa truyền qua một đường truyền trong một đơn vị thời gian là
A. Thông lượng
B. Tốc độ lan truyền
C. Tốc độ xử lý
D. Băng thông
ans: D

Câu 97: Đâu là các phát biểu ĐÚNG về giao thức định tuyến liên vùng và nội vùng
A. Giao thức định tuyến liên vùng (BGP) quan tâm đến hiệu năng (performance) hơn là chính sách (policy)
B. Giao thức định tuyến nội vùng thường dựa trên 2 thuật toán dạng link-state và distance vector
C. Giao thức định tuyến liên vùng (BGP) dựa trên link-state
D. Giao thức định tuyến nội vùng của các miền tự trị (AS) khác nhau có thể khác nhau
ans: B,D

Câu 98: (Các) thiết bị mạng nào dưới đây hoạt động cả ở tầng 1-2-3 trong mô hình TCP/IP
A. Repeater
B. Hub
C. Bridge
D. Switch
E. Router
F. Computer
ans: E,F
```

----- Page 35 -----
```md
Câu 99: Trong các loại đường truyền dưới đây, đường truyền nào cho khả năng truyền tải với băng thông tốt nhất?
A. Cáp xoắn đôi
B. Cáp đồng trục
C. Cáp quang
D. Truyền không dây
ans: C

Câu 100: Trong các phát biểu sau, phát biểu nào là ĐÚNG về địa chỉ MAC
A. Có độ dài 48 bit
B. Mỗi nhà sản xuất CHỈ CÓ MỘT số OUI
C. Địa chỉ MAC có thể thay đổi khi một máy kết nối với các mạng khác nhau
D. Router dùng địa chỉ MAC để xác định đường đi
E. Có 24 bit đầu là số OUI để phân biệt các nhà sản xuất
F. Một thiết bị đầu cuối (máy tính, điện thoại thông minh) chỉ có thể có một địa chỉ MAC
ans: A,E
```

----- Page 36 -----
```md
Câu 101: Vì sao chuẩn Ethernet không dây (IEEE 802.11) sử dụng kỹ thuật truy cập đường truyền CSMA/CA thay vì CSMA/CD vốn có khả năng giảm giảm thời gian phát lại khi có xung đột?
A. Vì CSMA/CA cho tốc độ truyền tốt hơn
B. Vì CSMA/CD yêu cầu đường truyền dây trì tốc độ cố định
C. Vì CSMA/CD yêu cầu thiết bị phức tạp hơn
D. Vì môi trường truyền không dây có đặc thù nhiều nên nhiều trường hợp tin hiệu truyền không truyền đến hết các máy trong mạng
ans: D

Câu 102: (Các) thiết bị mạng nào dưới đây hoạt động cả ở tầng 1–2–3 trong mô hình TCP/IP
A. Repeater
B. Hub
C. Bridge
D. Switch
E. Router
F. Computer
ans: E,F

Câu 103: Đường kết nối mạng sử dụng công nghệ ADSL là dựa vào kỹ thuật chia kênh nào?
A. Kỹ thuật khác
B. Chia kênh mã code (CDMA)
C. Chia kênh tần số (FDMA)
ans: C
```

----- Page 37 -----
```md
Câu 104: Chia kênh thời gian (TDMA)
A. Chia kênh thời gian (TDMA)
ans: A

Câu 105: Việc phân chia mạng theo CIDR thay vì theo phân lớp đem lại lợi ích gì?
A. Tận dụng được không gian địa chỉ tốt hơn
B. Không có đáp án đúng
C. Cho phép chia thành nhiều phân lớp hơn so với trước
D. Có thể chia nhỏ thành nhiều mạng con (subnet)
ans: A

Câu 106: Nguyên tốc "longest matching" được áp dụng khi một địa chỉ đích khác với trong nhiều dòng của một bảng định tuyến vì ...
A. Vì đó là giao tiếp mạng có băng thông lớn nhất
B. Vì sẽ giảm giảm tải cho bộ định tuyến
C. Vì mạng có số bit cho phần NetworkID càng lớn thì mạng càng nhỏ và giải tin nhiều khả năng đến đích nhanh hơn
D. Vì mạng với số bit phần NetworkID càng lớn thì mạng càng lớn và tăng khả năng giải tin đến đứng đích
ans: C
```

----- Page 38 -----
```md
Câu 107: Một gói tin IP có kích thước là 2420 bytes, bao gồm 20 bytes là phần header. Gói tin này phải đi qua một đường kết nối có MTU=1100 bytes. Hỏi:
Gói tin phải phân chia thành mấy mảnh (fragment)?
A. 2
B. 3
C. 4
D. 5
ans: B

Câu 108: Trường offset của phần mảnh thứ 2 có giá trị là bao nhiêu
A. 128
B. 135
C. 140
D. 145
ans: B

Câu 109: Cho mô hình mạng gồi gồ tin từ C đến D như hình trên. Khi gói tin từ máy C gửi đến Switch 1 thì Địa chỉ MAC nguồn của gói tin tổng liên kết dữ liệu là
A. 111.111.111.111
B. CC-49-DE-D0-AB-7D
C. 222.222.222.222
D. 49-BD-C6-C7-90-3A
ans: B

Câu 110: Địa chỉ MAC đích của gói tin tổng liên kết dữ liệu là
A. 111.111.111.111
B. CC-49-DE-D0-AB-7D
C. 222.222.222.222
D. E6-E9-00-17-BB-4B
ans: D
```

----- Page 39 -----
```md
Câu 111: Địa chỉ IP nguồn của gói tin trong mạng là
A. 111.111.111.112
B. 222.222.222.221
C. 10.0.0.1
D. 192.168.1.1
ans: A

Câu 112: Địa chỉ IP đích của gói tin trong mạng là
A. 111.111.111.112
B. 222.222.222.221
C. 10.0.0.1
D. 192.168.1.1
ans: B

Câu 113: Đâu là các phát biểu ĐÚNG về giao thức định tuyến liên vùng và nội vùng
A. Giao thức định tuyến liên vùng (BGP) quan tâm đến hiệu năng (performance) hơn là chính sách (policy)
B. Giao thức định tuyến nội vùng thường dựa trên 2 thuật toán dạng link-state và distance vector
C. Giao thức định tuyến liên vùng (BGP) dựa trên link-state
D. Giao thức định tuyến nội vùng của các miền tự trị (AS) khác nhau có thể khác nhau
ans: B,D

Câu 114: Vì sao tổng giao vận có thêm định danh CỔNG (PORT) khi đó có địa chỉ IP và địa chỉ MAC để gửi dữ liệu từ máy nguồn đến máy đích?
A. Router cần thông tin cổng cho việc định tuyến
B. Máy gửi dùng thông tin cổng cho máy đích báo mật chống tấn công
C. Máy đích và nguồn cần thông tin cổng để phân biệt các ứng dụng giao tiếp mạng trên cùng một máy
D. Máy đích cần thông tin cổng cho việc xử lý dữ liệu trên tầng ứng dụng
ans: C

Câu 115: Khi sử dụng DHCP, chuyện gì xảy ra khi một client (máy tính) nhận được 2 offer từ 2 DHCP server khác nhau?
A. Client lựa chọn offer đến sớm hơn
B. Không có đáp án đúng
C. Client lựa chọn offer đến muộn hơn
D. Client từ chối cả 2 offer
ans: A
```

----- Page 40 -----
```md
Câu 116: Khi sử dụng DHCP, chuyện gì xảy ra khi một client (máy tính) nhận được 2 offer từ 2 DHCP server khác nhau?
A. Client từ chối cả 2 offer do xung đột
B. Client chấp nhận cả 2 offer
C. Client lựa chọn offer theo chính sách người quản trị để ra
D. Client lựa chọn offer đến sớm hơn
ans: D
```

----- Page 41 -----
```md
Câu 117: Cho các địa chỉ mạng dưới đây, hãy lựa chọn loại địa chỉ hợp lệ
A. 192.168.1.128/25 - Địa chỉ mạng
B. 192.168.1.128/24 - Địa chỉ máy
C. 192.168.1.255/25 - Địa chỉ quảng bá
D. 192.168.1.255/23 - Không hợp lệ
E. 192.168.1.255/23 - Địa chỉ quảng bá
F. 192.168.2.255/23 - Địa chỉ máy
G. 192.168.2.0/23 - Địa chỉ mạng
ans: A,B,C,G

Câu 118: Sắp xếp các giao thức định tuyến sau vào đúng loại của mình
A. Routing Information Protocol - RIP - Nội vùng - trạng thái liên kết (link-state)
B. Open Shortest Path First - OSPF - Nội vùng - vector khoảng cách (distance-vector)
C. Enhanced Interior Gateway Routing Protocol - EIGRP - Liên vùng - trạng thái liên kết (link-state)
D. Border Gateway Protocol - BGP - Liên vùng - vector khoảng cách (distance-vector)
ans: A,B,D
```

----- Page 42 -----
```md
Câu 119: Cho các địa chỉ mạng dưới đây thuộc các phân lớp nào khi sử dụng cơ chế phân lớp?
A. 200.168.1.128
B. 150.55.1.128
C. 10.168.255.240
D. 192.168.1.128
ans: B,C,A,D

Câu 120: Một đường truyền từ A tới B qua 3 kết nối vật lý nối tiếp nhau với băng thông lần lượt là 5 Mbps, 2 Mbps, 1 Mbps. Giả sử các đường kết nối này chỉ phục vụ liên kết giữa A và B và thời gian xử lý và lan truyền dữ liệu là không đáng kể (bằng 0). Hỏi thời gian cần thiết để truyền một gói tin có kích thước 43 MB từ A tới B là bao nhiêu giây?
A. 344
B. 344
C. 344
D. 344
ans: A
```

----- Page 43 -----
```md
Câu 121: Ưu điểm của giao thức UDP so với giao thức TCP là gì?
A. Có điều khiển luồng
B. Tốc độ gửi nhanh hơn
C. Quá trình bắt tay giữa máy nguồn và đích tốt hơn
D. Tin cậy hơn
ans: B
```

----- Page 44 -----
```md
Câu 122: (đạt 1/1 điểm, không tích lũy vào tiến trình học) Chuyện gì xảy ra nếu MTU của một đường truyền kết nối quá nhỏ?
A. Giảm băng thông của đường truyền
B. Tăng khả năng tải bít trên đường truyền
C. Tăng khả năng tác nghẽn do số gói tin tăng lên
D. Giảm hiệu suất truyền dữ liệu do phản header dồn kích thước cố định
ans: D

Câu 123: (đạt 1/1 điểm, không tích lũy vào tiến trình học) Lương dữ liệu tối đa truyền qua một đường truyền trong một đơn vị thời gian là:
A. Thông lượng
B. Tốc độ lan truyền
C. Tốc độ xử lý
D. Băng thông
ans: D

Câu 124: (đạt 1/1 điểm, không tích lũy vào tiến trình học) Trong các loại đường truyền dưới đây, đường truyền nào cho khả năng truyền tải với băng thông tốt nhất?
A. Cáp xoắn đôi
B. Cáp đồng trục
C. Cáp quang
D. Truyền không dây
ans: C
```

----- Page 45 -----
```md
Câu 125: Đâu là những nhược điểm của cáp quang so với các loại cáp khác?
A. Giá thành đắt đỏ
B. Lắp đặt phức tạp do cần thiết bị chuyên dụng
C. Dễ suy hao tín hiệu
D. Dễ bị ảnh hưởng bởi nhiều từ sóng điện từ
E. Dễ hư hỏng
F. Kích thước lớn
ans: A,B,E

Câu 126: Vì sao khi sử dụng mã hóa Manchester và Manchester vi sai không xảy ra tình trạng mất đồng bộ giữa máy gửi và máy nhận?
A. Luôn có sự chuyển mức ở giữa các chu kỳ bit tín hiệu
B. Chỉ sử dụng 2 mức điện áp
C. Các đợt tín hiệu dài đều nhau
D. Có tốc độ tín hiệu lớn hơn với cùng tốc độ dữ liệu
ans: A

Câu 127: Trong các phát biểu sau, phát biểu nào là ĐÚNG về địa chỉ MAC
A. Có độ dài 48 bit
B. Mỗi nhà sản xuất CHỈ CÓ MỘT số OUI
C. Địa chỉ MAC có thể thay đổi khi một máy kết nối với các mạng khác nhau
D. Router dùng địa chỉ MAC để xác định đường đi
E. Có 24 bit đầu là số OUI để phân biệt các nhà sản xuất
F. Một thiết bị đầu cuối (máy tính, điện thoại thông minh) chỉ có thể có một địa chỉ MAC
ans: A,E
```

----- Page 46 -----
```md
Câu 128: Đường kết nối mạng sử dụng công nghệ ADSL, là dựa vào kỹ thuật chia kênh nào?
A. Kỹ thuật khác
B. Chia kênh mã code (CDMA)
C. Chia kênh tần số (FDMA)
D. Chia kênh thời gian (TDMA)
ans: C

Câu 129: Trong phương pháp điều khiển truy cập đường truyền CSMA, vì sao đụng độ vẫn xảy ra dù các máy đã lắng nghe trước khi truyền?
A. Do có độ trễ truyền thông tin trong đường truyền
B. Có những máy truyền trên các tần số máy khác không lắng nghe được
C. Các máy một đứng bị nên không thể lắng nghe tín hiệu trên đường truyền
D. Các phương án khác đều sai
ans: A

Câu 130: Cho switch với bảng địa chỉ MAC và kết nối các máy như hình trên. Khi A gửi tin với địa chỉ đích là D, đến switch thì switch sẽ ...
A. Cập nhật bảng địa chỉ MAC của A vào bảng địa chỉ MAC
B. Cập nhật địa chỉ MAC của D vào bảng địa chỉ MAC
C. Gửi gói tin theo cổng số 4 kết nối đến D
D. Gửi gói tin qua bộ đệm các cổng từ 2~6
E. Gửi gói tin qua bộ đệm các cổng từ 1~6
ans: A,E
```

----- Page 47 -----
```md
Câu 131: Thiết bị mạng nào dưới đây hoạt động cả ở tầng 1-2-3 trong mô hình TCP/IP
A. Repeater
B. Hub
C. Bridge
D. Switch
E. Router
F. Computer
ans: E,F

Câu 132: Cho mô hình mạng gồi gói tin từ C đến D như hình trên. Khi gói tin từ máy C gửi đến Switch 1 thì địa chỉ MAC nguồn của gói tin tổng tiến kết dữ liệu là
A. CC-49-DE-D0-AB-7D
B. E6-E9-00-17-BB-8B
C. 111.111.111.112
D. 222.222.222.221
ans: B

Câu 133: Địa chỉ IP đích của gói tin tổng mạng là
A. CC-49-DE-D0-AB-7D
B. E6-E9-00-17-BB-8B
C. 111.111.111.112
D. 222.222.222.221
ans: D
```

----- Page 48 -----
```md
Câu 134: Vì sao chuẩn Ethernet không dây (IEEE 802.11) sử dụng kỹ thuật truy cập đường truyền CSMA/CA thay vì CSMA/CD vốn có khả năng giảm giảm thiểu giam phát bị lỗi và xung đột?
A. Vì CSMA/CA cho tốc độ truyền tốt hơn
B. Vì CSMA/CD yêu cầu đường truyền dự trữ đủ rộng
C. Vì CSMA/CD yêu cầu thiết bị phải toàn hơn
D. Vì môi trường truyền không dây có đặc thù nên không thể thực hiện việc truyền không truyền đến hết các máy trong mạng
ans: D

Câu 135: Khi sử dụng DHCP, chuyện gì xảy ra khi một client (máy tính) nhận được 2 offer từ 2 DHCP server khác nhau?
A. Client lựa chọn offer đến sớm hơn
B. Không có đáp án đúng
C. Client từ chối cả 2 offer đo xung đột
D. Client chấp nhận cả 2 offer
E. Client lựa chọn offer theo chính sách người quản trị đề ra
ans: A
```

----- Page 49 -----
```md
Câu 136: Cho các địa chỉ mạng dưới đây, hãy lựa chọn loại địa chỉ hợp lệ:
A. 192.168.1.128/25
B. 192.168.1.128/24
C. 192.168.1.255/25
D. 192.168.1.256/23
E. 192.168.1.255/23
F. 192.168.2.255/23
G. 192.168.2.0./23
ans: A,C,F

Câu 137: Việc phân chia mạng theo CIDR thay vì theo phân lớp đem lại lợi ích gì?
A. Tận dụng được không gian địa chỉ tốt hơn
B. Không có đáp án đúng
C. Cho phép chia thành nhiều phân lớp hơn so với trước
D. Có thể chia nhỏ thành nhiều mạng con (subnet)
ans: A
```

----- Page 50 -----
```md
Câu 138: Cho các địa chỉ mạng dưới đây thuộc các phân lớp nào khi sử dụng cơ chế phân lớp?
150.55.1.128
A. 10.168.255.240
B. 192.168.1.128
C. 200.168.1.128
D. 150.55.1.128
ans: B

Câu 139: Khi nhận được một gói tin, router chuyển tiếp gói tin ra cổng tương ứng dựa trên
A. Các dòng thông tin trong bảng định tuyến
B. Theo cấu hình do máy gửi yêu cầu
C. Chính sách do người quản trị mạng đề ra
D. Giao thức định tuyến được thiết lập
ans: A

Câu 140: Nguyên tắc "longest matching" được áp dụng khi một địa chỉ đích khi với trong nhiều dòng của một bảng định tuyến vì...
A. Vì đó là giao tiếp mang có thông thông lớn nhất
B. Vì sẽ giảm giảm tải cho bộ định tuyến
C. Vì trong cơ sở dữ liệu NetworkID cùng lớp thì trong cùng nhỏ và giải trí nhiều khả năng đến đích nhanh hơn
D. Vì trong cơ sở dữ liệu NetworkID cùng lớp thì mạng càng lớn sẽ càng khả năng gói tin đến đích
ans: C
```

----- Page 51 -----
```md
Câu 141: Đâu là các phát biểu ĐÚNG về giao thức định tuyến liên vùng và nội vùng
A. Giao thức định tuyến liên vùng (BGP) quan tâm đến hiệu năng (performance) hơn là chính sách (policy)
B. Giao thức định tuyến nội vùng thường dựa trên 2 thuật toán link-state và distance vector
C. Giao thức định tuyến liên vùng (BGP) dựa trên link-state
D. Giao thức định tuyến nội vùng của các miền tự trị (AS) khác nhau có thể khác nhau
ans: B,D

Câu 142: Sắp xếp các giao thức định tuyến sau vào đúng loại của mình
Routing Information Protocol – RIP
A. Nội vùng - trạng thái liên kết (link-state)
B. Nội vùng - khoảng cách vector (distance vector)
C. Liên vùng
Open Shortest Path First – OSPF
A. Nội vùng - trạng thái liên kết (link-state)
B. Nội vùng - khoảng cách vector (distance vector)
C. Liên vùng
Enhanced Interior Gateway Routing Protocol – EIGRP
A. Nội vùng - trạng thái liên kết (link-state)
B. Nội vùng - khoảng cách vector (distance vector)
C. Liên vùng
Border Gateway Protocol – BGP
A. Nội vùng - trạng thái liên kết (link-state)
B. Nội vùng - khoảng cách vector (distance vector)
C. Liên vùng
ans: B,A,B,C
```

----- Page 52 -----
```md
Câu 143: Vì sao tầng giao vận có thêm định danh CỔNG (PORT) khi đã có địa chỉ IP và địa chỉ MAC để gửi điều từ máy nguồn đến máy đích?
A. Router cần thông tin cổng cho việc định tuyến
B. Máy gửi dùng thông tin cổng cho mục đích báo một chống tấn công
C. Máy đích và nguồn cần thông tin cổng để phân biệt các ứng dụng giao tiếp mạng trên cùng một máy
D. Máy đích cần thông tin cổng cho việc xử lý dữ liệu trên từng ứng dụng
ans: C

Câu 144: Ưu điểm của giao thức UDP so với giao thức TCP là gì?
A. Có điều khiển luồng
B. Tốc độ gửi nhanh hơn
C. Quá trình bắt tay giữa máy nguồn và đích tốt hơn
D. Tin cậy hơn
ans: B
```

----- Page 53 -----
```md
Câu 145: Hãy tính số mạng con tối đa có thể chia từ? (Chỉ ghi số)
A. 32
B. 33
ans: A

Câu 146: Số máy tối đa trong mỗi mạng con là? (Chỉ ghi số)
A. 2046
B. 2046
ans: A

Câu 147: Giá trị phân chia thành mấy mảnh (fragment)?
A. 3
B. 3
ans: A

Câu 148: Trường offset của phân mảnh thứ 2 có giá trị là bao nhiêu
A. 135
B. 135
ans: A

Câu 149: Giá trị phân chia thành mấy mảnh (fragment)?
A. 2
B. 2
ans: A

Câu 150: Trường offset của phân mảnh thứ 2 có giá trị là bao nhiêu
A. 175
B. 175
ans: A
```

----- Page 54 -----
```md
Câu 151: Truyền tin (đơn đường truyền) - Một đường truyền từ A đến B gồm 3 kết nối với tổng tốc độ lần lượt là 5 Mbps, 5 Mbps, 20 Mbps. Giả sử các đường kết nối này chỉ phục vụ liên kết giữa A và B và thời gian xử lý và lan truyền đều lấy là không đáng kể (bằng 0). Hỏi thời gian cần thiết để truyền một gói tin có kích thước 2,3 MB từ A tới B là bao nhiêu giây? Chỉ ghi số giây, không ghi đơn vị hay bất cứ từ từ nào khác. Thường hợp số giây là, làm tròn đến 2 chữ số sau phần thập phân.
A. 36,8
B. 35,8
ans: A

Câu 152: CRC - Mô tả liên kết bằng tích lũy vào (tiến trình học) - Để liệu của một gói tin gửi đi là 110111011001 (dạng nhị phân). Mã CRC cần gắn vào cho dữ liệu bao nhiêu bit (dùng G = 10111 (dạng nhị phân)). Lưu ý chỉ ghi mã CRC dưới dạng nhị phân, không ghi thêm bất cứ kí tự nào.
A. 0100
B. 0100
ans: A

Câu 153: Truyền tin qua nhiều đường truyền - Một đường truyền từ A đến B gồm 3 kết nối với tổng tốc độ lần lượt là 5 Mbps, 2 Mbps, 1 Mbps. Giả sử các đường kết nối này chỉ phục vụ liên kết giữa A và B và thời gian xử lý và lan truyền đều lấy là không đáng kể (bằng 0). Hỏi thời gian cần thiết để truyền một gói tin có kích thước 4,3 MB từ A tới B là bao nhiêu giây? Chỉ ghi số giây, không ghi đơn vị hay bất cứ từ từ nào khác. Thường hợp số giây là, làm tròn đến 2 chữ số sau phần thập phân.
A. 34,4
B. 34,1
C. 60
ans: A

Câu 154: Thời gian truyền tin - Thời gian truyền tin 1/1 point (ungraded) - Mô tả bài tập - Các gói tin có độ dài là 1200 bytes được truyền qua đường dây cáp quang với tốc độ 28 Mbps. Độ dài của đường dây là 1200 km. Biết tốc độ lan truyền thông tin là 200000 km/s. Hỏi thời gian để truyền một gói tin là bao nhiêu micro giây? (Chỉ ghi số, không ghi đơn vị)
A. 1484
B. 1484
ans: A
```

----- Page 55 -----
```md
Câu 155: Cho switch với bảng địa chỉ MAC và kết nối các máy như hình trên. Khi A gửi gói tin vừa địa chỉ D đến switch thì switch sẽ ... **(Chọn 2 đáp án)**
A. Cập nhật bảng địa chỉ MAC của A vào bảng địa chỉ MAC
B. Cập nhật địa chỉ MAC của D vào bảng địa chỉ MAC
C. Gửi gói tin theo cổng số 4 kết nối đến D
D. Gửi gói tin quảng bá đến các cổng từ 2~6
E. Gửi gói tin quảng bá đến các cổng từ 1~6
ans: A,D

Câu 156: Đâu là những nhược điểm của các quang sợi các tọi cáp khác? **(Chọn 4 đáp án)**
A. Giới thành đắt đỏ
B. Lắp đặt phức tạp do cần thiết bị chuyên dụng
C. Dễ suy hao tín hiệu
D. Dễ bị ảnh hưởng bởi nhiễu từ sóng điện từ
E. Dễ hư hỏng
F. Kích thước lớn
ans: A,B,E,F
```

----- Page 56 -----
```md
Câu 157: Dã liên của một gói tin gửi đi là 100110101101 (dạng nhị phân). Mã CRC cần gắn vào cho dãy liệu là bao nhiêu biết rằng G = 1101 (dạng nhị phân). Lưu ý chỉ ghi mã CRC dưới dạng nhị phân, không ghi thêm bất cứ kí tự nào
A. 110
B. 111
C. 101
D. 100
ans: A [suy luận]

Câu 158: Một gói tin IP có kích thước là 2420 bytes, bao gồm 20 bytes là phần header. Gởi tin này phải đi qua một đường kết nối có MTU=1420 bytes. Hỏi:
Phân mảnh gói tin (đạt 1.0/1.0 điểm, không tích lũy vào tiến trình học)
Gói tin phân chia thành mấy mảnh (fragment)?
A. 2
B. 3
C. 4
D. 5
ans: A

Câu 159: Trường offset của phần mảnh thứ 2 có giá trị là bao nhiêu
A. 175
B. 176
C. 177
D. 178
ans: A

Câu 160: Cho các địa chỉ mạng dưới đây, hãy lựa chọn loại địa chỉ hợp lệ (đạt 2.0/2.0 điểm, không tích lũy vào tiến trình học)
192.168.1.128/25
A. Địa chỉ mạng
B. Địa chỉ máy
C. Địa chỉ quảng bá
D. Không hợp lệ
ans: B

Câu 161: 192.168.1.128/24
A. Địa chỉ mạng
B. Địa chỉ máy
C. Địa chỉ quảng bá
D. Không hợp lệ
ans: B

Câu 162: 192.168.1.255/25
A. Địa chỉ mạng
B. Địa chỉ máy
C. Địa chỉ quảng bá
D. Không hợp lệ
ans: C

Câu 163: 192.168.1.256/23
A. Địa chỉ mạng
B. Địa chỉ máy
C. Địa chỉ quảng bá
D. Không hợp lệ
ans: D
```

----- Page 57 -----
```md
Câu 164: 192.168.1.255/23
A. Địa chỉ mạng
B. Địa chỉ máy
C. Địa chỉ quảng bá
D. Không hợp lệ
ans: C

Câu 165: 192.168.2.256/23
A. Địa chỉ mạng
B. Địa chỉ máy
C. Địa chỉ quảng bá
D. Không hợp lệ
ans: D

Câu 166: 192.168.2.0/23
A. Địa chỉ mạng
B. Địa chỉ máy
C. Địa chỉ quảng bá
D. Không hợp lệ
ans: A
```

----- Page 58 -----
```md
Câu 167: Vì sao khi sử dụng mã hóa Manchester và Manchester với không xảy ra tình trạng mất đồng bộ giữa máy gửi và máy nhận?
A. Các đáp án khác đều sai
B. Luôn có sự chuyển mức ở giữa các chu kỳ bit tín hiệu
C. Có tốc độ tín hiệu lớn hơn với cùng tốc độ dữ liệu
D. Chỉ sử dụng 2 mức điện áp
ans: B

Câu 168: Lượng dữ liệu tối đa truyền qua một đường truyền trong một đơn vị thời gian là
A. Thông lượng
B. Tốc độ xử lý
C. Tốc độ lan truyền
D. Băng thông
ans: D

Câu 169: Đâu là những nhược điểm của cặp quang so với các loại cáp khác?
A. Giá thành đắt đỏ
B. Lắp đặt phức tạp do cần thiết bị chuyên dụng
C. Độ suy hao tín hiệu lớn
D. Dễ bị ảnh hưởng bởi nhiễu từ sóng điện từ
E. Dễ hư hỏng
F. Kích thước lớn
ans: A,B,E
```

----- Page 59 -----
```md
Câu 170: Các gói tin có độ dài là 1000 bytes được truyền qua đường dây cáp quang với tốc độ 200 Mbps. Độ dài của đường dây là 380 km. Biết tốc độ lan truyền thông tin là 200000 km/s. Hỏi thời gian để truyền một gói tin là bao nhiêu micro giây? (chỉ ghi số, không ghi đơn vị)
A. 1940
B. 194
C. 19.4
D. 1.94
ans: A

Câu 171: Cho các địa chỉ mạng dưới đây thuộc các phân lớp nào khi sử dụng cả chế phân lớp?
150.55.1.128
A. Lớp B
B. Lớp C
C. Lớp A
D. Lớp D
ans: A

Câu 172: 192.168.1.128 thuộc lớp nào?
A. Lớp B
B. Lớp C
C. Lớp A
D. Lớp D
ans: B

Câu 173: 10.168.255.240 thuộc lớp nào?
A. Lớp A
B. Lớp B
C. Lớp C
D. Lớp D
ans: A

Câu 174: 200.168.1.128 thuộc lớp nào?
A. Lớp A
B. Lớp B
C. Lớp C
D. Lớp D
ans: C
```

----- Page 60 -----
```md
Câu 175: Khi nhận được một gói tin, router chuyển tiếp gói tin ra cổng tương ứng dựa trên
A. Các dòng thông tin trong bảng định tuyến
B. Theo cấu hình do máy gửi yêu cầu
C. Chính sách do người quản trị mạng đề ra
D. Giao thức định tuyến được thiết lập
ans: A

Câu 176: Các gói tin có độ dài là 1200 bytes được truyền qua đường dây có dung lượng với tốc độ 25 Mbps. Độ dài của đường dây là 220 km. Biết tốc độ lan truyền thông tin là 200000 km/s. Hỏi thời gian để truyền một gói tin là bao nhiêu micro giây? (Chỉ ghi số, không ghi đơn vị)
A. 1484
B. 148
C. 14840
D. 148400
ans: A

Câu 177: Trong các phát biểu sau, phát biểu nào là ĐÚNG về địa chỉ MAC
A. Có độ dài 48 bit
B. Mỗi nhà sản xuất CHỈ CÓ MỘT số OUI
C. Địa chỉ MAC có thể thay đổi khi một máy kết nối với các mạng khác nhau
D. Router dùng địa chỉ MAC để xác định đường đi
E. Có 24 bit đầu là số OUI để phân biệt các nhà sản xuất
F. Một thiết bị đầu cuối (máy tính, điện thoại thông minh) chỉ có thể có một địa chỉ MAC
ans: A,E
```

----- Page 61 -----
```md
Câu 178: Cho các địa chỉ mạng dưới đây thuộc các phân lớp nào khi sử dụng cơ chế phân lớp?
A. 150.55.1.128
B. 192.168.1.128
C. 10.168.255.240
D. 200.168.1.128
ans: B,C,A,D

Câu 179: (Các) thiết bị mạng nào dưới đây hoạt động ở tầng 1-2-3 trong mô hình TCP/IP
A. Repeater
B. Hub
C. Bridge
D. Switch
E. Router
F. Computer
ans: E,F
```

----- Page 62 -----
```md
Câu 180: Vì sao khi sử dụng mã hoá Manchester và Manchester vi sai không xảy ra tình trạng mất đồng bộ giữa máy gửi và máy nhận?
A. Luôn có sự chuyển mức ở giữa các chu kỳ bit tín hiệu
B. Chỉ sử dụng 2 mức điện áp
C. Có tốc độ tín hiệu lớn hơn với cùng tốc độ dữ liệu
D. Các cặp án khác đều sai
ans: A

Câu 181: Cho sơ đồ mạng như hình vẽ. Bảng MAC của switch A như sau:

| MAC addr | Interface | TTL |
|:--------:|:---------:|:---:|
| B        | 2         | 60  |

img: assets/mc_03_06_topology.png

Khi A nhận được frame từ máy C gửi đến máy D, switch A sẽ xử lý như thế nào?
A. Forward frame ra tất cả các cổng trừ cổng nhận
B. Forward frame ra cổng 2
C. Forward frame ra cổng 1
D. Drop frame
ans: A [suy luận]
```

----- Page 63 -----
```md
Câu 182: Cho switch với bảng địa chỉ MAC và kết nối các máy như hình trên. Khi A gửi gói tin với địa chỉ đích là D đến switch thì switch sẽ ...
A. Cập nhật bảng địa chỉ MAC của A vào bảng địa chỉ MAC
B. Cập nhật địa chỉ MAC của D vào bảng địa chỉ MAC
C. Gửi gói tin theo cổng số 4 kết nối đến D
D. Gửi gói tin qua bốn các cổng từ 2-6
E. Gửi gói tin qua bốn các cổng từ 1-6
ans: A,D

Câu 183: Trong phương pháp điều khiển truy cập đường truyền CSMA, vì sao đụng độ vẫn xảy ra dù các máy đã lắng nghe trước khi truyền?
A. Có những máy truyền trên các tần số máy khác không lắng nghe được
B. Các phương án khác đều sai
C. Do cố độ tr� lan truyền thông tin trong đường truyền
D. Các máy một đường bộ nên không thể lắng nghe tin hiệu trên đường truyền
ans: C

Câu 184: Cho các địa chỉ mạng dưới đây thuộc các phân lớp nào khi sử dụng có phân lớp?
A. 150.55.1.128 - B
B. 192.168.1.128 - C
C. 10.168.255.240 - A
D. 200.168.1.128 - C
ans: A,B,C
```

----- Page 64 -----
```md
Câu 185: Khi nhận được một gói tin, router chuyển tiếp gói tin ra cổng tương ứng dựa trên
A. Các dòng thông tin trong bảng định tuyến
B. Giao thức định tuyến được thiết lập
C. Theo cấu hình do máy gửi yêu cầu
D. Chính sách do người quản trị mạng đề ra
ans: A

Câu 186: Đâu là những điểm điểm của cáp quang so với các loại cáp khác?
A. Giá thành đắt đỏ
B. Lắp đặt phức tạp do cần thiết bị chuyên dụng
C. Độ suy hao tín hiệu lớn
D. Bị ảnh hưởng bởi nhiễu từ sóng điện từ
E. Dễ hỏng
F. Kích thước lớn
ans: A,B

Câu 187: (Các) thiết bị mạng nào dưới đây hoạt động cả ở tầng 1–2–3 trong mô hình TCP/IP
A. Repeater
B. Hub
C. Bridge
D. Switch
E. Router
ans: E
```

----- Page 65 -----
```md
Câu 188: Vì sao chuẩn Ethernet không dây (IEEE 802.1) sử dụng kỹ thuật truy cập đường truyền CSMA/CA thay vì CSMA/CD với cơ chế nâng giúp giảm thời gian phát khi bị có xung đột?
A. Vì CSMA/CD yêu cầu thiết bị phức tạp hơn
B. Vì CSMA/CA cho tốc độ truyền tốt hơn
C. Vì CSMA/CD yêu cầu đường truyền dây tức tốc độ định
D. Vì môi trường truyền không dây có đặc thù nhiều nên nhiều trường hợp tin hiệu truyền không truyền đến hết các máy trong mạng
ans: D

Câu 189: Trong các loại đường truyền dưới đây, đường truyền nào cho khả năng truyền tải với băng thông tốt nhất?
A. Cáp quang
B. Cáp đồng trục
C. Cáp xoắn đôi
D. Truyền không dây
ans: A
```

----- Page 66 -----
```md
Câu 190: Truyền tin qua nhiều đường truyền (đạt 1/1 điểm, không tích lũy vào tiến trình học)

Một đường truyền từ A tới B qua 3 kết nối vật lý nối tiếp nhau với băng thông lần lượt là 5 Mbps, 5 Mbps, 20 Mbps. Giả sử các đường kết nối này chỉ phục vụ liên kết giữa A và B và thời gian xử lý và lan truyền dữ liệu là không đáng kể (bằng 0). Hỏi thời gian cần thiết để truyền một gói tin có kích thước 23 MB từ A tới B là bao nhiêu giây?

Chỉ ghi số giây, không ghi đơn vị hay bất cứ kí tự nào khác. Trường hợp số giây là, làm tròn đến 2 chữ số sau phần thập phân

A. 36.8
B. 36.8
ans: A

Câu 191: Vì sao khi sử dụng mã hóa Manchester và Manchester vi sai không xảy ra tình trạng mất đồng bộ giữa máy gửi và máy nhận? (đạt 1/1 điểm, không tích lũy vào tiến trình học)
A. Luôn có sự chuyển mức ở giữa các chu kỳ bit tín hiệu
B. Chỉ sử dụng 2 mức điện áp
C. Các đáp án khác đều sai
D. Có tốc độ tín hiệu lớn hơn với cùng tốc độ dữ liệu
ans: A

Câu 192: Trong phương pháp điều khiển truy cập đường truyền CSMA, vì sao dung độ vẫn xảy ra dù các máy đồng nghe trước khi truyền? (đạt 1/1 điểm, không tích lũy vào tiến trình học)
A. Do cơ độ trễ lan truyền không thì trong đường truyền
B. Có những máy truyền trên các tần số máy khác không lắng nghe được
C. Các máy mất đồng bộ nên không thể lắng nghe tín hiệu trên đường truyền
D. Các phương án khác đều sai
ans: A
```

----- Page 67 -----
```md
Câu 193: Mã CRC (đạt 2/2 điểm, không tích lũy vào tiến trình học)
Dữ liệu của một gói tin gửi đi là 1101110110001 (dạng nhị phân). Mã CRC cần gắn vào cho dữ liệu là bao nhiêu biết rằng G = 10111 (dạng nhị phân). Lưu ý chỉ ghi mã CRC dưới dạng nhị phân, không ghi thêm bất cứ ký tự nào

A. 0100
B. 0110
C. 0101
D. 0010

ans: A

Câu 194: Trong các phát biểu sau, phát biểu nào là ĐÚNG về địa chỉ MAC (đạt 1/1 điểm, không tích lũy vào tiến trình học)

A. Có độ dài 48 bit
B. Mỗi nhà sản xuất chỉ có MỘT số OUI
C. Địa chỉ MAC có thể thay đổi khi một máy kết nối với các mạng khác nhau
D. Router dùng địa chỉ MAC để xác định đường đi
E. Có 24 bit đầu là số OUI để phân biệt các nhà sản xuất
F. Một thiết bị bị đầu cuối (máy tính, điện thoại thông minh) chỉ có thể có một địa chỉ MAC

ans: A,E
```

----- Page 68 -----
```md
Câu 195: Cho các địa chỉ mạng dưới đây thuộc các phân lớp nào khi sử dụng cơ chế phân lớp lớp 150.55.1.128
A. 192.168.1.128
B. 192.168.1.128
C. 10.168.255.240
D. 200.168.1.128
ans: B

Câu 196: Đường kết nối mạng sử dụng công nghệ ADSL là dựa vào kỹ thuật chia kênh nào?
A. Chia kênh mã code (CDMA)
B. Chia kênh tần số (FDMA)
C. Kỹ thuật khác
D. Chia kênh thời gian (TDMA)
ans: D

Câu 197: Đâu là các phát biểu ĐÚNG về giao thức định tuyến liên vùng và nội vùng
A. Giao thức định tuyến liên vùng (BGP) quan tâm đến hiệu năng (performance) hơn là chính sách (policy)
B. Giao thức định tuyến nội vùng (OSPF) quan tâm đến hiệu năng (performance) hơn là chính sách (policy)
C. Giao thức định tuyến liên vùng (BGP) quan tâm đến chính sách (policy) hơn là hiệu năng (performance)
D. Giao thức định tuyến nội vùng (OSPF) quan tâm đến chính sách (policy) hơn là hiệu năng (performance)
ans: B,C
```

----- Page 69 -----
```md
Câu 1: Một gói tin IP có kích thước là 2820 bytes, bao gồm 20 bytes là phần header. Gói tin này phải đi qua một đường kết nối có MTU=700 bytes. Hỏi gói tin phải phân chia thành mấy mảnh (fragment)?
A. 2
B. 3
C. 4
D. 5
ans: C

Câu 2: Trường offset của phần mảnh thứ 2 có giá trị là bao nhiêu
A. 80
B. 85
C. 90
D. 95
ans: B

Câu 3: Khi nhận được một gói tin, router chuyển tiếp gói tin ra cổng tương ứng dựa trên
A. Giao thức định tuyến được thiết lập
B. Chính sách do người quản trị mạng đề ra
C. Các dòng thông tin trong bảng định tuyến
D. Theo cấu hình do máy gửi yêu cầu
ans: C
```

----- Page 70 -----
```md
Câu 4: Assume the path from A to B through 3 connection links with the bandwidths of 4Mbps, 2Mbps, and 2 Mbps. If all links only serve the connection between A and B, and propagation delay is nearly zero, how long (seconds) does A need to transfer a 20MB file to B?
A. 340
B. 160
C. 220
D. 200
E. 80
ans: B

Câu 5: What will happen if MTU of a network connection is too small?
A. It increases the error probability
B. It reduces the performance of data transmission because header has a fixed size
C. It increases the network congestion because of the number of packets
D. It reduces the bandwidth of the network connection
ans: B

Câu 6: The first Network was called
A. CRNET
B. NSFNET
C. ASAPNET
D. ARPANET
ans: D

Câu 7: In the layer hierarchy as the data packet moves from the upper to the lower layers, headers are
A. Added
B. Removed
C. Rearranged
D. Modified
ans: A

Câu 8: Which of the following statement(s) are TRUE about the routing table?
A. A router consults the routing table to determine the optimal path for reaching the destination, considering the destination IP address of the incoming IP packets.
B. A router consults the routing table to determine the optimal path for reaching the destination, considering the source IP address of the incoming IP packets.
C. If a router cannot find the matching entry in its routing table for the incoming IP packet, it will broadcast the incoming packet to all ports except the incoming port.
D. If a router cannot find the matching entry in its routing table for the incoming IP packet, it will broadcast the incoming packet to all ports
ans: A

Câu 9: Which of the following statements are TRUE about the self-learning mechanism of switches? (Can be multiple correct answers)
A. When a frame arrives a switch, switch will update its MAC address table based on the source address field of the frame
B. When a frame arrives a switch, switch will update the address table based on the destination address field of the frame
C. When an entry of the MAC address table being updated, it will remain until being updated by the new information.
D. An entry in the MAC address table will expire if left unused and reached the timeout.
ans: A,D

Câu 10: A network uses 4-bit CHECKSUM to detect error caused by network transmission. Providing data as 1001 1011 1101, what is the transmitted checksum code?
A. 1111
B. 0111
C. 0011
D. 1000
E. 0000
F. 1110
G. None of the mentioned
ans: F

Câu 11: Which of the following IPv4 addresses are VALID addresses for allocating IP addresses and for IP address if we use CIDR method for allocating IP addresses and using a prefix routing?
A. 192.168.1.16
B. 10.0.0.1
C. 233.4.256
D. 11.0.0.1
E. 172.15.4.9
F. 172.26.9.4
ans: A,B,E,F

Câu 12: Servers are those computers which provide resources to other computers connected by?
A. Network
B. Mainframe
C. Super computer
D. Client
ans: A

Câu 13: Which type of network would use phone lines?
A. WAN
B. LAN
C. Wireless
D. WWAN
ans: A

Câu 14: A device that connects to a network without the use of cables is said to be?
A. Distributed
B. Centralised
C. Wireless
D. Open source
ans: C

Câu 15: Switch is associated with ____ network?
A. Bus
B. Ring
C. Star
D. Mesh
ans: C

Câu 16: Which of the following represents the fastest data transmission speed?
A. bps
B. Mbps
C. Gbps
D. Kbps
ans: C

Câu 17: In OSI network architecture, the routing is performed by?
A. Network layer
B. Transport layer
C. Data link layer
D. Application layer
ans: A

Câu 18: How many bits are there in the ethernet address?
A. 64 bits
B. 48 bits
C. 32 bits
D. 16 bits
ans: B

Câu 19: Why do we need ports in Transport Layer while we have IP address to send data packet to the destinated computer?
A. Routers need port information for routing
B. A destinated computer needs port information for data processing
C. A destinated computer needs port information to distinguish/ separate its programs
D. Senders use port information to hide themselves from intruders
ans: C

Câu 20: What is the disadvantage of dynamic routing protocols?
A. Backup link cannot be used
B. Difficult to manage
C. Difficult to adapt with changes of network structure
D. Insecure
ans: C

Câu 21: A network uses parity bit to detect error caused by network transmission. Providing data as 1001 1100, what parity code should be used?
A. 0
B. 1
C. 10
D. 11
ans: B

Câu 22: A datagram (1011 1000 0011 1100) was sent using Cyclic Redundancy Check (CRC) for error detection. Knowing that G = 1001, what is the transmitted frame?
A. 1011 1000 0011 1100 000
B. 1011 1000 0011 1100 011
C. 1011 1000 0011 1100 100
D. 1011 1000 0011 1100 101
ans: B
```

----- Page 71 -----
```md
Câu 23: Among the optical-distribution architectures that are essentially switched ethernet is _______________.
A. PON
B. MON
C. AON
D. NON
ans: C

Câu 24: In wireless ad-hoc network,
A. Access point is must
B. All nodes are access points
C. Access point is not required
D. Access point is not required only for edge devices
ans: C

Câu 25: Which of these is not a network edge device?
A. Switch
B. PC
C. Smartphone
D. Laptop
ans: A

Câu 26: Which multiple access technique is used by IEEE 802.11 standard for wireless LAN?
A. CDMA
B. CSMA/CA
C. CSMA/CD
D. ALOHA
ans: B

Câu 27: Which field helps to check rearrangement of the fragments?
A. Flag
B. Identifier
C. TTL
D. Offset
ans: D

Câu 28: In classful addressing, a large part of available addresses are ________.
A. Organized
B. Blocked
C. Wasted
D. Communicated
ans: C

Câu 29: Which of the following devices are working at the Datalink layer in the OSI Reference Model?(Can be multiple correct answers)
A. Repeater
B. Hub
C. Bridge
D. Switch
E. Router
F. Personal computer
ans: C,D

Câu 30: How many layers are in the TCP/IP model?
A. 5
B. 6
C. 7
D. 4
ans: D

Câu 31: Which of the following items is not used in Local Area Networks (LAN)?
A. Interface card
B. Cable
C. Computer
D. Modem
ans: D

Câu 32: Which transmission media offers the highest potential transmission speed in a network?
A. Coaxial cable
B. Twisted-pair cable
C. Optical cable
D. Electric cable
ans: C

Câu 33: An alternate name for the completely interconnected network topology is?
A. Mesh
B. Star
C. Tree
D. Ring
ans: A

Câu 34: What is the benefit of UDP in comparison with TCP?
A. Higher speed
B. Flow control
C. More reliable
D. Better handshaking step
ans: A

Câu 35: Given a Network connection between two hosts with a Round-Trip Time (RTT) of 100 ms, a bandwidth rate of 15 Mbps, and a maximum payload size of 1500 bytes, if we need to transfer 15000 bytes of data using the stop-and-wait mechanism, how long would it take to complete the data transfer? (in milliseconds)
A. 1080
B. 1005
C. 40
D. 1000
E. 104
F. 1040
ans: F

Câu 36: What will the switch do when it receives a frame with destination address 12-12-12-ab-ab-ab and source address 11-11-11-dd-dd-dd from the port e3?
A. Destroy the frame
B. Forward the frame to port e1
C. Forward the frame to port e2
D. Broadcast the frame
E. Add/Update the address 12-12-12-ab-ab-ab to the forwarding table
F. Add/Update the address 11-11-11-dd-dd-dd to the forwarding table
ans: B,F

Câu 37: What will the switch do when it receives a frame with destination address 12-12-12-ab-ab-aa and source address 33-33-33-ee-ee-ee from the port e3.
A. Destroy the frame
B. Forward the frame to port e1
C. Forward the frame to port e2
D. Broadcast the frame
E. Add/Update the address 12-12-12-ab-ab-aa to the forwarding table
F. Add/Update the address 33-33-35-ee-ee-ee to the forwarding table
ans: D

Câu 38: If an IP packet with a payload size of 4926 bytes is sent into a network segment with an MTU of 880 bytes, and assuming the IP header size to be 20 bytes.
How many fragments do we need to split the IP packet to meet the requirement of network segment?
A. 4
B. 6
C. 5
D. 7
ans: B

Câu 39: What will be the size of data (payload) in the last IP fragment?
A. 526
B. 426
C. 640
D. 440
E. 540
F. 520
ans: A

Câu 40: Given a routing table of a router as follows:

| Network Address | Next-hop | Interface |
|-----------------|----------|-----------|
| 192.168.4.0/22  | -        | 1         |
| 192.168.7.0/24  | B        | 2         |
| 192.168.0.0/16  | C        | 3         |
| 10.0.0.128/25   | D        | 4         |
| 10.0.0.0/26     | E        | 5         |

Which operation will the router do if it receives an IP packet with the destination IP address as follows:
40. 192.168.6.31?
A. It will forward the packet to the interface 1
B. It will forward the packet to the interface 2
C. It will forward the packet to the interface 3
D. It will forward the packet to the interface 4
E. It will forward the packet to the interface 5
F. It will discard the packet
ans: A

Câu 41: 192.168.8.31
A. It will forward the packet to the interface 1
B. It will forward the packet to the interface 2
C. It will forward the packet to the interface 3
D. It will forward the packet to the interface 4
E. It will forward the packet to the interface 5
F. It will discard the packet
ans: F

Câu 42: 10.0.1.0
A. It will forward the packet to the interface 1
B. It will forward the packet to the interface 2
C. It will forward the packet to the interface 3
D. It will forward the packet to the interface 4
E. It will forward the packet to the interface 5
F. It will discard the packet
ans: E

Câu 43: Giving a network with the following IP information: 200.23.0.0/22
How many bits are used to distinguish this network from others?
A. 10
B. 200
C. 22
D. 32
ans: C

Câu 44: Maximum devices belong to this network?
A. 1024
B. 2^10
C. 1022
D. 512
ans: C
```

----- Page 72 -----
```md
Câu 45: How many subnets having 24 bits for network ID can be splitted from the original network?
A. 2
B. 8
C. 4
D. 6
ans: B

Câu 46: We want to split the original network to sub-networks. Each sub-network has 32 PCs. What is the maximum number of sub-networks that can be generated from the original network?
A. 16
B. 32
C. 64
D. 8
ans: D

Câu 47: Which address does not belong to the original network?
A. 200.23.2.1
B. 200.23.1.1
C. 200.23.3.1
D. 200.23.4.1
ans: C
```

----- Page 73 -----
```md
Câu 48: In TCP/IP model, at which layer the following functionalities could be performed?

| Functionality                                  | Layer          |
|-----------------------------------------------|----------------|
| Transferring between applications             |                |
| Forwarding data according to MAC address     | Datalink layer |
| Acknowledgement and Retransmission           |                |
| Controlling data transmission between hosts connected by a physical link | Transport layer |

A. Physical layer
B. Datalink layer
C. Network layer
D. Transport layer
ans: D

Câu 49: According to layer architecture, what layer does not perform?
A. Encapsulate the data received from the upper layer
B. Extract the header of the data received from the lower layer
C. Call service of the lower layer
D. Replace the header of the data received from the upper layer
ans: B

Câu 50: Which comparison between packet switching and circuit switching communication is correct?
A. Packet switching offers better line transmission efficiency
B. Circuit switching offers better line transmission efficiency
C. Packet switching guarantees no congestion
D. Circuit switching guarantees no congestion
ans: A

Câu 51: What are the advantages of the connectionless-oriented communication over connection-oriented communication? (Choose all correct answers)
A. Simpler
B. More reliable
C. More efficient
D. More flexible
ans: A,C,D
```

----- Page 74 -----
```md
Câu 52: Why data transferring from an upper layer to a lower is encapsulated?
A. To divide data to small amount
B. To protect data from attacks
C. To add control information serving for the protocol of the layer
D. No need
ans: C

Câu 53: What is the correct statement about protocol?
A. Protocol is a mechanism to collaborate between different layers of a network node.
B. Protocol is a mechanism to collaborate between different layer of 2 network nodes.
C. Protocol is a mechanism to collaborate between the same layer of 2 network nodes.
D. None of above.
ans: C

Câu 54: Which of the following characteristics belong to NRZ-L?(Choose 2 answers)
A. Using 2 voltage levels +V and -V
B. Each bit is represented by one pulse +V and one pulse -V
C. Bit 1 is represented by one pulse +V or 1 pulse -V
D. In the middle of bit interval, the voltage level crosses 0.
ans: A,C

Câu 55: A transmission line can transmit 20,000,000 pulse/s. In expecting to be able to transmit data with rate at least 8 Mbps, which encoding technique should be used?
A. Manchester 10Mbps
B. NRZ-L 20Mbps
C. AMI-Bipolar 20Mbps
D. All of above
ans: B

Câu 56: The datalink layer may perform which of following functionalities (choose all correct answers)
A. Represent bits by signals and vice visa
B. Numbering data frames
C. Check if there are errors in received data
D. Deliver data to the upper layer
ans: A,B,C,D

Câu 57: Amongst below CRC, which code can detect the most of errors?
A. CRC-8
B. CRC-12
C. CRC-16
D. CRC-32
ans: D

Câu 58: A and B are connected to each other. A follows Fast Ethernet standard and the network interface of B follows the network interface of following Giga Ethernet standard. Which of data in a mechanism allows to keep B capacity of A speed suitable to the processing capacity of B?
A. Flow control
B. Congestion control
C. Media access control
D. Error control
ans: A

Câu 59: Given a star topology network, choose the media control method appropriate to the network
A. CSMA
B. TDMA
C. Self-learning mechanism of switch
D. None of above
ans: C

Câu 60: Forwarding table of a switch is as following. What the switch does when it receives a frame with source address 11-22-33-11-22-33 and destination address a1-a1-b2-b2-c3-c3? (Choose all possible actions)
| Host | Interface |
|:----:|:---------:|
| a1-a1-b2-b2-c3-c3 | e0 |
| a2-a2-b3-b3-c4-c4 | e1 |
| aa-bb-cc-11-22-33 | e2 |
| bc-bc-ac-ac-11-11 | e3 |

A. Send frame to one port
B. Send the frame out of all its port except where the frame comes from
C. Add the destination address to the forwarding table
D. Add the source address to the forwarding table
ans: B,D

Câu 61: 10 network nodes connected to each other according to Ethernet standard using star topology, which of the following control method can be used?
A. CSMA/CD
B. Using self-learning mechanism of switch
C. Token Ring
ans: B
```

----- Page 75 -----
```md
Câu 15: How many networks can use class B IP addresses?
A. 2^13
B. 2^14
C. 2^15
D. 2^16
ans: B

Câu 16: Which network the IP address 97.0.3.21/21 belongs to?
97.0.1110 0001
class A
ans: class A

Câu 17: How many hosts the network with mask 25 may have?
2^(32-25) - 2 = 126
ans: 126

Câu 18: In which situation the ARP mechanism is used?
A. To convert an IP address to MAC address
B. To convert an IP address to domain name
C. To convert a private IP address to a public IP address
D. To automatically assign IP address to a host
ans: A

Câu 19: Hosts A, B and C belongs to the same LAN. Which of following the set of IP addresses can be used to assigned to A, B and C in that order in the set.
A. 192.168.1.0/24, 192.168.2.0/24, 192.168.3.0/24
B. 192.168.1.1/24, 192.168.1.2/24, 192.168.2.3/24
C. 192.168.1.2/24, 192.168.2.3/24, 192.168.2.4/24
D. 192.168.1.7/24, 192.168.1.21/24, 192.168.1.31/24
ans: D

Câu 20: Router does not perform which steps amongst the following when it processes an IP packet?
A. Check the value of the field TTL of the packet
B. Fragment the packet if its size is greater than MTU of the transmission line.
C. Add the destination IP address into the routing table if it was not there
D. Reduce TTL of the packet.
ans: C

Câu 21: An administrator is given a range of IP addresses in the network 10.20.64.0/22. He intends to organize his network in as many subnetworks as possible so that each subnetwork may have 400 hosts? How can he using IP addresses to the subnetworks? Explain the choice. What are addresses and masks of subnetworks. How many subnetworks there could be?
ans: [suy luận]
Giải thích:
- Mạng 10.20.64.0/22 có 10 bit host (32-22=10), cho phép tối đa 2^10 - 2 = 1022 hosts.
- Để có 400 hosts mỗi subnet, cần ít nhất 9 bit host (2^9 - 2 = 510 > 400).
- Số bit subnet còn lại: 32 - 22 - 9 = 1 bit subnet → 2^1 = 2 subnet.
- Subnet mask mới: /23 (22+1).
- Hai subnet:
  + Subnet 1: 10.20.64.0/23
  + Subnet 2: 10.20.66.0/23
```

----- Page 76 -----
```md
Câu 1: Anh xạ các phương pháp sau về các loại tường ứng.

TDMA

A. Phương pháp đa truy nhập phân chia theo thời gian
B. Phương pháp đa truy nhập phân chia theo tần số
C. Phương pháp đa truy nhập phân chia theo mã
D. Phương pháp đa truy nhập dùng token
ans: A

Câu 2: Anh xạ các phương pháp sau về các loại tường ứng.

FDMA

A. Phương pháp đa truy nhập phân chia theo thời gian
B. Phương pháp đa truy nhập phân chia theo tần số
C. Phương pháp đa truy nhập phân chia theo mã
D. Phương pháp đa truy nhập dùng token
ans: B

Câu 3: Anh xạ các phương pháp sau về các loại tường ứng.

CSMA

A. Phương pháp đa truy nhập phân chia theo thời gian
B. Phương pháp đa truy nhập phân chia theo tần số
C. Phương pháp đa truy nhập cảm nhận sóng mang
D. Phương pháp đa truy nhập dùng token
ans: C

Câu 4: Anh xạ các phương pháp sau về các loại tường ứng.

Token Ring

A. Phương pháp đa truy nhập phân chia theo thời gian
B. Phương pháp đa truy nhập phân chia theo tần số
C. Phương pháp đa truy nhập phân chia theo mã
D. Phương pháp đa truy nhập dùng token
ans: D
```

----- Page 77 -----
```md
Câu 5: Đâu là hình trạng mạng sử dụng một đường truyền dùng chung cho mọi nút?
A. Hình lưới (Mesh)
B. Hình trục (Bus)
C. Hình vòng (Ring)
D. Hình sao (Star)
ans: B

Câu 6: Khi truyền dữ liệu từ máy A đến máy B, giả thiết gói tin đi qua 13 router trong mạng, số các mạng gói tin đi qua là bao nhiêu?
A. 13
B. 1
C. 24
D. 28
ans: A
```

----- Page 78 -----
```md
Câu 7: Khi nhận được một gói tin có TTL = 0, nút mạng báo lỗi bằng thông điệp nào?
A. ICMP Echo Request
B. ICMP Echo Reply
C. ICMP Destination Network Unknown
D. ICMP Time exceeded
ans: D

Câu 8: Các yếu tố nào sau đây ảnh hưởng đến trễ khứ hồi (Round Trip Time) trong mạng?
A. Tốc độ xử lý của các thiết bị mạng
B. Tắt cả các yếu tố đã được đề cập
C. Trễ trên đường truyền
D. Tốc độ xử lý của nút nhận
E. Băng thông đường truyền
ans: A,C,D,E
```

----- Page 79 -----
```md
Câu 9: Mạng cần cung cấp địa chỉ IP cho 51 máy cần dùng mặt nạ mạng nào để hạn chế du thừa địa chỉ IP? (Nhập mặt nạ mạng dạng thập phân, ví dụ: 255.255.255.0)
A. 255.255.255.128
B. 255.255.255.192
C. 255.255.255.224
D. 255.255.254.0
ans: B

Câu 10: Hai tiến trình thực hiện truyền tin theo giao thức TCP. Tiến trình gửi đang sử dụng cửa sổ kiểm soát tắc nghẽn (congestion window) là 14.000 byte và ngưỡng kiểm soát tắc nghẽn (ssthreshold) là 11.200 byte. Tiến trình gửi nhận được gói tin ACK báo thành công cho các gói tin đã gửi, trong đó giá trị trì Receive Window là 65.535. Giá trị các bên đã thỏa thuận 1 MSS = 1.400 byte. Trong lượt tiếp theo, tiến trình gửi có thể gửi tối đa bao nhiêu byte?(Chỉ ghi đáp án số, không kèm đơn vị)
A. 11200
B. 12600
C. 14000
D. 15400
ans: B
```

----- Page 80 -----
```md
Câu 11: Phát biểu nào sau đây là SAI về số hiệu cổng ứng dụng?
A. Là một số nguyên 16 bit
B. Các chương trình ứng dụng trên một nút mạng phải đăng ký số hiệu cổng ứng dụng khác nhau
C. Được sử dụng trong quá trình truyền tin giữa các ứng dụng tại tầng giao vận
D. Được sử dụng để xác định đường đi khi chuyển tiếp gói tin
ans: D
```

----- Page 81 -----
```md
Câu 12: Bảng MAC/CAM của một switch có nội dung như sau. Switch thực hiện các xử lý nào khi trên cổng e2 nhận được một khung tin có địa chỉ nguồn là 55-55-55-ee-ee-ee và địa chỉ đích là 11-11-11-aa-aa-aa. (Chọn 2 đáp án)

A. Hủy khung tin
B. Gửi khung tin ra cổng e1
C. Gửi khung tin ra cổng e2
D. Gửi báo lỗi cho nút nguồn
E. Gửi khung tin ra tất cả các cổng trừ cổng e2
F. Thêm địa chỉ 55-55-55-ee-ee-ee vào bảng MAC/CAM với cổng chuyển tiếp là e2

ans: B,F
```

----- Page 82 -----
```md
Câu 13: Cho một đường truyền từ A đến B đi qua 3 đoạn kết nối như sau có băng thông lần lượt là 5 Mbps, 10 Mbps và 15 Mbps. Giả sử các đường kết nối này chỉ phục vụ cho việc truyền dữ liệu từ A đến B, trên thiết bị không đăng kế, và tỷ lệ lỗi và mất gói tin bằng 0. Hỏi thông lượng truyền tin từ A đến B là bao nhiêu?
A. 10 Mbps
B. 5 Mbps
C. 15 Mbps
D. Không thể xác định được
ans: B

Câu 14: Điểm khác biệt triệt để nhất giữa mô hình P2P so với mô hình Client-Server là gì? (Chọn 3 đáp án)
A. Không cần tất cả các nút mạng thành phần phải duy trì kết nối liên tục
B. Không cần quản lý tài nguyên tập trung
C. Các nút mạng có thể vừa gửi yêu cầu dịch vụ, vừa cung cấp dịch vụ cho các nút khác
D. Có điểm thắt nút cổ chai
ans: A,B,C
```

----- Page 83 -----
```md
Câu 15: Giao thức nào sau đây nằm ở tầng giao vận? (Chọn 2 đáp án)
A. IP
B. TCP
C. UDP
D. HTTP
ans: B,C

Câu 16: Đâu là đặc điểm của mạng sử dụng kỹ thuật chuyển mạch kênh (Chọn 3 đáp án)
A. Thiết lập kênh trước khi truyền
B. Gửi tin được truyền đi ngay
C. Các gói tin có thể tới đích không đúng thứ tự
D. Các gói tin trong mỗi kênh truyền giữa 2 nút luôn đi theo tuyến đường giống nhau
E. Tài nguyên được cấp phát để dùng riêng trên mỗi kênh truyền giữa 2 nút
ans: A,D,E
```

----- Page 84 -----
```md
Câu 17: Cơ chế tự học của switch được dùng để làm gì
A. Giúp chuyển tiếp dữ liệu giữa các mạng
B. Giúp chuyển tiếp dữ liệu trong một mạng LAN có topo dạng trục
C. Giúp chuyển tiếp dữ liệu trong một mạng LAN không dây.
D. Giúp chuyển tiếp dữ liệu trong một mạng LAN có topo dạng điểm-điểm
ans: D

Câu 18: Phát biểu nào sau đây là đúng về máy chủ tên miền gốc (root server) trong hệ thống DNS? (Chọn 2 đáp án)
A. Quản lý thông tin các máy chủ tên miền cấp 1 (TLD Server)
B. Lưu trữ thông tin của toàn bộ tên miền trên Internet
C. Không trả lời các thông điệp DNS Query truy vấn tên miền
D. Triển khai ở nhiều vị trí khác nhau trên Internet
ans: A,D
```

----- Page 85 -----
```md
Câu 19: Cho một đường truyền có thể phát được 2<sup>20</sup> xung/s (pulse/s), khi áp dụng phương pháp mã hoá NRZ-L, tốc độ dữ liệu sẽ là bao nhiêu.
A. 10 Mbps
B. 1 Mbps
C. 0.5 Mbps
D. 100 Mbps
ans: B

Câu 20: Phát biểu nào sau đây là đúng về các chương trình trên tầng ứng dụng? (Chọn 2 đáp án)
A. Sử dụng socket để truyền dữ liệu
B. Chỉ cần triển khai trên hệ thống đầu cuối
C. Phải cài đặt các cơ chế để đảm bảo truyền thông tin cậy
D. Chọn đường đi tốt nhất để truyền dữ liệu
ans: A,B
```

----- Page 86 -----
```md
Câu 21: Hãy lựa chọn thứ tự của tầng trong mô hình OSI khi liệt kê theo thứ tự từ dưới lên (Đáp án lựa chọn là 1 - 7 cho mỗi tầng, các tầng sẽ được sắp xếp không theo thứ tự)
A. Tầng ứng dụng (Application Layer)
B. Tầng trình diễn (Presentation Layer)
C. Tầng liên kết dữ liệu (Data-link Layer)
D. Tầng vật lý (Physical Layer)
E. Tầng phiên (Session Layer)
F. Tầng giao vận (Transport Layer)
G. Tầng liên mạng (Internetwork Layer)
ans: D,C,G,F,E,B,A
```

----- Page 87 -----
```md
Câu 22: Quá trình định tuyến được thực hiện để làm gì?
A. Tìm đường đi giữa 2 switch
B. Tìm đường đi tới router mặc định
C. Tìm đường đi giữa 2 máy tính trong cùng mạng
D. Tìm đường đi giữa 2 router
ans: D
```

----- Page 88 -----
```md
Câu 24: Trong hoạt động của giao thức UDP, bên nhận thực hiện những hoạt động nào? (Chọn 2 đáp án)
A. Kiểm tra lỗi trên gói tin
B. Chuyển dữ liệu tới đúng ứng dụng
C. Đưa các gói tin không đúng thứ tự vào bộ đệm
D. Gửi báo nhận
ans: B,C [suy luận]

Câu 25: Thông điệp DHCP nào được client gửi đi khi vừa kết nối vào mạng và xin cấp phát địa chỉ IP mới?
A. DHCP Discover
B. DHCP Offer
C. DHCP Request
D. DHCP ACK
ans: A
```

----- Page 89 -----
```md
Câu 26: Các phương pháp mã hoá như Manchester, NRZ-L, AMI Bipolar được sử dụng để làm gì?
A. Kiểm soát luồng
B. Kiểm soát lỗi của khi truyền dữ liệu trên đường truyền
C. Biểu diễn dữ liệu thành tín hiệu
D. Bảo mật cho dữ liệu
ans: C

Câu 27: Các gói tin TCP nào sau đây được sử dụng để đóng liên kết? (Chọn 2 đáp án)
A. SYN
B. ACK
C. FIN
D. SYN/ACK
ans: A,C [suy luận]
```

----- Page 90 -----
```md
Câu 28: Ánh xạ các mô tả vào các kỹ thuật điều khiển lỗi tương ứng:

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

----- Page 91 -----
```md
Câu 29: Đặc điểm của phương pháp CSMA là gì? (Chọn 2 đáp án)
A. Các nút sử dụng đường truyền một cách ngẫu nhiên
B. Lắng nghe tín hiệu sóng mang (carrier) trên đường truyền trước khi gửi
C. Các nút sử dụng đường truyền đồng thời, mỗi nút mạng sử dụng một mã để truyền tin
D. Không có đáp án đúng
ans: A,B

Câu 30: Đâu là ưu điểm của phương pháp chuyển mạch kênh so sánh với chuyển mạch gói? (Chọn 2 đáp án)
A. Cung cấp chất lượng dịch vụ tốt hơn
B. Hầu như không có trễ trung gian sau khi kênh truyền được thiết lập
C. Hiệu quả sử dụng kênh truyền tốt hơn
D. Giảm chi phí vận hành một hệ thống mạng
ans: A,B
```

----- Page 92 -----
```md
Câu 31: Khi không tìm thấy tài nguyên được yêu cầu, máy chủ Web gửi thông điệp HTTP Response với mã trả lời là bao nhiêu?
A. 200
B. 301
C. 404
D. 500
ans: C

Câu 32: Trong kỹ thuật Cửa sổ trượt (Sliding windows), phía gửi được phép truyền lượng dữ liệu tối đa là bao nhiêu?
A. Bằng kích thước vùng đệm của bên nhận
B. Bằng kích thước vùng đệm còn trống của bên nhận
C. Bằng kích thước của số phát của bên gửi
D. Một gói tin
ans: C
```

----- Page 93 -----
```md
Câu 33: Mã Checksum được sử dụng để làm gì?
A. Báo hiệu cho bên gửi dữ liệu rằng dữ liệu có lỗi.
B. Phát hiện lỗi phát sinh do quá trình truyền dữ liệu.
C. Báo một cho dữ liệu.
D. Sửa lỗi phát sinh do quá trình truyền dữ liệu.
ans: B

Câu 34: Dữ liệu của một gói tin gửi đi là 111000011101 (dạng nhị phân). Hệ thống sử dụng mã checksum 4-bit để kiểm tra lỗi. Hãy cho biết mã checksum cần được đính kèm với dữ liệu (Chỉ ghi mã checksum dưới dạng nhị phân, không thêm bất cứ kí tự nào)
A. 0010
B. 0101
C. 1010
D. 1110
ans: A [suy luận]
```

----- Page 94 -----
```md
Câu 35: Cho mạng có địa chỉ 222.17.188.0/25, hỏi địa chỉ quảng bá của mạng đó là địa chỉ nào? (Nhập địa chỉ IP dạng thập phân, ví dụ: 192.168.1.0)
A. 222.17.188.127
B. 222.17.188.128
C. 222.17.188.255
D. 222.17.188.0
ans: A [suy luận]

Câu 36: Mạng đang sử dụng địa chỉ 172.31.0.0/16 có thể có bao nhiêu mạng con nếu dùng một mặt nạ mạng 255.255.128.0? (Nhập số mạng con, ví dụ: 2)
A. 2
B. 4
C. 8
D. 512
ans: D [suy luận]
```

----- Page 95 -----
```md
Câu 37: Trong kiến trúc phân tầng, tại bên nhận, hoạt động nào sau đây có thể được thực hiện trong xử lý ở mỗi tầng?
A. Thêm tiêu đề mới và chuyển xuống tầng dưới
B. Thay thế tiêu đề của gói tin bằng tiêu đề mới và chuyển lên tầng trên
C. Bóc tách tiêu đề và chuyển phần thân của gói tin lên tầng trên
D. Phân nhỏ gói tin
ans: C

Câu 38: Làm thế nào để kiểm tra xem địa chỉ IP của gói tin có nằm trong một mạng cục bộ không?
A. Gửi bản tin RARP với địa chỉ IP của gói tin
B. Không có cách nào đúng
C. Gửi gói tin đến Default Gateway
D. Kiểm tra địa chỉ IP và mặt nạ mạng
ans: D
```

----- Page 96 -----
```md
Câu 39: Có 6 mạng đang kết nối với nhau sử dụng 5 router, hỏi có bao nhiêu bảng định tuyến được sử dụng?
A. 11
B. 5
C. 1
D. 6
ans: B

Câu 40: Phát biểu nào sau đây là đúng về giao thức định tuyến (routing protocol) dạng link-state? (Chọn 2 đáp án)
A. Các router trao đổi với nhau thông tin khoảng cách đường đi
B. Các router trao đổi với nhau thông tin về các liên kết (links)
C. Mỗi router có thể nhận thông tin từ tất cả các router khác
D. Các router hợp tác với nhau để tính toán đường đi
ans: B,D
```

----- Page 97 -----
```md
Câu 41: Trường nào trong tiêu đề của gói tin IP được dùng để xác định loại dữ liệu (payload) mà gói tin IP đang vận chuyển?
A. Checksum
B. Type of service
C. Protocol
D. Identification
ans: C

Câu 42: Để có thể yêu cầu phía gửi phát lại dữ liệu khi có lỗi, kỹ thuật nào sau đây có thể được áp dụng? (Chọn 2 đáp án)
A. Dừng và chờ (Stop-and-wait)
B. Go back N
C. Checksum
D. Slowstart
ans: A,B
```

----- Page 98 -----
```md
Câu 43: Tầng vật lý thực hiện các chức năng nào sau đây?
A. Đóng gói dữ liệu thành các gói tin
B. Kiểm tra dữ liệu nhận được có bị lỗi không
C. Đánh số các gói dữ liệu gửi đi
D. Biểu diễn các bit thành tín hiệu vô nguỡ lại
ans: D

Câu 44: Trong hoạt động của giao thức TCP, bên gửi thực hiện hoạt động nào? (Chọn 3 đáp án)
A. Yêu cầu thiết lập liên kết trước khi gửi
B. Chờ báo nhận
C. Phát lại dữ liệu khi có lỗi
D. Gửi dữ liệu với tốc độ nhanh nhất
ans: A,B,C
```

----- Page 99 -----
```md
Câu 45: Dịch vụ phân giải tên miền đăng ký sử dụng số hiệu công dịch vụ là bao nhiêu?
A. 13
B. 21
C. 53
D. 80
ans: C [suy luận]

Câu 46: Ưu điểm của giao thức UDP so với TCP là gì? (Chọn 2 đáp án)
A. Tốc độ truyền nhanh hơn
B. Đơn giản hơn
C. Tin cậy hơn
D. Không gây tắc nghẽn (congestion) đường truyền
ans: A,B [suy luận]
```

----- Page 100 -----
```md
Câu 47: Vấn đề mà kiểm soát đa truy nhập đường truyền (media access control) giải quyết là gì?
A. Điều khiển nút gửi không truyền với tốc độ quá nhanh, làm quá tải nút nhận
B. Điều khiển việc sử dụng đường truyền chung khi có nhiều nút cùng muốn truyền tin.
C. Điều khiển truyền dữ liệu giữa các nút mạng nối với nhau bằng switch
D. Điều khiển hai nút truyền theo thứ tự của giao thức mạng
ans: B

Câu 48: Những thay đổi của giao thức HTTP 1.1 so với HTTP 1.0 là gì? (Chọn 3 đáp án)
A. Chỉ thiết lập 1 liên kết TCP để truyền nhiều thông điệp khác nhau
B. Có cơ chế pipeline để tăng tốc độ truyền tin
C. Bổ sung thêm các phương thức yêu cầu mới cho thông điệp HTTP Request
D. Sử dụng các cơ chế truyền thông tin cậy để luôn đảm bảo truyền thành công
ans: A,B,C
```

----- Page 101 -----
```md
Câu 49: Trường nào trong tiêu đề của gói tin IP được dùng để xác định loại dữ liệu (payload) mà gói tin IP đang vận chuyển?
A. Checksum
B. Type of service
C. Protocol
D. Identification
ans: C

Câu 50: Để có thể yêu cầu phía gửi phát lại dữ liệu khi có lỗi, kỹ thuật nào sau đây có thể được áp dụng? (Chọn 2 đáp án)
A. Dừng và chờ (Stop-and-wait)
B. Go back N
C. Checksum
D. Slowstart
ans: A,B
```

----- Page 102 -----
```md
Câu 51: Ưu điểm của giao thức UDP so với TCP là gì? (Chọn 2 đáp án)
A. Tốc độ truyền nhanh hơn
B. Đơn giản hơn
C. Tin cậy hơn
D. Không gây tắc nghẽn (congestion) đường truyền
ans: A,B

Câu 52: Vấn đề mà kiểm soát đa truy nhập đường truyền (media access control) giải quyết là gì?
A. Điều khiển rút gọt khoảng truyền với tốc độ quá nhanh, làm quá tải nút nhận
B. Điều khiển việc sử dụng đường truyền chung khi có nhiều nút cùng muốn truyền tin.
C. Điều khiển truyền dữ liệu giữa các nút mạng nối với nhau bằng switch
D. Điều khiển địa chỉ truyền theo thứ tự của giao thức mạng
ans: B

Câu 53: Khi nhận được một gói tin có TTL = 0, nút mạng báo lỗi bằng thông điệp nào?
A. ICMP Time exceeded
B. ICMP Echo Reply
C. ICMP Echo Request
D. ICMP Destination Network Unknown
ans: A
```

----- Page 103 -----
```md
Câu 54: Bạn đang tham gia "Lớp 3.1" là một kỳ thi tính giờ. Đồng hồ ở bên phải hiển thị thời gian còn lại trong bài thi. Để nhận được điểm cho câu hỏi, bạn phải chọn "Gửi" cho từng câu hỏi trước khi bạn chọn "Kết thúc bài thi của tôi". Hiển thị rất gọn. **(Chọn 2 đáp án)**
A. Bốc tách tiêu đề và chuyển phần thân của gói tin lên tầng trên.
B. Thay thế tiêu đề của gói tin bằng tiêu đề mới và chuyển lên tầng trên.
C. Đóng gói dữ liệu và thêm header mới cho mỗi tầng dưới.
D. Giải mã dữ liệu và chuyển phần thân lên tầng trên.
ans: A,B

Câu 55: Điểm khác biệt triển khai dịch vụ theo mô hình P2P so với mô hình Client-Server là gì? **(Chọn 3 đáp án)**
A. Không cần tốt các đặc nút mạng thành phần phối duy trì kết nối liên tục
B. Không cần quản lý tài nguyên tập trung
C. Các nút mạng có thể vừa gửi yêu cầu dịch vụ, vừa cung cấp dịch vụ cho các nút khác
D. Có điểm thiết nút cố định
ans: A,B,C

Câu 56: Mã Checksum được sử dụng để làm gì?
A. Phát hiện lỗi phát sinh do quá trình truyền dữ liệu.
B. Báo một cho dữ liệu.
C. Sửa lỗi phát sinh do quá trình truyền dữ liệu.
D. Báo hiệu cho bên gửi dữ liệu rằng dữ liệu có lỗi.
ans: A

Câu 57: Đâu là đặc điểm của mạng sử dụng kỹ thuật chuyển mạch kênh **(Chọn 3 đáp án)**
A. Thiết lập kênh trước khi truyền
B. Gửi tin được truyền đi ngay
C. Các gói tin có thể tới đích không đúng thứ tự
D. Các gói tin trong mỗi kênh truyền giữa 2 nút luôn đi theo tuyến đường giống nhau
E. Tài nguyên được cấp phát để dòng riêng trên mỗi kênh truyền giữa 2 nút
ans: A,D,E
```

----- Page 104 -----
```md
Câu 58: Bạn đang tham gia "Lớp 3.1" tổ một kỳ thi tính giờ. Đồng hồ ở bên phải hiển thị thời gian còn lại trong bài thi. Để nhận được điểm cho các câu hỏi, bạn phải chọn "Gửi" cho từng câu hỏi trước khi bạn chọn "Kết thúc bài thi của tôi". Hiển thị rất rộng.

Phát biểu nào sau đây là SAI về số hiệu công ứng dụng?
A. Là một số nguyên 16 bit
B. Được sử dụng để xác định đường đi khi chuyển tiếp gói tin
C. Các chương trình ứng dụng trên một máy phải dùng ký số hiệu công ứng dụng khác nhau
D. Được sử dụng trong quá trình truyền tin giữa các ứng dụng tại tầng giao vận
ans: B

Câu 59: Đặc điểm của phương pháp CSMA là gì? (Chọn 2 đáp án)
A. Các nút sử dụng đường truyền một cách ngẫu nhiên
B. Lắng nghe tín hiệu mạng (carrier) trên đường truyền trước khi gửi
C. Các nút sử dụng đường truyền đồng thời, mỗi nút mang sử dụng một mã để truyền tin
D. Không có đáp án đúng
ans: A,B

Câu 60: Trong hoạt động của giao thức TCP, bên gửi thực hiện hoạt động nào? (Chọn 3 đáp án)
A. Yêu cầu thiết lập liên kết trước khi gửi
B. Chờ báo nhận
C. Phát lại dữ liệu khi có lỗi
D. Giải đi liệu với tốc độ nhanh nhất
ans: A,B,C

Câu 61: Trong hoạt động của giao thức UDP, bên nhận thực hiện những hoạt động nào? (Chọn 2 đáp án)
A. Kiểm tra lỗi trên gói tin
B. Chuyển dữ liệu tới ứng dụng
C. Đưa các gói tin không đúng thứ tự vào bộ đệm
D. Giữ báo nhận
ans: A,B
```

----- Page 105 -----
```md
Câu 62: Đâu là hình trạng mạng sử dụng một đường truyền dùng chung cho mọi nút?
A. Hình trục (Bus)
B. Hình lưới (Mesh)
C. Hình sao (Star)
D. Hình vòng (Ring)
ans: A

Câu 63: Trong kỹ thuật Cửa sổ trượt (Sliding windows), phía gửi được phép truyền lưng dữ liệu tối đa là bao nhiêu?
A. Bằng kích thước vùng đệm của bên nhận
B. Bằng kích thước vùng đệm của bên gửi
C. Một gói tin
D. Bằng kích thước cửa sổ phát của bên gửi
ans: A

Câu 64: Trường nào trong tiêu đề của gói tin IP được dùng để xác định loại dịch vụ (payload) mà gói tin IP đang vận chuyển?
A. Type of service
B. Checksum
C. Identification
D. Protocol
ans: A
```

----- Page 106 -----
```md
Câu 65: Các yếu tố nào sau đây ảnh hưởng đến trễ khứ hồi (Round-Trip Time) trong mạng?
A. Tốc độ xử lý của các thiết bị mạng
B. Tất cả các yếu tố được đề cập
ans: B

Câu 66: Thông điệp DHCP nào được client gửi đi khi vào kết nối vào mạng và xin cấp phát địa chỉ IP mới?
A. DHCP Request
B. DHCP ACK
C. DHCP Discover
D. DHCP Offer
ans: C

Câu 67: Cho một đường truyền có thể phát được 2²⁰ xung/s (pulse/s), khi áp dụng phương pháp mã hoa NRZ-L, tốc độ dữ liệu tối đa là bao nhiêu.
A. 10 Mbps
B. 1Mbps
C. 0.5 Mbps
D. 100 Mbps
ans: B

Câu 68: Dữ liệu của một gói tin gửi đi là 100001000110 (dạng nhị phân). Hệ thống sử dụng mã checksum 4-bit để kiểm tra lỗi. Hãy cho biết mã checksum cần được đính kèm vào dữ liệu (Chỉ ghi mã checksum dưới dạng nhị phân, không thêm bít cứ từ nào)
A. 1100
B. 0011
C. 0100
D. 0110
ans: A
```

----- Page 107 -----
```md
Câu 69: Cơ chế ly hợp của switch được dùng để làm gì?
A. Tăng tốc độ truyền dữ liệu
B. Giảm đụng độ trong mạng
C. Tách riêng các miền đụng độ (collision domain) cho mỗi cổng
D. Kết nối các mạng khác nhau với nhau
ans: C [suy luận]

Câu 70: Cho một đường truyền từ A đến B đi qua 3 đoạn kết nối nhau có băng thông lần lượt là 5 Mbps, 10 Mbps và 15 Mbps. Giả sử các đường kết nối này chỉ phục vụ cho việc truyền dữ liệu từ A đến B, trừ trên thiết bị không đăng ký, và tỷ lệ lỗi của một gói tin bằng 0. Hỏi thông lượng truyền từ A đến B là bao nhiêu?
A. 15 Mbps
B. Không thể xác định được
C. 10 Mbps
D. 5 Mbps
ans: D

Câu 71: Cho mạng có địa chỉ 199.163.32.0/27, hỏi địa chỉ quảng bá của mạng đó là địa chỉ nào? (Nhập địa chỉ IP dạng thập phân, ví dụ: 192.168.1.0)
A. 199.163.32.31
B. 199.163.32.32
C. 199.163.32.63
D. 199.163.32.64
ans: A

Câu 72: Tầng vật lý thực hiện các chức năng nào sau đây?
A. Đảnh số các gói dữ liệu gửi đi
B. Kiểm tra dữ liệu nhận được có bị lỗi không
C. Đồng bộ dữ liệu giữa các gói tin
D. Biểu diễn các bit thành tín hiệu và ngược lại
ans: D
```

----- Page 108 -----
```md
Câu 73: Bạn đang tham gia "Lớp 3.1" là một kỳ thi tính giờ. Đồng hồ ở bên phải hiển thị thời gian còn lại trong bài thi. Để nhận được điểm cho "Gửi" cho từng câu hỏi trước khi bạn chọn "Kết thúc bài thi của tôi", Hiển thị rất rõ ràng:

| 33-33-33-cc-cc-cc | e2 |
| 44-44-44-dd-dd-dd | e1 |

A. Hãy khung tin
B. Giữ khung tin ra cổng e1
C. Giữ khung tin ra cổng e2
D. Giữ bảo tải cho một nguồn
E. Giữ khung tin ra tất cả các cổng trừ cổng e2
F. Thêm địa chỉ 55-55-55-ee-ee-ee vào bảng MAC/CAM với cổng chuyển tiếp là e2
ans: B,E

Câu 74: Hai tiến trình thực hiện truyền tin theo giao thức TCP. Tiến trình gửi đang sử dụng cửa sổ kiểm soát tắc nghẽn (congestion window) là 14.000 byte và ngưỡng khởi tạo tắc nghẽn (ssthreshold) là 11.200 byte. Tiến trình gửi nhận được gói tin ACK báo thành công cho các gói tin đã gửi, trong đó giá trị Receive Window là 65.535. Giá sử các bên đều thành thành 1 MSS = 1.400 byte. Trong lượt tiếp theo, tiến trình gửi có thể gửi tối đa bao nhiêu byte? Chỉ ghi đáp án số, không kèm đơn vị).
ans: 15400 [suy luận]

Câu 75: Đều là ưu điểm của phương pháp chuyển mạch kênh khi so sánh với chuyển mạch gói? (Chọn 2 đáp án)
A. Cung cấp chất lượng dịch vụ tốt hơn
B. Hầu như không có trễ trung gian sau khi kênh truyền được thiết lập
C. Hiệu quả sử dụng kênh truyền tốt hơn
D. Giảm chi phí vận hành một hệ thống mạng
ans: A,B
```

----- Page 109 -----
```md
Câu 76: Bạn đang tham gia "Lớp 3.1" là một kỳ thi tính giờ. Đồng hồ ở bên phải hiển thị thời gian còn lại trong bài thi. Để nhận được điểm cho các câu hỏi, bạn phải nhấn nút "Gửi" cho từng câu hỏi trước khi bạn chọn "Kết thúc bài thi của tôi". Hiển thị rất rõ ràng.
A. 1
B. 28
ans: A

Câu 77: Để có thể cứu được gói phát lại đã liệu khi có lỗi, kỹ thuật nào sau đây có thể được áp dụng? (Chọn 2 đáp án)
A. Dừng và chờ (Stop-and-wait)
B. Go back N
C. Checksum
D. Slowstart
ans: A,B

Câu 78: Ánh xạ các phương pháp sau với các loại tương ứng.

TDMA
A. Chọn một tùy chọn
ans: 

FDMA
A. Chọn một tùy chọn
ans: 

CSMA
A. Chọn một tùy chọn
ans: 

Token Ring
A. Chọn một tùy chọn
ans:
```


----- Page 110 -----
```md
Câu 79: Mạng đang sử dụng địa chỉ lớp 2 0.0/16 có thể có bao nhiêu mạng con nếu dùng một mạng con 255.255.255.128? (Nhập số mạng con, ví dụ: 2)
ans: 512

Câu 80: Bạn đang tham gia "Lớp 3.1" là một kỳ thi tính giờ. Đồng hồ ở bên phải hiển thị thời gian còn lại trong bài thi. Để nhận được điểm cho câu hỏi hỏi, bạn phải chọn "Gửi" cho từng câu hỏi trước khi bạn chọn "Kết thúc bài thi của tôi". Hiển thị rút gọn.
A. Đúng
B. Sai
ans: A

Câu 81: Phía giải được phép gửi nhiều gói tin mà không cần chờ báo nhận
A. Cửa sổ trượt - Sliding windows
B. Loại bỏ chọn lọc - Selective Reject
C. Dừng và chờ - Stop-and-wait
D. Go back N
ans: A

Câu 82: Phía giải chỉ được phép gửi một gói tin và phải chờ báo nhận
A. Cửa sổ trượt - Sliding windows
B. Loại bỏ chọn lọc - Selective Reject
C. Dừng và chờ - Stop-and-wait
D. Go back N
ans: C

Câu 83: Phía giải phải gửi lại đúng gói tin bị lỗi
A. Cửa sổ trượt - Sliding windows
B. Loại bỏ chọn lọc - Selective Reject
C. Dừng và chờ - Stop-and-wait
D. Go back N
ans: B

Câu 84: Phía giải phải gửi lại một số gói tin gồm cả gói tin không bị lỗi
A. Cửa sổ trượt - Sliding windows
B. Loại bỏ chọn lọc - Selective Reject
C. Dừng và chờ - Stop-and-wait
D. Go back N
ans: D

Câu 85: Quá trình định tuyến được thực hiện để làm gì?
A. Tìm đường đi giữa 2 switch
B. Tìm đường đi giữa 2 router
C. Tìm đường đi tới router mặc định
D. Tìm đường đi giữa 2 máy tính trong cùng mạng
ans: B

Câu 86: Phát biểu nào sau đây là đúng về giao thức định tuyến (routing protocol) dạng link-state? (Chọn 2 đáp án)
A. Các router trao đổi với nhau thông tin không có cấu trúc đường đi
B. Các router trao đổi với nhau thông tin về các liên kết (links)
C. Mỗi router có thể nhận thông tin từ tất cả các router khác
D. Các router hợp tác với nhau để tính toán đường đi
ans: B,D
```


----- Page 111 -----
```md
Câu 87: Một gói tin IP với kích thước payload là 5246 byte đi vào mạng có MTU = 1192 byte, biết tiêu đề IP có kích thước 20 byte, hỏi tổng đã liêu ở mảnh IP cuối là bao nhiêu? (Nhập số nguyên, không nhập đơn vị, ví dụ: 52)
A. 558
B. 476
C. 1192
D. 5246
ans: A

Câu 88: Các phương pháp mô hoá như Manchester, NRZ-L, AMI Bipolar được sử dụng để làm gì?
A. Bảo mật cho dữ liệu
B. Biếu diễn dữ liệu thành tín hiệu
C. Kiểm soát tường
D. Kiểm soát lỗi của khi truyền dữ liệu trên đường truyền
ans: B

Câu 89: Các gói tin TCP nào sau đây được sử dụng để đóng kết nối? (Chọn 2 đáp án)
A. SYN
B. ACK
C. FIN
D. SYN/ACK
ans: B,C

Câu 90: Có 6 mạng đang kết nối với nhau sử dụng 5 router, hỏi có bao nhiêu bảng định tuyến được sử dụng?
A. 6
B. 1
C. 11
D. 5
ans: D
```


----- Page 112 -----
```md
Câu 91: Bạn đang tham gia "Lớp 3.1" là một kỳ thi tính giá. Đồng hồ ở bên phải hiển thị thời gian còn lại trong bài thi. Để nhận được điểm cho các câu hỏi, bạn phải chọn "Gửi" cho từng câu hỏi trước khi bạn chọn "Kết thúc bài thi của tôi". **Hiển thị tất cả gợi ý**

Giao thức nào sau đây nằm ở tầng giao vận? **(Chọn 2 đáp án)**
A. IP
B. TCP
C. UDP
D. HTTP
ans: B,C

Câu 92: Khi không tìm thấy tên nguyên được yêu cầu, máy chủ Web giải thông đáp HTTP Response với mã trả lời là bao nhiêu?
A. 404
B. 403
C. 503
D. 200
ans: A

Câu 93: Phát biểu nào sau đây là đúng về máy chủ tên miền gốc (root server) trong hệ thống DNS? **(Chọn 2 đáp án)**
A. Quản lý thông tin của máy chủ tên miền cấp 1 (TLD Server)
B. Lưu trữ thông tin của toàn bộ hệ tên miền Internet
C. Không trả lời các thông điệp DNS Query truy vấn tên miền
D. Triển khai ở nhiều vị trí khác nhau trên Internet
ans: A,D

Câu 94: Dịch vụ phân giải tên miền đang ký sử dụng số hiệu cổng dịch vụ là bao nhiêu?
A. 53
B. 80
C. 443
D. 25
ans: A
```


----- Page 113 -----
```md
Câu 95: Phát biểu nào sau đây là đúng về các chương trình trên tầng ứng dụng? (Chọn 2 đáp án)
A. Sử dụng socket để truyền dữ liệu
B. Chỉ cần trên khi trên hệ thống đầu cuối
C. Phải cài đặt các cơ chế để đảm bảo truyền thông tin cậy
D. Chọn đường đi tốt nhất để truyền dữ liệu
ans: A,B

Câu 96: Làm thế nào để kiểm tra xem địa chỉ IP của gói tin có nằm trong một mạng cục bộ không?
A. Giả gửi tin đến Default Gateway
B. Kiểm tra địa chỉ IP và mặt nạ mạng
C. Gửi bản tin RARP với địa chỉ IP của gói tin
D. Không có cách nào đúng
ans: B

Câu 97: Những thay đổi của giao thức HTTP 1.1 so với HTTP 1.0 là gì? (Chọn 3 đáp án)
A. Chỉ thiết lập 1 liên kết TCP để truyền nhiều thông điệp khác nhau
B. Có cơ chế pipeline để tăng tốc độ truyền tin
C. Bỏ sung thêm các phương thức yêu cầu mới cho thông điệp HTTP Request
D. Sử dụng các cơ chế truyền thông tin cậy để luôn đảm bảo truyền thành công
ans: A,B,C
```


----- Page 114 -----
```md
Câu 98: Bạn đang tham gia "Lớp 3.1" tổ một kỹ thi tính giờ. Đồng hồ ở bên phải hiển thị thời gian còn lại trong bài thi. Để nhận được điểm cho các câu hỏi, bạn phải chọn "Gửi" cho từng câu hỏi trước khi bạn chọn "Kết thúc bài thi của tôi". Hiển thị rút gọn.
A. Tầng trình diễn (Presentation Layer) - 6
B. Tầng liên kết dữ liệu (Data-link Layer) - 2
C. Tầng vật lý (Physical Layer) - 1
D. Tầng phiên (Session Layer) - 5
E. Tầng giao vận (Transport Layer) - 4
F. Tầng liên mạng (Internetwork Layer) - 3
ans: C,F,B,E,A,D
```
