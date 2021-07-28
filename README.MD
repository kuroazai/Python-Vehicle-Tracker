#Tracker Device Service

## Usage 

Tracker GET responses will be formatted within json  

```Json
{
    "Data":"[Device_id,Coordinates,Battery_Life,Motion]"
}
``` 

All required data that should be returned from our device will be given through this method. 
 
###Get Trackers on server(Admin)
**Definition**
`Get /Tracker/Locate_All/<Secret_Key>`

**Arguments**
- "Secret_Key":string` A unique key that only the Admins will have access to
 
**Responses**
- `200 OK` on success

```Json
[
    {
        "Device_ID":"xxxxxx"
        "GPS_Coords":"[x,y,z]"
        "Motion":"False"
        "Battery_Life":"1.0"
        "Mode":"Armed"
    }
    {
        "Device_ID":"xxxxxx"
        "GPS_Coords":"[x,y,z]"
        "Motion":"False"
        "Battery_Life":"1.0"
        "Mode":"Armed"
    }     
]
```
Returns all devices that on the server and their location

###Get Location of Tracker(User/Admin)

**Definition**
`Get /Tracker/Locate/<Device_ID>`

**Responses**
- `200 OK` on success
- `404 Not Found` If device ID doesn't exist

**Arguments**
- "Device_ID":string` automatically generated ID that uses trackers onboard information

```Json
{
    "Device_ID":"xxxxxx"
    "GPS_Coords":"[x,y,z]"
    "Motion":"False"
    "Battery_Life":"1.0"
    "Mode":"Armed"
}
```
### Update Live Location for all Devices (Admin)

**Definition**
`Post /Tracker/Update/<Secret_key>`

**Responses**
-`200 OK` on success
-`401 Unauthorized ` for unauthorized Access

**Arguments**
- "Secret_Key":string` A unique key that only the Admins will have access to
  
This call will get all the current coordinates of the devices on the server and update them onto a live map. 

###Register A new Tracker on server(Admin)

**Definition**
`Post /Tracker/Activate`

**Arguments**
- "Device_ID":string` automatically generated ID that uses trackers onboard information

This creates an object on the server and gives it a unique ID which is randomly generated

###Remove a Tracker from the server(Admin)

**Definition**
`Post /Tracker/Delete/<Device_ID>`

**Arguments**
- "Device_ID":string` automatically generated ID that uses trackers onboard information

This deletes a given device ID from the server and doesn't allow further information to be retrieved from it


