#!/usr/bin/env python
# coding: utf-8

# In[17]:


pip install pybluez2


# In[18]:


import bluetooth


# In[45]:


pip install csvfile


# In[46]:


import csvfile


# In[19]:


import webbrowser


# # Searching for Bluetooth devices on finding any device, write the MAC addresses and devices names in a text file & Loading different content based on the location/context of each device.

# In[67]:


print("performing inquiry...")

nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, lookup_class=False)

print("found %d devices" % len(nearby_devices))

for addr, name in nearby_devices:
    try:
        
        with open("MAC address devices2.txt",'a')as file:
            file.write("  %s - %s" % (addr, name))
            file.close
    
        
        
        
    except UnicodeEncodeError:
        print("  %s - %s" % (addr, name.encode('utf-8', 'replace')))
      
        
    if addr=="00:11:67:11:18:D1":
        #webbrowser.open("https://www.youtube.com/watch?v=hTobZFggexE")
        print(name)
        
        
    if addr=="F0:5A:09:09:F5:4D":
        #webbrowser.open("https://www.youtube.com/watch?v=EMQC0GaP3hU")
        print("Samsung")
        


# # Read the text file where detected bluetooth devices were written

# In[25]:


f = open("MAC address devices2.txt","r")
content = f.readlines()
print(content)


# # Another Way!!
# #Writing the detected Bluetooth devices first then reading the file and looping over it without using ready made library function handling the condition of detecting MAC address and loading different content on that basis.

# In[61]:


print("performing inquiry...")

nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, lookup_class=False)

print("found %d devices" % len(nearby_devices))

for addr, name in nearby_devices:
    try:
        
        with open("MAC address devices2.txt",'a')as file:
            file.write("%s,%s," % (addr, name))
            file.close
    
        
        
        
    except UnicodeEncodeError:
        print("%s,%s," % (addr, name.encode('utf-8', 'replace')))
      


# In[62]:


f = open("MAC address devices2.txt","r")
content = f.readlines()
print(content)


# In[66]:


for line in content :
    
    x = line.split(",")
    #print(x[0])
    if x[0]:
        webbrowser.open("https://www.youtube.com/watch?v=hTobZFggexE")
        #print(x[1])
        
    if x[2]:
        webbrowser.open("https://www.youtube.com/watch?v=EMQC0GaP3hU")
        #print(x[3])
        
        


# In[ ]:




