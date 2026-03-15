# 2. GeoLocator

### Overview
GeoLocator is a C# console application that retrieves geographic information about an IP address using an external API.

The program displays information such as country, city, coordinates, network provider, and a Google Maps location link.

### Features
IP address lookup  
Geographic information retrieval  
ASN and network provider identification  
Coordinates extraction  
Google Maps link generation  

### Technologies
C#  
.NET  
HTTP requests with HttpClient  
JSON parsing with Newtonsoft.Json  
IP geolocation API  

### How It Works
The program sends a request to the ipinfo API using the provided IP address. The response is returned as JSON and deserialized into a structured object. The data is then displayed in the console.

### Example Usage

```
Enter IP Address:
8.8.8.8
```

Output example:

```
Country: US
City: Mountain View
Coordinates: 37.3860,-122.0840
Postal Code: 94035
Region: California
ASN: AS15169 Google LLC
Google Maps: https://www.google.com/maps?q=37.3860,-122.0840
```

### Learning Goals
Working with REST APIs  
Handling JSON data in C#  
Asynchronous HTTP requests  

---
