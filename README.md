# Proyek Akhir: Menyelesaikan Permasalahan Institusi Pendidikan

## Business Understanding

Jaya Jaya Institut, sebuah institusi pendidikan yang telah berdiri sejak tahun 2000, telah menghasilkan banyak lulusan dengan reputasi yang sangat baik. Namun, institusi ini juga menghadapi tantangan besar dalam bentuk tingginya jumlah siswa yang tidak menyelesaikan pendidikan mereka, atau yang lebih dikenal sebagai dropout.

Tingginya tingkat dropout menjadi masalah serius bagi institusi pendidikan. Oleh karena itu, Jaya Jaya Institut bertekad untuk mendeteksi dini siswa-siswa yang berisiko melakukan dropout, sehingga mereka dapat diberikan bimbingan khusus.

Dari total 4.424 siswa yang terdaftar, 1.421 siswa mengalami dropout, atau sekitar 32% dari total siswa. Berdasarkan analisis data, faktor-faktor tertentu telah diidentifikasi sebagai penyebab tingginya tingkat dropout di institusi ini.

### Permasalahan Bisnis

Tingginya tingkat siswa yang dropout, dengan rasio jumlah siswa yang keluar/dropout dibandingkan dengan total siswa mencapai lebih dari 30%, merupakan tantangan signifikan bagi institusi dalam mempertahankan siswa berkualitas.

Analisis terhadap faktor-faktor yang mempengaruhi tingkat dropout mengungkap beberapa pola menarik. Sebagai contoh, ditemukan bahwa tingkat dropout yang tinggi terjadi terutama pada siswa dengan karakteristik tertentu, seperti Application mode dengan pilihan "Over 23 years old", diikuti oleh "1st phase", dan "2nd phase - general contingent", course, nacionality, mothers and fathers qualification, Tuition fees up to the dare, dan lainnya.

Dari analisis ini, dapat disimpulkan bahwa terdapat beberapa faktor yang berkontribusi terhadap tingginya tingkat dropout di Jaya Jaya Institut. Identifikasi faktor-faktor ini dapat membantu institusi dalam mengambil langkah-langkah yang tepat untuk mengurangi dropout, termasuk kebijakan, penerimaan, dukungan akademik, dan pengelolaan SDM.

### Cakupan Proyek

1. Persiapan
   - Menyiapkan library yang dibutuhkan
   - Menyiapkan data yang akan digunakan
2. Data Understanding: Mengumpulkan informasi tentang data yang dimiliki, untuk memahami struktur, kualitas, dan karakteristik data secara keseluruhan, terutama dalam hal perubahan tipe data.
   - EDA: Melakukan eksplorasi data secara visual dan deskriptif untuk memahami karakteristik dan pola dalam data.
3. Data Preparation/Preprocessing: Menyiapkan data untuk analisis dengan membersihkan, merapihkan, dan mengubah format data agar sesuai dengan kebutuhan analisis.
4. Modelling: Melakukan pemodelan data menggunakan algoritma decision tree, random forest, dan gradient boosting.
5. Evaluation: Melakukan evaluasi terhadap algoritma-algoritma tersebut. Algoritma dengann akurasi terbaik akan dipilih untuk melakukan prediksi.

Output akhir dari proyek ini adalah dashboard visualisasi data yang memberikan pandangan menyeluruh tentang kondisi siswa di Jaya Jaya Institut. Dashboard ini akan membantu dalam memahami faktor-faktor yang mempengaruhi tingginya tingkat dropout dan menyusun strategi yang tepat untuk mengatasi masalah tersebut. Selain itu, sistem machine learning yang telah dibuat juga akan di-deploy menggunakan Streamlit, sehingga pengguna dapat dengan mudah mengakses dan menggunakan model prediksi secara real-time.

### Persiapan

Sumber data: [https://github.com/dicodingacademy/dicoding_dataset/blob/main/students_performance]

Setup environment - Anaconda

```
conda create --name edutech python=3.9
conda activate edutech
pip install numpy pandas scipy matplotlib seaborn jupyter sqlalchemy scikit-learn==1.3.2 joblib==1.3.1 streamlit==1.24.0
jupyter-notebook .
```

## Business Dashboard

Dashboard yang dibuat menggunakan aplikasi Metabase berfungsi sebagai alat visualisasi untuk memantau berbagai aspek terkait siswa di Jaya Jaya Institut. Dashboard ini menyajikan informasi penting seperti jumlah siswa, distribusi status siswa, dan faktor-faktor yang menyebabkan tingginya tingkat dropout (rasio jumlah siswa yang keluar dari institut).

## Menjalankan Sistem Machine Learning

Buka terminal atau command prompt, lalu arahkan ke direktori tempat file berada. jalankan perintah berikut untuk menjalankan aplikasi streamlit. Run Streamlit App

```
streamlit run status_app.py
```

Deploy a streamlit app

```
https://education-institut-portfolio-lia.streamlit.app/
```

## Conclusion

Diketahui bahwa Jaya Jaya Institut memiliki 4.424 siswa, dan lebih dari 30% dari siswa dropout. Berdasarkan analisis data,terdapat beberapa faktor yang mempengaruhi tingginya dropout tersebut, antara lain:

1. Application Mode: Metode pendaftaran yang digunakan oleh siswa, dengan mayoritas siswa yang dropout berasal dari kelompok aplikasi "Over 23 years old" (435 siswa), diikuti oleh "1st phase" (345 siswa), dan "2nd phase - general contingent" (256 siswa).
2. Application Order: Urutan pendaftaran siswa juga memengaruhi, dengan siswa yang mendaftar pada pilihan 1 (antara 0 - pilihan pertama; dan 9 - pilihan terakhir) memiliki jumlah dropout mencapai 1.053.
3. Course: Course yang diambil oleh siswa juga berpengaruh, dengan tingkat dropout tertinggi terjadi pada course "Manajemen" (kehadiran malam) dengan 136 siswa, diikuti oleh "Manajemen" (134 siswa), dan "Keperawatan" (118 siswa).
4. Previous Qualification: Kualifikasi yang diperoleh oleh siswa sebelum mendaftar di institusi juga memainkan peran, dengan siswa yang memiliki kualifikasi pendidikan menengah memiliki jumlah dropout sebesar 1.078.
5. Nacionality: Siswa yang memiliki kewarganegaraan Portugal memiliki tingkat dropout sebesar 1.389 siswa.
6. Mothers Qualification: Kualifikasi pendidikan ibu juga memengaruhi, dengan jumlah dropout tertinggi terjadi pada ibu dengan kualifikasi "Pendidikan Dasar 1st Cycle" (383 siswa), diikuti oleh "Pendidikan Menengah" (300 siswa), dan "Pendidikan Dasar 3rd Cycle" (271 siswa).
7. Fathers Qaulification: Kualifikasi pendidikan ayah juga memengaruhi, dengan jumlah dropout tertinggi terjadi pada ayah dengan kualifikasi "Pendidikan Dasar 1st Cycle" (432 siswa), diikuti oleh "Pendidikan Menengah" (281 siswa), dan "Pendidikan Dasar 3rd Cycle" (264 siswa).
8. Admission Grade: Siswa dengan nilai masuk sebesar 120, 130, dan 140, serta 100, memiliki jumlah dropout yang signifikan.
9. Attendance: Kehadiran siswa pada kelas siang atau malam juga mempengaruhi, dengan jumlah dropout terbesar terjadi pada siswa yang menghadiri kelas siang (1.214 siswa).
10. Tuition Fees Up To the Date: Biaya pendidikan hingga saat ini juga berperan, dengan 964 siswa yang dropout.
11. Age at Enrollment: Usia siswa saat mendaftar juga memainkan peran, dengan jumlah dropout tertinggi terjadi pada usia 19, 18, dan 20 tahun (masing-masing 207, 202, 133 siswa).
12. Grade: Siswa dengan nilai mata kuliah yang rendah cenderung memiliki tingkat dropout yang lebih tinggi.

### Rekomendasi Action Items

Berikan beberapa rekomendasi action items yang harus dilakukan institusi guna menyelesaikan permasalahan atau mencapai target mereka.

- Pengembangan program: Meningkatkan kualitas course yang memiliki tingkat dropout tinggi dengan memperhatikan kebutuhan dan minat siswa.
- Peningkatan rekrutmen: Menyusun strategi rekrutmen yang lebih efektif untuk siswa dengan kualifikasi pendidikan menengah.
- Dukungan psikologis: Menyediakan layanan dukungan psikologis dan akademis bagi siswa dengan masalah keuangan atau pribadi yang mungkin memengaruhi siswa dalam sekolah.
- Penyuluhan orang tua: Melakukan penyuluhan kepada orang tua tentang pentingnya pendidikan tinggi dan peran mereka dalam mendukung keberhasilan akademis anak-anak mereka.
- Mendirikan perkumpulan siswa berdasarkan kenegaraan untuk memfasilitasi integrasi sosial dan dukungan kultural antara siswa dari negara yang sama.

email: root@mail.com
password: root123
