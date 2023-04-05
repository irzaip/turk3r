from django.shortcuts import render

# Create your views here.

def home_page(request):
    # navmenu = get_user_menu(request)

    # import datetime
    # today = datetime.datetime.today()
    # kegiatans = Kegiatan.objects.filter(tanggal_mulai__lt=today, tanggal_selesai__gt=today)

    # materis = Materi.objects.order_by('-created_at')[:4]

    # featured = Materi.objects.filter(featured=True)[:4]

    # playlist = Materi.objects.order_by('-created_at').filter(playlist=True)

    # pengumuman = Pengumuman.objects.filter(frontpage=True)

    # _inspirasi = inspirasi()

    # context = {'materis': materis, 
    #     'playlist': playlist, 
    #     'kegiatans': kegiatans, 
    #     'pengumuman': pengumuman, 
    #     'inspirasi': _inspirasi,
    #     'featured': featured}
    # context = {**context, **navmenu}
    
    return render(request, 'basic/home.html')