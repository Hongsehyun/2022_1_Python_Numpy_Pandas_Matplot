import pickle
'''
# Pickle - Write
profile_file = open("profile.pickle","wb")
    # 'wb' = write binary type
    # pickle을 쓰기 위해서는 항상 binary type으로 정의해야 한다.

profile = {"이름":"박명수", "나이":30, "취미":["축구","골프","코딩"]}
print(profile)

pickle.dump(profile, profile_file)
    # profile에 있는 정보를 pickle을 이용하여 file에 저장하는 코드

profile_file.close()
'''



# Pickle - Read
profile_file = open("profile.pickle","rb")

profile = pickle.load(profile_file)
    # pickle을 이용하여 file에 저장된 정보를 읽어오는 코드

print(profile)
profile_file.close()


