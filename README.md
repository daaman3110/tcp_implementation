# AsyncIO TCP Server & Client (Python)

This project demonstrates a **minimal working TCP server and client** using Python’s `asyncio` module.  
It shows how asynchronous networking works in the simplest possible way.

---

## Features

### **TCP Server**
- Listens on `0.0.0.0:9000`
- Accepts a client connection
- Reads a message sent by the client
- Sends a reply back
- Closes the connection gracefully

### **TCP Client**
- Connects to the server
- Has two asynchronous tasks running:
  - **Listen Task:** continuously reads messages from the server  
  - **Send Task:** lets you type messages and send them to the server
- Uses `asyncio.gather()` for concurrency

---

## File Structure

```
├── tcp_server.py
└── tcp_client.py
```

---

## Running the Server

```bash
python tcp_server.py
```

You should see:

```
<img width="867" height="87" alt="image" src="https://github.com/user-attachments/assets/92447e9a-46b0-4688-a005-2de9c468ffcc" />
```

---

## Running the Client

```bash
python tcp_client.py
```

Expected output:

```
<img width="830" height="113" alt="image" src="https://github.com/user-attachments/assets/b877cd60-5275-46f4-bec8-491c34187342" />
```

Now you can type anything and send it to the server.

---

## Message Exchange between Server and Client
***Client***
<img width="825" height="133" alt="image" src="https://github.com/user-attachments/assets/d32a0528-5d60-4a5c-9766-df674a837021" />

***Server***
<img width="843" height="127" alt="image" src="https://github.com/user-attachments/assets/e9a19e27-f65a-4951-815c-07a4262e7bdc" />


---
## How It Works (Very Simple Explanation)

### **Server**
The server uses:

```python
await asyncio.start_server(handle_client, "0.0.0.0", 9000)
```

This creates a TCP server that:
- waits for clients  
- calls `handle_client` whenever someone connects  

Inside `handle_client`:
1. Read data from client  
2. Print it  
3. Reply  
4. Close connection  

---

### **Client**
The client opens a connection using:

```python
reader, writer = await asyncio.open_connection("127.0.0.1", 9000)
```

Then two tasks run at the same time:

#### 1: Listen Task
Reads all messages sent by the server.

#### 2️: Send Task
Takes user input and sends it to the server.

Both run together using:

```python
await asyncio.gather(listen(), send())
```

This makes it behave like a real chat application.

---

## Requirements

- Python 3.10+
- No external libraries required

---
