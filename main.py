meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "salfok":"salah fokus",
            "odgj":"orang dengan genetik jawa",
            }
            
word = input("Ketik kata yang tidak Kamu mengerti: ")\




if word in meme_dict.keys():
    # Apa yang harus kita lakukan jika kata itu ditemukan?
    print(meme_dict[word])
else:
    # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
    print("katanya gak di catet oleh si pembuat karena males")
 
