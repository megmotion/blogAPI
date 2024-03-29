from rest_framework.serializers import (
	HyperlinkedIdentityField, 
	ModelSerializer, 
	SerializerMethodField
	)
from accounts.api.serializers import UserDetailSerializer  
from comments.api.serializers import CommentSerializer
from comments.models import Comment
from posts.models import Post

class PostCreateUpdateSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
			'title',
			# 'slug',
			'content',
			'published'
		]

post_detail_url = HyperlinkedIdentityField(
        view_name='posts-api:detail',
        lookup_field='slug'
        )

class PostDetailSerializer(ModelSerializer):
	url =post_detail_url
	user = UserDetailSerializer(read_only=True)
	image = SerializerMethodField()
	html = SerializerMethodField()
	comments = SerializerMethodField()
	class Meta:
		model = Post
		fields = [
			'id',
			'url',
			'user', 
			'title',
			'slug',
			'content',
			'html',
			'published',
			'image',
			'comments'
		]
	def get_html(self, obj):
		return obj.get_markdown()

	def get_image(self, obj):
		try:
			image = obj.image.url
		except:
			image = None
		return image					

	def get_comments(self, obj):
		c_qs = Comment.objects.filter_by_instance(obj)
		comments = CommentSerializer(c_qs, many=True).data
		return comments


class PostListSerializer(ModelSerializer):
	url = post_detail_url
	user = UserDetailSerializer(read_only=True)
	class Meta:
		model = Post
		fields = [
			'url',
			'user',
			'title',
			'content',
			'published',
		]	