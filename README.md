# Proyek Akhir: Menyelesaikan Permasalahan Perusahaan Edutech

## Business Understanding

Attrition (tingkat keluar-masuk karyawan) adalah salah satu tantangan utama yang dihadapi oleh perusahaan. 
Tingginya tingkat attrition dapat menyebabkan biaya tambahan seperti rekrutmen, pelatihan, dan penurunan produktivitas. 
Dengan menganalisis faktor-faktor yang memengaruhi attrition, perusahaan dapat mengidentifikasi penyebab utama dan mengambil 
langkah untuk mengurangi tingkat keluar-masuk karyawan..


### Permasalahan Bisnis

Beberapa masalah bisnis yang perlu dijawab adalah:

1. Apakah kelompok umur tertentu lebih rentan terhadap attrition?
2. Apakah gender memengaruhi pola attrition?
3. Departemen mana yang memiliki tingkat attrition tertinggi, dan mengapa?
4. Apakah gaji rendah menyebabkan karyawan lebih mungkin keluar?
5. Berapa lama rata-rata seorang karyawan bertahan di perusahaan?
6. Apakah ada hubungan antara kenaikan gaji/bonus dengan tingkat retensi karyawan?
7. Apakah jam kerja yang panjang atau pendek memengaruhi keputusan karyawan untuk keluar?.

### Cakupan Proyek

1. Analisis Data Attrition
    <p>Mengumpulkan data historis terkait dengan:</p>

- Usia, gender, departemen, gaji, durasi bekerja, kenaikan gaji/bonus, jam kerja, dan status attrition.
- Mengidentifikasi pola dan korelasi di antara variabel-variabel tersebut.

2. Pengukuran dan Evaluasi

- Menghitung tingkat attrition berdasarkan kelompok umur, gender, departemen, tingkat gaji, dan lainnya.
- Menentukan durasi rata-rata seorang karyawan bekerja sebelum keluar.

3. Rekomendasi Strategis

- Memberikan rekomendasi kepada manajemen untuk mengurangi tingkat attrition melalui kebijakan seperti kenaikan gaji,
  bonus, jam kerja fleksibel, atau program kepuasan kerja.

### Persiapan

Sumber data: <a href="https://github.com/dicodingacademy/dicoding_dataset/blob/main/employee/employee_data.csv?raw=true">Link Dataset</a>

Setup environment:

```bash
conda create -n myenv
conda activate myenv
pip install -r requirements.txt
```

## Business Dashboard
<img src="Employee_Analysis.png" alt="dashboard">

<a href="https://lookerstudio.google.com/reporting/20abbeb8-00c6-4b5c-a080-979679ec415e">Link Dashboard</a>

## Conclusion
1. Apakah kelompok umur tertentu memiliki tingkat attrition yang lebih tinggi?
- Dari analisis tersebut terlihat bahwa karyawan pada kelompok usia awal karir dan kelompok paruh baya cenderung memiliki 
tingkat atrisi yang lebih tinggi dibandingkan kelompok usia lainnya. Hal ini menunjukkan bahwa karyawan muda dan mereka 
yang berada pada tahap pertengahan karir mereka mungkin menghadapi tantangan atau ketidakpuasan yang menyebabkan mereka meninggalkan organisasi.
2. Bagaimana tingkat attrition bervariasi berdasarkan gender?
- Data menunjukkan bahwa karyawan laki-laki memiliki tingkat atrisi yang lebih tinggi dibandingkan karyawan perempuan. 
Hal ini menunjukkan bahwa karyawan laki-laki mungkin menghadapi tantangan atau ketidakpuasan berbeda yang menyebabkan 
mereka keluar dari perusahaan
3. Departemen mana yang memiliki tingkat attrition tertinggi?
- Data menunjukkan bahwa departemen Penelitian & Pengembangan memiliki pengurangan yang sedikit lebih rendah dibandingkan
dengan departemen Sumber Daya Manusia dan Penjualan. Namun perbedaannya relatif kecil.
4. Apakah tingkat attrition lebih tinggi di antara karyawan dengan gaji lebih rendah?
- Data tersebut menunjukkan bahwa karyawan dengan gaji rendah mempunyai kemungkinan lebih besar untuk berhenti bekerja 
(attrition) dibandingkan dengan karyawan dengan gaji sedang atau tinggi.
5. Berapa lama rata-rata karyawan bertahan di perusahaan sebelum mereka mengalami attrition?
- Data tersebut menunjukkan bahwa karyawan dengan masa kerja jangka pendek (masa kerja kurang dari 5 tahun) dan lulusan 
baru (pengalaman kurang dari 1 tahun) lebih besar kemungkinannya untuk keluar (mengalami atrisi) dibandingkan dengan kelompok lainnya.
6. Bagaimana tingkat attrition bervariasi berdasarkan kenaikan gaji atau bonus
- Data menunjukkan bahwa memberikan kenaikan gaji saja mungkin bukan strategi yang efektif untuk mengurangi pengurangan karyawan
7. Bagaimana tingkat attrition dipengaruhi oleh jam kerja rata-rata?
- Data menunjukkan bahwa karyawan dengan keseimbangan kehidupan kerja yang sangat baik dan tidak bekerja lembur lebih 
mungkin untuk berhenti dibandingkan dengan kelompok lain.
8. Apakah kelompok yang sudah menikah tingkat attrition lebih tinggi?
- Data tersebut menunjukkan bahwa karyawan yang masih single lebih besar kemungkinannya untuk berhenti bekerja (attrisi)
dibandingkan dengan karyawan yang sudah menikah atau bercerai.



### Rekomendasi Action Items

Untuk mengurangi tingkat attrition, organisasi perlu fokus pada retensi karyawan muda dan di tahap karier menengah melalui
program pengembangan karier dan survei kebutuhan. Tingkatkan pengalaman kerja pria dengan kebijakan keseimbangan kerja-hidup
yang lebih baik, serta perhatian khusus pada departemen HR dan Sales dengan insentif berbasis kinerja dan pengelolaan beban kerja.
Gaji rendah sebagai pemicu attrition dapat diatasi dengan menawarkan kompensasi kompetitif dan program penghargaan. Memperpanjang 
masa kerja karyawan melalui onboarding yang efektif dan rencana karier yang jelas juga penting. Selain itu, kenaikan gaji 
saja tidak cukup, sehingga perlu pendekatan holistik yang melibatkan pengembangan karier dan kesejahteraan kerja. 
Untuk keseimbangan kerja-hidup, pastikan apresiasi atas kontribusi karyawan tetap terjaga. Terakhir, tingkatkan keterhubungan sosial 
bagi karyawan lajang melalui kegiatan sosial dan kebijakan kerja fleksibel. Pendekatan terpadu ini akan menciptakan lingkungan kerja 
yang mendukung dan menekan tingkat attrition.