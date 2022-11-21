#!/usr/bin/env python
# coding: utf-8

# In[10]:


pip install --upgrade pip setuptools==57.5.0 


# In[13]:


pip install pybluez2


# In[14]:


1import bluetooth


# In[21]:


print("performing inquiry...")

nearby_devices = bluetooth.discover_devices(duration=8, lookup_names=True, flush_cache=True, lookup_class=False)

print("found %d devices" % len(nearby_devices))

for addr, name in nearby_devices:
    try:
        print("  %s - %s" % (addr, name))
    except UnicodeEncodeError:
        print("  %s - %s" % (addr, name.encode('utf-8', 'replace')))
        
        
    if name=="ABINGO BT10":
        
        print("Hello World!")


# In[ ]:




