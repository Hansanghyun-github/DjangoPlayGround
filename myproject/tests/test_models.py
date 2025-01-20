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

@pytest.mark.django_db
def test_update():
    post = Post.objects.create(title='제목', content='내용')
    title = '수정된 제목'
    content = '수정된 내용'
    Post.objects.update_or_create(pk=post.pk, defaults={'title': title, 'content': content})
    assert Post.objects.get(pk=post.pk).title == title
    assert Post.objects.get(pk=post.pk).content == content

@pytest.mark.django_db
def test_bulk_update():
    # 게시물 생성 및 저장
    posts = [
        Post(title='제목1', content='내용1'),
        Post(title='제목2', content='내용2'),
        Post(title='제목3', content='내용3'),
    ]
    Post.objects.bulk_create(posts)

    # 저장된 게시물 다시 가져오기
    posts = list(Post.objects.all())

    # 게시물 업데이트
    for post in posts:
        post.content = '수정된 ' + post.content

    Post.objects.bulk_update(posts, ['content'])

    for post in posts:
        assert Post.objects.get(pk=post.pk).content == post.content

@pytest.mark.django_db
def test_create_pk():
    post = Post.objects.create(title='제목', content='내용')
    assert post.pk is not None

@pytest.mark.django_db
def test_bulk_create_pk():
    posts = [
        Post(title='제목1', content='내용1'),
        Post(title='제목2', content='내용2'),
        Post(title='제목3', content='내용3'),
    ]
    Post.objects.bulk_create(posts)
    for post in posts:
        assert post.pk is None