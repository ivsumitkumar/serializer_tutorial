# CursorPagination
# from rest_framework.pagination import CursorPagination

# class myPaginations(CursorPagination):
#     page_size = 5
#     ordering = 'name'
#     cursor_query_param = 'cu'

# LimitOffsetPagination
# from rest_framework.pagination import LimitOffsetPagination

# class myPaginations(LimitOffsetPagination):
#     default_limit = 5
#     limit_query_param = 'mylimit'
#     offset_query_param='myoffset'
#     max_limit = 12


#   PageNumberPagination
# from rest_framework.pagination import PageNumberPagination

# class myPaginations(PageNumberPagination):
#     page_size = 3
#     # page_query_param = 'mypage'
#     # page_size_query_param = 'records'
    # max_page_size = 7