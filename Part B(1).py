#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install pybluez2


# In[2]:


import bluetooth


# In[3]:


import webbrowser


# In[8]:


with open("MAC address devices.txt",'r')as file:
    var=file.read()
    print(var)
    


# In[14]:


print("performing inquiry...")

nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, lookup_class=False)

print("found %d devices" % len(nearby_devices))

for addr, name in nearby_devices:
    try:
        
        with open("MAC address devices.txt",'a')as file:
            file.write("  %s - %s" % (addr, name))
            file.close
    
        
        
        
    except UnicodeEncodeError:
        print("  %s - %s" % (addr, name.encode('utf-8', 'replace')))
      
        
    if addr=="00:11:67:11:18:D1":
        webbrowser.open("https://www.youtube.com/watch?v=hTobZFggexE")
        #print("Abingo 10")
        
        
    if addr=="F0:5A:09:09:F5:4D":
        webbrowser.open("https://www.youtube.com/watch?v=EMQC0GaP3hU")
        #print("Samsung")
        


# In[ ]:




