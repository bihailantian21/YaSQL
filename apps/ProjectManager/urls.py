# -*- coding:utf-8 -*-
# edit by fuzongfei

from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import ProjectListView, BeautifySQLView, GetInceptionHostConfigView, \
    GetDatabaseListView, InceptionSqlOperateView

urlpatterns = [
    path(r'index/', ProjectListView.as_view(), name='p_project'),
    path(r'beautify_sql/', login_required(BeautifySQLView.as_view()), name='p_beautify_sql'),
    path(r'inception_sql_operate/', login_required(InceptionSqlOperateView.as_view()), name='p_sql_operate'),
    path(r'get_inception_hostconfig/', login_required(GetInceptionHostConfigView.as_view()),
         name='p_inception_hostconfig'),
    path(r'get_database/', login_required(GetDatabaseListView.as_view()), name='p_get_database'),
]