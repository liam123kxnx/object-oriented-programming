class anime_characters:
    print("anime_character created successfully")
    def __init__(self,name,grade,hobby):
     self.name =name
     self.grade =grade
     self.hobby =hobby
    def run(self):
       print(self.name,"is running")


anime_characters1 =anime_characters("kurosaki-ichigo","12","bankai")
anime_characters2 =anime_characters("isagi-yoichi","11","football")
anime_characters3 =anime_characters("mugiwara-no-luffy","13","meat")
print(anime_characters2.hobby)
print(anime_characters1.name)
print(anime_characters3.grade)
anime_characters3.run()