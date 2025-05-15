# UPNPDevice

**Inherits:** RefCounted < Object

Universal Plug and Play (UPnP) device. See UPNP for UPnP discovery and utility functions. Provides low-level access to UPNP control commands. Allows managing port mappings (port forwarding) and querying network information (local/external IP address, status). Methods are synchronous and block the calling thread.

---

## Properties

- **description_url**: String = ""  
  URL to the device description.

- **igd_control_url**: String = ""  
  IGD control URL.

- **igd_our_addr**: String = ""  
  Address of the local machine in the network connecting it to this UPNPDevice.

- **igd_service_type**: String = ""  
  IGD service type.

- **igd_status**: IGDStatus = 9  
  IGD status. See IGDStatus enum.

- **service_type**: String = ""  
  Service type.

---

## Methods

- **add_port_mapping**(port: int, port_internal: int = 0, desc: String = "", proto: String = "UDP", duration: int = 0) → int  
  Adds a port mapping to forward the given external port on this UPNPDevice for the given protocol to the local machine. See UPNP.add_port_mapping().

- **delete_port_mapping**(port: int, proto: String = "UDP") → int  
  Deletes the port mapping identified by the given port and protocol combination on this device. See UPNP.delete_port_mapping().

- **is_valid_gateway**() → bool  
  Returns true if this is a valid IGD (InternetGatewayDevice) which potentially supports port forwarding.

- **query_external_address**() → String  
  Returns the external IP address of this UPNPDevice or an empty string.

---

## IGDStatus Enum

- **IGDStatus.9**: 9  
  IGD status. See IGDStatus enum.

- **IGDStatus.0**: 0  
  IGD status. See IGDStatus enum.

- **IGDStatus.1**: 1  
  IGD status. See IGDStatus enum.

- **IGDStatus.2**: 2  
  IGD status. See IGDStatus enum.

- **IGDStatus.3**: 3  
  IGD status. See IGDStatus enum.

- **IGDStatus.4**: 4  
  IGD status. See IGDStatus enum.

- **IGDStatus.5**: 5  
  IGD status. See IGDStatus enum.

- **IGDStatus.6**: 6  
  IGD status. See IGDStatus enum.

- **IGDStatus.7**: 7  
  IGD status. See IGDStatus enum.

- **IGDStatus.8**: 8  
  IGD status. See IGDStatus enum.