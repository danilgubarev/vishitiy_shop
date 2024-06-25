from main.utils import header_links_list

def header_links(request):
    print("header_links is", header_links_list)
    return {"header_links": header_links_list}