# IP  
**Inherits:** Object  

## Description  
IP contains support functions for the Internet Protocol (IP). TCP/IP support is in different classes (see StreamPeerTCP and TCPServer). IP provides DNS hostname resolution support, both blocking and threaded.  

---

## Enumerations  

### ResolverStatus  
- **RESOLVER_STATUS_NONE** = 0  
  DNS hostname resolver status: No status.  
- **RESOLVER_STATUS_WAITING** = 1  
  DNS hostname resolver status: Waiting.  
- **RESOLVER_STATUS_DONE** = 2  
  DNS hostname resolver status: Done.  
- **RESOLVER_STATUS_ERROR** = 3  
  DNS hostname resolver status: Error.  

### Type  
- **TYPE_NONE** = 0  
  Address type: None.  
- **TYPE_IPV4** = 1  
  Address type: Internet protocol version 4 (IPv4).  
- **TYPE_IPV6** = 2  
  Address type: Internet protocol version 6 (IPv6).  
- **TYPE_ANY** = 3  
  Address type: Any.  

---

## Constants  
- **RESOLVER_MAX_QUERIES** = 256  
  Maximum number of concurrent DNS resolver queries allowed. Returns RESOLVER_INVALID_ID if exceeded.  
- **RESOLVER_INVALID_ID** = -1  
  Invalid ID constant. Returned if RESOLVER_MAX_QUERIES is exceeded.  

---

## Methods  

- **clear_cache(hostname: String = "")**  
  Removes all cached references for a hostname. If no hostname is provided, clears all cached data.  

- **get_resolve_item_address(id: int)**  
  Returns a queued hostname's IP address. Returns an empty string on error or if resolution hasn't completed.  

- **get_resolve_item_addresses(id: int)**  
  Returns resolved addresses as an array. Returns an empty array on error or if resolution hasn't completed.  

- **get_resolve_item_status(id: int)**  
  Returns a queued hostname's status as a ResolverStatus constant.  

- **resolve_hostname(host: String, ip_type: Type = 3)**  
  Returns a hostname's IPv4 or IPv6 address (blocking method). The address type depends on the ip_type parameter.  

- **resolve_hostname_addresses(host: String, ip_type: Type = 3)**  
  Resolves a hostname and returns addresses as an array of IPv4 or IPv6 addresses based on ip_type.  

- **resolve_hostname_queue_item(host: String, ip_type: Type = 3)**  
  Creates a queue item to resolve a hostname. Returns the queue ID if successful, or RESOLVER_INVALID_ID on error.  

---

## Key Functionality  
- **Blocking vs. Asynchronous Resolution:**  
  `resolve_hostname` and `resolve_hostname_addresses` perform blocking resolution.  
  `resolve_hostname_queue_item` allows non-blocking resolution via a queue.  

- **Caching:**  
  `clear_cache` manages cached data, which can improve performance for repeated DNS queries.  

- **Status Tracking:**  
  Use `get_resolve_item_status` to monitor the progress of queued resolution tasks.