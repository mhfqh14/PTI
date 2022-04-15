from django import forms
from .models import berita

class BeritaForm(forms.ModelForm):
	class Meta:
		model = berita
		fields = [
			'judul',
			'tanggal',
			'penulis',
			'editor',
			'gambar',
			'isi_berita',
		]