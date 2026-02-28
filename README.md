# Day 1 – Try Again for Learning Django

Django adalah framework Python yang sangat ramah bagi pengembang karena mendukung pembuatan aplikasi web dengan cepat, aman, dan fleksibel. Django menerapkan arsitektur MVT (Model–View–Template), yang serupa dengan konsep MVC pada framework lain.


- Model: Komponen yang mendefinisikan struktur data dalam basis data. Model digunakan untuk mengelola operasi CRUD (Create, Read, Update, Delete) sehingga logika data tetap terpisah dari logika tampilan.

- View: Komponen yang berfungsi memproses permintaan (request) dari pengguna, menjalankan business logic, dan mengembalikan response berupa halaman web yang dirender melalui template.

- Template: Komponen yang berfungsi menampilkan antarmuka pengguna (user interface). Template berisi struktur HTML yang akan diisi oleh data dari view.

[![1.png](https://i.postimg.cc/VvyWwywV/1.png)](https://postimg.cc/7GV21Wf3)

Sebelum memulai proyek Django, langkah terbaik adalah membuat virtual environment untuk mengelola dependensi agar tidak bercampur dengan sistem utama.

Jalankan perintah berikut di cmd, PowerShell, atau Git Bash (direkomendasikan agar menghindari error “running scripts is disabled on this system”):

```
python -m venv env
```

Aktifkan environment tersebut dengan perintah
 
```
source env/Scripts/activate
```

Lalu instal Django dengan versi tertentu, misalnya
 
```
pip install Django==6.0.2
```

Untuk membuat proyek baru, gunakan perintah

```
django-admin startproject mysite djangotutorial
```

Perintah ini akan membuat struktur dasar proyek Django dengan file dan direktori yang diperlukan.

[![2.png](https://i.postimg.cc/k4SWfj8C/2.png)](https://postimg.cc/8J1FCmtX)

Agar halaman dapat diakses melalui URL tertentu, kita harus menambahkan URL pattern di file urls.py. Misalnya, untuk membuat homepage dan about page, tambahkan kode berikut

```
"""
Jika ingin membuat url lainnya berarti harus menambahkan pathnya di dalam list urlpatterns
dan gunakan modul yang diinginkan
contoh saya membuat url pattern home dan menyimpannya di dalam module
views.py dan function home sesuai dengan url pattern yang dibuat

lalu jangan lupa import semua dari module yang dibuat, contoh saya 
mengimport views
"""

urlpatterns = [
    path('admin/', admin.site.urls),
    # contoh membuat url pattern home 
    path('', views.home), # homepage 
    path('about/', views.about), # about page
]
```

Pastikan Anda sudah mengimpor modul views agar fungsi home dan about dapat diakses

```
from django.contrib import admin
from django.urls import path
# jangan lupa import views
from . import views
```
Selanjutnya, buat folder bernama templates di direktori utama proyek (base directory). Folder ini akan digunakan untuk menyimpan semua file HTML yang akan dirender oleh Django.

Setelah folder dibuat, ubah konfigurasi pada settings.py agar Django dapat menemukan direktori template Anda

```
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```
Pastikan bagian 'DIRS' disesuaikan dengan lokasi folder templates Anda.

[![3.png](https://i.postimg.cc/zXxHSmMK/3.png)](https://postimg.cc/hf7GcYKt)
