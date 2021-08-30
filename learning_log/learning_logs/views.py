from django.shortcuts import render,redirect
from django.contrib.auth.decorators import login_required
from .models import Topic,Entry
from .forms import TopicForm,EntryForm
from django.http import Http404


def index(request):
	return render(request,'learning_logs/index.html')


@login_required
def topics(request):
	"""显示所有主题"""
	topics=Topic.objects.filter(owner=request.user).order_by('date_added')
	context={'topics': topics}
	return render(request,'learning_logs/topics.html',context)


@ login_required
def topic(request,topic_id):
	"""显示单个主题及其所有条目"""
	topic=Topic.objects.get(id=topic_id)
	# 确认请求的主题输入当前用户
	if topic.owner!=request.user:
		raise Http404
	entries=topic.entry_set.order_by('-date_added')
	context={'topic':topic,'entries':entries}
	return render(request,'learning_logs/topic.html',context)


@login_required
def new_topic(request):
	"""添加新主题"""
	if request.method!='POST':
		# 未提交数据时，创建一个新表单
		form=TopicForm()
	else:
		form=TopicForm(data=request.POST)
		if form.is_valid():
			new_topic=form.save(commit=False)
			new_topic.owner=request.user
			new_topic.save()
			return redirect('learning_logs:topics')


	# 显示空表单或指出表单数据无效
	context={'form':form}
	return render(request,'learning_logs/new_topic.html',context)


@login_required
def new_entry(request,topic_id):
	"""在特定主题中添加新条目"""
	topic=Topic.objects.get(id=topic_id)
	if request.method!='POST':
		# 未提交数据，创建一个空表单
		form=EntryForm()
	else:
		# 对提交的数据进行处理
		form=EntryForm(data=request.POST)
		if form_is_valid():
			new_entry=form.save(commit=False)
			new_entry.topic=topic
			new_entry.save()
			return redirect('learning_logs:topic',topic_id=topic_id)


	# 显示空表单或提示表单数据无效
	context={'topic':topic,'form':form}
	return render(request,'learning_logs/new_entry.html',context)


@login_required
def edit_entry(request,entry_id):
	"""编辑既有条目"""
	entry=Entry.objects.get(id=entry_id)
	topic=entry.topic
	if topic.owner!=request.user:
		raise Http404

	if request.method!='POST':
		# 初请求，用当前条目填充表单
		form=EntryForm(instance=entry)
	else:
		# 对提交的数据进行处理
		form=EntryForm(instance=entry,data=request.POST)
		if form.is_valid():
			form.save()
			return redirect('learning_logs:topic',topic_id=topic_id)
	context={'entry':entry,'topic':topic,'form':form}
	return render(request,'learning_logs/edit_entry.html',context)



