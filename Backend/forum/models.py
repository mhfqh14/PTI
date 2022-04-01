from django.db import models
from home.models import user

# Create your models here.

class topik(models.Model):

	List_Kategori = [
		('UMKM', 'UMKM'),
		('Berita', 'Berita'),
		('Forum', 'Forum'),
		('Rekomendasi', 'Rekomendasi'),
		('Aplikasi', 'Aplikasi'),
		('Serba Serbi Ramadhan', 'Serba Serbi Ramadhan'),
		('Modal UMKM', 'Modal UMKM'),

	]


	username = models.ForeignKey(user, on_delete=models.CASCADE)
	judul = models.CharField(max_length=255)
	isi_topik = models.TextField()
	tanggal_upload = models.DateField()
	gambar = models.ImageField()
	kategori = models.CharField(max_length=100, choices=List_Kategori)

	def __str__(self):
		return "{}.{}".format(self.id, self.username, self.judul)


class komentar(models.Model):
	username_user = models.ForeignKey(user, on_delete=models.CASCADE)
	tanggal_upload = models.DateField()
	isi_komentar = models.TextField()
	id_topik = models.ForeignKey(topik, on_delete=models.CASCADE)

	def __str__(self):
		return "{}.{}".format(self.id, self.id_topik, self.isi_komentar)