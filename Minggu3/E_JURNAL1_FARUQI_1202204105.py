n = 3
attempt = 0
login_succeed = False
for i in range(n):
    a = input("Masukkan username Anda: ")
    b = input("Masukkan password Anda: ")
    # success flow
    if a == "alpro" and b == "daspro123":
      login_succeed = True
      print("Selamat, Anda berhasil login")
      break
    # jika user salah maka percobaan ditambah
    else:
      # percobaan dit
      attempt += 1 
      # jika percobaan sudah 0 lanjut ke fail flow
      # fail flow
      if n - attempt != 0:
        print("Login gagal, Sisa percobaan login sebanyak",n - attempt)
# fail flow, jika login_succeed false, dan percobaan sudah sebanyak n lalu print
# limit habis
if login_succeed == False and n == attempt:
  print("limit habis")
