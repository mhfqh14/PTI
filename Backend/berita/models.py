from django.db import models

# Create your models here.

class berita(models.Model):
	id=models.IntegerField(primary_key=True)
	judul = models.CharField(max_length=200)
	tanggal = models.DateField()
	penulis= models.CharField(max_length=100)
	editor= models.CharField(max_length=100)
	gambar= models.ImageField(upload_to='static/berita/%Y/%m/%d')
	isi_berita= models.TextField()

	def __str__(self):
		return "{}".format(self.judul)