#https://algodaily.com/challenge_slides/implement-a-hash-map
class Hashmap:
    def __init__(self):
        self.storage = [None for _ in range(16)]
        self.size = 0

    def hashStr(self, key):
        result = 5381
        for char in key:
            result = 33 * result + ord(char)
        return result

    def set(self, key, val):
        n = len(self.storage)
        idx = self.hashStr(key) % n
        if self.storage[idx] is not None:
          for k in self.storage[idx]:
            if k[0] == key:
              k[1] = val
              break
            else:
              self.storage[idx].append([key, val])  
        else:
          self.storage[idx] = []
          self.storage[idx].append([key, val])          
        
    def get(self, key):
        n = len(self.storage)
        idx = self.hashStr(key) % n
        if self.storage[idx] is None:
          return None
        else:
          for k in self.storage[idx]:
            if k[0] == key:
              return k[1]

obj = Hashmap()
obj.set("jess", "213-559-6840")
res = obj.get("jess")
print(res)
obj.set("james", "123-456-7890")
res = obj.get("james" )
print(res)
