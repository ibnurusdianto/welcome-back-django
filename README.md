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

# Day 2 - File Static Django

File static di Django digunakan untuk menyimpan berkas-berkas seperti gambar, file CSS, JavaScript, atau resource eksternal lainnya yang dibutuhkan oleh tampilan (template) aplikasi.

Penerapan file static di Django cukup mudah. Langkah-langkah dasarnya sebagai berikut:

1. Buat direktori bernama static di dalam folder proyek atau aplikasi Django.
2. Jika diperlukan, buat subfolder di dalamnya sesuai kebutuhan, misalnya css, js, atau img.
3. Konfigurasikan bagian settings.py seperti contoh berikut:

```
STATIC_URL = 'static/'
STATIC_ROOT = BASE_DIR / 'static'
STATICFILES_DIRS = [
    'mysite/static'
]
```
Konfigurasi di atas berarti: “Django akan mencari semua file static yang berada di dalam folder mysite/static lalu mengumpulkannya ke dalam folder static utama pada proyek.”

Untuk menggunakan file static di template (views), pertama-tama load tag {% static %} di bagian atas file HTML. Contoh penerapannya sebagai berikut:

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bootstrap Integration</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet"
        crossorigin="anonymous">
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>

<body>
    <div class="container pt-5">
        <h1>Hello, world!</h1>
        <table class="table">
            <thead>
                <tr>
                    <th scope="col">#</th>
                    <th scope="col">First</th>
                    <th scope="col">Last</th>
                    <th scope="col">Handle</th>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <th scope="row">1</th>
                    <td>Mark</td>
                    <td>Otto</td>
                    <td>@mdo</td>
                </tr>
                <tr>
                    <th scope="row">2</th>
                    <td>Jacob</td>
                    <td>Thornton</td>
                    <td>@fat</td>
                </tr>
                <tr>
                    <th scope="row">3</th>
                    <td>John</td>
                    <td>Doe</td>
                    <td>@social</td>
                </tr>
            </tbody>
        </table>
    </div>

    <!-- <img src="{% static 'img/2.png' %}" alt="test" width="400"> -->

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"
        crossorigin="anonymous"></script>
</body>

</html>
```
Poin pentingnya adalah selalu load tag {% static %} terlebih dahulu, kemudian panggil file static menggunakan sintaks {% static 'path/ke/file' %}.

Sebagai contoh, untuk menampilkan gambar yang berada di folder img, gunakan:
{% static 'img/2.png' %}

[![2.png](https://i.postimg.cc/xdYwbf4y/2.png)](https://postimg.cc/TK77z6Gp)

### Django Apps & Models 
Dalam Django, sebuah proyek biasanya terdiri dari beberapa aplikasi kecil (apps) yang masing-masing menangani satu fitur atau domain tertentu, misalnya karyawan, customer, produk, dan lain-lain. Setiap app bersifat terpisah dan mandiri sehingga struktur kode lebih rapi dan mudah dikelola.

Sebagai contoh, untuk membuat app khusus karyawan, kamu bisa menjalankan perintah:
```
python manage.py startapp karyawan

```
Perintah ini akan membuat folder karyawan yang berisi berkas-berkas Django standar, tempat kamu mendefinisikan models, admin, views, dan kebutuhan lain yang terkait dengan data karyawan. Model yang kamu buat di models.py bisa didaftarkan ke admin Django di admin.py agar mudah dikelola melalui antarmuka admin.

Django juga sudah menyediakan admin panel bawaan. Untuk menggunakannya, lakukan migrasi terlebih dahulu:

```
python manage.py makemigrations
python manage.py migrate

```
Setelah itu, buat akun superuser dengan:
```
python manage.py createsuperuser

```
Isi semua kredensial yang diminta. Jika sudah, kamu bisa mengakses admin panel melalui URL:
```
http://localhost:8000/admin/

```
di mana kamu bisa login menggunakan akun superuser tersebut dan mengelola data dari apps dan models yang sudah kamu daftarkan.

[![Gemini-Generated-Image-6ne76k6ne76k6ne7.png](https://i.postimg.cc/9FgrWfJS/Gemini-Generated-Image-6ne76k6ne76k6ne7.png)](https://postimg.cc/8jW14T8B)

### Fetch data dari database dan tampilkan dalam tabel di Django
 
Dalam Django, proses menampilkan data dari database ke dalam tabel HTML dilakukan lewat tiga tahap utama: mendefinisikan model, mengambil data di views, lalu merendernya di template.

1. Mendefinisikan model Employee

Pertama, buat model di models.py pada app karyawan:

```python
from django.db import models
# Create your models here.

# implementasikan model employee 
class employee(models.Model):
    name = models.CharField(max_length=100) # charfield adalah karakter field
    age = models.IntegerField() # integerfield adalah integer field
    salary = models.IntegerField() # integerfield adalah integer field
    photo = models.ImageField(upload_to='photos/') # imagefield adalah image field
    designation = models.CharField(max_length=100) # charfield adalah karakter field
    email_address = models.EmailField(max_length=100, unique=True) # emailfield adalah email field
    phone_number = models.CharField(max_length=15, unique=True) # charfield adalah karakter field
    address = models.TextField() # textfield adalah text field
    created_at = models.DateTimeField(auto_now_add=True) # datetimefield adalah datetime field
    updated_at = models.DateTimeField(auto_now=True) # datetimefield adalah datetime field
    
    # untuk menampilkan nama employee di admin
    def __str__(self):
        return self.name
```
Setelah model dibuat, jalankan:
```
python manage.py makemigrations
python manage.py migrate

```
Perintah ini akan membuat dan meng-update tabel di database berdasarkan model employee.

[![Gemini-Generated-Image-ujaz1xujaz1xujaz.png](https://i.postimg.cc/tCRKHKRJ/Gemini-Generated-Image-ujaz1xujaz1xujaz.png)](https://postimg.cc/Z0g78Ddz)

2. Fetch data di views.py

Berikut contoh view untuk mengambil semua data karyawan dan mengirimkannya ke template:

```python
from django.http import HttpResponse
from django.shortcuts import render

from employess.models import employee


def home(request):
    # ambil semua data dari model Employee
    employees = employee.objects.all()
    # print(employees)
    context = {
        'employees': employees,
    }
    return render(request, 'home.html', context)
```

Pada kode di atas:
- employee.objects.all() akan mengambil semua baris data dari tabel employee.
- Data tersebut dimasukkan ke dalam context dengan key 'employees', yang nantinya bisa diakses di template.

[![Gemini-Generated-Image-zb1etzzb1etzzb1e.png](https://i.postimg.cc/8CCdpbJY/Gemini-Generated-Image-zb1etzzb1etzzb1e.png)](https://postimg.cc/PCBvKYMb)

3. Menampilkan data dalam tabel di template

Di file home.html, gunakan loop for di template untuk menampilkan data dalam bentuk tabel:

```html
{% load static %}
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Bootstrap Integration</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/css/bootstrap.min.css" rel="stylesheet"
        crossorigin="anonymous">
    <link rel="stylesheet" href="{% static 'css/style.css' %}">
</head>

<body>
    <div class="container pt-5">
        <h1>Hello, world!</h1>
        <table class="table">
            <thead>
                <tr>
                    <th scope="col">Id</th>
                    <th scope="col">Nama</th>
                    <th scope="col">Usia</th>
                    <th scope="col">Photo</th>
                    <th scope="col">Jabatan</th>
                    <th scope="col">Email</th>
                    <th scope="col">No. Telp</th>
                    <th scope="col">Alamat</th>
                    <th scope="col">Dibuat Pada</th>
                    <th scope="col">Diupdate Pada</th>
                </tr>
            </thead>
            <tbody>
                {% for emp in employees %}
                <tr>
                    <th scope="row">{{forloop.counter}}</th>
                    <td>{{emp.name }}</td>
                    <td>{{emp.age }}</td>
                    <td><img src="{{emp.photo.url}}" alt="foto" width="30px" height="30px"></td>
                    <td>{{emp.designation }}</td>
                    <td>{{emp.email_address }}</td>
                    <td>{{emp.phone_number }}</td>
                    <td>{{emp.address }}</td>
                    <td>{{emp.created_at }}</td>
                    <td>{{emp.updated_at }}</td>
                </tr>
                {% endfor %}



            </tbody>
        </table>
    </div>

    <!-- <img src="{% static 'img/2.png' %}" alt="test" width="400"> -->

    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.8/dist/js/bootstrap.bundle.min.js"
        crossorigin="anonymous"></script>

</body>

</html>
```

Beberapa poin penting dari template di atas:
- employees adalah nama variabel context yang dikirim dari view.
- {% for emp in employees %} akan melakukan iterasi untuk setiap objek employee.
- {{ forloop.counter }} menampilkan nomor urut baris mulai dari 1.
- {{ emp.photo.url }} digunakan untuk mengambil URL file gambar dari field ImageField (pastikan konfigurasi MEDIA_URL dan MEDIA_ROOT sudah benar).

[![Gemini-Generated-Image-h7chneh7chneh7ch.png](https://i.postimg.cc/W1gCmTXf/Gemini-Generated-Image-h7chneh7chneh7ch.png)](https://postimg.cc/87kZNQ8h)
