import os
from replit import db


admin_id = os.environ['admin_id']

active_channels = db["active_channels"]

def add_channel_to_db(id_canal):
  if("active_channels" in db.keys()):
    holder = db["active_channels"]
    for item in holder:
      if(item == id_canal):
        print("Este Canal ya estaba en la lista")
        return False

    holder.append(id_canal)
    db["active_channels"] = holder
    print("Se agrego el nuevo canal a la lista")
    #print("Canales:",holder)
  return True

def remove_channel_from_db(id_canal):
  if("active_channels" in db.keys()):
    holder = db["active_channels"]
    #print("Holder: ",holder)
# Si esta en la lista , lo quitamos
    if(id_canal in holder): 
      holder.remove(id_canal)
      print("Se removio ese canal de la lista de activos")
      return True
    else:
      print("Ese canal no esta en la lista")
      return False


def reset_active_channels(id_key):
  #print(type(id_key),type(admin_id))
  if(str(id_key) == admin_id):
    print("Admin detectado, limpiando lista")
    db["active_channels"] = []
    return True
  else:
    return False

def check_active_channels_list(id_key):
  if(str(id_key) == admin_id):
    show_list = []
    lista = db["active_channels"]
    print("Admin detectado, imprimiendo lista")
    for item in lista:
      show_list.append(item)
    return True,show_list
  else:
    return False,show_list

def check_if_channel_is_active(channel_id):
  if (channel_id in db["active_channels"]):
    return True
  else:
    return False

