# WebRTCMultiplayerPeer

**Inherits:** MultiplayerPeer < PacketPeer < RefCounted < Object

A class for creating a peer-to-peer mesh network using WebRTCPeerConnection compatible with MultiplayerAPI.

## Description

- Creates a full mesh of WebRTCPeerConnection (one connection per peer)
- Used as MultiplayerAPI.multiplayer_peer
- Peers must be added in STATE_NEW state
- Manages connections and disconnections
- Supports peer exchange and packet relaying when supported by MultiplayerAPI

**Android Note:** Enable INTERNET permission in export preset for network communication.

## Methods

- **add_peer(peer: WebRTCPeerConnection, peer_id: int, unreliable_lifetime: int = 1) → Error**
  - Adds a peer to the mesh
  - Requires peer in STATE_NEW state
  - Creates 3 channels: reliable, unreliable, ordered
  - unreliable_lifetime is passed to "maxPacketLifetime" option

- **create_client(peer_id: int, channels_config: Array = []) → Error**
  - Initializes as client
  - peer_id must be between 2-2147483647
  - Only call add_peer once with peer_id=1
  - Supports server relay if MultiplayerAPI supports it

- **create_mesh(peer_id: int, channels_config: Array = []) → Error**
  - Initializes as mesh network
  - peer_id must be between 1-2147483647

- **create_server(channels_config: Array = []) → Error**
  - Initializes as server with unique ID 1
  - Supports server relay if MultiplayerAPI supports it

- **get_peer(peer_id: int) → Dictionary**
  - Returns peer data: connection, channels, connected status

- **get_peers() → Dictionary**
  - Returns all peers as dictionary

- **has_peer(peer_id: int) → bool**
  - Returns true if peer exists in map

- **remove_peer(peer_id: int) → void**
  - Removes peer from mesh
  - Triggers peer_disconnected signal if connected

## Key Features

- Supports multiple transfer modes per channel
- Manages data channels for reliable/unreliable communication
- Handles peer connections and disconnections
- Works with MultiplayerAPI for peer exchange
- Android requires INTERNET permission for network functionality