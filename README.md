# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding
Jaya Jaya Institut merupakan salah satu institusi pendidikan perguruan yang telah berdiri sejak tahun 2000. Hingga saat ini ia telah mencetak banyak lulusan dengan reputasi yang sangat baik. Akan tetapi, terdapat banyak juga siswa yang tidak menyelesaikan pendidikannya alias dropout. Jumlah dropout yang tinggi ini tentunya menjadi salah satu masalah yang besar untuk sebuah institusi pendidikan. Oleh karena itu, Jaya Jaya Institut ingin mendeteksi secepat mungkin siswa yang mungkin akan melakukan dropout sehingga dapat diberi bimbingan khusus.

### Permasalahan Bisnis
1. Mengidentifikasi faktor-faktor yang mempengaruhi Dropout di institusi pendidikan
2. Memperhatikan masalah siswa diluar pendidikan
3. Mengidentifikasi mata kuliah yang menyumbang siswa dropout

### Cakupan Proyek
1. Eksplorasi serta pemahaman data
2. Data preparasi
3. Menganalisa faktor-faktor penyebab terjadinya dropout yang tinggi
4. Membuat business dashboard
5. Menjalankan sistem machine learning
6. Kesimpulan dan saran penyelesaian

### Persiapan

Sumber data: https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance/data.csv.

Setup environment:
1. Menginstall environment python terlebih dahulu seperti Anaconda, VS Code atau bisa langsung membuka Google Colab
2. Jalankan file notebook.ipynb
    - Import library yang dibutuhkan sesuai file requirement.txt atau dapat juga dengan menjalankan "pip install -r requirements.txt" di environment yang dipakai
    - Jalankan seluruh isi file notebook.ipynb menggunakan Google Colab/Anaconda/VS Code untuk melihat hasil analisis dan insight yang diperoleh
3. Membuat dashboard
    - Dashboard dapat dibuat dengan Tableu,Looker Studio maupun Metabase. Disini dashboard yang dibuat dengan metabase (perlu diperhatikan untuk menginstal Docker terlebih dahulu)
    - Jalankan perintah [docker pull metabase/metabase:v0.46.4 di terminal] atau dapat langsung diinstal melalui docker [images > tambahkan > metabase]
    - Untuk menjalankan container Metabase [docker run -p 3000:3000 --name metabase metabase/metabase] atau melalui docker [images > klik run > isi nama container dan jangan lupa isi port dengan 3000]
    - Login metabase dengan
        username : ivanyurdean50@gmail.com
        password : Athene50

## Business Dashboard
Dashboard yang dibuat dapat mempermudah institusi pendidikan memantau faktor yang menyebabkan terjadinya Dropout yang tinggi secara visualisasi yang mudah untuk dipahami.
Untuk mengakses dashboard tersebut anda dapat menjalankan docker lalu login ke metabase dengan username dan password sesuai yang diatas

## Menjalankan Sistem Machine Learning
1. Melakukan splitting data
2. Membuat berbagai model machine learning seperti model logistic regression, random forest dll
3. Membandingkan model dengan melihat accuracy

Untuk mengaksesnya dapat menjalankan file prediction.ipynb

4. Membuat solusi machine learning dengan streamlit sesuai dengan file app.py lalu jangan lupa menjalankannya di terminal (streamlit run app.py)

link deploy yang siap digunakan dapat diakses pada :
https://tugasakhir-drvfdwiv79apgykjtzgxp4.streamlit.app/

## Conclusion
1. Faktor utama penyebab Dropout adalah Tuition fee/biaya pendidikan yang membuat siswa tidak mampu untuk melanjutkan pendidikan
2. Model prediksi terbaik yang digunakan adalah model xgboost dengan akurasi 80%
3. Mata kuliah Management dan management (evening attendance) banyak menyumbang dropoutnya siswa

### Rekomendasi Action Items
Berikan beberapa rekomendasi action items yang harus dilakukan perusahaan guna menyelesaikan permasalahan atau mencapai target mereka.
- Mengkaji kembali biaya pendidikan supaya siswa dapat membayarnya serta seleksi ulang beasiswa yang telah diberikan supaya on target.
- Melakukan rapat untuk memperbaiki kurikulum atau gaya mengajar terutama pada mata kuliah Management dan management (evening attendance).
- Sosialisasikan tentang hasil kajian Tuition fee untuk siswa yang sedang menempuh ataupun yang akan masuk kuliah pada institusi pendidikan.
- Gunakan model xgboost untuk prediksi.
