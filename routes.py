from flask import Blueprint, request, jsonify
from models import db, Post, Comment, Users

api = Blueprint('api', __name__)

@api.route('/posts', methods=['POST'])
def create_post():
    data = request.json
    new_post = Post(
        image=data['image'],
        nickname=data['nickname'],
        email=data['email'],
        description=data['description']
    )
    db.session.add(new_post)
    db.session.commit()

    for comment in data.get('comments', []):
        new_comment = Comment(
            nickname=comment['nickname'],
            comment=comment['comment'],
            post_id=new_post.id
        )
        db.session.add(new_comment)
    
    db.session.commit()
    return jsonify({'message': 'Post created successfully!'}), 201

@api.route('/posts', methods=['GET'])
def get_posts():
    posts = Post.query.all()
    output = []

    for post in posts:
        post_data = {
            'id': post.id,
            'image': post.image,
            'nickname': post.nickname,
            'email': post.email,
            'description': post.description,
            'comments': [{'nickname': comment.nickname, 'comment': comment.comment} for comment in post.comments]
        }
        output.append(post_data)

    return jsonify({'posts': output})

@api.route('/posts/getpost/<int:post_id>', methods=['GET'])
def get_post(post_id):
    posts = Post.query.all()
    output = []

    for post in posts:
        post_data = {
            'id': post.id,
            'image': post.image,
            'nickname': post.nickname,
            'email': post.email,
            'description': post.description,
            'comments': [{'nickname': comment.nickname, 'comment': comment.comment} for comment in post.comments]
        }
        output.append(post_data)

    return jsonify({'posts': output[post_id - 1]})

@api.route('/users', methods=['GET'])
def get_users():
    users = Users.query.all()
    output = []

    for user in users:
        user_data = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'password': user.password
        }
        output.append(user_data)

    return jsonify({'users': output})

@api.route('/users', methods=['POST'])
def create_user():
    data = request.json
    new_user = Users(
        name=data['name'],
        email=data['email'],
        password=data['password'],
    )
    db.session.add(new_user)
    db.session.commit()

    return jsonify({'message': 'User created successfully!'}), 201

@api.route('/users/getposts/<string:nickname>', methods=['GET'])
def create_user(nickname):
    posts = Post.query.all()
    output = []

    for post in posts:
        if nickname == post.nickname:
            post_data = {
                'id': post.id,
                'image': post.image,
                'nickname': post.nickname,
                'email': post.email,
                'description': post.description,
                'comments': [{'nickname': comment.nickname, 'comment': comment.comment} for comment in post.comments]
            }
            output.append(post_data)

    return jsonify({'posts': output})

@api.route('/posts/patchpost/<int:post_id>', methods=['PATCH'])
def patch_post(post_id):
    post = Post.query.get_or_404(post_id)
    data = request.get_json()
    comments_data = data.get('comments', [])
    
    Comment.query.filter_by(post_id=post.id).delete()

    for comment_data in comments_data:
        new_comment = Comment(
            nickname=comment_data.get('nickname'),
            comment=comment_data.get('comment'),
            post_id=post.id
        )
        db.session.add(new_comment)
    
    db.session.commit()
    return jsonify({'message': 'Post updated successfully'})

    

    