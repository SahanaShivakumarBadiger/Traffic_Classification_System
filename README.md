# SDN Traffic Classification System using POX & Mininet

## 📌 Problem Statement

Design and implement an SDN-based traffic classification system that identifies and categorizes network traffic into TCP, UDP, and ICMP using a controller-based approach.

---

## 🎯 Objectives

* Classify packets into TCP, UDP, and ICMP
* Maintain real-time statistics
* Display classification results
* Analyze traffic distribution

---

## 🛠️ Tools & Technologies

* Mininet (network simulation)
* POX Controller (SDN control logic)
* OpenFlow 1.0
* iperf (traffic generation)
* ping (ICMP testing)

---

## 🏗️ Network Topology

Single switch topology with 2 hosts:

h1 ---- s1 ---- h2

---

## ⚙️ Setup & Execution

### Step 1: Start Controller
In 1st Terminal
```
cd ~/pox
```
```
./pox.py openflow.of_01 ext.traffic_classifier
```

---

### Step 2: Start Mininet
In 2nd Terminal
```
sudo mn --topo single,2 --controller=remote,ip=127.0.0.1 --switch ovsk,protocols=OpenFlow10
```
---

## 🧪 Test Scenarios
2nd Terminal
### 1. ICMP Traffic
```
h1 ping -c 5 h2
```
### 2. TCP Traffic
```
h2 iperf -s &
```
```
h1 iperf -c h2
```
### 3. UDP Traffic
```
h2 iperf -s -u &
```
```
h1 iperf -c h2 -u
```
---

## 📊 Sample Output
In 1st Terminal

TCP Packet

UDP Packet

ICMP Packet

Stats → TCP: 45158, UDP: 898, ICMP: 10

---

## 📈 Traffic Analysis

* TCP dominates due to continuous data transfer using iperf
* UDP shows moderate traffic
* ICMP is minimal (only ping packets)

---


---

## ✅ Features Implemented

* Packet classification (TCP, UDP, ICMP)
* Real-time statistics tracking
* Controller-based packet processing
* Dynamic traffic monitoring

---

## 📌 Conclusion

The system successfully demonstrates SDN-based traffic classification using controller logic. It highlights how SDN enables centralized monitoring and control of network traffic.

---
