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
ans: A,B,C,D

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

Câu 9: Two processes communicate by a reliable protocol using stop-and-wait mechanism. The size of file to be sent is 10000 bytes, the size of each packet is 1000 bytes, assuming that the header size is zero. RTT between the 2 hosts is 100ms. The bandwidth of the transmission line is 1 Mbps (Megabits per second). How much of time it takes to complete file transmission? **(Câu điền — chỉ ghi số, đơn vị ms)**
A. 1080
ans: A
```

----- Page 4 -----
```md
Câu 10: Given a fixed pulse generation speed, how NRZ-L, Manchester, Bipolar AMI encodings provide data speed (bit/s)?
A. NRZ-L and Bipolar AMI result in higher data speeds than Manchester
B. The 3 methods result in identical data speeds
C. Manchester and Bipolar AMI result in higher data speeds than NRZ-L
D. NRZ-L and Manchester result in higher data speeds than Bipolar AMI
ans: A

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
ans: B,C

Câu 13: Assume that the window size in the Sliding window mechanism is equivalent N packets. Choose the correct statement about the efficiency of Sliding window in comparison with Stop-and-wait:
A. Data transmission efficiency of Sliding windows is N times higher
B. Data transmission efficiency of Sliding windows is 2N times higher
C. Data transmission efficiency of Sliding windows is N<sup>2</sup> times higher
D. Data transmission efficiency of the 2 methods are identical.
ans: A
```

----- Page 5 -----
```md
Câu 14: In the layering model, when a packet arrives to an intermediate node, how it is processed?
A. Forward from application layer to lower layers then physical layer.
B. Forward from physical layer to application later
C. Forward from upper layers to physical layer then from physical layer to upper layers
D. Forward from the physical layer to upper layers and then from the upper layers to the physical layer.
ans: D

Câu 15: Choose the correct statement(s) about interdomain routing protocol BGP.
A. BGP routing prioritizes management policies over performance
B. BGP does not have a mechanism to avoid loops in routing paths
C. BGP uses path-vector routing instead of link-state or distance-vector routing
D. BGP selects best paths based on bandwidth metric to achieve the best performance
ans: A,C

Câu 16: Identify the multiple access methods that have the following characteristics: **(Câu điền)**
1. Network nodes sequentially send data
2. Network nodes can send data simultaneously without collision
3. Network nodes only send data when the transmission line is free
4. Network nodes send data even if the transmission line is busy
A. 1-Token bus; 2-FDMA, CDMA; 3-CSMA; 4-Aloha
ans: A
```

----- Page 6 -----
```md
Câu 17: What is the purpose of the field TTL in IP packet?
A. To avoid the packet looping in an IP network forever
B. To limit the execution time of ping command
C. To help finding path from the source to the destination by using command traceroute
D. To help administrator limit the routing scope of the packet
ans: A

Câu 18: When a router receives a packet whose destination address matches several rows in the routing table, what the router does?
A. Router forwards the packet to the interface (port) with the smallest index
B. Router reports error because the destination address matches with more than one rows in routing table
C. No answer is correct
D. Router forwards the packet to the interface (port) corresponding to the destination network that has the largest mask
ans: D

Câu 19: Forwarding table (MAC table) of a switch is as belows. What the switch will do when it receives a frame with source address 12-12-12-ab-ab-ab and destination address 11-11-11-dd-dd-dd.

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
E. Add the address 11-11-11-dd-dd-dd to the forwarding table (MAC table)
F. Add the address 12-12-12-ab-ab-ab to the forwarding table (MAC table)
ans: C,F
```

----- Page 7 -----
```md
Câu 20: Which statement(s) are FALSE about congestion control mechanism of TCP?
A. Ssthreshold (Slow-start threshold) changes depending on the network bandwidth and it is updated periodically
B. Ssthreshold is updated when congestion happens
C. cwnd window reduces to 1 MSS when receiver receives 3 ACKs segment of the same index
D. cwnd window reduces to 1 MSS when a timeout occurs for one segment
E. slow-start period stop when the number of segments to be sent in the cycle meets the slow start threshold
F. After receiving 3 ACKs with the same index, sender move to slow-start state
ans: A,C,F

Câu 21: Why video streaming applications tend to use UDP instead of TCP?
A. TCP is more complicated so more error-prone
B. UDP has smaller header than TCP so the transmission efficiency is better
C. UDP can transmit data with larger bandwidth at the same transmission line
D. Video streaming application does not need the transmission accuracy 100%
ans: B,D

Câu 22: Sort the error detection codes Parity, Checksum, CRC in decreasing order of their error detection capacity
A. CRC-12, Parity, Checksum 8 bit
B. Checksum 8 bit, CRC-12, Parity
C. CRC-12, Checksum 8 bit, Parity
D. Parity, Checksum 8 bit, CRC-12
ans: C
```

----- Page 8 -----
```md
Câu 23: Sending host A and receiving host B uses ARQ Go-back-N with window size is 5. A sends packets numbered pk0, pk1, pk2, pk3, pk4 but pk2 gets errors on the transmission line. What is (are) the FALSE statement(s) about ARQ Go-back-N protocol?
A. Receiver sends acknowledgements ack0, ack1, ack3 and ack4 corresponding to the packets it received successfully
B. Receiver sends ack0 and (several times) ack1
C. Sender sends again pk2
D. Sender sends again packets pk2, pk3, pk4
ans: A

Câu 24: Choose the correct statement(s) about HTTP Cookie?
A. HTTP Cookie deals with the problem that HTTP does not keep track of the state of the session
B. HTTP Cookie helps to access to data faster when using HTTP protocol
C. HTTP Cookie is used for applications that require authentication like email and e-commerce
D. HTTP Cookie is used uniquely on web server.
ans: A,C

Câu 25: Below signal could be generated with which encoding method(s)?
img: waveform on +V/0/-V grid — pulses: +V, 0, -V, 0, +V, 0, +V, 0 (AMI: 1 = alternate ±V, 0 = 0V)
A. NRZ-L
B. Manchester
C. Bipolar AMI
D. No correct answer
ans: C

Câu 26: Choose the correct statement(s) about the applications on application layer?
A. Use socket to send data
B. Run only on end-systems
C. Multiple applications use a common port on transport layer
D. Need to implement mechanisms to achieve reliable transmission
E. Choose the best path to send data
ans: A,B
```

----- Page 9 -----
```md
Câu 27: Mapping the following characteristics to Packet switching mechanism and Circuit switching mechanism
1. Data is store in switches before being analysed and forwarded
2. Data must be divided into packets
3. Data always follow the same set of links in one transmission process
4. Data can follow different sets of links in one transmission process
A. 1-Packet switching mechanism, 2-Packet switching mechanism, 3-Circuit switching mechanism, 4-Packet switching mechanism
B. 1-Circuit switching mechanism, 2-Packet switching mechanism, 3-Circuit switching mechanism, 4-Packet switching mechanism
C. 1-Packet switching mechanism, 2-Circuit switching mechanism, 3-Packet switching mechanism, 4-Circuit switching mechanism
D. 1-Circuit switching mechanism, 2-Packet switching mechanism, 3-Packet switching mechanism, 4-Circuit switching mechanism
ans: A

Câu 28: Choose the correct answer(s) about NAT Overloading (PAT), a mechanism to convert from internal to public addresses
A. Each private address is converted STATICALLY to a separate public address
B. Each private address is converted DYNAMICALLY (change over time) to a separate public address
C. All local addresses are converted to an UNIQUE public address
D. Each application in a local network is refered to by a separate port of the public address
E. All of the above statements are false
ans: B,D

Câu 29: Choose the address(es) that IS (ARE) NOT ALLOWED to be assigned as public IP addresses?
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
Câu 30: In which scope MAC address is used to forward data?
A. To forward data between network nodes that connect directly to each other
B. To forward data between network nodes of two LANs
C. To forward data between network nodes connected to each other through switches
D. To forward data between network nodes on the Internet
ans: A,C

Câu 31: Why the connection-oriented transmission is more reliable than connectionless transmission?
A. Data cannot be lost
B. Data follows the same path
C. Connection-oriented transmission makes sure that the receiver is ready to receive data
D. Connection-oriented transmission makes sure that the receiver is not overloaded.
ans: C

Câu 32: In the header of a transport layer packet, which field is used to determine the application that sent the packet.
A. checksum code
B. Port of the destination application
C. Source IP address
D. Destination IP address
E. Port of the source application
ans: E

Câu 33: When an Web server found a requested resource, it sends HTTP Response with an answer code. What is the value of the answer code? **(Câu điền — chỉ ghi số)**
A. 200
ans: A
```

----- Page 11 -----
```md
Câu 34: The WiFi network that laptops, mobile phones connect to in a coffee shop belongs to what kind of network?
A. Local area network (LAN)
B. Wide area network (WAN)
C. Metro area network (MAN)
D. PAN
ans: A

Câu 35: Compare two communication lines whose BERs are 5.10⁻⁶ and 10⁻⁶ respectively, which one is better in terms of quality?
A. The line with BER 5.10⁻⁶ is better
B. The line with BER 10⁻⁶ is better
C. Two lines have similar quality
D. Impossible to compare
ans: B

Câu 36: What is the port that FTP service uses to transmit data? **(Câu điền — chỉ ghi số)**
A. 20
ans: A

Câu 37: Which statement(s) is/are correct about link-state routing protocol?
A. Routers exchange information about links
B. Routers exchange the information about distance of paths
C. Each router may have the information about all links of the network
D. Routers collaborate to calculate paths
E. The calculation converges slower than distance-vector protocol in large networks
ans: A,C,D
```

----- Page 12 -----
```md
Câu 38: In a TCP segment sent from host A to host B, the value of sequence number field is 100, the value of ACK field is 200, data payload is 1000 bytes length. The data is sent successfully to the destination. When B send back an acknowledgement, the fields in its TCP segment are: **(Câu điền — 2 giá trị)**
A. Sequence=200; ACK=1100
ans: A

Câu 39: What information is not defined in a network protocol
A. Packet format to be used during the transmission
B. How data packet should be processed by participants
C. No correct answer
D. Procedure to send and receive data
ans: C

Câu 40: Given a network with bus topology, the data transmission between two nodes can be performed by which methods?
A. CSMA
B. Using MAC table (forwarding table) and self-learning mechanism of switch
C. FDMA
D. Token bus
ans: A,C,D
```

----- Page 13 -----
```md
Câu 41: What network mask should be used to minimize IP address waste for 122 machine that needs to be assigned an address? (Enter the network mask in decimal format, for example, 255.255.255.0) **(Câu điền)**
A. 255.255.255.128
ans: A

Câu 42: If an IP packet with a payload size of 5246 bytes is sent into a network with an MTU of 1192 bytes, and assuming the IP header size is 20 bytes, what will be the size of data (payload) in the last IP fragment? (Enter an integer without any unit, for example: 52) **(Câu điền)**
A. 558
ans: A

Câu 43: Given a network with subnet address 219.131.107.0/26, what is the broadcast address of that network? (Enter the IP address in decimal format, for example: 192.168.1.0) **(Câu điền)**
A. 219.131.107.63
ans: A

Câu 44: How many subnets are possible for a network with address 172.19.0.0/16 if the network mask used is 255.255.192.0? (Enter the number of subnets, for example: 2) **(Câu điền)**
A. 4
ans: A

Câu 45: The data of a transmitted packet is 111110010011 (in binary form). What is the 4-bit checksum to be assigned to the data? (Only write the checksum in binary form, without adding any additional characters.) **(Câu điền)**
A. 0011
ans: A
```

----- Page 14 -----
```md
Câu 45: Đâu là các phát biểu ĐÚNG về giao thức định tuyến liên vùng và nội vùng
A. Giao thức định tuyến liên vùng (BGP) quan tâm đến hiệu năng (performance) hơn là chính sách (policy)
B. Giao thức định tuyến nội vùng thường dựa trên 2 thuật toán dạng link-state và distance vector
C. Giao thức định tuyến liên vùng (BGP) dựa trên link-state
D. Giao thức định tuyến nội vùng của các miền tự trị (AS) khác nhau có thể khác nhau
ans: B,D

Câu 46: Việc phân chia mạng theo CIDR thay vì theo phân lớp đem lại lợi ích gì?
A. Có thể chia nhỏ thành nhiều mạng con (subnet)
B. Tận dụng được không gian địa chỉ tốt hơn
C. Cho phép chia thành nhiều phân lớp hơn so với trước
D. Không có đáp án đúng
ans: B

Câu 47: Chuyện gì xảy ra nếu MTU của một đường truyền kết nối quá nhỏ
A. Giảm băng thông của đường truyền
B. Tăng khả năng lỗi bit trên đường truyền
C. Tăng khả năng tắc nghẽn do số gói tin tăng lên
D. Giảm hiệu suất truyền dữ liệu do phần header có kích thước cố định
ans: D
```

----- Page 15 -----
```md
Câu 48: Cho các địa chỉ mạng dưới đây, hãy lựa chọn loại địa chỉ hợp lệ: 192.168.1.128/25
A. Địa chỉ mạng
B. Địa chỉ máy
C. Địa chỉ quảng bá
D. Không hợp lệ
ans: A

Câu 49: Cho các địa chỉ mạng dưới đây, hãy lựa chọn loại địa chỉ hợp lệ: 192.168.1.128/24
A. Địa chỉ mạng
B. Địa chỉ máy
C. Địa chỉ quảng bá
D. Không hợp lệ
ans: B

Câu 50: Cho các địa chỉ mạng dưới đây, hãy lựa chọn loại địa chỉ hợp lệ: 192.168.1.255/25
A. Địa chỉ mạng
B. Địa chỉ máy
C. Địa chỉ quảng bá
D. Không hợp lệ
ans: C

Câu 51: Cho các địa chỉ mạng dưới đây, hãy lựa chọn loại địa chỉ hợp lệ: 192.168.1.256/23
A. Địa chỉ mạng
B. Địa chỉ máy
C. Địa chỉ quảng bá
D. Không hợp lệ
ans: D

Câu 52: Cho các địa chỉ mạng dưới đây, hãy lựa chọn loại địa chỉ hợp lệ: 192.168.1.255/23
A. Địa chỉ mạng
B. Địa chỉ máy
C. Địa chỉ quảng bá
D. Không hợp lệ
ans: C

Câu 53: Cho các địa chỉ mạng dưới đây, hãy lựa chọn loại địa chỉ hợp lệ: 192.168.2.255/23
A. Địa chỉ mạng
B. Địa chỉ máy
C. Địa chỉ quảng bá
D. Không hợp lệ
ans: B

Câu 54: Cho các địa chỉ mạng dưới đây, hãy lựa chọn loại địa chỉ hợp lệ: 192.168.2.0/23
A. Địa chỉ mạng
B. Địa chỉ máy
C. Địa chỉ quảng bá
D. Không hợp lệ
ans: A
```

----- Page 16 -----
```md
Câu 55: **Phân mảnh gói tin** (đạt 1/1 điểm, không tích lũy vào tiến trình học)

Một gói tin IP có kích thước là 2420 bytes, bao gồm 20 bytes là phần header. Gói tin này phải đi qua một đường kết nối có MTU=940 bytes. Hỏi: (1) Gói tin phải phân chia thành mấy mảnh (fragment)? (2) Trường offset của phân mảnh thứ 2 có giá trị là bao nhiêu? **(Câu điền — 2 giá trị)**
A. 3;115
ans: A

Câu 56: Chuyện gì xảy ra nếu MTU của một đường truyền kết nối quá nhỏ
A. Tăng khả năng lỗi bit trên đường truyền
B. Tăng khả năng tắc nghẽn do số gói tin tăng lên
C. Giảm hiệu suất truyền dữ liệu do phần header có kích thước cố định
D. Giảm băng thông của đường truyền
ans: C

Câu 57: **MC_05_02** (đạt 1.0/1.0 điểm, không tích lũy vào tiến trình học)

Ưu điểm của giao thức UDP so với giao thức TCP là gì?
A. Tốc độ gửi nhanh hơn
B. Có điều khiển luồng
C. Tin cậy hơn
D. Quá trình bắt tay giữa máy nguồn và đích tốt hơn
ans: A
```

----- Page 17 -----
```md
Câu 58: **Truyền tin qua nhiều đường truyền** (đạt 1/1 điểm, không tích lũy vào tiến trình học)

Một đường truyền từ A tới B qua 3 kết nối vật lý nối tiếp nhau với băng thông lần lượt là 20 Mbps, 1 Mbps, 10 Mbps. Giả sử các đường kết nối này chỉ phục vụ liên kết giữa A và B và thời gian xử lý và lan truyền dữ liệu là không đáng kể (bằng 0). Hỏi thời gian cần thiết để truyền một gói tin có kích thước 8 MB từ A tới B là bao nhiêu giây? Chỉ ghi số giây, không ghi đơn vị hay bất cứ ký tự nào khác. Trường hợp số giây lẻ, làm tròn đến 2 chữ số sau phần thập phân. **(Câu điền)**
A. 64
ans: A

Câu 59: **MC_03_07** (đạt 1.0/1.0 điểm, không tích lũy vào tiến trình học)

(Các) thiết bị mạng nào dưới đây hoạt động cả ở tầng 1-2-3 trong mô hình TCP/IP?
A. Repeater
B. Hub
C. Bridge
D. Switch
E. Router
F. Computer
ans: E,F

Câu 60: **Phân mảnh gói tin** (đạt 1/1 điểm, không tích lũy vào tiến trình học)

Một gói tin IP có kích thước là 2420 bytes, bao gồm 20 bytes là phần header. Gói tin này phải đi qua một đường kết nối có MTU=1100 bytes. Hỏi: (1) Gói tin phải phân chia thành mấy mảnh (fragment)? (2) Trường offset của phân mảnh thứ 2 có giá trị là bao nhiêu? **(Câu điền — 2 giá trị)**
A. 3;135
ans: A
```

----- Page 18 -----
```md
Câu 61: Đâu là những nhược điểm của cáp quang so với các loại cáp khác?
A. Giá thành đắt đỏ
B. Lắp đặt phức tạp do cần thiết bị chuyên dụng
C. Độ suy hao tín hiệu lớn
D. Dễ bị ảnh hưởng bởi nhiễu từ sóng điện từ
E. Dễ hư hỏng
F. Kích thước lớn
ans: A,B,E

Câu 62: Chuyện gì xảy ra nếu MTU của một đường truyền kết nối quá nhỏ
A. Giảm hiệu suất truyền dữ liệu do phần header có kích thước cố định
B. Tăng khả năng lỗi bit trên đường truyền
C. Tăng khả năng tắc nghẽn do số gói tin tăng lên
D. Giảm băng thông của đường truyền
ans: A

Câu 63: Vì sao khi sử dụng mã hóa Manchester và Manchester vi sai không xảy ra tình trạng mất đồng bộ giữa máy gửi và máy nhận?
A. Các đáp án khác đều sai
B. Chỉ sử dụng 2 mức điện áp
C. Luôn có sự chuyển mức ở giữa các chu kỳ bit tín hiệu
D. Có tốc độ tín hiệu lớn hơn với cùng tốc độ dữ liệu
ans: C

Câu 64: **MC_05_01** (đạt 1/1 điểm, không tích lũy vào tiến trình học)

Vì sao tầng giao vận có thêm định danh CỔNG (PORT) khi đã có địa chỉ IP và địa chỉ MAC để gửi dữ liệu từ máy nguồn đến máy đích?
A. Máy gửi dùng thông tin cổng cho mục đích bảo mật chống tấn công
B. Router cần thông tin cổng cho việc định tuyến
C. Máy đích cần thông tin cổng cho việc xử lý dữ liệu trên tầng ứng dụng
D. Máy đích và nguồn cần thông tin cổng để phân biệt các ứng dụng giao tiếp mạng trên cùng một máy
ans: D
```

----- Page 19 -----
```md
Câu 65: Cho các địa chỉ mạng dưới đây thuộc các phân lớp nào khi sử dụng cơ chế phân lớp? 150.55.1.128 **(Câu điền — chỉ ghi A/B/C/D)**
A. B
ans: A

Câu 66: Cho các địa chỉ mạng dưới đây thuộc các phân lớp nào khi sử dụng cơ chế phân lớp? 192.168.1.128 **(Câu điền — chỉ ghi A/B/C/D)**
A. C
ans: A

Câu 67: Cho các địa chỉ mạng dưới đây thuộc các phân lớp nào khi sử dụng cơ chế phân lớp? 10.168.255.240 **(Câu điền — chỉ ghi A/B/C/D)**
A. A
ans: A

Câu 68: Cho các địa chỉ mạng dưới đây thuộc các phân lớp nào khi sử dụng cơ chế phân lớp? 200.168.1.128 **(Câu điền — chỉ ghi A/B/C/D)**
A. C
ans: A
```

----- Page 20 -----
```md
Câu 69: Việc phân chia mạng theo CIDR thay vì theo phân lớp đem lại lợi ích gì?
A. Có thể chia nhỏ thành nhiều mạng con (subnet)
B. Cho phép chia thành nhiều phân lớp hơn so với trước
C. Tận dụng được không gian địa chỉ tốt hơn
D. Không có đáp án đúng
ans: C

Câu 70: **MC_03_01** (đạt 1/1 điểm, không tích lũy vào tiến trình học)

Trong các phát biểu sau, phát biểu nào là ĐÚNG về địa chỉ MAC
A. Có độ dài 48 bit
B. Mỗi nhà sản xuất CHỈ CÓ MỘT số OUI
C. Địa chỉ MAC có thể thay đổi khi một máy kết nối với các mạng khác nhau
D. Router dùng địa chỉ MAC để xác định đường đi
E. Có 24 bit đầu là số OUI để phân biệt các nhà sản xuất
F. Một thiết bị đầu cuối (máy tính, điện thoại thông minh) chỉ có thể có một địa chỉ MAC
ans: A,E
```

----- Page 21 -----
```md
Câu 71: (đạt 1/1 điểm, không tích lũy vào tiến trình học)

Khi sử dụng DHCP, chuyện gì xảy ra khi một client (máy tính) nhận được 2 offer từ 2 DHCP server khác nhau?
A. Client lựa chọn offer đến sớm hơn.
B. Client từ chối cả 2 offer do xung đột.
C. Client chấp nhận cả 2 offer.
D. Không có đáp án đúng.
E. Client lựa chọn offer theo chính sách người quản trị đề ra.
ans: A

Câu 72: **MC_03_09** (đạt 1/1 điểm, không tích lũy vào tiến trình học)

Vì sao chuẩn Ethernet không dây (IEEE 802.11) sử dụng kỹ thuật truy cập đường truyền CSMA/CA thay vì CSMA/CD vốn có khả năng giúp giảm thời gian phát lại khi có xung đột?
A. Vì CSMA/CA cho tốc độ truyền tốt hơn
B. Vì CSMA/CD yêu cầu thiết bị phức tạp hơn
C. Vì CSMA/CD yêu cầu đường truyền duy trì tốc độ cố định
D. Vì môi trường truyền không dây có đặc thù nhiễu nên nhiều trường hợp tín hiệu truyền không truyền đến hết các máy trong mạng
ans: D

Câu 73: **Số máy trong mạng** (đạt 2/2 điểm, không tích lũy vào tiến trình học)

Cho một mạng có địa chỉ 172.16.0.0/16. Người ta sử dụng 5 bit phần HostID để chia mạng thành các mạng con (subnet). Hỏi số mạng con tối đa có thể chia là? (Chỉ ghi số) **(Câu điền)**
A. 32
ans: A

Câu 74: Số máy tối đa trong mỗi mạng con là? (Chỉ ghi số) **(Câu điền)**
A. 2046
ans: A
```

----- Page 22 -----
```md
Câu 75: **MC_04_02** (đạt 0/2 điểm, không tích lũy vào tiến trình học)

Cho các địa chỉ mạng dưới đây, hãy lựa chọn loại địa chỉ hợp lệ: 192.168.1.128/25
A. Địa chỉ mạng
B. Địa chỉ máy
C. Địa chỉ quảng bá
D. Không hợp lệ
ans: A [suy luận]

Câu 76: Cho các địa chỉ mạng dưới đây, hãy lựa chọn loại địa chỉ hợp lệ: 192.168.1.128/24
A. Địa chỉ mạng
B. Địa chỉ máy
C. Địa chỉ quảng bá
D. Không hợp lệ
ans: B [suy luận]

Câu 77: Cho các địa chỉ mạng dưới đây, hãy lựa chọn loại địa chỉ hợp lệ: 192.168.1.255/25
A. Địa chỉ mạng
B. Địa chỉ máy
C. Địa chỉ quảng bá
D. Không hợp lệ
ans: C [suy luận]

Câu 78: Cho các địa chỉ mạng dưới đây, hãy lựa chọn loại địa chỉ hợp lệ: 192.168.1.256/23
A. Địa chỉ mạng
B. Địa chỉ máy
C. Địa chỉ quảng bá
D. Không hợp lệ
ans: D [suy luận]

Câu 79: Cho các địa chỉ mạng dưới đây, hãy lựa chọn loại địa chỉ hợp lệ: 192.168.1.255/23
A. Địa chỉ mạng
B. Địa chỉ máy
C. Địa chỉ quảng bá
D. Không hợp lệ
ans: C [suy luận]

Câu 80: Cho các địa chỉ mạng dưới đây, hãy lựa chọn loại địa chỉ hợp lệ: 192.168.2.255/23
A. Địa chỉ mạng
B. Địa chỉ máy
C. Địa chỉ quảng bá
D. Không hợp lệ
ans: B [suy luận]

Câu 81: Cho các địa chỉ mạng dưới đây, hãy lựa chọn loại địa chỉ hợp lệ: 192.168.2.0/23
A. Địa chỉ mạng
B. Địa chỉ máy
C. Địa chỉ quảng bá
D. Không hợp lệ
ans: A [suy luận]

Câu 82: **MC_04_08** (đạt 0.0/1.0 điểm, không tích lũy vào tiến trình học)

Sắp xếp các giao thức định tuyến sau vào đúng loại của mình
Routing Information Protocol - RIP
A. Nội vùng - trạng thái liên kết (link-state)
B. Nội vùng - khoảng cách vector (distance vector)
C. Liên vùng
Open Shortest Path First - OSPF
A. Nội vùng - trạng thái liên kết (link-state)
B. Nội vùng - khoảng cách vector (distance vector)
C. Liên vùng
ans: B,A [suy luận]
```

----- Page 23 -----
```md
Câu 83: **MC_04_08** (tiếp)

Enhanced Interior Gateway Routing Protocol - EIGRP
A. Nội vùng - trạng thái liên kết (link-state)
B. Nội vùng - khoảng cách vector (distance vector)
C. Liên vùng
Border Gateway Protocol - BGP
A. Nội vùng - trạng thái liên kết (link-state)
B. Nội vùng - khoảng cách vector (distance vector)
C. Liên vùng
ans: B,C [suy luận]

Câu 84: **MC_04_04** (đạt 0.0/1.5 điểm, không tích lũy vào tiến trình học)

Cho các địa chỉ mạng dưới đây thuộc các phân lớp nào khi sử dụng cơ chế phân lớp? **(Câu điền — 4 giá trị)**
A. 150.55.1.128=B; 192.168.1.128=C; 10.168.255.240=A; 200.168.1.128=C
ans: A [suy luận]

Câu 85: **Truyền tin qua nhiều đường truyền** (tối đa 1 điểm)

Một đường truyền từ A tới B qua 3 kết nối vật lý nối tiếp nhau với băng thông lần lượt là 5 Mbps, 2 Mbps, 1 Mbps. Giả sử các đường kết nối này chỉ phục vụ liên kết giữa A và B và thời gian xử lý và lan truyền dữ liệu là không đáng kể (bằng 0). Hỏi thời gian cần thiết để truyền một gói tin có kích thước 43 MB từ A tới B là bao nhiêu giây? Chỉ ghi số giây, không ghi đơn vị hay bất cứ kí tự nào khác. Trường hợp số giây lẻ, làm tròn đến 2 chữ số sau phần thập phân. **(Câu điền)**
A. 344
ans: A [suy luận]
```

----- Page 24 -----
```md
Câu 74: Ưu điểm của giao thức UDP so với giao thức TCP là gì?
A. Có điều khiển luồng
B. Tốc độ gửi nhanh hơn
C. Quá trình bắt tay giữa máy nguồn và đích tốt hơn
D. Tin cậy hơn
ans: B [suy luận]
```

----- Page 25 -----
```md
Câu 75: Việc phân chia mạng theo CIDR thay vì theo phân lớp đem lại lợi ích gì?
A. Tận dụng được không gian địa chỉ tốt hơn
B. Không có đáp án đúng
C. Có thể chia nhỏ thành nhiều mạng con (subnet)
D. Cho phép chia thành nhiều phân lớp hơn so với trước
ans: A

Câu 76: Cho switch với bảng địa chỉ MAC và kết nối các máy như hình trên. Khi A gửi gói tin với địa chỉ đích là D đến switch thì switch sẽ ....
A. Cập nhật bảng địa chỉ MAC của A vào bảng địa chỉ MAC
B. Cập nhật địa chỉ MAC của D vào bảng địa chỉ MAC
C. Gửi gói tin theo cổng số 4 kết nối đến D
D. Gửi gói tin quảng bá đến các cổng từ 2-6
E. Gửi gói tin quảng bá đến các cổng từ 1-6
ans: A,D
```

----- Page 26 -----
```md
Câu 77: Cho một mạng có địa chỉ 172.16.0.0/16. Người ta sử dụng 5 bit phần HostID để chia mạng thành các mạng con (subnet). Hỏi số mạng con tối đa có thể chia là? (Chỉ ghi số) **(Câu điền — chỉ ghi số)**
A. 32
ans: A

Câu 78: Số máy tối đa trong mỗi mạng con là? (Chỉ ghi số) **(Câu điền — chỉ ghi số)**
A. 2046
ans: A

Câu 79: Vì sao khi sử dụng mã hóa Manchester và Manchester vi sai không xảy ra tình trạng mất đồng bộ giữa máy gửi và máy nhận?
A. Các đáp án khác đều sai
B. Chỉ sử dụng 2 mức điện áp
C. Có tốc độ tín hiệu lớn hơn với cùng tốc độ dữ liệu
D. Luôn có sự chuyển mức ở giữa các chu kỳ bit tín hiệu
ans: D

Câu 80: Vì sao chuẩn Ethernet không dây (IEEE 802.11) sử dụng kỹ thuật truy cập đường truyền CSMA/CA thay vì CSMA/CD vốn có khả năng giúp giảm thời gian phát lại khi có xung đột?
A. Vì CSMA/CD yêu cầu đường truyền duy trì tốc độ cố định
B. Vì CSMA/CA cho tốc độ truyền tốt hơn
C. Vì môi trường truyền không dây có đặc thù nhiễu nên nhiều trường hợp tín hiệu truyền không truyền đến hết các máy trong mạng
D. Vì CSMA/CD yêu cầu thiết bị phức tạp hơn
ans: C
```

----- Page 27 -----
```md
Câu 81: Vì sao tầng giao vận có thêm định danh CỔNG (PORT) khi đã có địa chỉ IP và địa chỉ MAC để gửi dữ liệu từ máy nguồn đến máy đích?
A. Máy đích cần thông tin cổng cho việc xử lý dữ liệu trên tầng ứng dụng
B. Máy gửi dùng thông tin cổng cho mục đích bảo mật chống tấn công
C. Máy đích và nguồn cần thông tin cổng để phân biệt các ứng dụng giao tiếp mạng trên cùng một máy
D. Router cần thông tin cổng cho việc định tuyến
ans: C

Câu 82: Cho switch với bảng địa chỉ MAC và kết nối các máy như hình trên. Khi A gửi gói tin với địa chỉ đích là D đến switch thì switch sẽ ....
A. Cập nhật bảng địa chỉ MAC của A vào bảng địa chỉ MAC
B. Cập nhật địa chỉ MAC của D vào bảng địa chỉ MAC
C. Gửi gói tin theo cổng số 4 kết nối đến D
D. Gửi gói tin quảng bá đến các cổng từ 2-6
E. Gửi gói tin quảng bá đến các cổng từ 1-6
ans: A,D
```

----- Page 28 -----
```md
Câu 83: Nguyên tắc "longest matching" được áp dụng khi một địa chỉ đích khớp với trong nhiều dòng của một bảng định tuyến vì ...
A. Vì mạng có số bit cho phần NetworkID càng lớn thì mạng càng nhỏ và gói tin nhiều khả năng đến đích nhanh hơn
B. Vì sẽ giúp giảm tải cho bộ định tuyến
C. Vì đó là giao tiếp mạng có băng thông lớn nhất
D. Vì mạng với số bit phần NetworkID càng lớn thì mạng càng lớn và tăng khả năng gói tin đến được đích
ans: A

Câu 84: Dữ liệu của một gói tin gửi đi là 1010011010001 (dạng nhị phân). Mã CRC cần gắn vào cho dữ liệu là bao nhiêu biết rằng G = 10011 (dạng nhị phân). Lưu ý chỉ ghi mã CRC dưới dạng nhị phân, không ghi thêm bất cứ kí tự nào. **(Câu điền — chỉ ghi mã nhị phân)**
A. 0100
ans: A

Câu 85: Sắp xếp các giao thức định tuyến sau vào đúng loại của mình
Routing Information Protocol - RIP
A. Nội vùng - trạng thái liên kết (link-state)
B. Nội vùng - khoảng cách vector (distance vector)
C. Liên vùng
Open Shortest Path First - OSPF
A. Nội vùng - trạng thái liên kết (link-state)
B. Nội vùng - khoảng cách vector (distance vector)
C. Liên vùng
Enhanced Interior Gateway Routing Protocol - EIGRP
A. Nội vùng - trạng thái liên kết (link-state)
B. Nội vùng - khoảng cách vector (distance vector)
C. Liên vùng
Border Gateway Protocol - BGP
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
B. Giao thức định tuyến nội vùng thường dựa trên 2 thuật toán dạng link-state và distance vector
C. Giao thức định tuyến liên vùng (BGP) dựa trên link-state
D. Giao thức định tuyến nội vùng của các miền tự trị (AS) khác nhau có thể khác nhau
ans: B,D [suy luận]

Câu 87: (Các) thiết bị mạng nào dưới đây hoạt động cả ở tầng 1-2-3 trong mô hình TCP/IP
A. Repeater
B. Hub
C. Bridge
D. Switch
E. Router
F. Computer
ans: E,F

Câu 88: Sắp xếp các giao thức định tuyến sau vào đúng loại của mình
Routing Information Protocol - RIP
A. Nội vùng - trạng thái liên kết (link-state)
B. Nội vùng - khoảng cách vector (distance vector)
C. Liên vùng
Open Shortest Path First - OSPF
A. Nội vùng - trạng thái liên kết (link-state)
B. Nội vùng - khoảng cách vector (distance vector)
C. Liên vùng
ans: B,A [suy luận]
```

----- Page 31 -----
```md
Câu 88 (tiếp): Sắp xếp các giao thức định tuyến sau vào đúng loại của mình
IGRP
A. Nội vùng - trạng thái liên kết (link-state)
B. Nội vùng - khoảng cách vector (distance vector)
C. Liên vùng
Border Gateway Protocol - BGP
A. Nội vùng - trạng thái liên kết (link-state)
B. Nội vùng - khoảng cách vector (distance vector)
C. Liên vùng
ans: B,C [suy luận]

Câu 89: Khi nhận được một gói tin, router chuyển tiếp gói tin ra cổng tương ứng dựa trên
A. Chính sách do người quản trị mạng đề ra
B. Giao thức định tuyến được thiết lập
C. Các dòng thông tin trong bảng định tuyến
D. Theo cấu hình do máy gửi yêu cầu
ans: C [suy luận]

Câu 90: Cho các địa chỉ mạng dưới đây thuộc các phân lớp nào khi sử dụng cơ chế phân lớp? **(Câu điền — 4 giá trị)**
A. 150.55.1.128=B; 192.168.1.128=C; 10.168.255.240=A; 200.168.1.128=C
ans: A [suy luận]
```

----- Page 32 -----
```md
Câu 91: Các gói tin có độ dài là 1500 bytes được truyền qua đường dây cáp quang với tốc độ 25 Mbps. Độ dài của đường dây là 290 km. Biết tốc độ lan truyền thông tin là 200000 km/s. Hỏi thời gian để truyền một gói tin là bao nhiêu micro giây? (chỉ ghi số, không ghi đơn vị) **(Câu điền — chỉ ghi số)**
A. 1930
ans: A

Câu 92: Đâu là các phát biểu ĐÚNG về giao thức định tuyến liên vùng và nội vùng
A. Giao thức định tuyến liên vùng (BGP) quan tâm đến hiệu năng (performance) hơn là chính sách (policy)
B. Giao thức định tuyến nội vùng thường dựa trên 2 thuật toán dạng link-state và distance vector
C. Giao thức định tuyến liên vùng (BGP) dựa trên link-state
D. Giao thức định tuyến nội vùng của các miền tự trị (AS) khác nhau có thể khác nhau
ans: B,D

Câu 93: (Các) ưu điểm của các thuật toán định tuyến dựa trên vector khoảng cách (distance vector) so với các thuật toán định tuyến trạng thái liên kết (link-state) là
A. Có tốc độ hội tụ nhanh hơn
B. Yêu cầu khả năng tính toán của router thấp hơn
C. Áp dụng được cho các mạng cỡ trung bình và lớn
D. Tránh được việc lặp vòng vô hạn
E. Yêu cầu ít băng thông hơn để trao đổi thông tin giữa các router
ans: B,E
```

----- Page 33 -----
```md
Câu 94: Trong phương pháp điều khiển truy cập đường truyền CSMA, vì sao đụng độ vẫn xảy ra dù các máy đã lắng nghe trước khi truyền?
A. Do có độ trễ lan truyền thông tin trong đường truyền
B. Có những máy truyền trên các tần số máy khác không lắng nghe được
C. Các máy mất đồng bộ nên không thể lắng nghe tín hiệu trên đường truyền
D. Các phương án khác đều sai
ans: A

Câu 95: Trong các phát biểu sau, phát biểu nào là ĐÚNG về địa chỉ MAC
A. Có độ dài 48 bit
B. MỖI nhà sản xuất CHỈ CÓ MỘT số OUI
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
B. MỖI nhà sản xuất CHỈ CÓ MỘT số OUI
C. Địa chỉ MAC có thể thay đổi khi một máy kết nối với các mạng khác nhau
D. Router dùng địa chỉ MAC để xác định đường đi
E. Có 24 bit đầu là số OUI để phân biệt các nhà sản xuất
F. Một thiết bị đầu cuối (máy tính, điện thoại thông minh) chỉ có thể có một địa chỉ MAC
ans: A,E
```

----- Page 36 -----
```md
Câu 101: Vì sao chuẩn Ethernet không dây (IEEE 802.11) sử dụng kỹ thuật truy cập đường truyền CSMA/CA thay vì CSMA/CD vốn có khả năng giúp giảm thời gian phát lại khi có xung đột?
A. Vì CSMA/CA cho tốc độ truyền tốt hơn
B. Vì CSMA/CD yêu cầu đường truyền duy trì tốc độ cố định
C. Vì CSMA/CD yêu cầu thiết bị phức tạp hơn
D. Vì môi trường truyền không dây có đặc thù nhiễu nên nhiều trường hợp tín hiệu truyền không truyền đến hết các máy trong mạng
ans: D

Câu 102: (Các) thiết bị mạng nào dưới đây hoạt động cả ở tầng 1-2-3 trong mô hình TCP/IP
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
D. Chia kênh thời gian (TDMA)
ans: C
```

----- Page 37 -----
```md
Câu 105: Việc phân chia mạng theo CIDR thay vì theo phân lớp đem lại lợi ích gì?
A. Tận dụng được không gian địa chỉ tốt hơn
B. Không có đáp án đúng
C. Cho phép chia thành nhiều phân lớp hơn so với trước
D. Có thể chia nhỏ thành nhiều mạng con (subnet)
ans: A

Câu 106: Nguyên tắc "longest matching" được áp dụng khi một địa chỉ đích khớp với trong nhiều dòng của một bảng định tuyến vì ...
A. Vì đó là giao tiếp mạng có băng thông lớn nhất
B. Vì sẽ giúp giảm tải cho bộ định tuyến
C. Vì mạng có số bit cho phần NetworkID càng lớn thì mạng càng nhỏ và gói tin nhiều khả năng đến đích nhanh hơn
D. Vì mạng với số bit phần NetworkID càng lớn thì mạng càng lớn và tăng khả năng gói tin đến được đích
ans: C
```

----- Page 38 -----
```md
Câu 107: Một gói tin IP có kích thước là 2420 bytes, bao gồm 20 bytes là phần header. Gói tin này phải đi qua một đường kết nối có MTU=1100 bytes. Gói tin phải phân chia thành mấy mảnh (fragment)? **(Câu điền — chỉ ghi số)**
A. 3
ans: A

Câu 108: Một gói tin IP có kích thước là 2420 bytes, bao gồm 20 bytes là phần header. Gói tin này phải đi qua một đường kết nối có MTU=1100 bytes. Trường offset của phân mảnh thứ 2 có giá trị là bao nhiêu? **(Câu điền — chỉ ghi số)**
A. 135
ans: A

Câu 109: Cho mô hình mạng gửi gói tin từ C đến D như hình trên. Khi gói tin từ máy C gửi đến Switch 1 thì địa chỉ MAC nguồn của gói tin tầng liên kết dữ liệu là **(Câu điền)**
A. CC-49-DE-D0-AB-7D
ans: A

Câu 110: Cho mô hình mạng gửi gói tin từ C đến D như hình trên. Khi gói tin từ máy C gửi đến Switch 1 thì địa chỉ MAC đích của gói tin tầng liên kết dữ liệu là **(Câu điền)**
A. E6-E9-00-17-BB-4B
ans: A
```

----- Page 39 -----
```md
Câu 111: Cho mô hình mạng gửi gói tin từ C đến D như hình trên. Địa chỉ IP nguồn của gói tin tầng mạng là **(Câu điền)**
A. 111.111.111.112
ans: A

Câu 112: Cho mô hình mạng gửi gói tin từ C đến D như hình trên. Địa chỉ IP đích của gói tin tầng mạng là **(Câu điền)**
A. 222.222.222.221
ans: A

Câu 113: Đâu là các phát biểu ĐÚNG về giao thức định tuyến liên vùng và nội vùng
A. Giao thức định tuyến liên vùng (BGP) quan tâm đến hiệu năng (performance) hơn là chính sách (policy)
B. Giao thức định tuyến nội vùng thường dựa trên 2 thuật toán dạng link-state và distance vector
C. Giao thức định tuyến liên vùng (BGP) dựa trên link-state
D. Giao thức định tuyến nội vùng của các miền tự trị (AS) khác nhau có thể khác nhau
ans: B,D

Câu 114: Vì sao tầng giao vận có thêm định danh CỔNG (PORT) khi đã có địa chỉ IP và địa chỉ MAC để gửi dữ liệu từ máy nguồn đến máy đích?
A. Router cần thông tin cổng cho việc định tuyến
B. Máy gửi dùng thông tin cổng cho mục đích bảo mật chống tấn công
C. Máy đích và nguồn cần thông tin cổng để phân biệt các ứng dụng giao tiếp mạng trên cùng một máy
D. Máy đích cần thông tin cổng cho việc xử lý dữ liệu trên tầng ứng dụng
ans: C

Câu 115: Khi sử dụng DHCP, chuyện gì xảy ra khi một client (máy tính) nhận được 2 offer từ 2 DHCP server khác nhau?
A. Client lựa chọn offer đến sớm hơn
B. Không có đáp án đúng
C. Client từ chối cả 2 offer do xung đột
D. Client chấp nhận cả 2 offer
E. Client lựa chọn offer theo chính sách người quản trị đề ra
ans: A
```

----- Page 40 -----
```md
```

----- Page 41 -----
```md
Câu 117: Cho các địa chỉ mạng dưới đây, hãy lựa chọn loại địa chỉ hợp lệ **(Câu điền — 7 mapping)**
A. 192.168.1.128/25=Địa chỉ mạng; 192.168.1.128/24=Địa chỉ máy; 192.168.1.255/25=Địa chỉ quảng bá; 192.168.1.256/23=Không hợp lệ; 192.168.1.255/23=Địa chỉ quảng bá; 192.168.2.255/23=Địa chỉ máy; 192.168.2.0/23=Địa chỉ mạng
ans: A

Câu 118: Sắp xếp các giao thức định tuyến sau vào đúng loại của mình
Routing Information Protocol - RIP
A. Nội vùng - trạng thái liên kết (link-state)
B. Nội vùng - khoảng cách vector (distance vector)
C. Liên vùng
Open Shortest Path First - OSPF
A. Nội vùng - trạng thái liên kết (link-state)
B. Nội vùng - khoảng cách vector (distance vector)
C. Liên vùng
Enhanced Interior Gateway Routing Protocol - EIGRP
A. Nội vùng - trạng thái liên kết (link-state)
B. Nội vùng - khoảng cách vector (distance vector)
C. Liên vùng
Border Gateway Protocol - BGP
A. Nội vùng - trạng thái liên kết (link-state)
B. Nội vùng - khoảng cách vector (distance vector)
C. Liên vùng
ans: A,B,B,C
```

----- Page 42 -----
```md
Câu 119: Cho các địa chỉ mạng dưới đây thuộc các phân lớp nào khi sử dụng cơ chế phân lớp? **(Câu điền — 4 giá trị)**
A. 150.55.1.128=B; 192.168.1.128=C; 10.168.255.240=A; 200.168.1.128=D
ans: A

Câu 120: Một đường truyền từ A tới B qua 3 kết nối vật lý nối tiếp nhau với băng thông lần lượt là 5 Mbps, 2 Mbps, 1 Mbps. Giả sử các đường kết nối này chỉ phục vụ liên kết giữa A và B và thời gian xử lý và lan truyền dữ liệu là không đáng kể (bằng 0). Hỏi thời gian cần thiết để truyền một gói tin có kích thước 43 MB từ A tới B là bao nhiêu giây? Chỉ ghi số giây, không ghi đơn vị hay bất cứ kí tự nào khác. Trường hợp số giây lẻ, làm tròn đến 2 chữ số sau phần thập phân. **(Câu điền — chỉ ghi số)**
A. 344
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
Câu 122: Chuyện gì xảy ra nếu MTU của một đường truyền kết nối quá nhỏ?
A. Giảm băng thông của đường truyền
B. Tăng khả năng lỗi bit trên đường truyền
C. Tăng khả năng tắc nghẽn do số gói tin tăng lên
D. Giảm hiệu suất truyền dữ liệu do phần header có kích thước cố định
ans: D

Câu 123: Lượng dữ liệu tối đa truyền qua một đường truyền trong một đơn vị thời gian là
A. Thông lượng
B. Tốc độ lan truyền
C. Tốc độ xử lý
D. Băng thông
ans: D

Câu 124: Trong các loại đường truyền dưới đây, đường truyền nào cho khả năng truyền tải với băng thông tốt nhất?
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
C. Độ suy hao tín hiệu lớn
D. Dễ bị ảnh hưởng bởi nhiễu từ sóng điện từ
E. Dễ hư hỏng
F. Kích thước lớn
ans: A,B,E

Câu 126: Vì sao khi sử dụng mã hóa Manchester và Manchester vi sai không xảy ra tình trạng mất đồng bộ giữa máy gửi và máy nhận?
A. Luôn có sự chuyển mức ở giữa các chu kỳ bit tín hiệu
B. Chỉ sử dụng 2 mức điện áp
C. Các đáp án khác đều sai
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
Câu 128: Đường kết nối mạng sử dụng công nghệ ADSL là dựa vào kỹ thuật chia kênh nào?
A. Kỹ thuật khác
B. Chia kênh mã code (CDMA)
C. Chia kênh tần số (FDMA)
D. Chia kênh thời gian (TDMA)
ans: C

Câu 129: Trong phương pháp điều khiển truy cập đường truyền CSMA, vì sao đụng độ vẫn xảy ra dù các máy đã lắng nghe trước khi truyền?
A. Do có độ trễ lan truyền thông tin trong đường truyền
B. Có những máy truyền trên các tần số máy khác không lắng nghe được
C. Các máy mất đồng bộ nên không thể lắng nghe tín hiệu trên đường truyền
D. Các phương án khác đều sai
ans: A

Câu 130: Cho switch với bảng địa chỉ MAC và kết nối các máy như hình trên. Khi A gửi gói tin với địa chỉ đích là D đến switch thì switch sẽ ...
A. Cập nhật bảng địa chỉ MAC của A vào bảng địa chỉ MAC
B. Cập nhật địa chỉ MAC của D vào bảng địa chỉ MAC
C. Gửi gói tin theo cổng số 4 kết nối đến D
D. Gửi gói tin quảng bá đến các cổng từ 2-6
E. Gửi gói tin quảng bá đến các cổng từ 1-6
ans: A,D
```

----- Page 47 -----
```md
Câu 131: (Các) thiết bị mạng nào dưới đây hoạt động cả ở tầng 1-2-3 trong mô hình TCP/IP
A. Repeater
B. Hub
C. Bridge
D. Switch
E. Router
F. Computer
ans: E,F

Câu 132: Cho mô hình mạng gửi gói tin từ C đến D như hình trên. Khi gói tin từ máy C gửi đến Switch 1 thì **(Câu điền — 4 giá trị: MAC nguồn; MAC đích; IP nguồn; IP đích)**
A. MAC_src=CC-49-DE-D0-AB-7D; MAC_dst=E6-E9-00-17-BB-4B; IP_src=111.111.111.112; IP_dst=222.222.222.221
ans: A
```

----- Page 48 -----
```md
Câu 134: Vì sao chuẩn Ethernet không dây (IEEE 802.11) sử dụng kỹ thuật truy cập đường truyền CSMA/CA thay vì CSMA/CD vốn có khả năng giúp giảm thời gian phát lại khi có xung đột?
A. Vì CSMA/CA cho tốc độ truyền tốt hơn
B. Vì CSMA/CD yêu cầu đường truyền duy trì tốc độ cố định
C. Vì CSMA/CD yêu cầu thiết bị phức tạp hơn
D. Vì môi trường truyền không dây có đặc thù nhiễu nên nhiều trường hợp tín hiệu truyền không truyền đến hết các máy trong mạng
ans: D

Câu 135: Khi sử dụng DHCP, chuyện gì xảy ra khi một client (máy tính) nhận được 2 offer từ 2 DHCP server khác nhau?
A. Client lựa chọn offer đến sớm hơn
B. Không có đáp án đúng
C. Client từ chối cả 2 offer do xung đột
D. Client chấp nhận cả 2 offer
E. Client lựa chọn offer theo chính sách người quản trị đề ra
ans: A
```

----- Page 49 -----
```md
Câu 136: Cho các địa chỉ mạng dưới đây, hãy lựa chọn loại địa chỉ hợp lệ **(Câu điền — 7 mapping)**
A. 192.168.1.128/25=Địa chỉ mạng; 192.168.1.128/24=Địa chỉ máy; 192.168.1.255/25=Địa chỉ quảng bá; 192.168.1.256/23=Không hợp lệ; 192.168.1.255/23=Địa chỉ quảng bá; 192.168.2.255/23=Địa chỉ máy; 192.168.2.0/23=Địa chỉ mạng
ans: A

Câu 137: Việc phân chia mạng theo CIDR thay vì theo phân lớp đem lại lợi ích gì?
A. Tận dụng được không gian địa chỉ tốt hơn
B. Không có đáp án đúng
C. Cho phép chia thành nhiều phân lớp hơn so với trước
D. Có thể chia nhỏ thành nhiều mạng con (subnet)
ans: A
```

----- Page 50 -----
```md
Câu 138: Cho các địa chỉ mạng dưới đây thuộc các phân lớp nào khi sử dụng cơ chế phân lớp? **(Câu điền — 4 giá trị)**
A. 150.55.1.128=B; 192.168.1.128=C; 10.168.255.240=A; 200.168.1.128=D
ans: A

Câu 139: Khi nhận được một gói tin, router chuyển tiếp gói tin ra cổng tương ứng dựa trên
A. Các dòng thông tin trong bảng định tuyến
B. Theo cấu hình do máy gửi yêu cầu
C. Chính sách do người quản trị mạng đề ra
D. Giao thức định tuyến được thiết lập
ans: A

Câu 140: Nguyên tắc "longest matching" được áp dụng khi một địa chỉ đích khớp với trong nhiều dòng của một bảng định tuyến vì ...
A. Vì đó là giao tiếp mạng có băng thông lớn nhất
B. Vì sẽ giúp giảm tải cho bộ định tuyến
C. Vì mạng có số bit cho phần NetworkID càng lớn thì mạng càng nhỏ và gói tin nhiều khả năng đến đích nhanh hơn
D. Vì mạng với số bit phần NetworkID càng lớn thì mạng càng lớn và tăng khả năng gói tin đến được đích
ans: C
```

----- Page 51 -----
```md
Câu 141: Đâu là các phát biểu ĐÚNG về giao thức định tuyến liên vùng và nội vùng
A. Giao thức định tuyến liên vùng (BGP) quan tâm đến hiệu năng (performance) hơn là chính sách (policy)
B. Giao thức định tuyến nội vùng thường dựa trên 2 thuật toán dạng link-state và distance vector
C. Giao thức định tuyến liên vùng (BGP) dựa trên link-state
D. Giao thức định tuyến nội vùng của các miền tự trị (AS) khác nhau có thể khác nhau
ans: B,D

Câu 142: Sắp xếp các giao thức định tuyến sau vào đúng loại của mình
Routing Information Protocol - RIP
A. Nội vùng - trạng thái liên kết (link-state)
B. Nội vùng - khoảng cách vector (distance vector)
C. Liên vùng
Open Shortest Path First - OSPF
A. Nội vùng - trạng thái liên kết (link-state)
B. Nội vùng - khoảng cách vector (distance vector)
C. Liên vùng
Enhanced Interior Gateway Routing Protocol - EIGRP
A. Nội vùng - trạng thái liên kết (link-state)
B. Nội vùng - khoảng cách vector (distance vector)
C. Liên vùng
Border Gateway Protocol - BGP
A. Nội vùng - trạng thái liên kết (link-state)
B. Nội vùng - khoảng cách vector (distance vector)
C. Liên vùng
ans: A,B,B,C
```

----- Page 52 -----
```md
Câu 143: Vì sao tầng giao vận có thêm định danh CỔNG (PORT) khi đã có địa chỉ IP và địa chỉ MAC để gửi dữ liệu từ máy nguồn đến máy đích?
A. Router cần thông tin cổng cho việc định tuyến
B. Máy gửi dùng thông tin cổng cho mục đích bảo mật chống tấn công
C. Máy đích và nguồn cần thông tin cổng để phân biệt các ứng dụng giao tiếp mạng trên cùng một máy
D. Máy đích cần thông tin cổng cho việc xử lý dữ liệu trên tầng ứng dụng
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
Câu 145: Cho một mạng có địa chỉ 172.16.0.0/16. Người ta sử dụng 5 bit phần HostID để chia mạng thành các mạng con (subnet). Hỏi số mạng con tối đa có thể chia là? (Chỉ ghi số) **(Câu điền)**
A. 32
ans: A

Câu 146: Số máy tối đa trong mỗi mạng con là? (Chỉ ghi số) **(Câu điền)**
A. 2046
ans: A

Câu 147: Một gói tin IP có kích thước là 2420 bytes, bao gồm 20 bytes là phần header. Gói tin này phải đi qua một đường kết nối có MTU=1100 bytes. Hỏi: Gói tin phải phân chia thành mấy mảnh (fragment)? **(Câu điền — chỉ ghi số)**
A. 3
ans: A

Câu 148: Một gói tin IP có kích thước là 2420 bytes, bao gồm 20 bytes là phần header. Gói tin này phải đi qua một đường kết nối có MTU=1100 bytes. Trường offset của phân mảnh thứ 2 có giá trị là bao nhiêu? **(Câu điền — chỉ ghi số)**
A. 135
ans: A

Câu 149: Một gói tin IP có kích thước là 2420 bytes, bao gồm 20 bytes là phần header. Gói tin này phải đi qua một đường kết nối có MTU=1420 bytes. Hỏi: Gói tin phải phân chia thành mấy mảnh (fragment)? **(Câu điền — chỉ ghi số)**
A. 2
ans: A

Câu 150: Một gói tin IP có kích thước là 2420 bytes, bao gồm 20 bytes là phần header. Gói tin này phải đi qua một đường kết nối có MTU=1420 bytes. Trường offset của phân mảnh thứ 2 có giá trị là bao nhiêu? **(Câu điền — chỉ ghi số)**
A. 175
ans: A
```

----- Page 54 -----
```md
Câu 151: Một đường truyền từ A tới B qua 3 kết nối vật lý nối tiếp nhau với băng thông lần lượt là 5 Mbps, 5 Mbps, 20 Mbps. Giả sử các đường kết nối này chỉ phục vụ liên kết giữa A và B và thời gian xử lý và lan truyền dữ liệu là không đáng kể (bằng 0). Hỏi thời gian cần thiết để truyền một gói tin có kích thước 23 MB từ A tới B là bao nhiêu giây? Chỉ ghi số giây, không ghi đơn vị hay bất cứ kí tự nào khác. Trường hợp số giây lẻ, làm tròn đến 2 chữ số sau phần thập phân. **(Câu điền)**
A. 36.8
ans: A

Câu 152: Dữ liệu của một gói tin gửi đi là 1101110111001 (dạng nhị phân). Mã CRC cần gắn vào cho dữ liệu là bao nhiêu biết rằng G = 10111 (dạng nhị phân). Lưu ý chỉ ghi mã CRC dưới dạng nhị phân, không ghi thêm bất cứ kí tự nào. **(Câu điền)**
A. 0100
ans: A

Câu 153: Một đường truyền từ A tới B qua 3 kết nối vật lý nối tiếp nhau với băng thông lần lượt là 5 Mbps, 2 Mbps, 1 Mbps. Giả sử các đường kết nối này chỉ phục vụ liên kết giữa A và B và thời gian xử lý và lan truyền dữ liệu là không đáng kể (bằng 0). Hỏi thời gian cần thiết để truyền một gói tin có kích thước 43 MB từ A tới B là bao nhiêu giây? Chỉ ghi số giây, không ghi đơn vị hay bất cứ kí tự nào khác. Trường hợp số giây lẻ, làm tròn đến 2 chữ số sau phần thập phân. **(Câu điền)**
A. 344
ans: A

Câu 154: Các gói tin có độ dài là 1200 bytes được truyền qua đường dây cáp quang với tốc độ 25 Mbps. Độ dài của đường dây là 220 km. Biết tốc độ lan truyền thông tin là 200000 km/s. Hỏi thời gian để truyền một gói tin là bao nhiêu micro giây? (chỉ ghi số, không ghi đơn vị) **(Câu điền)**
A. 1484
ans: A
```

----- Page 55 -----
```md
Câu 155: Cho switch với bảng địa chỉ MAC và kết nối các máy như hình trên. Khi A gửi gói tin với địa chỉ đích là D đến switch thì switch sẽ .... **(Chọn 2 đáp án)**
A. Cập nhật bảng địa chỉ MAC của A vào bảng địa chỉ MAC
B. Cập nhật địa chỉ MAC của D vào bảng địa chỉ MAC
C. Gửi gói tin theo cổng số 4 kết nối đến D
D. Gửi gói tin quảng bá đến các cổng từ 2-6
E. Gửi gói tin quảng bá đến các cổng từ 1-6
ans: A,D

Câu 156: Đâu là những nhược điểm của cáp quang so với các loại cáp khác? **(Chọn nhiều đáp án)**
A. Giá thành đắt đỏ
B. Lắp đặt phức tạp do cần thiết bị chuyên dụng
C. Độ suy hao tín hiệu lớn
D. Dễ bị ảnh hưởng bởi nhiễu từ sóng điện từ
E. Dễ hư hỏng
F. Kích thước lớn
ans: A,B,E
```

----- Page 56 -----
```md
Câu 157: Dữ liệu của một gói tin gửi đi là 1001110101101 (dạng nhị phân). Mã CRC cần gắn vào cho dữ liệu là bao nhiêu biết rằng G = 11101 (dạng nhị phân). Lưu ý chỉ ghi mã CRC dưới dạng nhị phân, không ghi thêm bất cứ kí tự nào. **(Câu điền)**
A. 0110
ans: A [suy luận]

Câu 158: Một gói tin IP có kích thước là 2420 bytes, bao gồm 20 bytes là phần header. Gói tin này phải đi qua một đường kết nối có MTU=1420 bytes. Hỏi: Gói tin phải phân chia thành mấy mảnh (fragment)? **(Câu điền — chỉ ghi số)**
A. 2
ans: A

Câu 159: Một gói tin IP có kích thước là 2420 bytes, bao gồm 20 bytes là phần header. Gói tin này phải đi qua một đường kết nối có MTU=1420 bytes. Trường offset của phân mảnh thứ 2 có giá trị là bao nhiêu? **(Câu điền — chỉ ghi số)**
A. 175
ans: A

Câu 160: Cho các địa chỉ mạng dưới đây, hãy lựa chọn loại địa chỉ hợp lệ — 192.168.1.128/25
A. Địa chỉ mạng
B. Địa chỉ máy
C. Địa chỉ quảng bá
D. Không hợp lệ
ans: A

Câu 161: Cho các địa chỉ mạng dưới đây, hãy lựa chọn loại địa chỉ hợp lệ — 192.168.1.128/24
A. Địa chỉ mạng
B. Địa chỉ máy
C. Địa chỉ quảng bá
D. Không hợp lệ
ans: B

Câu 162: Cho các địa chỉ mạng dưới đây, hãy lựa chọn loại địa chỉ hợp lệ — 192.168.1.255/25
A. Địa chỉ mạng
B. Địa chỉ máy
C. Địa chỉ quảng bá
D. Không hợp lệ
ans: C

Câu 163: Cho các địa chỉ mạng dưới đây, hãy lựa chọn loại địa chỉ hợp lệ — 192.168.1.256/23
A. Địa chỉ mạng
B. Địa chỉ máy
C. Địa chỉ quảng bá
D. Không hợp lệ
ans: D
```

----- Page 57 -----
```md
Câu 164: Cho các địa chỉ mạng dưới đây, hãy lựa chọn loại địa chỉ hợp lệ — 192.168.1.255/23
A. Địa chỉ mạng
B. Địa chỉ máy
C. Địa chỉ quảng bá
D. Không hợp lệ
ans: C

Câu 165: Cho các địa chỉ mạng dưới đây, hãy lựa chọn loại địa chỉ hợp lệ — 192.168.2.255/23
A. Địa chỉ mạng
B. Địa chỉ máy
C. Địa chỉ quảng bá
D. Không hợp lệ
ans: B

Câu 166: Cho các địa chỉ mạng dưới đây, hãy lựa chọn loại địa chỉ hợp lệ — 192.168.2.0/23
A. Địa chỉ mạng
B. Địa chỉ máy
C. Địa chỉ quảng bá
D. Không hợp lệ
ans: A
```

----- Page 58 -----
```md
Câu 167: Vì sao khi sử dụng mã hóa Manchester và Manchester vi sai không xảy ra tình trạng mất đồng bộ giữa máy gửi và máy nhận?
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

Câu 169: Đâu là những nhược điểm của cáp quang so với các loại cáp khác? **(Chọn nhiều đáp án)**
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
Câu 170: Các gói tin có độ dài là 1000 bytes được truyền qua đường dây cáp quang với tốc độ 200 Mbps. Độ dài của đường dây là 380 km. Biết tốc độ lan truyền thông tin là 200000 km/s. Hỏi thời gian để truyền một gói tin là bao nhiêu micro giây? (chỉ ghi số, không ghi đơn vị) **(Câu điền)**
A. 1940
ans: A

Câu 171: Cho các địa chỉ mạng dưới đây thuộc các phân lớp nào khi sử dụng cơ chế phân lớp? — 150.55.1.128 **(Câu điền — chỉ ghi A/B/C/D)**
A. B
ans: A

Câu 172: Cho các địa chỉ mạng dưới đây thuộc các phân lớp nào khi sử dụng cơ chế phân lớp? — 192.168.1.128 **(Câu điền — chỉ ghi A/B/C/D)**
A. C
ans: A

Câu 173: Cho các địa chỉ mạng dưới đây thuộc các phân lớp nào khi sử dụng cơ chế phân lớp? — 10.168.255.240 **(Câu điền — chỉ ghi A/B/C/D)**
A. A
ans: A

Câu 174: Cho các địa chỉ mạng dưới đây thuộc các phân lớp nào khi sử dụng cơ chế phân lớp? — 200.168.1.128 **(Câu điền — chỉ ghi A/B/C/D)**
A. D
ans: A
```

----- Page 60 -----
```md
Câu 175: Khi nhận được một gói tin, router chuyển tiếp gói tin ra cổng tương ứng dựa trên
A. Các dòng thông tin trong bảng định tuyến
B. Theo cấu hình do máy gửi yêu cầu
C. Chính sách do người quản trị mạng đề ra
D. Giao thức định tuyến được thiết lập
ans: A

Câu 176: Các gói tin có độ dài là 1200 bytes được truyền qua đường dây cáp quang với tốc độ 25 Mbps. Độ dài của đường dây là 220 km. Biết tốc độ lan truyền thông tin là 200000 km/s. Hỏi thời gian để truyền một gói tin là bao nhiêu micro giây? (chỉ ghi số, không ghi đơn vị) **(Câu điền)**
A. 1484
ans: A

Câu 177: Trong các phát biểu sau, phát biểu nào là ĐÚNG về địa chỉ MAC **(Chọn nhiều đáp án)**
A. Có độ dài 48 bit
B. MỖI nhà sản xuất CHỈ CÓ MỘT số OUI
C. Địa chỉ MAC có thể thay đổi khi một máy kết nối với các mạng khác nhau
D. Router dùng địa chỉ MAC để xác định đường đi
E. Có 24 bit đầu là số OUI để phân biệt các nhà sản xuất
F. Một thiết bị đầu cuối (máy tính, điện thoại thông minh) chỉ có thể có một địa chỉ MAC
ans: A,E
```

----- Page 61 -----
```md
Câu 178: Cho các địa chỉ mạng dưới đây thuộc các phân lớp nào khi sử dụng cơ chế phân lớp? — 150.55.1.128 **(Câu điền — chỉ ghi A/B/C/D)**
A. B
ans: A

Câu 179: Cho các địa chỉ mạng dưới đây thuộc các phân lớp nào khi sử dụng cơ chế phân lớp? — 192.168.1.128 **(Câu điền — chỉ ghi A/B/C/D)**
A. C
ans: A

Câu 180: Cho các địa chỉ mạng dưới đây thuộc các phân lớp nào khi sử dụng cơ chế phân lớp? — 10.168.255.240 **(Câu điền — chỉ ghi A/B/C/D)**
A. A
ans: A

Câu 181: Cho các địa chỉ mạng dưới đây thuộc các phân lớp nào khi sử dụng cơ chế phân lớp? — 200.168.1.128 **(Câu điền — chỉ ghi A/B/C/D)**
A. D
ans: A

Câu 182: (Các) thiết bị mạng nào dưới đây hoạt động cả ở tầng 1-2-3 trong mô hình TCP/IP **(Chọn nhiều đáp án)**
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
Câu 183: (Các) thiết bị mạng nào dưới đây hoạt động cả ở tầng 1-2-3 trong mô hình TCP/IP **(Chọn nhiều đáp án)**
A. Repeater
B. Hub
C. Bridge
D. Switch
E. Router
F. Computer
ans: E,F

Câu 184: Vì sao khi sử dụng mã hóa Manchester và Manchester vi sai không xảy ra tình trạng mất đồng bộ giữa máy gửi và máy nhận?
A. Luôn có sự chuyển mức ở giữa các chu kỳ bit tín hiệu
B. Chỉ sử dụng 2 mức điện áp
C. Có tốc độ tín hiệu lớn hơn với cùng tốc độ dữ liệu
D. Các đáp án khác đều sai
ans: A
```

----- Page 63 -----
```md
Câu 185: Cho switch với bảng địa chỉ MAC và kết nối các máy như hình trên. Khi A gửi gói tin với địa chỉ đích là D đến switch thì switch sẽ .... **(Chọn 2 đáp án)**
A. Cập nhật bảng địa chỉ MAC của A vào bảng địa chỉ MAC
B. Cập nhật địa chỉ MAC của D vào bảng địa chỉ MAC
C. Gửi gói tin theo cổng số 4 kết nối đến D
D. Gửi gói tin quảng bá đến các cổng từ 2-6
E. Gửi gói tin quảng bá đến các cổng từ 1-6
ans: A,D

Câu 186: Trong phương pháp điều khiển truy cập đường truyền CSMA, vì sao đụng độ vẫn xảy ra dù các máy đã lắng nghe trước khi truyền?
A. Có những máy truyền trên các tần số máy khác không lắng nghe được
B. Các phương án khác đều sai
C. Do có độ trễ lan truyền thông tin trong đường truyền
D. Các máy mất đồng bộ nên không thể lắng nghe tín hiệu trên đường truyền
ans: C

Câu 187: Cho các địa chỉ mạng dưới đây thuộc các phân lớp nào khi sử dụng cơ chế phân lớp? — 150.55.1.128 **(Câu điền — chỉ ghi A/B/C/D)**
A. B
ans: A

Câu 188: Cho các địa chỉ mạng dưới đây thuộc các phân lớp nào khi sử dụng cơ chế phân lớp? — 192.168.1.128 **(Câu điền — chỉ ghi A/B/C/D)**
A. C
ans: A

Câu 189: Cho các địa chỉ mạng dưới đây thuộc các phân lớp nào khi sử dụng cơ chế phân lớp? — 10.168.255.240 **(Câu điền — chỉ ghi A/B/C/D)**
A. A
ans: A

Câu 190: Cho các địa chỉ mạng dưới đây thuộc các phân lớp nào khi sử dụng cơ chế phân lớp? — 200.168.1.128 **(Câu điền — chỉ ghi A/B/C/D)**
A. D
ans: A
```

----- Page 64 -----
```md
Câu 191: Khi nhận được một gói tin, router chuyển tiếp gói tin ra cổng tương ứng dựa trên
A. Các dòng thông tin trong bảng định tuyến
B. Giao thức định tuyến được thiết lập
C. Theo cấu hình do máy gửi yêu cầu
D. Chính sách do người quản trị mạng đề ra
ans: A

Câu 192: Đâu là những nhược điểm của cáp quang so với các loại cáp khác? **(Chọn nhiều đáp án)**
A. Giá thành đắt đỏ
B. Lắp đặt phức tạp do cần thiết bị chuyên dụng
C. Độ suy hao tín hiệu lớn
D. Dễ bị ảnh hưởng bởi nhiễu từ sóng điện từ
E. Dễ hư hỏng
F. Kích thước lớn
ans: A,B,E

Câu 193: (Các) thiết bị mạng nào dưới đây hoạt động cả ở tầng 1-2-3 trong mô hình TCP/IP **(Chọn nhiều đáp án)**
A. Repeater
B. Hub
C. Bridge
D. Switch
E. Router
F. Computer
ans: E,F
```

----- Page 65 -----
```md
Câu 194: Vì sao chuẩn Ethernet không dây (IEEE 802.11) sử dụng kỹ thuật truy cập đường truyền CSMA/CA thay vì CSMA/CD vốn có khả năng giúp giảm thời gian phát lại khi có xung đột?
A. Vì CSMA/CD yêu cầu thiết bị phức tạp hơn
B. Vì CSMA/CA cho tốc độ truyền tốt hơn
C. Vì CSMA/CD yêu cầu đường truyền duy trì tốc độ cố định
D. Vì môi trường truyền không dây có đặc thù nhiễu nên nhiều trường hợp tín hiệu truyền không truyền đến hết các máy trong mạng
ans: D

Câu 195: Trong các loại đường truyền dưới đây, đường truyền nào cho khả năng truyền tải với băng thông tốt nhất?
A. Cáp quang
B. Cáp đồng trục
C. Cáp xoắn đôi
D. Truyền không dây
ans: A
```

----- Page 66 -----
```md
Câu 190: Một đường truyền từ A tới B qua 3 kết nối vật lý nối tiếp nhau với băng thông lần lượt là 5 Mbps, 5 Mbps, 20 Mbps. Giả sử các đường kết nối này chỉ phục vụ liên kết giữa A và B và thời gian xử lý và lan truyền dữ liệu là không đáng kể (bằng 0). Hỏi thời gian cần thiết để truyền một gói tin có kích thước 23 MB từ A tới B là bao nhiêu giây? **(Câu điền — chỉ ghi số giây, làm tròn 2 chữ số thập phân nếu lẻ)**
A. 36.8
ans: A

Câu 191: Vì sao khi sử dụng mã hóa Manchester và Manchester vi sai không xảy ra tình trạng mất đồng bộ giữa máy gửi và máy nhận?
A. Luôn có sự chuyển mức ở giữa các chu kỳ bit tín hiệu
B. Chỉ sử dụng 2 mức điện áp
C. Các đáp án khác đều sai
D. Có tốc độ tín hiệu lớn hơn với cùng tốc độ dữ liệu
ans: A

Câu 192: Trong phương pháp điều khiển truy cập đường truyền CSMA, vì sao đụng độ vẫn xảy ra dù các máy đã lắng nghe trước khi truyền?
A. Do có độ trễ lan truyền thông tin trong đường truyền
B. Có những máy truyền trên các tần số máy khác không lắng nghe được
C. Các máy mất đồng bộ nên không thể lắng nghe tín hiệu trên đường truyền
D. Các phương án khác đều sai
ans: A
```

----- Page 67 -----
```md
Câu 193: Dữ liệu của một gói tin gửi đi là 1101110111001 (dạng nhị phân). Mã CRC cần gắn vào cho dữ liệu là bao nhiêu biết rằng G = 10111 (dạng nhị phân). Lưu ý chỉ ghi mã CRC dưới dạng nhị phân, không ghi thêm bất cứ ký tự nào **(Câu điền)**
A. 0100
ans: A

Câu 194: Trong các phát biểu sau, phát biểu nào là ĐÚNG về địa chỉ MAC
A. Có độ dài 48 bit
B. MỖI nhà sản xuất CHỈ CÓ MỘT số OUI
C. Địa chỉ MAC có thể thay đổi khi một máy kết nối với các mạng khác nhau
D. Router dùng địa chỉ MAC để xác định đường đi
E. Có 24 bit đầu là số OUI để phân biệt các nhà sản xuất
F. Một thiết bị đầu cuối (máy tính, điện thoại thông minh) chỉ có thể có một địa chỉ MAC
ans: A,E
```

----- Page 68 -----
```md
Câu 195: Cho địa chỉ mạng 150.55.1.128 thuộc phân lớp nào khi sử dụng cơ chế phân lớp? **(Câu điền — chỉ ghi A/B/C/D)**
A. B
ans: A

Câu 196: Cho địa chỉ mạng 192.168.1.128 thuộc phân lớp nào khi sử dụng cơ chế phân lớp? **(Câu điền — chỉ ghi A/B/C/D)**
A. C
ans: A

Câu 197: Cho địa chỉ mạng 10.168.255.240 thuộc phân lớp nào khi sử dụng cơ chế phân lớp? **(Câu điền — chỉ ghi A/B/C/D)**
A. A
ans: A

Câu 198: Cho địa chỉ mạng 200.168.1.128 thuộc phân lớp nào khi sử dụng cơ chế phân lớp? **(Câu điền — chỉ ghi A/B/C/D)**
A. C
ans: A

Câu 199: Đường kết nối mạng sử dụng công nghệ ADSL là dựa vào kỹ thuật chia kênh nào?
A. Chia kênh mã code (CDMA)
B. Chia kênh tần số (FDMA)
C. Kỹ thuật khác
D. Chia kênh thời gian (TDMA)
ans: B

Câu 200: Đâu là các phát biểu ĐÚNG về giao thức định tuyến liên vùng và nội vùng
A. Giao thức định tuyến liên vùng (BGP) quan tâm đến hiệu năng (performance) hơn là chính sách (policy)
B. Giao thức định tuyến nội vùng thường dựa trên 2 thuật toán dạng link-state và distance vector
C. Giao thức định tuyến liên vùng (BGP) dựa trên link-state
D. Giao thức định tuyến nội vùng của các miền tự trị (AS) khác nhau có thể khác nhau
ans: B,D
```

----- Page 69 -----
```md
Câu 201: Một gói tin IP có kích thước là 2820 bytes, bao gồm 20 bytes là phần header. Gói tin này phải đi qua một đường kết nối có MTU=700 bytes. Gói tin phải phân chia thành mấy mảnh (fragment)? **(Câu điền — chỉ ghi số)**
A. 4
ans: A

Câu 202: Một gói tin IP có kích thước là 2820 bytes, bao gồm 20 bytes là phần header. Gói tin này phải đi qua một đường kết nối có MTU=700 bytes. Trường offset của phân mảnh thứ 2 có giá trị là bao nhiêu? **(Câu điền — chỉ ghi số)**
A. 85
ans: A

Câu 203: Khi nhận được một gói tin, router chuyển tiếp gói tin ra cổng tương ứng dựa trên
A. Giao thức định tuyến được thiết lập
B. Chính sách do người quản trị mạng đề ra
C. Các dòng thông tin trong bảng định tuyến
D. Theo cấu hình do máy gửi yêu cầu
ans: C
```

----- Page 70 -----
```md
Câu 1: Assume the path from A to B through 3 connection links with the bandwidths of 4Mbps, 1Mbps, and 2 Mbps. If all links only serve the connection between A and B, and propagation delay is nearly zero, how long (seconds) does A need to transfer a 20MB file to B?
A. 140
B. 320
C. 40
D. 160
E. 80
F. 200
ans: D

Câu 2: What will happen if MTU of a network connection is too small?
A. It increases the error probability
B. It reduces the performance of data transmission because header has a fixed size
C. It increases the network congestion because of the number of packets
D. It reduces the bandwidth of the network connection
ans: B

Câu 3: The first Network was called ____________
A. CRNET
B. NSFNET
C. ASAPNET
D. ARPANET
ans: D

Câu 4: In the layer hierarchy as the data packet moves from the upper to the lower layers, headers are ____________
A. Added
B. Modified
C. Removed
D. Rearranged
ans: A

Câu 5: Which of the following statement(s) are TRUE about the routing table?
A. A router consults the routing table to determine the optimal path for reaching the destination, considering the destination IP address of the incoming IP packets.
B. A router consults the routing table to determine the optimal path for reaching the destination, considering the source IP address of the incoming IP packets.
C. If a router cannot find the matching entry in its routing table for the incoming IP packet, it will broadcast the incoming packet to all ports except the incoming port.
D. If a router cannot find the matching entry in its routing table for the incoming IP packet, it will broadcast the incoming packet to all ports.
ans: A

Câu 6: Which of the following statements are TRUE about the self-learning mechanism of switches? (Can be multiple correct answers)
A. When a frame arrives a switch, switch will update its MAC address table based on the source address field of the frame
B. When a frame arrives a switch, switch will update its MAC address table based on the destination address field of the frame
C. When an entry of the MAC address table was added, it will remain until being updated by the new information.
D. An entry in the MAC address table will expire if left unused and reached the timeout.
ans: A,D

Câu 7: A network uses 4-bit CHECKSUM to detect error caused by network transmission. Providing data as 1001 1011 1101, what is the generated checksum code?
A. 1111
B. 0111
C. 0011
E. 0000
F. 1110
G. None of the mentioned
ans: G

Câu 8: Which of the following IPv4 address(es) are VALID for a public IP address if we use CIDR method for allocating IP addresses and for IP routing?
A. 192.168.1.16
B. 10.0.0.1
C. 23.3.4.256
D. 11.0.0.1
E. 172.15.4.9
F. 172.16.9.4
ans: D,E

Câu 9: Servers are those computers which provide resources to other computers connected by?
A. Network
B. Server
C. Backup system
D. Modem
ans: A

Câu 10: Which type of network would use phone lines?
A. WAN
B. LAN
C. Wireless
D. WWAN
ans: A

Câu 11: A device that connects to a network without the use of cables is said to be?
A. Distributed
B. Centralised
C. Cable
D. Wireless
ans: D

Câu 12: Switch is associated with ______ network?
A. Bus
B. Ring
C. Star
D. Mesh
ans: C

Câu 13: Which of the following represents the fastest data transmission speed??
A. bps
B. Mbps
C. Kbps
D. Gbps
ans: D

Câu 14: In OSI network architecture, the routing is performed by?
A. Network Layer
B. Transport layer
C. Datalink layer
D. Application layer
ans: A

Câu 15: How many bits are there in the ethernet address?
A. 64 bits
B. 48 bits
C. 16 bits
D. 32 bits
ans: B

Câu 16: Why do we need ports in Transport Layer while we have IP Address to send data packet to the destinated computer?
A. Routers need port information for routing
B. A destinated computer needs port information for data processing
C. A destinated computer needs port information to distinguish/separate its programs
D. Senders use port information to hide themselves from intruders
ans: C

Câu 17: Which statement is WRONG about Autonomous System (AS) in routing?
A. The same routing policy is applied in a single AS
B. Intra-domain routing protocols are used inside AS
C. Inter-domain routing protocols are used to connect multiple AS together
D. Number of AS is fixed globally
ans: D

Câu 18: What is the purpose of Dynamic Host Configuration Protocol?
A. Dynamically obtains IP address from network server when it "joins" network
B. Transfer IP Address among computers
C. Configure computer routing tables
D. Set up computer configuration through remote connection
ans: A

Câu 19: What is the main function of multiple access protocols in Datalink Layer? (Can be multiple correct answers)
A. Let computers join a new network
B. Determines how nodes share channel
C. Communication about channel sharing must use channel itself
D. Help computers to access video, audio, images on Internet
ans: B,C

Câu 20: What is the disadvantage of dynamic routing protocols?
A. Backup link cannot be used
B. Difficult to manage
C. Difficult to adapt with changes of network structure
D. Insecure
ans: D

Câu 21: A network uses parity bit to detect error caused by network transmission. Providing data as 1001 1100, what parity code should be used?
A. 0
B. 01
C. 1
D. 11
ans: A

Câu 22: A datagram (1011 1000 0011 1100) was sent using Cyclic Redundancy Check (CRC) for error detection. Knowing that G = 10011, compute CRC that A need to append to the original datagram.
A. 1100
B. 1001
C. 0110
D. 1011
E. 0011
F. None of the mentioned
ans: A
```

----- Page 71 -----
```md
Câu 23: Among the optical-distribution architectures that are essentially switched ethernet is ___________
A. PON
B. MON
C. AON
D. NON
ans: C

Câu 24: In wireless ad-hoc network, ___________
A. Access point is must
B. All nodes are access points
C. Nodes are not required
D. Access point is not required
ans: D

Câu 25: Which of these is not a network edge device?
A. Switch
B. Server
C. PC
D. Smartphone
ans: A

Câu 26: Which multiple access technique is used by IEEE 802.11 standard for wireless LAN?
A. CDMA
B. CSMA/CA
C. CSMA/CD
D. ALOHA
ans: B

Câu 27: Which field helps to check rearrangement of the fragments?
A. Flag
B. TTL
C. Identifier
D. Offset
ans: D

Câu 28: In classful addressing, a large part of available addresses are ___________?
A. Organized
B. Wasted
C. Blocked
D. Communicated
ans: B

Câu 29: Which of the following devices are working at the Datalink-layer in the OSI Reference Model? (Can be multiple correct answers)
A. Repeater
B. Hub
C. Router
D. Switch
E. Bridge
F. Personal computer
ans: D,E

Câu 30: How many layers are in the TCP/IP model?
A. 4
B. 6
C. 5
D. 7
ans: A

Câu 31: Which of the following items is not used in Local Area Networks (LAN)??
A. Interface card
B. Computer
C. Cable
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
B. Tree
C. Star
D. Ring
ans: A

Câu 34: What is the benefit of UDP in comparison with TCP?
A. Higher speed
B. Flow Control
C. More reliable
D. Better handshaking step
ans: A

Câu 35: Given a network connection between two hosts with a Round-Trip Time (RTT) of 100 ms, a bandwidth rate of 15 Mbps, and a maximum payload size of 1500 bytes, if we need to transfer 15000 bytes of data using the stop-and-wait mechanism, how long would it take to complete the data transfer? (in milliseconds)
A. 1080
B. 1005
C. 40
D. 1000
E. 104
F. 1040
ans: D

Câu 36: Forwarding table (MAC table) of a switch is as bellows:

| Host | Interface |
| :--- | :--- |
| 12-12-12-ab-ab-ab | e1 |
| 11-11-11-dd-dd-dd | e2 |
| 33-33-33-ee-ee-ee | e3 |
| 55-55-55-cc-cc-cc | e4 |

What will the switch do when it receives a frame with destination address 12-12-12-ab-ab-ab and source address 11-11-11-dd-dd-dd from the port e3. (Can be multiple correct answers)
A. Destroy the frame
B. Forward the frame to port e1
C. Forward the frame to port e2
D. Broadcast the frame
E. Add/Update the address 12-12-12-ab-ab-ab to the forwarding table
F. Add/Update the address 11-11-11-dd-dd-dd to the forwarding table
ans: B,F

Câu 37: Forwarding table (MAC table) of a switch is as bellows:

| Host | Interface |
| :--- | :--- |
| 12-12-12-ab-ab-ab | e1 |
| 11-11-11-dd-dd-dd | e2 |
| 33-33-33-ee-ee-ee | e3 |
| 55-55-55-cc-cc-cc | e4 |

What will the switch do when it receives a frame with destination address 12-12-12-ab-ab-ae and source address 33-33-33-ee-ee-ee from the port e1. (Can be multiple correct answers)
A. Destroy the frame
B. Forward the frame to port e1
C. Forward the frame to port e2
D. Broadcast the frame
E. Add/Update the address 12-12-12-ab-ab-ae to the forwarding table
F. Add/Update the address 33-33-33-ee-ee-ee to the forwarding table
ans: D,F

Câu 38: If an IP packet with a payload size of 4926 bytes is sent into a network segment with an MTU of 880 bytes, and assuming the IP header size to be 20 bytes. How many fragments do we need to split the IP packet to meet the requirement of network segment?
A. 4
B. 6
C. 5
D. 7
ans: B

Câu 39: If an IP packet with a payload size of 4926 bytes is sent into a network segment with an MTU of 880 bytes, and assuming the IP header size to be 20 bytes. What will be the size of data (payload) in the last IP fragment?
A. 626
B. 426
C. 440
D. 526
E. 640
F. 520
ans: A

Câu 40: Giving a routing table of a router as follows:

| Network Address | Next-hop | Interface |
| :--- | :--- | :--- |
| 192.168.4.0/22 | A | 1 |
| 192.168.7.0/24 | B | 2 |
| 192.168.0.0/16 | C | 3 |
| 10.0.0.128/25 | D | 4 |
| 10.0.0.0/26 | E | 5 |

Which operation will the router do if it receives an IP packet with the destination IP address 192.168.6.31?
A. It will forward the packet to the interface 1
B. It will forward the packet to the interface 2
C. It will forward the packet to the interface 3
D. It will forward the packet to the interface 4
E. It will forward the packet to the interface 5
F. It will discard the packet
ans: A

Câu 41: Giving a routing table of a router as follows:

| Network Address | Next-hop | Interface |
| :--- | :--- | :--- |
| 192.168.4.0/22 | A | 1 |
| 192.168.7.0/24 | B | 2 |
| 192.168.0.0/16 | C | 3 |
| 10.0.0.128/25 | D | 4 |
| 10.0.0.0/26 | E | 5 |

Which operation will the router do if it receives an IP packet with the destination IP address 192.168.8.31?
A. It will forward the packet to the interface 1
B. It will forward the packet to the interface 2
C. It will forward the packet to the interface 3
D. It will forward the packet to the interface 4
E. It will forward the packet to the interface 5
F. It will discard the packet
ans: C

Câu 42: Giving a routing table of a router as follows:

| Network Address | Next-hop | Interface |
| :--- | :--- | :--- |
| 192.168.4.0/22 | A | 1 |
| 192.168.7.0/24 | B | 2 |
| 192.168.0.0/16 | C | 3 |
| 10.0.0.128/25 | D | 4 |
| 10.0.0.0/26 | E | 5 |

Which operation will the router do if it receives an IP packet with the destination IP address 10.0.1.0?
A. It will forward the packet to the interface 1
B. It will forward the packet to the interface 2
C. It will forward the packet to the interface 3
D. It will forward the packet to the interface 4
E. It will forward the packet to the interface 5
F. It will discard the packet
ans: F

Câu 43: Giving a network with the following IP information: 200.23.0.0/22. How many bits are used to distinguish this network from others?
A. 10
B. 200
C. 22
D. 32
ans: C

Câu 44: Giving a network with the following IP information: 200.23.0.0/22. Maximum devices belong to this network?
A. 1024
B. 2^22
C. 1022
D. 512
ans: C
```

----- Page 72 -----
```md
Câu 45: Giving a network with the following IP information: 200.23.0.0/22. How many subnets having 24 bits for network ID can be splitted from the original network?
A. 2
B. 8
C. 4
D. 6
ans: C

Câu 46: Giving a network with the following IP information: 200.23.0.0/22. We want to split the original network to sub-networks. Each sub-network has 32 PCs. What is the maximum number of sub-networks that can be generated from the original network?
A. 16
B. 32
C. 64
D. 14
E. 30
F. 62
ans: A

Câu 47: Giving a network with the following IP information: 200.23.0.0/22. Which address does not belong to the original network?
A. 200.23.2.1
B. 200.23.1.1
C. 200.23.3.1
D. 200.23.4.1
ans: D
```

----- Page 73 -----
```md
Câu 1: In TCP/IP model, at which layer the following functionalities could be performed? **(Ghép cặp)**
A. Transferring data between applications=Transport layer; Forwarding data according to MAC address=Datalink layer; Acknowledgement and Retransmission=Transport layer; Controlling data transmission between hosts connected by a physical link=Datalink layer
ans: A

Câu 2: According to layer architecture, what layer does not perform?
A. Encapsulate the data received from the upper layer
B. Extract the header of the data received from the lower layer
C. Call service of the lower layer
D. Replace the header of the data received from the upper layer.
ans: D

Câu 3: Which comparison between packet switching and circuit switching communication is correct?
A. Packet switching offers better line transmission efficiency
B. Circuit switching offers better line transmission efficiency
C. Packet switching guarantee no congestion
D. Circuit switching guarantee no congestion
ans: A

Câu 4: What are the advantages of the connectionless-oriented communication over connection-oriented communication? (Choose all correct answers)
A. Simpler
B. Faster
C. More reliable
D. No congestion
ans: A,B
```

----- Page 74 -----
```md
Câu 5: Why data transferring from an upper layer to a lower is encapsulated?
A. To divide data to small amount
B. To protect data from attacks
C. To add control information serving for the protocol of the layer
D. No need.
ans: C

Câu 6: What is the correct statement about protocol?
A. Protocol is a mechanism to collaborate between different layers of a network node.
B. Protocol is a mechanism to collaborate between different layer of 2 network nodes.
C. Protocol is a mechanism to collaborate between the same layer of 2 network nodes.
D. None of above.
ans: C

Câu 7: Which of the following characteristics belong to NRZ-L?(Choose 2 answers)
A. Using 2 voltage levels +V and -V
B. Each bit is represented by one pulse +V and one pulse -V
C. Bit 1 is represented by one pulse +V or 1 pulse -V
D. In the middle of bit interval, the voltage level crosses 0.
ans: A,C

Câu 8: A transmission line can transmit 20.000.000 pulse/s. In expecting to be able to transmit data with rate at least 8 Mbps, which encoding technique should be used?
A. Manchester
B. NRZ-L
C. AMI-Bipolar
D. All of above
ans: D

Câu 9: The datalink layer may perform which of following functionalities (choose all correct answers)
A. Represent bits by signals and vice visa
B. Numbering data frames
C. Check if there are errors in received data
D. Deliver data to the upper layer
ans: C,D

Câu 10: Amongst bellow CRC, which code can detect the most of errors?
A. CRC-8
B. CRC-12
C. CRC-16
D. CRC-32
ans: D

Câu 11: A and B are connected to each other, the network interface of A follows Fast Ethernet standard and the network interface of B follows Giga Ethernet standard. Which of following mechanisms allows to keep B sending data in a speed suitable to the processing capacity of A?
A. Flow control
B. Congestion control
C. Media access control
D. Error control
ans: A

Câu 12: Given a star topology network, choose the media control method appropriate to the network
A. CSMA
B. TDMA
C. Self-learning mechanism of switch
D. None of above
ans: C

Câu 13: Forwarding table of a switch is as following. What the switch does when it receives a frame with source address 11-22-33-11-22-33 and destination address a1-a1-b2-b2-c3-c3? (Choose all possible actions)

| Host | Interface |
| :--- | :--- |
| a1-a1-b2-b2-c3-c3 | e0 |
| a2-a2-b3-b3-c4-c4 | e1 |
| aa-bb-cc-11-22-33 | e2 |
| bc-bc-ac-ac-11-11 | e3 |

A. Send frame to one port
B. Send the frame out of all its port except where the frame comes from
C. Add the destination address to the forwarding table
D. Add the source address to the forwarding table.
ans: A,D

Câu 14: 10 network nodes connected to each other according to Ethernet standard using star topology, which of the following control method can be used?
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

Câu 16: Which network the IP address 97.0.3.21/21 belongs to? **(Câu điền)**
A. 97.0.0.0/21
ans: A

Câu 17: How many hosts the network with mask 25 may have? **(Câu điền — chỉ ghi số)**
A. 126
ans: A

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

Câu 21 (Tự luận): An administrator is given a range of IP address in the network 10.20.64.0/22. He intends to organize his network in as many subnetworks as possible so that each subnetwork may have 400 hosts? How can he assign IP addresses to the subnetworks? Explain the choice. What are addresses and masks of subnetworks. How many subnetworks there could be?
ans: [suy luận]

Câu 22 (Tự luận): Given a topology as in the figure where hosts are not shown. The administrator has defined routing tables for routers but recently link CD is failed. Help the administrator to define new routing table for routers B, C and D so that all communications between networks and the Internet can be continued.
ans: [suy luận]
```

----- Page 76 -----
```md
Câu 1: Ánh xạ các phương pháp sau về các loại tương ứng — TDMA
A. Phương pháp đa truy nhập phân chia theo thời gian
B. Phương pháp đa truy nhập phân chia theo tần số
C. Phương pháp đa truy nhập phân chia theo mã
D. Phương pháp đa truy nhập dùng token
ans: A

Câu 2: Ánh xạ các phương pháp sau về các loại tương ứng — FDMA
A. Phương pháp đa truy nhập phân chia theo thời gian
B. Phương pháp đa truy nhập phân chia theo tần số
C. Phương pháp đa truy nhập phân chia theo mã
D. Phương pháp đa truy nhập dùng token
ans: B

Câu 3: Ánh xạ các phương pháp sau về các loại tương ứng — CSMA
A. Phương pháp đa truy nhập phân chia theo thời gian
B. Phương pháp đa truy nhập phân chia theo tần số
C. Phương pháp đa truy nhập cảm nhận sóng mang
D. Phương pháp đa truy nhập dùng token
ans: C

Câu 4: Ánh xạ các phương pháp sau về các loại tương ứng — Token Ring
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

Câu 6: Khi truyền dữ liệu từ máy A đến máy B, giả thiết gói tin đi qua 13 router trong mạng, số card mạng gói tin đi qua là bao nhiêu?
A. 13
B. 1
C. 24
D. 28
ans: D
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
B. Tất cả các yếu tố đã được đề cập
C. Tải trên đường truyền
D. Tốc độ xử lý của nút nhận
E. Băng thông đường truyền
ans: B
```

----- Page 79 -----
```md
Câu 9: Mạng cần cung cấp địa chỉ cho 51 máy cần dùng mặt nạ mạng nào để hạn chế dư thừa địa chỉ ip? (Nhập mặt nạ mạng dạng thập phân, ví dụ: 255.255.255.0) **(Câu điền)**
A. 255.255.255.192
ans: A

Câu 10: Hai tiến trình thực hiện truyền tin theo giao thức TCP. Tiến trình gửi đang sử dụng cửa sổ kiểm soát tắc nghẽn (congestion window) là 14.000 byte và ngưỡng kiểm soát tắc nghẽn (ssthreshold) là 11.200 byte. Tiến trình gửi nhận được gói tin ACK báo thành công cho các gói tin đã gửi, trong đó giá trị Receive Window là 65.535. Giả sử các bên đã thỏa thuận 1 MSS = 1.400 byte. Trong lượt tiếp theo, tiến trình gửi có thể gửi tối đa bao nhiêu byte?(Chỉ ghi đáp án số, không kèm đơn vị) **(Câu điền)**
A. 15400
ans: A
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

Host | Interface
11-11-11-aa-aa-aa | e1
22-22-22-bb-bb-bb | e2
33-33-33-cc-cc-cc | e3
44-44-44-dd-dd-dd | e1

A. Hủy khung tin
B. Gửi khung tin ra cổng e1
C. Gửi khung tin ra cổng e2
D. Gửi báo lỗi cho nút nguồn
E. Gửi khung tin ra tất cả các cổng trừ cổng e2
F. Thêm địa chỉ 55-55-55-ee-ee-ee vào bảng MAC/CAM với cổng chuyển tiếp là e2
ans: B,F [suy luận]
```

----- Page 82 -----
```md
Câu 13: Cho một đường truyền từ A đến B đi qua 3 đoạn kết nối khác nhau có băng thông lần lượt là 5 Mbps, 10 Mbps và 15 Mbps. Giả sử các đường kết nối này chỉ phục vụ cho việc truyền dữ liệu từ A đến B, trễ trên thiết bị không đáng kể, và tỷ lệ lỗi và mất gói tin bằng 0. Hỏi thông lượng trung bình từ A đến B là bao nhiêu?
A. 10 Mbps
B. 5 Mbps
C. 15 Mbps
D. Không thể xác định được
ans: B [suy luận]

Câu 14: Điểm khác biệt khi triển khai dịch vụ theo mô hình P2P so với mô hình Client-Server là gì? (Chọn 3 đáp án)
A. Không cần tất cả các nút mạng thành phần phải duy trì kết nối liên tục
B. Không cần quản lý tài nguyên tập trung
C. Các nút mạng có thể vừa gửi yêu cầu dịch vụ, vừa cung cấp dịch vụ cho các nút khác
D. Có điểm thắt nút cổ chai
ans: A,B,C [suy luận]
```

----- Page 83 -----
```md
Câu 15: Giao thức nào sau đây nằm ở tầng giao vận? (Chọn 2 đáp án)
A. IP
B. TCP
C. UDP
D. HTTP
ans: B,C [suy luận]

Câu 16: Đâu là đặc điểm của mạng sử dụng kỹ thuật chuyển mạch kênh (Chọn 3 đáp án)
A. Thiết lập kênh trước khi truyền
B. Gói tin được truyền đi ngay
C. Các gói tin có thể tới đích không đúng thứ tự
D. Các gói tin trong mỗi kênh truyền giữa 2 nút luôn đi theo tuyến đường giống nhau
E. Tài nguyên được cấp phát để dùng riêng trên mỗi kênh truyền giữa 2 nút
ans: A,D,E [suy luận]
```

----- Page 84 -----
```md
Câu 17: Cơ chế tự học của switch được dùng để làm gì
A. Giúp chuyển tiếp dữ liệu giữa các mạng
B. Giúp chuyển tiếp dữ liệu trong một mạng LAN có topo dạng trục
C. Giúp chuyển tiếp dữ liệu trong một mạng LAN không dây.
D. Giúp chuyển tiếp dữ liệu trong một mạng LAN có topo dạng điểm-điểm
ans: D [suy luận]

Câu 18: Phát biểu nào sau đây là đúng về máy chủ tên miền gốc (root server) trong hệ thống DNS? (Chọn 2 đáp án)
A. Quản lý thông tin các máy chủ tên miền cấp 1 (TLD Server)
B. Lưu trữ thông tin của toàn bộ tên miền trên Internet
C. Không trả lời các thông điệp DNS Query truy vấn tên miền
D. Triển khai ở nhiều vị trí khác nhau trên Internet
ans: A,D [suy luận]
```

----- Page 85 -----
```md
Câu 19: Cho một đường truyền có thể phát được 2^20 xung/s (pulse/s), khi áp dụng phương pháp mã hoá NRZ-L, tốc độ dữ liệu sinh ra là bao nhiêu.
A. 10 Mbps
B. 1 Mbps
C. 0.5 Mbps
D. 100 Mbps
ans: B [suy luận]

Câu 20: Phát biểu nào sau đây là đúng về các chương trình trên tầng ứng dụng? (Chọn 2 đáp án)
A. Sử dụng socket để truyền dữ liệu
B. Chỉ cần triển khai trên hệ thống đầu cuối
C. Phải cài đặt các cơ chế để đảm bảo truyền thông tin cậy
D. Chọn đường đi tốt nhất để truyền dữ liệu
ans: A,B [suy luận]
```

----- Page 86 -----
```md
Câu 21: Hãy lựa chọn thứ tự của từng tầng trong mô hình OSI khi liệt kê theo thứ tự từ dưới lên (Đáp án lựa chọn là 1-7 cho mỗi tầng, các tầng sẽ được sắp xếp không theo thứ tự)

Tầng ứng dụng (Application Layer)
A. 1
B. 2
C. 3
D. 4
E. 5
F. 6
G. 7
ans: G [suy luận]

Tầng trình diễn (Presentation Layer)
A. 1
B. 2
C. 3
D. 4
E. 5
F. 6
G. 7
ans: F [suy luận]

Tầng liên kết dữ liệu (Data-link Layer)
A. 1
B. 2
C. 3
D. 4
E. 5
F. 6
G. 7
ans: B [suy luận]

Tầng vật lý (Physical Layer)
A. 1
B. 2
C. 3
D. 4
E. 5
F. 6
G. 7
ans: A [suy luận]

Tầng phiên (Session Layer)
A. 1
B. 2
C. 3
D. 4
E. 5
F. 6
G. 7
ans: E [suy luận]

Tầng giao vận (Transport Layer)
A. 1
B. 2
C. 3
D. 4
E. 5
F. 6
G. 7
ans: D [suy luận]

Tầng liên mạng (Internetwork Layer)
A. 1
B. 2
C. 3
D. 4
E. 5
F. 6
G. 7
ans: C [suy luận]
```

----- Page 87 -----
```md
Câu 22: Quá trình định tuyến được thực hiện để làm gì?
A. Tìm đường đi giữa 2 switch
B. Tìm đường đi tới router mặc định
C. Tìm đường đi giữa 2 máy tính trong cùng mạng
D. Tìm đường đi giữa 2 router
ans: D [suy luận]

Câu 23: Một gói tin IP với kích thước payload là 5354 byte đi vào mạng có MTU = 1224 byte, biết tiêu đề IP có kích thước 20 byte, hỏi lượng dữ liệu ở mảnh IP cuối là bao nhiêu? (Nhập số nguyên, không nhập đơn vị, ví dụ: 52) **(Câu điền — chỉ ghi số)**
A. 554
ans: A [suy luận]
```

----- Page 88 -----
```md
Câu 24: Trong hoạt động của giao thức UDP, bên nhận thực hiện những hoạt động nào? (Chọn 2 đáp án)
A. Kiểm tra lỗi trên gói tin
B. Chuyển dữ liệu tới đúng ứng dụng
C. Đưa các gói tin không đúng thứ tự vào bộ đệm
D. Gửi báo nhận
ans: A,B [suy luận]

Câu 25: Thông điệp DHCP nào được client gửi đi khi vừa kết nối vào mạng và xin cấp phát địa chỉ IP mới?
A. DHCP Discover
B. DHCP Offer
C. DHCP Request
D. DHCP ACK
ans: A [suy luận]
```

----- Page 89 -----
```md
Câu 26: Các phương pháp mã hoá như Manchester, NRZ-L, AMI Bipolar được sử dụng để làm gì?
A. Kiểm soát luồng
B. Kiểm soát lỗi của khi truyền dữ liệu trên đường truyền
C. Biểu diễn dữ liệu thành tín hiệu
D. Bảo mật cho dữ liệu
ans: C [suy luận]

Câu 27: Các gói tin TCP nào sau đây được sử dụng để đóng liên kết? (Chọn 2 đáp án)
A. SYN
B. ACK
C. FIN
D. SYN/ACK
ans: B,C [suy luận]
```

----- Page 90 -----
```md
Câu 28: Ánh xạ các mô tả vào các kỹ thuật tương ứng

Phía gửi được phép gửi nhiều gói tin mà không cần chờ báo nhận
A. Cửa sổ trượt - Sliding windows
B. Loại bỏ chọn lọc - Selective Reject
C. Dừng và chờ - Stop-and-wait
D. Go back N
ans: A [suy luận]

Phía gửi chỉ được phép gửi một gói tin và phải chờ báo nhận
A. Cửa sổ trượt - Sliding windows
B. Loại bỏ chọn lọc - Selective Reject
C. Dừng và chờ - Stop-and-wait
D. Go back N
ans: C [suy luận]

Phía gửi phải gửi lại đúng gói tin bị lỗi
A. Cửa sổ trượt - Sliding windows
B. Loại bỏ chọn lọc - Selective Reject
C. Dừng và chờ - Stop-and-wait
D. Go back N
ans: B [suy luận]

Phía gửi phải gửi lại một số gói tin gồm cả gói tin không bị lỗi
A. Cửa sổ trượt - Sliding windows
B. Loại bỏ chọn lọc - Selective Reject
C. Dừng và chờ - Stop-and-wait
D. Go back N
ans: D [suy luận]
```

----- Page 91 -----
```md
Câu 29: Đặc điểm của phương pháp CSMA là gì? (Chọn 2 đáp án)
A. Các nút sử dụng đường truyền một cách ngẫu nhiên
B. Lắng nghe tín hiệu sóng mang (carrier) trên đường truyền trước khi gửi
C. Các nút sử dụng đường truyền đồng thời, mỗi nút mạng sử dụng một mã để truyền tin
D. Không có đáp án đúng
ans: A,B [suy luận]

Câu 30: Đâu là ưu điểm của phương pháp chuyển mạch kênh khi so sánh với chuyển mạch gói? (Chọn 2 đáp án)
A. Cung cấp chất lượng dịch vụ tốt hơn
B. Hầu như không có trễ trung gian sau khi kênh truyền được thiết lập
C. Hiệu quả sử dụng kênh truyền tốt hơn
D. Giảm chi phí vận hành một hệ thống mạng
ans: A,B [suy luận]
```

----- Page 92 -----
```md
Câu 31: Khi không tìm thấy tài nguyên được yêu cầu, máy chủ Web gửi thông điệp HTTP Response với mã trả lời là bao nhiêu? **(Câu điền — chỉ ghi số)**
A. 404
ans: A [suy luận]

Câu 32: Trong kỹ thuật Cửa sổ trượt (Sliding windows), phía gửi được phép truyền lượng dữ liệu tối đa là bao nhiêu?
A. Bằng kích thước vùng đệm của bên nhận
B. Bằng kích thước vùng đệm còn trống của bên nhận
C. Bằng kích thước cửa sổ phát của bên gửi
D. Một gói tin
ans: C [suy luận]
```

----- Page 93 -----
```md
Câu 33: Mã Checksum được sử dụng để làm gì?
A. Báo hiệu cho bên gửi dữ liệu rằng dữ liệu có lỗi.
B. Phát hiện lỗi phát sinh do quá trình truyền dữ liệu.
C. Bảo mật cho dữ liệu.
D. Sửa lỗi phát sinh do quá trình truyền dữ liệu.
ans: B [suy luận]

Câu 34: Dữ liệu của một gói tin gửi đi là 111000011101 (dạng nhị phân). Hệ thống sử dụng mã checksum 4-bit để kiểm tra lỗi. Hãy cho biết mã checksum cần được đính kèm với dữ liệu (Chỉ ghi mã checksum dưới dạng nhị phân, không thêm bất cứ kí tự nào) **(Câu điền — chỉ ghi mã nhị phân)**
A. 0010
ans: A [suy luận]
```

----- Page 94 -----
```md
Câu 35: Cho mạng có địa chỉ 222.17.188.0/25, hỏi địa chỉ quảng bá của mạng đó là địa chỉ nào? (Nhập địa chỉ IP dạng thập phân, ví dụ: 192.168.1.0) **(Câu điền — địa chỉ IP)**
A. 222.17.188.127
ans: A [suy luận]

Câu 36: Mạng đang sử dụng địa chỉ 172.31.0.0/16 có thể có bao nhiêu mạng con nếu dùng mặt nạ mạng 255.255.128.0? (Nhập số mạng con, ví dụ: 2) **(Câu điền — chỉ ghi số)**
A. 2
ans: A [suy luận]
```

----- Page 95 -----
```md
Câu 37: Trong kiến trúc phân tầng, tại bên nhận, hoạt động nào sau đây có thể được thực hiện trong xử lý ở mỗi tầng?
A. Thêm tiêu đề mới và chuyển xuống tầng dưới
B. Thay thế tiêu đề của gói tin bằng tiêu đề mới và chuyển lên tầng trên
C. Bóc tách tiêu đề và chuyển phần thân của gói tin lên tầng trên
D. Phân nhỏ gói tin
ans: C [suy luận]

Câu 38: Làm thế nào để kiểm tra xem địa chỉ IP của gói tin có nằm trong một mạng cục bộ không?
A. Gửi bản tin RARP với địa chỉ IP của gói tin
B. Không có cách nào đúng
C. Gửi gói tin đến Default Gateway
D. Kiểm tra địa chỉ IP và mặt nạ mạng
ans: D [suy luận]
```

----- Page 96 -----
```md
Câu 39: Có 6 mạng đang kết nối với nhau sử dụng 5 router, hỏi có bao nhiêu bảng định tuyến được sử dụng?
A. 11
B. 5
C. 1
D. 6
ans: B [suy luận]

Câu 40: Phát biểu nào sau đây là đúng về giao thức định tuyến (routing protocol) dạng link-state? (Chọn 2 đáp án)
A. Các router trao đổi với nhau thông tin khoảng cách đường đi
B. Các router trao đổi với nhau thông tin về các liên kết (links)
C. Mỗi router có thể nhận thông tin từ tất cả các router khác
D. Các router hợp tác với nhau để tính toán đường đi
ans: B,D [suy luận]
```

----- Page 97 -----
```md
Câu 41: Trường nào trong tiêu đề của gói tin IP được dùng để xác định loại dữ liệu (payload) mà gói tin IP đang vận chuyển?
A. Checksum
B. Type of service
C. Protocol
D. Identification
ans: C [suy luận]

Câu 42: Để có thể yêu cầu phía gửi phát lại dữ liệu khi có lỗi, kỹ thuật nào sau đây có thể được áp dụng? (Chọn 2 đáp án)
A. Dừng và chờ (Stop-and-wait)
B. Go back N
C. Checksum
D. Slowstart
ans: A,B [suy luận]
```

----- Page 98 -----
```md
Câu 43: Tầng vật lý thực hiện các chức năng nào sau đây?
A. Đóng gói dữ liệu thành các gói tin
B. Kiểm tra dữ liệu nhận được có bị lỗi không
C. Đánh số các gói dữ liệu gửi đi
D. Biểu diễn các bit thành tín hiệu và ngược lại
ans: D [suy luận]

Câu 44: Trong hoạt động của giao thức TCP, bên gửi thực hiện hoạt động nào? (Chọn 3 đáp án)
A. Yêu cầu thiết lập liên kết trước khi gửi
B. Chờ báo nhận
C. Phát lại dữ liệu khi có lỗi
D. Gửi dữ liệu với tốc độ nhanh nhất
ans: A,B,C [suy luận]
```

----- Page 99 -----
```md
Câu 45: Dịch vụ phân giải tên miền đăng ký sử dụng số hiệu cổng dịch vụ là bao nhiêu? **(Câu điền — chỉ ghi số)**
A. 53
ans: A [suy luận]

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
ans: B [suy luận]

Câu 48: Những thay đổi của giao thức HTTP 1.1 so với HTTP 1.0 là gì? (Chọn 3 đáp án)
A. Chỉ thiết lập 1 liên kết TCP để truyền nhiều thông điệp khác nhau
B. Có cơ chế pipeline để tăng tốc độ truyền tin
C. Bổ sung thêm các phương thức yêu cầu mới cho thông điệp HTTP Request
D. Sử dụng các cơ chế truyền thông tin cậy để luôn đảm bảo truyền thành công
ans: A,B,C [suy luận]
```

----- Page 101 -----
```md
Câu 49: Trường nào trong tiêu đề của gói tin IP được dùng để xác định loại dữ liệu (payload) mà gói tin IP đang vận chuyển?
A. Checksum
B. Type of service
C. Protocol
D. Identification
ans: C [suy luận]

Câu 50: Để có thể yêu cầu phía gửi phát lại dữ liệu khi có lỗi, kỹ thuật nào sau đây có thể được áp dụng? (Chọn 2 đáp án)
A. Dừng và chờ (Stop-and-wait)
B. Go back N
C. Checksum
D. Slowstart
ans: A,B [suy luận]
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
A. Điều khiển nút gửi không truyền với tốc độ quá nhanh, làm quá tải nút nhận
B. Điều khiển việc sử dụng đường truyền chung khi có nhiều nút cùng muốn truyền tin.
C. Điều khiển truyền dữ liệu giữa các nút mạng nối với nhau bằng switch
D. Điều khiển hai nút truyền theo thứ tự của giao thức mạng
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
Câu 54: Trong kiến trúc phân tầng, hoạt động nào sau đây có thể được thực hiện trong quá trình xử lý dữ liệu? (Chọn 2 đáp án)
A. Bóc tách tiêu đề và chuyển phần thân của gói tin lên tầng trên
B. Thay thế tiêu đề của gói tin bằng tiêu đề mới và chuyển lên tầng trên
C. Đóng gói dữ liệu và thêm header mới cho mỗi tầng dưới
D. Giải mã dữ liệu và chuyển phần thân lên tầng trên
ans: A,C [suy luận]

Câu 55: Điểm khác biệt khi triển khai dịch vụ theo mô hình P2P so với mô hình Client-Server là gì? (Chọn 3 đáp án)
A. Không cần tất cả các nút mạng thành phần phải duy trì kết nối liên tục
B. Không cần quản lý tài nguyên tập trung
C. Các nút mạng có thể vừa gửi yêu cầu dịch vụ, vừa cung cấp dịch vụ cho các nút khác
D. Có điểm thắt nút cổ chai
ans: A,B,C

Câu 56: Mã Checksum được sử dụng để làm gì?
A. Phát hiện lỗi phát sinh do quá trình truyền dữ liệu.
B. Bảo mật cho dữ liệu.
C. Sửa lỗi phát sinh do quá trình truyền dữ liệu.
D. Báo hiệu cho bên gửi dữ liệu rằng dữ liệu có lỗi.
ans: A

Câu 57: Đâu là đặc điểm của mạng sử dụng kỹ thuật chuyển mạch kênh (Chọn 3 đáp án)
A. Thiết lập kênh trước khi truyền
B. Gói tin được truyền đi ngay
C. Các gói tin có thể tới đích không đúng thứ tự
D. Các gói tin trong mỗi kênh truyền giữa 2 nút luôn đi theo tuyến đường giống nhau
E. Tài nguyên được cấp phát để dùng riêng trên mỗi kênh truyền giữa 2 nút
ans: A,D,E
```

----- Page 104 -----
```md
Câu 58: Phát biểu nào sau đây là SAI về số hiệu cổng ứng dụng?
A. Là một số nguyên 16 bit
B. Được sử dụng để xác định đường đi khi chuyển tiếp gói tin
C. Các chương trình ứng dụng trên một nút mạng phải đăng ký số hiệu cổng ứng dụng khác nhau
D. Được sử dụng trong quá trình truyền tin giữa các ứng dụng tại tầng giao vận
ans: B

Câu 59: Đặc điểm của phương pháp CSMA là gì? (Chọn 2 đáp án)
A. Các nút sử dụng đường truyền một cách ngẫu nhiên
B. Lắng nghe tín hiệu sóng mang (carrier) trên đường truyền trước khi gửi
C. Các nút sử dụng đường truyền đồng thời, mỗi nút mạng sử dụng một mã để truyền tin
D. Không có đáp án đúng
ans: A,B

Câu 60: Trong hoạt động của giao thức TCP, bên gửi thực hiện hoạt động nào? (Chọn 3 đáp án)
A. Yêu cầu thiết lập liên kết trước khi gửi
B. Chờ báo nhận
C. Phát lại dữ liệu khi có lỗi
D. Gửi dữ liệu với tốc độ nhanh nhất
ans: A,B,C

Câu 61: Trong hoạt động của giao thức UDP, bên nhận thực hiện những hoạt động nào? (Chọn 2 đáp án)
A. Kiểm tra lỗi trên gói tin
B. Chuyển dữ liệu tới đúng ứng dụng
C. Đưa các gói tin không đúng thứ tự vào bộ đệm
D. Gửi báo nhận
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

Câu 63: Trong kỹ thuật Cửa sổ trượt (Sliding windows), phía gửi được phép truyền lượng dữ liệu tối đa là bao nhiêu?
A. Bằng kích thước vùng đệm còn trống của bên nhận
B. Bằng kích thước vùng đệm của bên nhận
C. Một gói tin
D. Bằng kích thước cửa sổ phát của bên gửi
ans: A

Câu 64: Trường nào trong tiêu đề của gói tin IP được dùng để xác định loại dữ liệu (payload) mà gói tin IP đang vận chuyển?
A. Type of service
B. Checksum
C. Identification
D. Protocol
ans: A

Câu 65: Các yếu tố nào sau đây ảnh hưởng đến trễ khứ hồi (Round-Trip Time) trong mạng?
A. Tốc độ xử lý của các thiết bị mạng
B. Tất cả các yếu tố đã được đề cập
ans: B [suy luận]
```

----- Page 106 -----
```md
Câu 66: Thông điệp DHCP nào được client gửi đi khi vừa kết nối vào mạng và xin cấp phát địa chỉ IP mới?
A. DHCP Request
B. DHCP ACK
C. DHCP Discover
D. DHCP Offer
ans: C

Câu 67: Cho một đường truyền có thể phát được 2²⁰ xung/s (pulse/s), khi áp dụng phương pháp mã hoá NRZ-L, tốc độ dữ liệu sinh ra là bao nhiêu.
A. 10 Mbps
B. 1 Mbps
C. 0.5 Mbps
D. 100 Mbps
ans: B

Câu 68: Dữ liệu của một gói tin gửi đi là 100001000110 (dạng nhị phân). Hệ thống sử dụng mã checksum 4-bit để kiểm tra lỗi. Hãy cho biết mã checksum cần được đính kèm với dữ liệu (Chỉ ghi mã checksum dưới dạng nhị phân, không thêm bất cứ kí tự nào) **(Câu điền — mã nhị phân)**
A. 1100
ans: A

Câu 69: Cơ chế tự học của switch được dùng để làm gì?
A. Giúp chuyển tiếp dữ liệu trong một mạng LAN có topo dạng trục
B. Giúp chuyển tiếp dữ liệu trong một mạng LAN không dây
C. Giúp chuyển tiếp dữ liệu trong một mạng LAN có topo dạng điểm-điểm
D. Giúp chuyển tiếp dữ liệu giữa các mạng
ans: C [suy luận]
```

----- Page 107 -----
```md
Câu 70: Cho một đường truyền từ A đến B đi qua 3 đoạn kết nối khác nhau có băng thông lần lượt là 5 Mbps, 10 Mbps và 15 Mbps. Giả sử các đường kết nối này chỉ phục vụ cho việc truyền dữ liệu từ A đến B, trễ trên thiết bị không đáng kể, và tỷ lệ lỗi và mất gói tin bằng 0. Hỏi thông lượng trung bình từ A đến B là bao nhiêu?
A. 15 Mbps
B. Không thể xác định được
C. 10 Mbps
D. 5 Mbps
ans: D

Câu 71: Cho mạng có địa chỉ 199.163.32.0/27, hỏi địa chỉ quảng bá của mạng đó là địa chỉ nào? (Nhập địa chỉ IP dạng thập phân, ví dụ: 192.168.1.0) **(Câu điền — địa chỉ IP)**
A. 199.163.32.31
ans: A

Câu 72: Tầng vật lý thực hiện các chức năng nào sau đây?
A. Đánh số các gói dữ liệu gửi đi
B. Kiểm tra dữ liệu nhận được có bị lỗi không
C. Đóng gói dữ liệu thành các gói tin
D. Biểu diễn các bit thành tín hiệu và ngược lại
ans: D
```

----- Page 108 -----
```md
Câu 73: Bảng MAC/CAM của một switch có nội dung như sau. Switch thực hiện các xử lý nào khi trên cổng e2 nhận được một khung tin có địa chỉ nguồn là 55-55-55-ee-ee-ee và địa chỉ đích là 11-11-11-aa-aa-aa. (Chọn 2 đáp án)

| Địa chỉ MAC | Cổng |
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

Câu 74: Hai tiến trình thực hiện truyền tin theo giao thức TCP. Tiến trình gửi đang sử dụng cửa sổ kiểm soát tắc nghẽn (congestion window) là 14.000 byte và ngưỡng kiểm soát tắc nghẽn (ssthreshold) là 11.200 byte. Tiến trình gửi nhận được gói tin ACK báo thành công cho các gói tin đã gửi, trong đó giá trị Receive Window là 65.535. Giả sử các bên đã thỏa thuận 1 MSS = 1.400 byte. Trong lượt tiếp theo, tiến trình gửi có thể gửi tối đa bao nhiêu byte? (Chỉ ghi đáp án số, không kèm đơn vị) **(Câu điền — chỉ ghi số)**
A. 15400
ans: A

Câu 75: Đâu là ưu điểm của phương pháp chuyển mạch kênh khi so sánh với chuyển mạch gói? (Chọn 2 đáp án)
A. Cung cấp chất lượng dịch vụ tốt hơn
B. Hầu như không có trễ trung gian sau khi kênh truyền được thiết lập
C. Hiệu quả sử dụng kênh truyền tốt hơn
D. Giảm chi phí vận hành một hệ thống mạng
ans: A,B
```

----- Page 109 -----
```md
Câu 76: Khi truyển dữ liệu từ máy A đến máy B, giả thiết gói tin đi qua 13 router trong mạng, số các mạng gói tin đi qua là bao nhiêu?
A. 1
B. 24
C. 13
D. 28
ans: D [suy luận]

Câu 77: Để có thể yêu cầu phía gửi phát lại dữ liệu khi có lỗi, kỹ thuật nào sau đây có thể được áp dụng? (Chọn 2 đáp án)
A. Dừng và chờ (Stop-and-wait)
B. Go back N
C. Checksum
D. Slowstart
ans: A,B

Câu 78: Ánh xạ các phương pháp sau về các loại tương ứng.

TDMA
A. Phương pháp đa truy nhập phân chia theo thời gian
B. Phương pháp đa truy nhập phân chia theo tần số
C. Phương pháp đa truy nhập cảm nhận sóng mang
D. Phương pháp đa truy nhập dùng token
ans: A

FDMA
A. Phương pháp đa truy nhập phân chia theo thời gian
B. Phương pháp đa truy nhập phân chia theo tần số
C. Phương pháp đa truy nhập cảm nhận sóng mang
D. Phương pháp đa truy nhập dùng token
ans: B

CSMA
A. Phương pháp đa truy nhập phân chia theo thời gian
B. Phương pháp đa truy nhập phân chia theo tần số
C. Phương pháp đa truy nhập cảm nhận sóng mang
D. Phương pháp đa truy nhập dùng token
ans: C

Token Ring
A. Phương pháp đa truy nhập phân chia theo thời gian
B. Phương pháp đa truy nhập phân chia theo tần số
C. Phương pháp đa truy nhập cảm nhận sóng mang
D. Phương pháp đa truy nhập dùng token
ans: D

Câu 79: Mạng đang sử dụng địa chỉ 172.20.0.0/16 có thể có bao nhiêu mạng con nếu dùng mặt nạ mạng 255.255.255.128? (Nhập số mạng con, ví dụ: 2) **(Câu điền — chỉ ghi số)**
A. 512
ans: A
```

----- Page 110 -----
```md
Câu 81: Ánh xạ các mô tả vào các kỹ thuật tương ứng — Phía gửi được phép gửi nhiều gói tin mà không cần chờ báo nhận
A. Cửa sổ trượt - Sliding windows
B. Loại bỏ chọn lọc - Selective Reject
C. Dừng và chờ - Stop-and-wait
D. Go back N
ans: A [suy luận]

Câu 82: Ánh xạ các mô tả vào các kỹ thuật tương ứng — Phía gửi chỉ được phép gửi một gói tin và phải chờ báo nhận
A. Cửa sổ trượt - Sliding windows
B. Loại bỏ chọn lọc - Selective Reject
C. Dừng và chờ - Stop-and-wait
D. Go back N
ans: C [suy luận]

Câu 83: Ánh xạ các mô tả vào các kỹ thuật tương ứng — Phía gửi phải gửi lại đúng gói tin bị lỗi
A. Cửa sổ trượt - Sliding windows
B. Loại bỏ chọn lọc - Selective Reject
C. Dừng và chờ - Stop-and-wait
D. Go back N
ans: B [suy luận]

Câu 84: Ánh xạ các mô tả vào các kỹ thuật tương ứng — Phía gửi phải gửi lại một số gói tin gồm cả gói tin không bị lỗi
A. Cửa sổ trượt - Sliding windows
B. Loại bỏ chọn lọc - Selective Reject
C. Dừng và chờ - Stop-and-wait
D. Go back N
ans: D [suy luận]

Câu 85: Quá trình định tuyến được thực hiện để làm gì?
A. Tìm đường đi giữa 2 switch
B. Tìm đường đi giữa 2 router
C. Tìm đường đi tới router mặc định
D. Tìm đường đi giữa 2 máy tính trong cùng mạng
ans: B

Câu 86: Phát biểu nào sau đây là đúng về giao thức định tuyến (routing protocol) dạng link-state? (Chọn 2 đáp án)
A. Các router trao đổi với nhau thông tin khoảng cách đường đi
B. Các router trao đổi với nhau thông tin về các liên kết (links)
C. Mỗi router có thể nhận thông tin từ tất cả các router khác
D. Các router hợp tác với nhau để tính toán đường đi
ans: B,D [suy luận]
```

----- Page 111 -----
```md
Câu 87: Một gói tin IP với kích thước payload là 5246 byte đi vào mạng có MTU = 1192 byte, biết tiêu đề IP có kích thước 20 byte, hỏi lượng dữ liệu ở mảnh IP cuối là bao nhiêu? (Nhập số nguyên, không nhập đơn vị, ví dụ: 52) **(Câu điền — chỉ ghi số)**
A. 558
ans: A

Câu 88: Các phương pháp mã hoá như Manchester, NRZ-L, AMI Bipolar được sử dụng để làm gì?
A. Bảo mật cho dữ liệu
B. Biểu diễn dữ liệu thành tín hiệu
C. Kiểm soát luồng
D. Kiểm soát lỗi khi truyền dữ liệu trên đường truyền
ans: B

Câu 89: Các gói tin TCP nào sau đây được sử dụng để đóng liên kết? (Chọn 2 đáp án)
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
Câu 91: Giao thức nào sau đây nằm ở tầng giao vận? (Chọn 2 đáp án)
A. IP
B. TCP
C. UDP
D. HTTP
ans: B,C

Câu 92: Khi không tìm thấy tài nguyên được yêu cầu, máy chủ Web gửi thông điệp HTTP Response với mã trả lời là bao nhiêu? **(Câu điền — chỉ ghi số)**
A. 404
ans: A

Câu 93: Phát biểu nào sau đây là đúng về máy chủ tên miền gốc (root server) trong hệ thống DNS? (Chọn 2 đáp án)
A. Quản lý thông tin các máy chủ tên miền cấp 1 (TLD Server)
B. Lưu trữ thông tin của toàn bộ tên miền trên Internet
C. Không trả lời các thông điệp DNS Query truy vấn tên miền
D. Triển khai ở nhiều vị trí khác nhau trên Internet
ans: A,C

Câu 94: Dịch vụ phân giải tên miền đăng ký sử dụng số hiệu cổng dịch vụ là bao nhiêu? **(Câu điền — chỉ ghi số)**
A. 53
ans: A
```

----- Page 113 -----
```md
Câu 95: Phát biểu nào sau đây là đúng về các chương trình trên tầng ứng dụng? (Chọn 2 đáp án)
A. Sử dụng socket để truyền dữ liệu
B. Chỉ cần triển khai trên hệ thống đầu cuối
C. Phải cài đặt các cơ chế để đảm bảo truyền thông tin cậy
D. Chọn đường đi tốt nhất để truyền dữ liệu
ans: A,B

Câu 96: Làm thế nào để kiểm tra xem địa chỉ IP của gói tin có nằm trong một mạng cục bộ không?
A. Gửi gói tin đến Default Gateway
B. Kiểm tra địa chỉ IP và mặt nạ mạng
C. Gửi bản tin RARP với địa chỉ IP của gói tin
D. Không có cách nào đúng
ans: B

Câu 97: Những thay đổi của giao thức HTTP 1.1 so với HTTP 1.0 là gì? (Chọn 3 đáp án)
A. Chỉ thiết lập 1 liên kết TCP để truyền nhiều thông điệp khác nhau
B. Có cơ chế pipeline để tăng tốc độ truyền tin
C. Bổ sung thêm các phương thức yêu cầu mới cho thông điệp HTTP Request
D. Sử dụng các cơ chế truyền thông tin cậy để luôn đảm bảo truyền thành công
ans: A,C,D
```

----- Page 114 -----
```md
Câu 98: Sắp xếp số thứ tự (1–7, từ dưới lên trên) cho các tầng sau: **(Câu điền — 7 giá trị)**
A. Tầng ứng dụng=7; Tầng trình diễn=6; Tầng liên kết dữ liệu=2; Tầng vật lý=1; Tầng phiên=5; Tầng giao vận=4; Tầng liên mạng=3
ans: A
```
