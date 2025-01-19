import pytest
from myapp.models import Post

@pytest.mark.django_db
def test_post_create():
    post = Post.objects.create(title='제목', content='내용')
    assert post.title == '제목'
    assert post.content == '내용'
    assert Post.objects.count() == 1

@pytest.mark.django_db
def test_post_get():
    post = Post.objects.create(title='제목', content='내용')
    saved_post = Post.objects.get(pk=post.pk)
    assert post.title == saved_post.title
    assert post.content == saved_post.content

@pytest.mark.django_db
def test_count():
    Post.objects.create(title='제목1', content='내용1')
    Post.objects.create(title='제목2', content='내용2')
    Post.objects.create(title='제목3', content='내용3')
    assert Post.objects.count() == 3