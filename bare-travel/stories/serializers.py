from rest_framework.serializers import HyperlinkedIdentityField, ModelSerializer, SerializerMethodField

from users.serializers import UserSerializer

from .models import Story


post_detail_url = HyperlinkedIdentityField(view_name='stories:detail', lookup_field='slug')


class StoryCreateUpdateSerializer(ModelSerializer):
    class Meta:
        model = Story
        fields = ['title', 'content']


class StoryDetailSerializer(ModelSerializer):
    url = post_detail_url
    user = UserSerializer(read_only=True)
    html = SerializerMethodField()

    class Meta:
        model = Story
        fields = ['url', 'id', 'user', 'title', 'slug', 'content', 'html',]

    def get_html(self, obj):
        return obj.get_markdown()

    def get_image(self, obj):
        try:
            image = obj.image.url
        except:
            image = None
        return image


class StoryListSerializer(ModelSerializer):
    url = post_detail_url
    user = UserSerializer(read_only=True)

    class Meta:
        model = Story
        fields = ['url', 'user', 'title', 'content']
