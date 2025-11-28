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
Server is running on port 9000
```

---

## Running the Client

```bash
python tcp_client.py
```

Expected output:

```
Connected to Server!!
> 
```

Now you can type anything and send it to the server.

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

## 📚 Requirements

- Python 3.10+
- No external libraries required

---
